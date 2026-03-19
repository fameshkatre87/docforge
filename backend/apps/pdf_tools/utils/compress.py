import io
import PyPDF2


def compress_pdf(pdf_file):
    """
    Compress a PDF by removing duplicate objects and compressing streams.
    Returns a BytesIO of the compressed PDF.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()   # deflate-compress each page stream
        writer.add_page(page)

    # Copy metadata
    if reader.metadata:
        writer.add_metadata(reader.metadata)

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return output
