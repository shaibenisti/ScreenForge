"""Main entry point for ScreenForge."""

import os
from datetime import datetime
from pathlib import Path
from screenforge.capture.capturer import ScreenCapturer
from screenforge.utils.save import save_image
from screenforge.utils.clipboard import copy_image_to_clipboard
from screenforge.hotkey import start_hotkey_listener, stop_hotkey_listener
from screenforge.tray import run_tray

try:
    from winotify import Notification
    _has_notifications = True
except ImportError:
    _has_notifications = False


def get_screenshot_dir():
    """Get the screenshot directory, checking OneDrive first, then local Pictures."""
    # Try OneDrive Pictures first
    onedrive = os.getenv('OneDrive')
    if onedrive:
        onedrive_screenshots = Path(onedrive) / "Pictures" / "Screenshots"
        if onedrive_screenshots.parent.exists():
            return str(onedrive_screenshots)

    # Fall back to local Pictures
    return str(Path.home() / "Pictures" / "Screenshots")


def capture_and_save():
    """Capture a screenshot and save it to the configured directory."""
    try:
        # Initialize the screen capturer for the primary monitor
        capturer = ScreenCapturer(monitor_index=1)

        # Capture the screenshot
        image = capturer.capture()

        # Generate timestamp-based filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"

        # Get output directory
        output_dir = get_screenshot_dir()
        output_path = os.path.join(output_dir, filename)

        # Save the image
        save_image(image, output_path)

        # Copy to clipboard
        copy_image_to_clipboard(image)

        # Show notification
        if _has_notifications:
            try:
                toast = Notification(
                    app_id="ScreenForge",
                    title="Screenshot Captured!",
                    msg="Saved and copied to clipboard",
                    duration="short"
                )
                toast.show()
            except Exception as e:
                print(f"Screenshot saved and copied to clipboard: {filename}")
        else:
            print(f"Screenshot saved and copied to clipboard: {filename}")

    except Exception as e:
        print(f"Screenshot failed: {e}")
        if _has_notifications:
            try:
                toast = Notification(
                    app_id="ScreenForge",
                    title="Screenshot Failed",
                    msg=str(e),
                    duration="short"
                )
                toast.show()
            except:
                pass  # Notification failed, already printed error


def main():
    """Start the ScreenForge system tray application."""

    def on_exit():
        """Handle application exit."""
        stop_hotkey_listener()
        print("ScreenForge exiting...")

    # Register the global hotkey
    if not start_hotkey_listener(capture_and_save):
        print("Failed to start. Please run as administrator.")
        return

    # Print startup message
    print("ScreenForge is running. Press CTRL+ALT+S to capture, or use tray icon to exit.")

    # Run the system tray icon (blocks until user exits)
    try:
        run_tray(on_exit)
    except Exception as e:
        print(f"Error: {e}")
        on_exit()


if __name__ == "__main__":
    main()
