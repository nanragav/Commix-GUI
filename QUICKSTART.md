# Commix GUI - Quick Start Guide

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Launch GUI

**Windows:**
```cmd
launch_gui.bat
```
or
```cmd
python commix_gui.py
```

**Linux/macOS:**
```bash
chmod +x launch_gui.sh
./launch_gui.sh
```
or
```bash
python3 commix_gui.py
```

### Step 3: Configure and Attack

1. Enter target URL in the **Target** tab
2. Click **🚀 Start Attack**
3. Monitor results in real-time

## 📋 Example: Basic SQL Injection Test

1. **Target Tab:**
   - URL: `http://testphp.vulnweb.com/listproducts.php?cat=1`

2. **Click "Start Attack"**

3. View results in output console

## 📋 Example: POST Request with Cookie

1. **Target Tab:**
   - URL: `http://example.com/admin/profile.php`
   - POST Data: `id=1&action=update`

2. **Request Tab:**
   - Cookie: `PHPSESSID=abc123; user=admin`

3. **Injection Tab:**
   - Test Parameter: `id`

4. **Click "Start Attack"**

## 📋 Example: Full Enumeration

1. **Target Tab:**
   - URL: `http://example.com/page.php?id=1`

2. **Detection Tab:**
   - Test Level: `3` (thorough)

3. **Enumeration Tab:**
   - ✓ Check "Retrieve everything"

4. **Click "Start Attack"**

## 💡 Tips

### Save Time with Projects

- **Save Project** (Ctrl+S): Save current configuration
- **Open Project** (Ctrl+O): Load saved configuration
- Share `.cproj` files with team members

### Generate Commands

- Click **📋 Generate Command** to see the exact Commix command
- Copy and run manually in terminal if needed
- Useful for scripting and automation

### Batch Mode

For non-interactive testing:
- **Miscellaneous Tab** → Check "Never ask for user input (batch mode)"
- Prevents interactive prompts during execution

### Verbose Output

For detailed debugging:
- **Miscellaneous Tab** → Set "Verbosity Level" to `3` or `4`
- See all HTTP requests and responses

## 🎯 Common Use Cases

### 1. Test Single Parameter

```
Target: http://site.com/page.php?id=1&user=admin
Injection Tab → Test Parameter: id
```

### 2. Test with Custom Headers

```
Request Tab:
- User-Agent: Custom Agent
- Referer: http://trusted-site.com
- Header: X-Forwarded-For: 127.0.0.1
```

### 3. Use Tamper Scripts for WAF Bypass

```
Injection Tab → Tamper Scripts:
space2plus,base64encode,randomcase
```

### 4. Time-Based Blind Injection

```
Injection Tab:
- Technique: t (time-based)
- Time Delay: 3 seconds
```

### 5. File Upload After Exploitation

```
File Access Tab:
- Local File: C:\path\to\shell.php
- Remote Destination: /var/www/html/uploads/shell.php
```

## ⚠️ Important Notes

1. **Always get authorization** before testing any system
2. **Start with low test levels** (level 1) to avoid detection
3. **Use batch mode** for automated testing
4. **Save sessions** to resume interrupted scans
5. **Check logs** in the output directory for detailed results

## 🔧 Keyboard Shortcuts

- `Ctrl+N`: New Project
- `Ctrl+O`: Open Project
- `Ctrl+S`: Save Project
- `Ctrl+Q`: Quit

## 📞 Need Help?

- Check the full **README.md** for detailed documentation
- Visit Commix documentation: https://commixproject.com
- Check Commix GitHub: https://github.com/commixproject/commix

---

**Happy (Ethical) Hacking! 🔒**
