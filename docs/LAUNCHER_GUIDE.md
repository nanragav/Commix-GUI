# Launcher Scripts Guide

## Overview

The Commix GUI includes smart launcher scripts that handle privilege elevation, dependency checking, and automatic setup.

---

## 📁 Available Launchers

### Windows

| Script | Purpose | Admin Mode |
|--------|---------|------------|
| `launch_gui.bat` | Standard launcher with optional elevation | Prompts when needed |
| `launch_gui_admin.bat` | Always requests administrator privileges | Forces admin mode |

### Linux/macOS

| Script | Purpose | Root Mode |
|--------|---------|-----------|
| `launch_gui.sh` | Standard launcher with optional elevation | Prompts when needed |

---

## 🚀 Windows Launchers

### launch_gui.bat (Recommended)

**Usage:**
```cmd
launch_gui.bat
```

**Features:**
- ✅ Detects if running with admin privileges
- ✅ Prompts user if they want to elevate
- ✅ Checks Python installation and version
- ✅ Auto-installs PyQt6 if missing
- ✅ Color-coded status messages
- ✅ Launches GUI automatically

**Workflow:**
```
Start → Check Admin → Prompt for Elevation? → Check Python → Install Deps → Launch GUI
```

**User Interaction:**
```
========================================
 Commix GUI - Command Injection Tool
========================================

[!] Running without Administrator privileges
[!] Some features may require elevation:
    - System-wide Commix installation
    - Certain scan types
    - Network operations

[?] Do you want to restart as Administrator? (Y/N)
Press Y for Yes, N for No:
```

### launch_gui_admin.bat

**Usage:**
```cmd
launch_gui_admin.bat
```

**Features:**
- ✅ Always requests UAC elevation
- ✅ Forces administrator mode
- ✅ Best for system-wide installation
- ✅ Ideal for enterprise deployment

**When to Use:**
- Installing Commix system-wide to `C:\Program Files\commix`
- Running scans that require admin privileges
- Creating system-level symlinks or shortcuts
- Modifying system PATH

---

## 🐧 Linux/macOS Launcher

### launch_gui.sh

**Usage:**
```bash
# First time - make executable
chmod +x launch_gui.sh

# Normal launch
./launch_gui.sh

# Force sudo
sudo ./launch_gui.sh
```

**Features:**
- ✅ Detects if running as root
- ✅ Prompts user if they want to use sudo
- ✅ Color-coded output (green/yellow/red)
- ✅ Checks Python 3 and version
- ✅ Auto-installs dependencies with pip3
- ✅ Handles both pip and pip3 commands

**Workflow:**
```
Start → Check Root → Prompt for Sudo? → Check Python → Install Deps → Launch GUI
```

**User Interaction:**
```
========================================
 Commix GUI - Command Injection Tool
========================================

[!] Running without root privileges
[!] Some features may require elevation:
    - System-wide Commix installation (/opt/commix)
    - Creating symlinks in /usr/local/bin
    - Certain scan types
    - Network operations

[?] Do you want to restart with sudo? (y/N):
```

---

## 🎨 Status Message Guide

### Windows Messages

| Prefix | Meaning | Example |
|--------|---------|---------|
| `[*]` | Info/Success | `[*] Running with Administrator privileges` |
| `[!]` | Warning | `[!] PyQt6 is not installed` |
| `[X]` | Error | `[X] Error: Python is not installed` |
| `[?]` | Question | `[?] Do you want to restart as Administrator?` |

### Linux/macOS Colors

| Color | Meaning | Usage |
|-------|---------|-------|
| 🟢 Green | Success | Successful operations |
| 🟡 Yellow | Warning | Missing privileges or dependencies |
| 🔴 Red | Error | Critical errors |
| 🔵 Blue | Info | General information |

---

## 🔧 What the Launchers Check

### 1. Privilege Detection

**Windows:**
```batch
net session >nul 2>&1
if %errorLevel% == 0 (
    REM Running as admin
)
```

**Linux/macOS:**
```bash
if [ "$EUID" -eq 0 ]; then
    # Running as root
fi
```

### 2. Python Installation

**Windows:**
```batch
python --version >nul 2>&1
```

**Linux/macOS:**
```bash
command -v python3 &> /dev/null
```

### 3. Python Version Check

**Linux/macOS:**
```bash
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.7"
```

### 4. PyQt6 Dependency

**All Platforms:**
```python
python -c "import PyQt6"
```

---

## 📊 Decision Flow

### Privilege Elevation Decision

```
User Launches Script
        ↓
    Is Admin/Root?
        ↓
    ┌───No───┐
    │        │
    ↓        ↓
Show Warn  Success
    ↓
Prompt User
    ↓
Want Elevate?
    ↓
┌───Yes───┬───No───┐
│         │        │
↓         ↓        ↓
Restart   Continue Launch
as Admin  Without  GUI
          Admin
```

