"""Screen capture module using mss library."""

import mss
from PIL import Image


class ScreenCapturer:
    """Captures screenshots from specified monitors at full native resolution."""

    def __init__(self, monitor_index: int = 1):
        """
        Initialize the screen capturer.

        Args:
            monitor_index: Monitor to capture (1 for primary monitor, 0 for all monitors).

        Raises:
            ValueError: If monitor_index is invalid.
        """
        # Validate monitor index
        with mss.mss() as sct:
            max_monitors = len(sct.monitors) - 1

        if monitor_index < 0:
            raise ValueError(f"Monitor index must be non-negative, got {monitor_index}")
        if monitor_index > max_monitors:
            raise ValueError(f"Monitor index {monitor_index} out of range (max: {max_monitors})")

        self.monitor_index = monitor_index

    def capture(self) -> Image.Image:
        """
        Capture a screenshot from the specified monitor.

        Returns:
            PIL.Image.Image: The captured screenshot in RGB format.
        """
        with mss.mss() as sct:
            # Grab the monitor frame
            monitor = sct.monitors[self.monitor_index]
            screenshot = sct.grab(monitor)

            # Convert to PIL Image (RGB format)
            img = Image.frombytes(
                "RGB",
                (screenshot.width, screenshot.height),
                screenshot.rgb
            )

            return img
