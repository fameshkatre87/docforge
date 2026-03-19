from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import FileResponse
from .utils.resize import resize_image
from .utils.compress import compress_image
from .models import ImageRecord



def _record(user, operation, original, result):
    if not user or not user.is_authenticated:
        return
    ImageRecord.objects.create(
        user=user, operation=operation,
        original_filename=original, result_filename=result,
    )
    user.files_processed += 1
    user.save(update_fields=['files_processed'])


class ResizeImageView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        try:
            width = int(request.data.get('width', 800))
            height = int(request.data.get('height', 600))
        except (TypeError, ValueError):
            return Response({'error': 'Width and height must be integers.'}, status=400)

        maintain = request.data.get('maintain_aspect', 'false').lower() == 'true'
        output, fmt = resize_image(file, width, height, maintain)
        result_name = f'resized_{width}x{height}.{fmt}'
        _record(request.user, 'resize', file.name, result_name)
        return FileResponse(output, as_attachment=True, filename=result_name)


class CompressImageView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)
        try:
            quality = int(request.data.get('quality', 70))
            quality = max(10, min(quality, 95))
        except (TypeError, ValueError):
            quality = 70

        output = compress_image(file, quality)
        result_name = 'compressed.jpg'
        _record(request.user, 'compress', file.name, result_name)
        return FileResponse(output, as_attachment=True, filename=result_name,
                            content_type='image/jpeg')


class ImageHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        from rest_framework import serializers
        records = ImageRecord.objects.filter(user=request.user)[:50]

        class S(serializers.ModelSerializer):
            class Meta:
                model = ImageRecord
                fields = ['id', 'operation', 'original_filename', 'result_filename', 'created_at']
        return Response(S(records, many=True).data)
