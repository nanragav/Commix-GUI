# Commix GUI - Complete User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Interface Overview](#interface-overview)
4. [Tab Reference](#tab-reference)
5. [Common Scenarios](#common-scenarios)
6. [Tips & Tricks](#tips--tricks)
7. [Troubleshooting](#troubleshooting)

---

## Introduction

Commix GUI is a cross-platform graphical interface for Commix (Command Injection Exploitation Tool). It provides all CLI features in an intuitive, user-friendly interface.

### Key Benefits
- ✅ No need to memorize command syntax
- ✅ Visual organization of options
- ✅ Real-time output monitoring
- ✅ Save and load configurations
- ✅ Generate CLI commands
- ✅ Cross-platform (Windows, Linux, macOS)

---

## Installation

### Prerequisites
- Python 3.7+
- PyQt6

### Quick Install

**Option 1: Using launcher scripts**

Windows:
```cmd
launch_gui.bat
```

Linux/macOS:
```bash
chmod +x launch_gui.sh
./launch_gui.sh
```

**Option 2: Manual**

```bash
pip install -r requirements.txt
python commix_gui.py
```

---

## Interface Overview

### Main Window Components

```
┌─────────────────────────────────────────────────┐
│  File  Edit  View  Help                         │
├─────────────────────────────────────────────────┤
│  [New] [Open] [Save]                            │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │ 🎯Target │📡Request│🔐Auth│💉Injection │  │ │
│  │─────────────────────────────────────────│  │ │
│  │                                         │  │ │
│  │        Configuration Tabs               │  │ │
│  │                                         │  │ │
│  └───────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────┐ │
│  │ Output Console                          │  │ │
│  │ [Real-time output with colors]          │  │ │
│  └───────────────────────────────────────────┘ │
│  [🚀 Start] [⏹️ Stop] [📋 Generate Command]    │
│─────────────────────────────────────────────────│
│  Status: Ready                                  │
└─────────────────────────────────────────────────┘
```

### Menu Bar

**File Menu**
- New Project (Ctrl+N): Clear all settings
- Open Project (Ctrl+O): Load saved configuration
- Save Project (Ctrl+S): Save current configuration
- Save As (Ctrl+Shift+S): Save with new name
- Exit (Ctrl+Q): Close application

**Edit Menu**
- Clear Output: Clear console window

**Help Menu**
- About: Version information
- Documentation: Links to resources

---

## Tab Reference

### 🎯 Target Tab

**Purpose**: Configure target URL and basic request settings

**Fields:**

1. **Target URL**
   - Main URL to test
   - Example: `http://example.com/page.php?id=1`

2. **Request File**
   - Load HTTP request from file
   - Use Burp Suite saved requests
   - Click "Browse..." to select file

3. **Proxy Log File**
   - Parse targets from proxy logs
   - Supports Burp/ZAP formats

4. **Bulk File**
   - Test multiple targets
   - One URL per line
   - Click "Browse..." to select file

5. **Sitemap URL**
   - Load targets from sitemap.xml
   - Example: `http://example.com/sitemap.xml`

6. **HTTP Method**
   - GET (default)
   - POST, PUT, DELETE, etc.

7. **Crawler Settings**
   - Crawl Depth: 0-10 (0=disabled)
   - Exclude Pattern: Regex to skip pages

8. **POST Data**
   - POST parameters
   - Example: `username=admin&password=test`

**Example Configuration:**
```
URL: http://testsite.com/products.php?id=1
Method: GET
POST Data: (empty for GET)
```

---

### 📡 Request Tab

**Purpose**: Configure HTTP headers and connection options

**Sections:**

#### HTTP Headers
- **User-Agent**: Custom browser identification
- **Random Agent**: Use random User-Agent
- **Mobile**: Imitate smartphone
- **Host Header**: Override HTTP Host
- **Referer**: HTTP Referer header
- **Cookie**: Session cookies
- **Extra Headers**: Custom headers

**Example:**
```
Cookie: PHPSESSID=abc123; user=admin
Header: X-Forwarded-For: 127.0.0.1
```

#### Connection Options
- **Timeout**: Seconds before timeout (default: 30)
- **Retries**: Connection retry attempts (default: 3)
- **Delay**: Delay between requests (seconds)
- **HTTP/1.0**: Force HTTP/1.0 protocol
- **Force SSL**: Require HTTPS
- **Ignore Redirects**: Don't follow 302/301

#### Proxy & Tor
- **Proxy**: HTTP/SOCKS proxy URL
  - Example: `http://127.0.0.1:8080`
- **Tor**: Use Tor network
- **Tor Port**: Tor proxy port (default: 8118)
- **Check Tor**: Verify Tor usage

#### Error Handling
- **Abort on Error Code**: Stop if specific HTTP codes
  - Example: `401,403`
- **Ignore Error Code**: Continue despite errors
  - Example: `404,500`

---

### 🔐 Authentication Tab

**Purpose**: Configure authentication mechanisms

#### HTTP Authentication
- **Auth Type**: Basic, Digest, or Bearer
- **Credentials**: username:password format
  - Example: `admin:P@ssw0rd`

#### Form-Based Authentication
- **Login URL**: Login page URL
  - Example: `http://example.com/login.php`
- **Login Data**: POST data for login
  - Example: `user=admin&pass=test&submit=Login`

**Use Case:**
Test authenticated areas by logging in first.

---

### 💉 Injection Tab

**Purpose**: Configure injection parameters and techniques

#### Parameter Testing
- **Test Parameter(s)**: Comma-separated list
  - Example: `id,user,category`
- **Skip Parameter(s)**: Exclude from testing
  - Example: `csrf_token,submit`

#### Injection Payload
- **Prefix**: Add before payload
  - Example: `'` or `"`
- **Suffix**: Add after payload
  - Example: `'` or `--`

#### Techniques
- **Technique(s)**: Injection methods to use
  - `c` = Classic
  - `e` = Eval-based
  - `t` = Time-based blind
  - `f` = File-based
  - Example: `c,t` (classic and time-based)

- **Skip Technique(s)**: Methods to avoid
  - Example: `f` (skip file-based)

#### Time-Based Options
- **Time Delay**: Seconds for sleep command (default: 1)
- **Max Output Length**: Character limit (default: 10000)

#### OS Options
- **Single OS Command**: Execute one command
  - Example: `whoami`
- **Force OS**: Windows or Unix
- **Alternative Shell**: Python, etc.

#### File-Based Options
- **Temp Path**: Temporary directory
  - Example: `/tmp` or `C:\Windows\Temp`
- **Web Root**: Document root
  - Example: `/var/www/html`

#### Tamper Scripts
Multiple scripts, comma-separated:
- `space2plus`: Space to +
- `base64encode`: Base64 encoding
- `randomcase`: Random capitalization
- `doublequotes`: Add double quotes
- And more...

**Example:**
```
Test Parameters: id
Technique: c,t
Tamper: space2plus,randomcase
```

---

### 🔍 Detection Tab

**Purpose**: Configure detection and testing options

#### Detection Configuration
- **Test Level**: 1-3
  - Level 1: Basic (fast, less thorough)
  - Level 2: Medium (balanced)
  - Level 3: Thorough (slow, comprehensive)

- **Skip Calculation**: Faster testing
- **Skip Empty Parameters**: Ignore empty values
- **Smart Detection**: Only thorough if heuristics positive

#### File-Based Technique
- **Failed Tries**: Retry attempts for file-based

**Recommended:**
- Start with Level 1
- Use Level 3 only when needed
- Enable Smart Detection for efficiency

---

### 📊 Enumeration Tab

**Purpose**: Select post-exploitation enumeration

#### System Information
- ✓ **Retrieve Everything**: All options below
- ✓ **Current User**: Get username
- ✓ **Hostname**: Get machine name
- ✓ **Is Root/Admin**: Check privileges
- ✓ **System Info**: OS details
- ✓ **PowerShell Version**: Windows only

#### User Information
- ✓ **System Users**: List all users
- ✓ **Passwords**: Password hashes
- ✓ **Privileges**: User permissions

**Note:** Executes AFTER successful injection

---

### 📁 File Access Tab

**Purpose**: Read, write, and upload files

#### File Read
- **File to Read**: Remote file path
  - Example: `/etc/passwd`
  - Example: `C:\Windows\System32\drivers\etc\hosts`

#### File Write
- **Content to Write**: Text to write
- **Destination Path**: Where to write
  - Example: `/tmp/test.txt`

#### File Upload
- **Local File**: File on your computer
  - Click "Browse..." to select
- **Remote Destination**: Target path
  - Example: `/var/www/html/shell.php`

**Security Warning:**
Only upload to systems you own or have permission to test!

---

### 🧩 Modules Tab

**Purpose**: Enable special detection modules

#### Available Modules
- ✓ **Shellshock**: Test for CVE-2014-6271
  - Tests HTTP headers and CGI scripts
  - Famous Bash vulnerability

**Note:** More modules may be added in future versions

---

### ⚙️ Miscellaneous Tab

**Purpose**: General settings and advanced options

#### General Options
- **Verbosity Level**: 0-4 (0=minimal, 4=debug)
- **Batch Mode**: No user prompts
- **Wizard**: Beginner-friendly mode
- **Offline Mode**: No internet checks

#### Session Management
- **Session File**: Save/load session
  - Example: `session.sqlite`
- **Flush Session**: Clear session data
- **Ignore Session**: Don't use cached data

#### Output & Logging
- **Output Directory**: Save results here
- **Traffic Log**: Log HTTP traffic
- **No Logging**: Disable file logging

#### Detection & Filtering
- **Skip Heuristics**: Disable auto-detection
- **Skip WAF**: Don't detect WAF/IPS

#### Advanced Options
- **Character Encoding**: utf-8, ascii, etc.
- **Injection Charset**: Custom character set
- **Time Limit**: Max execution time (seconds)
- **Check Internet**: Verify connectivity

#### Alerts
- **Alert Command**: Run on successful injection
  - Example: `notify-send "Injection found!"`

#### Predefined Answers
- **Answers**: Auto-respond to prompts
  - Example: `quit=N,follow=N`

---

## Common Scenarios

### Scenario 1: Basic GET Parameter Test

**Goal:** Test a single GET parameter

**Steps:**
1. **Target Tab**
   - URL: `http://example.com/page.php?id=1`

2. **Click "🚀 Start Attack"**

**Output:** Real-time results in console

---

### Scenario 2: POST Request with Authentication

**Goal:** Test POST parameter in authenticated area

**Steps:**
1. **Target Tab**
   - URL: `http://example.com/admin/profile.php`
   - POST Data: `user_id=1&action=view`

2. **Request Tab**
   - Cookie: `PHPSESSID=your_session_id`

3. **Injection Tab**
   - Test Parameter: `user_id`

4. **Click "🚀 Start Attack"**

---

### Scenario 3: Bypass WAF with Tamper Scripts

**Goal:** Evade WAF detection

**Steps:**
1. **Target Tab**
   - URL: `http://protected-site.com/page?id=1`

2. **Injection Tab**
   - Tamper Scripts: `space2plus,randomcase,base64encode`

3. **Detection Tab**
   - Test Level: 2

4. **Miscellaneous Tab**
   - Skip WAF: ✓ (checked)

5. **Click "🚀 Start Attack"**

---

### Scenario 4: Full Enumeration After Exploitation

**Goal:** Gather all possible information

**Steps:**
1. **Target Tab**
   - URL: `http://vulnerable-site.com/item?id=5`

2. **Enumeration Tab**
   - ✓ Retrieve Everything

3. **File Access Tab**
   - File to Read: `/etc/passwd`

4. **Click "🚀 Start Attack"**

**Result:** Full system enumeration + file contents

---

### Scenario 5: Time-Based Blind Injection

**Goal:** Test for blind injection

**Steps:**
1. **Target Tab**
   - URL: `http://site.com/search?q=test`

2. **Injection Tab**
   - Technique: `t` (time-based)
   - Time Delay: 3 seconds
   - Test Parameter: `q`

3. **Detection Tab**
   - Test Level: 2

4. **Miscellaneous Tab**
   - Batch Mode: ✓

5. **Click "🚀 Start Attack"**

---

## Tips & Tricks

### 💡 Productivity Tips

1. **Save Frequently**
   - Use Ctrl+S to save configurations
   - Create templates for common tests

2. **Use Batch Mode**
   - Enable for unattended testing
   - Prevents interactive prompts

3. **Generate Commands**
   - Click "📋 Generate Command"
   - Learn CLI syntax
   - Use in scripts

4. **Start Small**
   - Begin with Level 1 detection
   - Increase only if needed

5. **Monitor Output**
   - Watch real-time console
   - Look for success messages

### 🎯 Testing Tips

1. **Test Single Parameters First**
   - Isolate injectable params
   - Faster and more accurate

2. **Use Appropriate Techniques**
   - Fast sites: All techniques
   - Slow sites: Avoid time-based initially

3. **WAF Bypass**
   - Try different tamper combinations
   - Randomcase + space2plus often effective

4. **Session Management**
   - Save sessions for long tests
   - Resume if interrupted

5. **Verbosity**
   - Use level 1-2 for normal testing
   - Use level 3-4 for debugging

### 🔒 Security Tips

1. **Always Get Permission**
   - Only test authorized systems
   - Document authorization

2. **Use Responsibly**
   - Don't overload servers
   - Add delays if needed

3. **Cleanup**
   - Remove uploaded files
   - Clear any artifacts

4. **Legal Compliance**
   - Follow local laws
   - Respect bug bounty rules

---

## Troubleshooting

### Problem: "Commix not found" error

**Solution:**
```
Ensure structure:
Commix-GUI/
├── commix/
│   └── commix.py
└── commix_gui.py
```

---

### Problem: PyQt6 import error

**Solution:**
```bash
pip uninstall PyQt6 PyQt6-Qt6 PyQt6-sip
pip install PyQt6
```

---

### Problem: No output showing

**Solutions:**
1. Check verbosity level (increase it)
2. Look for errors in red
3. Verify target URL is accessible
4. Check firewall/proxy settings

---

### Problem: GUI won't start

**Solutions:**
1. Check Python version: `python --version` (need 3.7+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Try launcher script: `launch_gui.bat` or `launch_gui.sh`

---

### Problem: Attack not finding injection

**Solutions:**
1. Increase test level (Detection tab)
2. Try different techniques
3. Add tamper scripts
4. Check parameter syntax
5. Verify target is actually vulnerable

---

### Problem: Session errors

**Solutions:**
1. Click "Flush Session" checkbox
2. Delete old session files
3. Use "Ignore Session" for fresh start

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+N | New Project |
| Ctrl+O | Open Project |
| Ctrl+S | Save Project |
| Ctrl+Shift+S | Save As |
| Ctrl+Q | Quit |

---

## Support & Resources

- **Commix Project**: https://commixproject.com
- **GitHub**: https://github.com/commixproject/commix
- **Documentation**: https://github.com/commixproject/commix/wiki

---

## License

This GUI wrapper follows Commix's GPL-3.0 license.

**Commix Author:** Anastasios Stasinopoulos (@ancst)

---

**Happy Ethical Hacking! 🔒**
