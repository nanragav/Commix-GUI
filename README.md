# Commix GUI - Installation and Setup

A comprehensive cross-platform GUI wrapper for [Commix](https://github.com/commixproject/commix) - Automated Command Injection Exploitation Tool.

## 🌟 Features

- **Complete Feature Coverage**: All Commix CLI options available through intuitive GUI
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **User-Friendly**: Organized tabs for different configuration categories
- **Real-Time Output**: Live output display with syntax highlighting
- **Project Management**: Save and load attack configurations
- **Command Generation**: View and copy generated Commix commands
- **Modern Interface**: Clean, professional PyQt6-based design

## 📋 Requirements

- Python 3.7 or higher
- PyQt6
- Commix (included in the `commix/` directory)

## 🚀 Installation

### Step 1: Clone or Download

```bash
git clone <repository-url>
cd Commix-GUI
```

### Step 2: Create Virtual Environment (Recommended Best Practice)

Creating a virtual environment ensures clean dependency management and avoids conflicts:

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install PyQt6
```

### Step 4: Launch the GUI

Use the cross-platform launcher:

```bash
python launch.py
```

The launcher will:
- ✅ Automatically detect if you're running as admin/root
- ✅ Prompt you to elevate privileges if beneficial (y/n)
- ✅ Check and install dependencies if missing
- ✅ Detect if Commix is installed
- ✅ Offer to install Commix from GitHub if not found
- ✅ Launch the GUI in your current environment

**Privilege Selection:**
- **Press 'y'**: Restart with admin/root privileges (recommended for system-wide installation)
- **Press 'n'**: Continue in normal mode (user-level operations only)

### Commix Installation

The GUI includes an **automatic installation system** for Commix:

- On first launch, the GUI will detect if Commix is installed
- If not found, it will offer to install the latest version from GitHub
- **With admin/root**: Installs to system directories (`/opt/commix` or `Program Files`)
- **Without admin/root**: Installs to user directories (`~/.local/commix` or `%APPDATA%`)

For detailed installation instructions, see [docs/INSTALLATION.md](docs/INSTALLATION.md)

## 🎯 Usage

### Starting the GUI

**Single Command - All Platforms:**

```bash
python launch.py
```

**With Virtual Environment (Recommended):**

```bash
# Activate venv first
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

python launch.py
```

**Features of the Launcher:**
- Works from any directory
- Handles privileges intelligently
- Cross-platform compatible
- Auto-detects and installs dependencies
- No path or working directory issues

### Administrator/Root Privileges

The `launch.py` script intelligently handles privileges across all platforms:

#### How It Works:

1. **Automatic Detection**: Detects if you're already running as admin/root
2. **Interactive Prompt**: Asks if you want to elevate (if not already elevated)
3. **Smart Elevation**: 
   - **Windows**: Uses UAC to request admin rights
   - **Linux/macOS**: Uses `sudo` to request root privileges
4. **Continues Gracefully**: If you decline or elevation fails, continues in normal mode

#### When Admin/Root is Beneficial:

- ✅ System-wide Commix installation (to `/opt` or `Program Files`)
- ✅ Creating system symlinks
- ✅ Certain network scan types
- ✅ System-level operations

#### When Normal Mode is Sufficient:

- ✅ User-level Commix installation (to `~/.local` or `%APPDATA%`)
- ✅ Most scan types
- ✅ Testing and development
- ✅ Standard command injection testing

#### Manual Elevation (if needed):

**Windows:**
```cmd
# Right-click command prompt → "Run as administrator", then:
python launch.py
```

**Linux/macOS:**
```bash
sudo python launch.py
```

**Note:** On Linux/macOS, the launcher automatically uses `sudo` internally when you select 'y' for elevation, so you don't need to run it with sudo manually unless you want to force root mode from the start.

### Basic Workflow

1. **Configure Target**
   - Navigate to the "🎯 Target" tab
   - Enter target URL or load a request file

2. **Set Request Options** (Optional)
   - Configure HTTP headers, cookies, and connection settings in "📡 Request" tab
   - Set up authentication if needed in "🔐 Authentication" tab

3. **Configure Injection** (Optional)
   - Customize injection parameters in "💉 Injection" tab
   - Set detection options in "🔍 Detection" tab

4. **Select Post-Exploitation** (Optional)
   - Choose enumeration options in "📊 Enumeration" tab
   - Configure file access in "📁 File Access" tab

5. **Start Attack**
   - Click "🚀 Start Attack" button
   - Monitor real-time output in the console

6. **Save Configuration** (Optional)
   - Use File → Save Project to save your configuration
   - Load later with File → Open Project

## 📚 Tab Reference

### 🎯 Target Tab
- **Target URL**: Main target URL to test
- **Request File**: Load HTTP request from file
- **Bulk Testing**: Test multiple targets from file
- **POST Data**: Configure POST parameters
- **Web Crawler**: Enable crawling with depth control

### 📡 Request Tab
- **HTTP Headers**: Custom User-Agent, Referer, Host, Cookie
- **Connection Options**: Timeout, retries, delay
- **Proxy & Tor**: Proxy configuration and Tor integration
- **Error Handling**: Abort/ignore specific HTTP codes

### 🔐 Authentication Tab
- **HTTP Authentication**: Basic, Digest, Bearer
- **Form-Based Auth**: Login URL and credentials

### 💉 Injection Tab
- **Parameters**: Specify which parameters to test/skip
- **Payload Customization**: Prefix, suffix
- **Techniques**: Classic, eval, time-based, file-based
- **Tamper Scripts**: Encoding and evasion scripts
- **OS Options**: Command execution settings

### 🔍 Detection Tab
- **Test Level**: 1 (basic) to 3 (thorough)
- **Smart Detection**: Optimize testing based on heuristics
- **Calculation Skip**: Faster testing
- **Empty Parameters**: Skip empty value testing

### 📊 Enumeration Tab
- **System Info**: Hostname, OS, user information
- **Privilege Check**: Root/admin status
- **User Enumeration**: List users, passwords, privileges

### 📁 File Access Tab
- **File Read**: Read files from target
- **File Write**: Write content to target
- **File Upload**: Upload local files

### 🧩 Modules Tab
- **Shellshock**: CVE-2014-6271 detection

### ⚙️ Miscellaneous Tab
- **Verbosity**: Output detail level (0-4)
- **Session Management**: Save/load attack sessions
- **Logging**: Traffic logging and output directory
- **Advanced Options**: Encoding, charset, time limits

## 🔧 Advanced Features

### Command Generation

Click "📋 Generate Command" to:
- View the exact Commix command
- Copy to clipboard for manual execution
- Verify configuration before running

### Project Files

Save configurations as `.cproj` files:
- All tab settings preserved
- Easy sharing between team members
- Quick setup for repeated tests

### Real-Time Output

The output console provides:
- Color-coded messages (errors, warnings, info)
- Auto-scrolling during execution
- Save output to file
- Copy output to clipboard

## 🛡️ Security Notice

**⚠️ LEGAL DISCLAIMER:**

This tool is provided for educational and authorized penetration testing purposes only. Users must:

- Only test systems you own or have explicit permission to test
- Comply with all applicable laws and regulations
- Understand that unauthorized access is illegal
- Use responsibly and ethically

The developers assume no liability for misuse or damage caused by this tool.

## 🐛 Troubleshooting

### "Commix not found" Error

Ensure the `commix/` directory is in the same folder as `commix_gui.py`:

```
Commix-GUI/
├── commix/          ← Must exist
│   └── commix.py
└── commix_gui.py
```

### PyQt6 Import Errors

Reinstall PyQt6:
```bash
pip uninstall PyQt6 PyQt6-Qt6 PyQt6-sip
pip install PyQt6
```

### Permission Errors (Linux/macOS)

Run with appropriate permissions:
```bash
sudo python3 commix_gui.py  # Only if testing local services
```

### Window Not Appearing

Check Python version:
```bash
python --version  # Should be 3.7+
```

## 📖 Additional Resources

- **Commix Documentation**: https://commixproject.com
- **Commix GitHub**: https://github.com/commixproject/commix
- **Commix Wiki**: https://github.com/commixproject/commix/wiki

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This GUI wrapper follows the same license as Commix (GPL-3.0).

Commix is developed by Anastasios Stasinopoulos (@ancst).

---

**Note**: This is a GUI wrapper for Commix. All credit for the core Commix functionality goes to the original developers.

## 🎨 Screenshots

*(Add screenshots here showing different tabs and features)*

## 📝 Version History

### Version 1.0.0
- Initial release
- All Commix features implemented
- Cross-platform support
- Project save/load functionality
- Real-time output display
- Command generation
