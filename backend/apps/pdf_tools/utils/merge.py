import io
import PyPDF2


def merge_pdfs(pdf_files):
    """Merge a list of PDF file-like objects into one PDF. Returns BytesIO."""
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    output = io.BytesIO()
    merger.write(output)
    merger.close()
    output.seek(0)
    return output


def split_pdf(pdf_file, pages_per_chunk=1):
    """
    Split a PDF into chunks of `pages_per_chunk` pages each.
    Returns a list of BytesIO objects.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    total = len(reader.pages)
    chunks = []
    for i in range(0, total, pages_per_chunk):
        writer = PyPDF2.PdfWriter()
        for j in range(i, min(i + pages_per_chunk, total)):
            writer.add_page(reader.pages[j])
        output = io.BytesIO()
        writer.write(output)
        output.seek(0)
        chunks.append(output)
    return chunks

def remove_pages(pdf_file, pages_to_remove):
    """
    Remove specific pages from a PDF.
    pages_to_remove: list of 1-based page numbers to delete.
    Returns BytesIO.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()
    total  = len(reader.pages)

    remove_set = set(int(p) for p in pages_to_remove)

    for i in range(total):
        page_num = i + 1  # 1-based
        if page_num not in remove_set:
            writer.add_page(reader.pages[i])

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return output, total