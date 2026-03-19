import zipfile
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import FileResponse
from .utils.merge import merge_pdfs, split_pdf, remove_pages
from .utils.compress import compress_pdf
from .utils.convert import word_to_pdf, pdf_to_word, images_to_pdf
from .models import FileRecord
from .serializers import FileRecordSerializer


# def _record(user, operation, original, result):
#     FileRecord.objects.create(
#         user=user,
#         operation=operation,
#         original_filename=original,
#         result_filename=result,
#     )
#     user.files_processed += 1
#     user.save(update_fields=['files_processed'])

def _record(user, operation, original, result):
    if not user or not user.is_authenticated:
        return
    FileRecord.objects.create(
        user=user,
        operation=operation,
        original_filename=original,
        result_filename=result,
    )
    user.files_processed += 1
    user.save(update_fields=['files_processed'])

class MergePdfView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        files = request.FILES.getlist('files')
        if len(files) < 2:
            return Response({'error': 'At least 2 PDF files are required.'}, status=400)
        merged = merge_pdfs(files)
        _record(request.user, 'merge', files[0].name, 'merged.pdf')
        return FileResponse(merged, as_attachment=True, filename='merged.pdf',
                            content_type='application/pdf')


class SplitPdfView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        pages_per_chunk = int(request.data.get('pages_per_chunk', 1))
        chunks = split_pdf(file, pages_per_chunk)

        # Return a ZIP containing all chunks
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, chunk in enumerate(chunks, start=1):
                zf.writestr(f'part_{i}.pdf', chunk.read())
        zip_buffer.seek(0)

        _record(request.user, 'split', file.name, f'split_{len(chunks)}_parts.zip')
        return FileResponse(zip_buffer, as_attachment=True, filename='split_parts.zip',
                            content_type='application/zip')


class CompressPdfView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        compressed = compress_pdf(file)
        _record(request.user, 'compress_pdf', file.name, 'compressed.pdf')
        return FileResponse(compressed, as_attachment=True, filename='compressed.pdf',
                            content_type='application/pdf')


class WordToPdfView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        result = word_to_pdf(file)
        _record(request.user, 'word_to_pdf', file.name, 'converted.pdf')
        return FileResponse(result, as_attachment=True, filename='converted.pdf',
                            content_type='application/pdf')


class PdfToWordView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        result = pdf_to_word(file)
        _record(request.user, 'pdf_to_word', file.name, 'converted.docx')
        return FileResponse(
            result, as_attachment=True, filename='converted.docx',
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )


class FileHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = FileRecord.objects.filter(user=request.user)[:50]
        return Response(FileRecordSerializer(records, many=True).data)
class ImagesToPdfView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        files = request.FILES.getlist('files')
        if not files:
            return Response({'error': 'No images provided.'}, status=400)
        try:
            result = images_to_pdf(files)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        _record(request.user, 'images_to_pdf', files[0].name, 'converted.pdf')
        return FileResponse(result, as_attachment=True, filename='images.pdf',
                            content_type='application/pdf')
        
class RemovePagesView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file  = request.FILES.get('file')
        pages = request.data.get('pages', '')

        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        if not pages:
            return Response({'error': 'No pages specified.'}, status=400)

        try:
            pages_list = [p.strip() for p in pages.split(',') if p.strip()]
            result, total = remove_pages(file, pages_list)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

        _record(request.user, 'remove_pages', file.name, 'cleaned.pdf')
        return FileResponse(result, as_attachment=True, filename='cleaned.pdf',
                            content_type='application/pdf')
        
class GetPdfInfoView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        try:
            reader = __import__('PyPDF2').PdfReader(file)
            return Response({'total_pages': len(reader.pages)})
        except Exception as e:
            return Response({'error': str(e)}, status=400)