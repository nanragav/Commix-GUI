# Commix GUI - Launch Guide

## Quick Start

### Single Command (All Platforms)

```bash
python launch.py
```

That's it! The launcher handles everything else automatically.

## Best Practice: Use Virtual Environment

Before running for the first time:

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python launch.py
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python launch.py
```

## What the Launcher Does

### 1. Privilege Detection
- Automatically detects if you're running as admin/root
- Shows your current privilege level
- Explains what features need elevation

### 2. Interactive Privilege Request
When not running as admin/root, you'll see:
```
[?] Do you want to restart with admin privileges? (y/N):
```

**Press 'y':**
- **Windows**: Triggers UAC prompt, restarts with admin rights
- **Linux/macOS**: Uses `sudo`, prompts for password, restarts with root
- Recommended if you want system-wide Commix installation

**Press 'n' or Enter:**
- Continues in normal mode
- User-level Commix installation only
- Sufficient for most use cases

### 3. Dependency Management
- Checks if PyQt6 is installed
- Automatically installs missing dependencies
- Uses your current Python environment (or venv if activated)

### 4. Commix Detection
When GUI launches, it will:
- Check if Commix is already installed
- Offer to install from GitHub if missing
- **With admin/root**: Installs to system directories
  - Linux/macOS: `/opt/commix`
  - Windows: `C:\Program Files\Commix`
- **Without admin/root**: Installs to user directories
  - Linux/macOS: `~/.local/share/commix`
  - Windows: `%APPDATA%\Commix`

### 5. GUI Launch
- Launches the full GUI application
- Ready to configure and run Commix attacks

## Platform-Specific Notes

### Windows

**Normal Launch:**
```cmd
python launch.py
```

**Force Admin Mode:**
```cmd
# Right-click Command Prompt → "Run as administrator"
python launch.py
```

**Benefits of Admin Mode:**
- System-wide installation
- No UAC prompts during scans
- Full network access

### Linux

**Normal Launch:**
```bash
python3 launch.py
```

**Force Root Mode:**
```bash
sudo python3 launch.py
```

**How Sudo Works:**
- When you select 'y' for elevation, launcher calls `sudo` internally
- You'll be prompted for your password
- Script restarts with root privileges
- Commix can be installed to `/opt/commix`

**Sudo for Scans:**
- If Commix is installed system-wide, it's accessible to all users
- For certain scans requiring root, the GUI will prompt separately
- No need to run GUI as root for normal operations

### macOS

**Normal Launch:**
```bash
python3 launch.py
```

**Force Root Mode:**
```bash
sudo python3 launch.py
```

**Behavior:**
- Same as Linux - uses `sudo` for elevation
- Commix installs to `/opt/commix` with root
- User installation goes to `~/Library/Application Support/Commix`

## Troubleshooting

### Issue: GUI doesn't launch after selecting 'n'

**Fixed in latest version!** The launcher now properly continues when you decline elevation.

**If you still have issues:**
1. Make sure you're using the latest `launch.py`
2. Try running with verbose output:
   ```bash
   python launch.py --skip-admin-prompt
   ```

### Issue: "PyQt6 not installed" error

**Solution:**
```bash
pip install PyQt6
```

Or let the launcher install it automatically.

### Issue: Can't install Commix without admin

**Solution:**
- This is expected behavior for system-wide installation
- Either:
  - Option 1: Restart launcher with admin/root (`python launch.py`, then select 'y')
  - Option 2: Continue without admin - Commix will install to user directory

### Issue: Launcher prompts multiple times

**Fixed in latest version!** The `--skip-admin-prompt` flag prevents re-prompting.

### Issue: Linux/Mac - sudo not working

**Check:**
1. Is `sudo` available? Try: `which sudo`
2. Do you have sudo permissions? Try: `sudo -v`
3. If in venv, make sure `sudo -E` preserves environment

**Alternative:**
```bash
# Run as root directly
sudo su
source venv/bin/activate  # if using venv
python launch.py
```

## Command Line Options

### Skip Admin Prompt

```bash
python launch.py --skip-admin-prompt
```

Launches directly without asking about elevation. Useful for:
- Automation scripts
- CI/CD pipelines
- When you know you don't need admin

## Advantages of launch.py

✅ **Cross-Platform**: Same command on Windows, Linux, and macOS
✅ **Smart Privileges**: Detects and requests elevation only when beneficial
✅ **Dependency Handling**: Auto-installs missing packages
✅ **No Working Directory Issues**: Always launches from correct location
✅ **Clean Exit**: Properly handles Ctrl+C and user cancellation
✅ **Pythonic**: Pure Python, no shell script complexity

## Comparison: Old vs New

### ❌ Old Way (Deleted)
- `launch_gui.bat` (Windows only)
- `launch_gui_admin.bat` (Windows only)
- `launch_gui.sh` (Linux/Mac only)
- Different commands per platform
- Working directory issues
- Manual dependency management

### ✅ New Way
- Single `launch.py` (all platforms)
- Same command everywhere: `python launch.py`
- Smart privilege handling
- Auto dependency installation
- Reliable and tested

## Why Virtual Environment?

Using a virtual environment (`venv`) is **best practice** because:

1. **Isolation**: Dependencies don't conflict with system Python
2. **Reproducibility**: Easy to recreate exact environment
3. **Cleanliness**: Can delete and recreate without affecting system
4. **Safety**: System Python remains untouched
5. **Portability**: `requirements.txt` captures all dependencies

**Recommended workflow:**
```bash
# One-time setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Every time you work on project
source venv/bin/activate  # or venv\Scripts\activate on Windows
python launch.py

# When done
deactivate
```

## Support

If you encounter issues:
1. Check this guide first
2. Ensure Python 3.7+ is installed: `python --version`
3. Try with `--skip-admin-prompt` flag
4. Check if dependencies are installed: `pip list | grep PyQt6`
5. Report issues with full error output

---

**Happy Testing with Commix GUI!** 🚀
