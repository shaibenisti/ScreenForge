# ScreenForge

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Windows screenshot utility with global hotkey support and system tray integration.

## Features

- Global hotkey (CTRL+ALT+S) for screenshot capture
- Automatic clipboard integration
- Configurable save location (OneDrive Pictures or local Pictures folder)
- Windows notification support
- System tray interface

## Requirements

- Python 3.8+
- Windows OS
- Administrator privileges recommended for global hotkey functionality

## Installation

Clone the repository:
```bash
git clone https://github.com/shaibenisti/ScreenForge.git
cd ScreenForge
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python -m screenforge.main
```

For reliable hotkey support, run as administrator:
```bash
# Right-click Command Prompt -> Run as administrator
python -m screenforge.main
```

The application will run in the system tray. Press CTRL+ALT+S to capture a screenshot. Screenshots are automatically saved to `Pictures/Screenshots` with timestamp-based filenames and copied to the clipboard.

To exit, right-click the system tray icon and select Exit.

## Dependencies

- mss - Screenshot capture
- Pillow - Image processing
- keyboard - Global hotkey registration
- pystray - System tray interface
- pywin32 - Windows clipboard operations
- winotify - Windows notifications

## Project Structure

```
ScreenForge/
├── src/
│   └── screenforge/
│       ├── __init__.py
│       ├── main.py              # Application entry point
│       ├── hotkey.py            # Hotkey registration
│       ├── tray.py              # System tray implementation
│       ├── capture/
│       │   ├── __init__.py
│       │   └── capturer.py      # Screenshot capture
│       └── utils/
│           ├── __init__.py
│           ├── save.py          # File operations
│           └── clipboard.py     # Clipboard operations
├── requirements.txt
├── README.md
└── LICENSE
```

## License

MIT License. See [LICENSE](LICENSE) for details.
