"""System tray icon for ScreenForge."""

import pystray
from PIL import Image, ImageDraw


def _create_image():
    """
    Create a simple icon image for the system tray.

    Returns:
        PIL.Image.Image: A 64x64 icon image.
    """
    # Create a 64x64 image with a transparent background
    width = 64
    height = 64
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw a simple camera-like icon (rectangle with a small circle)
    # Outer rectangle (camera body)
    draw.rectangle([10, 20, 54, 50], fill="blue", outline="darkblue", width=2)

    # Lens (circle in the center)
    draw.ellipse([24, 28, 40, 44], fill="lightblue", outline="darkblue", width=2)

    # Top rectangle (camera viewfinder)
    draw.rectangle([26, 14, 38, 20], fill="blue", outline="darkblue", width=1)

    return image


def run_tray(on_exit):
    """
    Create and run the ScreenForge system tray icon.

    Args:
        on_exit: Callback function to call when the user chooses Exit.

    This function blocks until the user exits via the tray menu.
    """
    # Create the icon image
    icon_image = _create_image()

    # Define the exit action
    def exit_action(icon, item):
        """Handle the Exit menu action."""
        on_exit()
        icon.stop()

    # Create the tray icon with a menu
    icon = pystray.Icon(
        "ScreenForge",
        icon_image,
        "ScreenForge",
        menu=pystray.Menu(
            pystray.MenuItem("Exit", exit_action)
        )
    )

    # Run the tray icon (blocks until stopped)
    icon.run()
