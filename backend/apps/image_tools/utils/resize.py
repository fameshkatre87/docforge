import io
from PIL import Image


def resize_image(image_file, width, height, maintain_aspect=False):
    """
    Resize an image to the given width x height.
    If maintain_aspect=True, fits inside the box while keeping aspect ratio.
    Returns BytesIO and the format string (e.g. 'PNG', 'JPEG').
    """
    img = Image.open(image_file)
    original_format = img.format or 'PNG'

    # Convert palette/transparency images to RGBA for safety
    if img.mode in ('P', 'RGBA'):
        img = img.convert('RGBA')
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    if maintain_aspect:
        img.thumbnail((width, height), Image.LANCZOS)
    else:
        img = img.resize((width, height), Image.LANCZOS)

    output = io.BytesIO()
    save_format = original_format if original_format in ('PNG', 'JPEG', 'WEBP', 'GIF') else 'PNG'
    if save_format == 'JPEG' and img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(output, format=save_format)
    output.seek(0)
    return output, save_format.lower()
