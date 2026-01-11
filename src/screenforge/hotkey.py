"""Global hotkey registration for ScreenForge."""

import keyboard
import ctypes


def _is_admin():
    """Check if running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def start_hotkey_listener(callback):
    """
    Register the global hotkey (CTRL + ALT + S) for screenshot capture.

    This function does NOT block the main thread.

    Args:
        callback: Function to call when the hotkey is pressed.

    Returns:
        bool: True if successful, False otherwise.
    """
    if not _is_admin():
        print("Warning: Not running as administrator. Hotkeys may not work.")
        print("Right-click and 'Run as administrator' for reliable hotkey support.")

    try:
        keyboard.add_hotkey("ctrl+alt+s", callback)
        return True
    except Exception as e:
        print(f"Failed to register hotkey: {e}")
        return False


def stop_hotkey_listener():
    """Clear all registered hotkeys for clean exit."""
    try:
        keyboard.clear_all_hotkeys()
    except Exception as e:
        print(f"Warning: Error clearing hotkeys: {e}")
