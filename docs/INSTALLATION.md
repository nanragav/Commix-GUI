# Commix GUI - Installation Guide

## System Requirements

- **Python**: 3.7 or higher
- **PyQt6**: 6.4.0 or higher
- **Git**: Required for automatic Commix installation from GitHub
- **Operating Systems**: Windows, Linux, macOS

## Installation Methods

### Method 1: Automatic Installation (Recommended)

The Commix GUI will automatically detect if Commix is installed on your system. If not found, it will offer to install it for you.

1. **Launch the GUI**:
   ```bash
   # Windows
   launch_gui.bat
   
   # Linux/macOS
   ./launch_gui.sh
   ```

2. **Setup Dialog**: On first launch, you'll see the Commix Setup Dialog that will:
   - ✅ Check for existing Commix installation
   - ✅ Search system PATH and common installation directories
   - ✅ Offer to install from GitHub if not found
   - ✅ Handle administrator privileges automatically

3. **Installation Options**:
   - **Install from GitHub**: Automatically clones the latest Commix from official repository
   - **Custom Path**: Specify an existing Commix installation directory

### Method 2: Manual Commix Installation

If you prefer to install Commix manually before using the GUI:

#### System-Wide Installation (Recommended)

**Linux/macOS:**
```bash
# Clone Commix repository
git clone https://github.com/commixproject/commix.git /opt/commix

# Create symlink (requires sudo)
sudo ln -s /opt/commix/commix.py /usr/local/bin/commix

# Make executable
sudo chmod +x /opt/commix/commix.py
```

**Windows (Administrator Command Prompt):**
```cmd
# Clone to Program Files
cd "C:\Program Files"
git clone https://github.com/commixproject/commix.git

# Add to PATH or create batch script
echo @python "C:\Program Files\commix\commix.py" %* > C:\Windows\commix.bat
```

#### User-Level Installation

**Linux/macOS:**
```bash
# Clone to user directory
git clone https://github.com/commixproject/commix.git ~/commix

# Add to PATH in ~/.bashrc or ~/.zshrc
echo 'export PATH="$HOME/commix:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Windows:**
```cmd
# Clone to user directory
git clone https://github.com/commixproject/commix.git %USERPROFILE%\commix

# Add to user PATH through System Properties
```

### Method 3: GUI Requirements Only

If you just want to run the GUI without Commix initially:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Launch GUI
python commix_gui.py
```

The GUI will prompt you to install Commix on first run.

---

## Installation Detection

The GUI searches for Commix in the following order:

1. **System PATH**: Checks if `commix` command is available
2. **Common Directories**:
   - `/usr/local/bin/commix` (Linux/macOS)
   - `/opt/commix` (Linux/macOS)
   - `C:\Program Files\commix` (Windows)
   - `C:\commix` (Windows)
3. **User Directories**:
   - `~/commix` (Linux/macOS)
   - `%USERPROFILE%\commix` (Windows)
4. **Local Directory**: `./commix` folder next to GUI

---

## Administrator Privileges

### Why Admin Rights Are Needed

**For Installation:**
- Installing to system directories (`/opt`, `Program Files`)
- Creating system-wide symlinks
- Modifying system PATH

**For Scanning:**
- Some Commix techniques require elevated privileges
- Network sniffing and low-level operations
- Writing to protected directories

### Privilege Handling

The GUI automatically:
- ✅ Detects if running with admin/root privileges
- ✅ Prompts for elevation when needed
- ✅ Restarts with elevated privileges if user agrees
- ✅ Warns about limited functionality without admin

**Windows:**
```cmd
# Run as Administrator
Right-click launch_gui.bat → "Run as administrator"
```

**Linux/macOS:**
```bash
# Run with sudo
sudo ./launch_gui.sh

# Or elevate when prompted by GUI
```

---

## Verification

### Check Installation Status

1. **Via GUI Menu**: 
   - `Tools` → `Check Commix Installation`

2. **Via Command Line**:
   ```bash
   # Check if Commix is in PATH
   commix --version
   
   # Or run directly
   python /path/to/commix/commix.py --version
   ```

### Expected Output

```
Commix v3.x-dev#xx
By Anastasios Stasinopoulos
```

---

## Updating Commix

### Via GUI (Recommended)

1. Open Commix GUI
2. Go to `Tools` → `Update Commix`
3. The GUI will automatically pull the latest changes from GitHub

### Manual Update

```bash
# Navigate to Commix directory
cd /path/to/commix

# Pull latest changes
git pull origin master
```

---

## Troubleshooting

### Issue: "Commix not found"

**Solution 1**: Use automatic installation
- Let the GUI install Commix from GitHub

**Solution 2**: Manual installation
- Follow Method 2 above
- Ensure Commix path is correct

**Solution 3**: Specify custom path
- In setup dialog, choose "Specify custom Commix path"
- Browse to your Commix directory

### Issue: "Administrator privileges required"

**Windows:**
- Right-click `launch_gui.bat` → "Run as administrator"
- Or allow GUI to restart with elevation

**Linux/macOS:**
- Run with `sudo ./launch_gui.sh`
- Or allow GUI to restart with sudo

### Issue: "Git not found"

**Windows:**
- Install Git from https://git-scm.com/
- Add Git to system PATH

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get install git

# RedHat/CentOS
sudo yum install git

# Arch
sudo pacman -S git
```

**macOS:**
```bash
# Using Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

### Issue: Python version incompatibility

```bash
# Check Python version
python --version

# If too old, install Python 3.7+
# Windows: Download from python.org
# Linux: sudo apt-get install python3.7
# macOS: brew install python@3.7
```

---

## Directory Structure

After installation, your structure should look like:

```
Commix-GUI/
├── commix_gui.py           # Main application
├── launch_gui.bat          # Windows launcher
├── launch_gui.sh           # Linux/macOS launcher
├── requirements.txt        # Python dependencies
├── gui_modules/
│   ├── commix_manager.py       # NEW: Installation manager
│   ├── commix_setup_dialog.py  # NEW: Setup dialog
│   ├── commix_runner.py        # Commix execution
│   └── ...
└── docs/
    └── INSTALLATION.md     # This file

/opt/commix/                # System Commix installation (Linux)
or
C:\Program Files\commix\    # System Commix installation (Windows)
or
~/commix/                   # User Commix installation
```

---

## Security Notes

⚠️ **Important**:
- Only install Commix from official sources
- Verify the GitHub repository: `https://github.com/commixproject/commix`
- Be cautious when running with administrator privileges
- Use admin rights only when necessary
- Review Commix output before executing in production environments

---

## Support

- **Commix Project**: https://commixproject.com
- **GitHub**: https://github.com/commixproject/commix
- **Issues**: Report bugs on GitHub

---

## Quick Start After Installation

1. ✅ **Verify Installation**: Tools → Check Commix Installation
2. ✅ **Set Target**: Enter URL in Target tab
3. ✅ **Configure Options**: Adjust settings in other tabs
4. ✅ **Start Attack**: Click "🚀 Start Attack"
5. ✅ **View Output**: Check Output Console tab for results

For detailed usage, see [USER_GUIDE.md](USER_GUIDE.md)
