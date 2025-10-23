# ⚡ Quick Start - Commix GUI

## 🚀 Fastest Way to Get Started

### Step 1: Download/Clone

```bash
git clone <your-repo-url>
cd Commix-GUI
```

### Step 2: Launch

```bash
python launch.py
```

That's it! The launcher handles everything else automatically.

---

## 🎯 What Happens Next?

### First Launch Scenario

```
1. Python launcher starts
   ↓
2. Checks admin privileges
   ↓
3. Prompts if you want elevation (optional)
   ↓
4. Checks Python dependencies
   ↓
5. Installs PyQt6 if needed
   ↓
6. Opens Commix GUI
   ↓
7. Setup dialog appears
   ↓
8. Choose installation method:
   • Use local commix/ folder (if present) ✅ Easiest
   • Install from GitHub (if not found)
   • Browse to custom location
   ↓
9. Click "Install Commix" or "Continue"
   ↓
10. Start testing!
```

---

## 💡 Typical User Scenarios

### Scenario A: You Have `commix/` Folder

**What you have:**
```
Commix-GUI/
├── commix/              ← You have this
│   ├── commix.py
│   └── src/
├── launch.py
└── commix_gui.py
```

**What to do:**
```bash
python launch.py
```

**What happens:**
1. GUI opens
2. Dialog shows: "Use local Commix folder and run --install"
3. Click "Install Commix"
4. Done! (No admin needed)

**Time:** < 30 seconds

---

### Scenario B: No `commix/` Folder

**What you have:**
```
Commix-GUI/
├── launch.py
├── commix_gui.py
└── gui_modules/
```

**What to do:**
```bash
python launch.py
```

**What happens:**
1. GUI opens
2. Dialog shows: "Commix not found"
3. Choose "Install from GitHub"
4. May prompt for admin (for system-wide install)
5. Downloads and installs automatically
6. Done!

**Time:** 1-2 minutes (depending on internet)

---

### Scenario C: Already Installed System-Wide

**What you have:**
- Commix already in `/opt/commix` or `C:\Program Files\commix`
- Or commix command available in PATH

**What to do:**
```bash
python launch.py
```

**What happens:**
1. GUI opens
2. Dialog shows: "✓ Commix found (system installation)"
3. Click "Continue"
4. Start testing immediately!

**Time:** < 5 seconds

---

## 🔧 Advanced Options

### Run Without Admin Prompt

```bash
python launch.py --skip-admin-prompt
```

### Force Admin Mode

**Windows:**
```cmd
# Option 1: Right-click
Right-click launch.py → "Run as administrator"

# Option 2: Batch file
launch_gui_admin.bat

# Option 3: Command
runas /user:Administrator "python launch.py"
```

**Linux/macOS:**
```bash
sudo python launch.py
```

### Direct GUI Launch (No Launcher)

```bash
# Windows
python commix_gui.py

# Linux/macOS
python3 commix_gui.py
```

**Note:** Direct launch won't handle admin privileges or dependency checks automatically.

---

## 📝 First Attack

Once GUI is running:

### 1. Set Target
```
🎯 Target tab
URL: http://testsite.com/page.php?id=1
```

### 2. Configure (Optional)
```
📡 Request tab: Set headers, timeout
💉 Injection tab: Choose technique
```

### 3. Start Attack
```
Click: 🚀 Start Attack
```

### 4. View Results
```
Switch to: Output Console tab
Watch real-time output
```

### 5. Save Configuration
```
Menu: File → Save Project
Name: my-test.cproj
```

---

## ⚙️ Configuration Examples

### Basic GET Request

```
Target: http://example.com/page.php?id=1
Method: GET (default)
Click: 🚀 Start Attack
```

### POST Request with Data

```
🎯 Target tab:
URL: http://example.com/login.php
POST Data: username=admin&password=test

Click: 🚀 Start Attack
```

### With Custom Headers

```
🎯 Target: http://example.com/api/
📡 Request tab:
User-Agent: Custom/1.0
Cookie: session=abc123

Click: 🚀 Start Attack
```

### Through Proxy

```
📡 Request tab:
Proxy: 127.0.0.1:8080
☑ Use Proxy

Click: 🚀 Start Attack
```

---

## 🎓 Learning Path

### Beginner

1. **Day 1**: Install and launch
2. **Day 2**: Test basic GET parameter
3. **Day 3**: Try POST data injection
4. **Day 4**: Explore enumeration options
5. **Day 5**: Save and load projects

### Intermediate

1. **Week 1**: Master all injection techniques
2. **Week 2**: Use tamper scripts
3. **Week 3**: Configure authentication
4. **Week 4**: Integrate with proxy tools
5. **Week 5**: Automate with project files

### Advanced

1. Custom tamper scripts
2. Multi-target bulk scanning
3. Complex authentication scenarios
4. Integration with CI/CD
5. Enterprise deployment

---

## 🐛 Common First-Time Issues

### Issue: "Python not found"

**Solution:**
```bash
# Install Python 3.7+
# Windows: https://python.org/downloads
# Linux: sudo apt install python3
# macOS: brew install python3

# Verify
python --version
```

### Issue: "PyQt6 not installed"

**Solution:**
```bash
# Auto-installed by launcher, but manual:
pip install PyQt6

# Or
pip install -r requirements.txt
```

### Issue: "Commix not found"

**Solution:**
```bash
# Let GUI install automatically
python launch.py
# Then click "Install Commix" in dialog

# Or manually:
git clone https://github.com/commixproject/commix.git
```

### Issue: "Permission denied"

**Solution:**
```bash
# Run with admin/sudo
# Windows
launch_gui_admin.bat

# Linux/macOS
sudo python launch.py
```

---

## 📱 Quick Reference Card

```
╔════════════════════════════════════════╗
║       COMMIX GUI QUICK START           ║
╠════════════════════════════════════════╣
║ LAUNCH:                                ║
║   python launch.py                     ║
║                                        ║
║ SET TARGET:                            ║
║   🎯 Target tab → Enter URL            ║
║                                        ║
║ START:                                 ║
║   Click 🚀 Start Attack                ║
║                                        ║
║ VIEW OUTPUT:                           ║
║   Output Console tab                   ║
║                                        ║
║ SAVE:                                  ║
║   File → Save Project                  ║
║                                        ║
║ HELP:                                  ║
║   Help → Documentation                 ║
╚════════════════════════════════════════╝
```

---

## 📚 Next Steps

After quick start:

1. **Read:** [USER_GUIDE.md](USER_GUIDE.md) - Complete user manual
2. **Explore:** [FEATURES.md](FEATURES.md) - All available features
3. **Reference:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command reference
4. **Install:** [INSTALLATION.md](INSTALLATION.md) - Detailed installation

---

## 🎉 You're Ready!

```bash
python launch.py
```

Start testing in under 1 minute! 🚀

**Questions?**
- Check docs/ folder for detailed guides
- Review example projects
- Explore all tabs in the GUI

**Happy Testing!** 🎯