---

## 🛠️ Customization

### Disable Elevation Prompt

**Windows (launch_gui.bat):**
```batch
REM Comment out the elevation prompt section
REM Lines 22-26
goto :continue
```

**Linux/macOS (launch_gui.sh):**
```bash
# Comment out the sudo prompt section
# Lines ~25-35
```

### Force Silent Mode

**Windows:**
```batch
REM Remove all 'pause' commands
REM Remove 'choice' prompts
```

**Linux/macOS:**
```bash
# Remove 'read -p' prompts
# Use '-y' or '--yes' flags
```

---

## 🐛 Troubleshooting

### Issue: "Python is not installed"

**Solution:**
- Install Python 3.7+ from https://python.org (Windows)
- Use package manager: `sudo apt install python3` (Linux)
- Install via Homebrew: `brew install python3` (macOS)
- Ensure Python is in PATH

### Issue: "UAC prompt doesn't appear" (Windows)

**Solution:**
- Run from Command Prompt (not PowerShell)
- Ensure VBScript is not blocked by policy
- Try `launch_gui_admin.bat` directly
- Right-click `launch_gui.bat` → "Run as administrator"

### Issue: "sudo: command not found"

**Solution:**
- You might be root already
- Or sudo is not installed: `apt install sudo`
- Use `su` instead: `su -c './launch_gui.sh'`

### Issue: "Permission denied" (Linux/macOS)

**Solution:**
```bash
# Make script executable
chmod +x launch_gui.sh

# Check file permissions
ls -l launch_gui.sh
```

### Issue: "Dependencies fail to install"

**Solution:**
- Run launcher as admin/root
- Or manually install: `pip install -r requirements.txt`
- Check internet connection
- Verify pip is installed: `pip --version`

---

## 💡 Best Practices

### For Regular Users

1. **First Launch**: Use standard launcher (`launch_gui.bat` or `launch_gui.sh`)
2. **Choose "No"**: When prompted for elevation (unless you need it)
3. **Let GUI Handle**: The GUI will prompt for elevation when truly needed
4. **Save Config**: Use GUI's project save feature to avoid re-entering data

### For System Administrators

1. **Use Admin Launcher**: `launch_gui_admin.bat` or `sudo ./launch_gui.sh`
2. **Install System-Wide**: Let GUI install Commix to `/opt` or `Program Files`
3. **Create Shortcuts**: Add desktop/start menu shortcuts to launcher
4. **Deploy Scripts**: Include launchers in deployment packages

### For Developers

1. **Test Both Modes**: Run with and without elevation
2. **Check Logs**: Review console output for errors
3. **Modify Scripts**: Customize for your environment
4. **Document Changes**: Comment any modifications

---

## 📝 Script Comparison

| Feature | Windows BAT | Linux/macOS SH |
|---------|-------------|----------------|
| Admin detection | ✅ `net session` | ✅ `$EUID` check |
| Elevation | ✅ VBScript UAC | ✅ `sudo` re-exec |
| Color output | ❌ Plain text | ✅ ANSI colors |
| Python check | ✅ `python` | ✅ `python3` |
| Version check | ❌ Not included | ✅ Version compare |
| Dependency install | ✅ pip | ✅ pip3/pip |
| Error handling | ✅ errorlevel | ✅ Exit codes |
| User prompts | ✅ choice command | ✅ read command |

---

## 🔗 Related Documentation

- **[INSTALLATION.md](INSTALLATION.md)** - Complete installation guide
- **[NEW_FEATURES.md](NEW_FEATURES.md)** - System integration features
- **[SYSTEM_INTEGRATION.md](SYSTEM_INTEGRATION.md)** - Technical details
- **[README.md](../README.md)** - Main documentation

---

## 🎯 Quick Reference

### Windows Quick Start

```cmd
# Standard mode
launch_gui.bat

# Admin mode
launch_gui_admin.bat

# Or right-click launch_gui.bat → Run as administrator
```

### Linux/macOS Quick Start

```bash
# First time
chmod +x launch_gui.sh

# Standard mode
./launch_gui.sh

# Root mode
sudo ./launch_gui.sh
```

---

## ✅ Success Indicators

You'll know the launcher worked when you see:

**Windows:**
```
========================================
 Commix GUI - Command Injection Tool
========================================

[*] Running with Administrator privileges

[*] Python detected:
Python 3.x.x

[*] Launching Commix GUI...
```

**Linux/macOS:**
```
========================================
 Commix GUI - Command Injection Tool
========================================

[*] Running with root privileges

[*] Python detected: 3.x

[*] Launching Commix GUI...
```

Then the GUI window should appear! 🎉
