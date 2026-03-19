import io
import PyPDF2
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def word_to_pdf(docx_file):
    """Convert a .docx file-like object to PDF. Returns BytesIO."""
    doc = Document(docx_file)
    output = io.BytesIO()
    pdf = SimpleDocTemplate(output, pagesize=letter,
                            rightMargin=50, leftMargin=50,
                            topMargin=60, bottomMargin=60)
    styles = getSampleStyleSheet()
    story = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            story.append(Spacer(1, 8))
            continue
        # Basic heading detection
        if para.style.name.startswith('Heading 1'):
            style = styles['Heading1']
        elif para.style.name.startswith('Heading 2'):
            style = styles['Heading2']
        else:
            style = styles['Normal']
        story.append(Paragraph(text, style))
        story.append(Spacer(1, 4))

    pdf.build(story)
    output.seek(0)
    return output


def pdf_to_word(pdf_file):
    """Convert a PDF file-like object to .docx. Returns BytesIO."""
    reader = PyPDF2.PdfReader(pdf_file)
    doc = Document()
    doc.add_heading('Converted Document', level=1)

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            doc.add_heading(f'Page {i + 1}', level=2)
            for line in text.split('\n'):
                line = line.strip()
                if line:
                    doc.add_paragraph(line)
        doc.add_page_break()

    output = io.BytesIO()
    doc.save(output)
    output.seek(0)
    return output

def images_to_pdf(image_files):
    """Convert multiple image files to a single PDF. Returns BytesIO."""
    from PIL import Image
    import io

    output = io.BytesIO()
    image_list = []

    for img_file in image_files:
        img = Image.open(img_file)
        if img.mode in ('RGBA', 'P', 'LA'):
            img = img.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        image_list.append(img)

    if not image_list:
        raise ValueError("No valid images provided.")

    first = image_list[0]
    rest  = image_list[1:]
    first.save(output, format='PDF', save_all=True, append_images=rest)
    output.seek(0)
    return output