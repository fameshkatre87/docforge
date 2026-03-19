import io
from PIL import Image


def compress_image(image_file, quality=70):
    """
    Compress an image by reducing JPEG quality.
    Always outputs JPEG for best compression.
    Returns BytesIO.
    """
    img = Image.open(image_file)

    # Convert to RGB (JPEG does not support alpha)
    if img.mode in ('RGBA', 'P', 'LA'):
        img = img.convert('RGB')
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    output = io.BytesIO()
    img.save(output, format='JPEG', quality=int(quality), optimize=True)
    output.seek(0)
    return output
