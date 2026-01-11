# 🖼️ ScreenForge

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

> A lightweight, fast screenshot tool for Windows with global hotkey support and system tray integration.

## ✨ Features

- 📸 **Instant Screenshots** - Capture with a simple `CTRL+ALT+S` hotkey
- 📋 **Auto Clipboard** - Screenshots automatically copied to clipboard
- 💾 **Smart Saving** - Auto-saves to OneDrive or local Pictures folder
- 🔔 **Notifications** - Native Windows notifications for capture status
- 🎯 **System Tray** - Minimal interface that stays out of your way
- ⚡ **Lightning Fast** - Built with performance in mind

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows OS
- Administrator privileges (recommended for reliable hotkey support)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ScreenForge.git
cd ScreenForge
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python -m screenforge.main
```

Or run as administrator (recommended):
```bash
# Right-click Command Prompt → Run as administrator
python -m screenforge.main
```

## 🎮 Usage

1. **Launch ScreenForge** - The app runs in your system tray
2. **Press `CTRL+ALT+S`** - Capture a screenshot
3. **Your screenshot is:**
   - ✅ Saved to `Pictures/Screenshots` (or OneDrive if available)
   - ✅ Copied to clipboard for instant pasting
   - ✅ Named with timestamp: `screenshot_2026-01-11_14-30-45.png`

### Exit

- Right-click the system tray icon and select "Exit"
- Or close from the console window

## 📦 Dependencies

- **mss** - Fast cross-platform screenshots
- **Pillow** - Image processing
- **keyboard** - Global hotkey registration
- **pystray** - System tray icon
- **pywin32** - Windows clipboard integration
- **winotify** - Native Windows notifications

## 🛠️ Project Structure

```
ScreenForge/
├── src/
│   └── screenforge/
│       ├── __init__.py
│       ├── main.py              # Entry point
│       ├── hotkey.py            # Global hotkey handler
│       ├── tray.py              # System tray icon
│       ├── capture/
│       │   ├── __init__.py
│       │   └── capturer.py      # Screenshot capture logic
│       └── utils/
│           ├── __init__.py
│           ├── save.py          # Image saving
│           └── clipboard.py     # Clipboard operations
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with ❤️ using:
- [mss](https://github.com/BoboTiG/python-mss) for fast screenshots
- [pystray](https://github.com/moses-palmer/pystray) for system tray support
- [keyboard](https://github.com/boppreh/keyboard) for global hotkeys

## 📧 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/ScreenForge/issues).

---

**Made with** ⚡ **by developers, for developers**
