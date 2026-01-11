"""Clipboard utilities for Windows."""

import io
import win32clipboard
from PIL import Image


def copy_image_to_clipboard(image: Image.Image) -> None:
    """
    Copy a PIL Image to the Windows clipboard.

    Args:
        image: The PIL Image to copy.
    """
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # Remove BMP header
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
