"""
Dynamic test-image generation for upload boundary tests.

Avoids storing large binary fixtures in the repo by generating images on the fly.
PNG with random pixel data and `compress_level=0` is used because the resulting
size is ~width*height*3 bytes plus a small fixed overhead — predictable enough
to hit specific MB targets within ±0.1 MB.
"""

import io
import os
from PIL import Image


_PNG_OVERHEAD_BYTES = 200  # rough fixed-cost of headers/IDAT chunks


def make_png_bytes(target_mb: float) -> bytes:
    """Generate a PNG with high-entropy pixels at ~target_mb size.

    Random RGB data does not compress, and compress_level=0 disables zlib filtering,
    so output size ≈ width*height*3 + ~200 bytes. Returns the encoded PNG bytes.
    """
    target_bytes = max(1, int(target_mb * 1024 * 1024) - _PNG_OVERHEAD_BYTES)
    pixel_count = max(1, target_bytes // 3)
    side = max(1, int(pixel_count ** 0.5))
    width = side
    height = max(1, pixel_count // width)
    raw = os.urandom(width * height * 3)
    img = Image.frombytes("RGB", (width, height), raw)
    buf = io.BytesIO()
    img.save(buf, "PNG", compress_level=0)
    return buf.getvalue()


def make_jpeg_bytes(target_mb: float) -> bytes:
    """Generate a JPEG sized roughly to target_mb. JPEG sizes are harder to predict
    than PNG, so we iterate resolution until we land within ±10% of the target."""
    target_bytes = int(target_mb * 1024 * 1024)
    width, height = 1024, 768
    for _ in range(10):
        raw = os.urandom(width * height * 3)
        img = Image.frombytes("RGB", (width, height), raw)
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=95)
        size = buf.tell()
        if 0.9 * target_bytes <= size <= 1.1 * target_bytes:
            return buf.getvalue()
        ratio = (target_bytes / size) ** 0.5
        width = max(64, int(width * ratio))
        height = max(64, int(height * ratio))
    return buf.getvalue()


def make_text_file_bytes(repeat: int = 200) -> bytes:
    """Plain-text bytes (NOT an image). Used to test that a file mislabeled as a PNG
    or uploaded with a .txt extension is rejected."""
    return (b"This is a plain text file, not an image. Lorem ipsum dolor sit amet, "
            b"consectetur adipiscing elit.\n") * repeat
