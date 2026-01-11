"""Image saving utilities."""

import os
import shutil
from pathlib import Path
from PIL import Image


def save_image(image: Image.Image, output_path: str) -> None:
    """
    Save a PIL Image to the specified path as PNG.

    Creates parent directories if they don't exist.

    Args:
        image: The PIL Image to save.
        output_path: Full path where the image should be saved.

    Raises:
        OSError: If insufficient disk space or cannot write to directory.
    """
    # Ensure parent directory exists
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check disk space
    stat = shutil.disk_usage(output_dir)
    free_mb = stat.free / (1024 * 1024)

    if free_mb < 10:  # Need at least 10MB free
        raise OSError(f"Insufficient disk space: {free_mb:.1f}MB free")

    # Save the image as PNG
    try:
        image.save(output_path, format="PNG")
    except Exception as e:
        # Clean up partial file if save failed
        if Path(output_path).exists():
            Path(output_path).unlink()
        raise OSError(f"Failed to save image: {e}") from e
