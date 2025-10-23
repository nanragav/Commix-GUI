# 🚀 Commix GUI - Quick Reference Card

## Installation (One-Liner)
```bash
pip install -r requirements.txt && python commix_gui.py
```

## File Structure
```
📁 Commix-GUI/
├── 🎯 commix_gui.py          → Main application
├── 📁 gui_modules/            → GUI components (14 files)
├── 📁 commix/                 → Commix CLI
├── 📄 requirements.txt        → Dependencies
├── 🚀 launch_gui.bat/sh       → Launchers
└── 📚 Docs (README, guides)   → Documentation
```

## Launch Commands

| Platform | Command |
|----------|---------|
| Windows | `launch_gui.bat` or `python commix_gui.py` |
| Linux | `./launch_gui.sh` or `python3 commix_gui.py` |
| macOS | `./launch_gui.sh` or `python3 commix_gui.py` |

## GUI Tabs Quick Reference

| Tab | Icon | Purpose | Key Fields |
|-----|------|---------|------------|
| Target | 🎯 | Set target URL | URL, POST data, crawler |
| Request | 📡 | HTTP options | Headers, cookies, timeout |
| Auth | 🔐 | Authentication | Login URL, credentials |
| Injection | 💉 | Injection config | Parameters, techniques, tamper |
| Detection | 🔍 | Detection level | Test level, smart mode |
| Enumeration | 📊 | Post-exploit | Users, passwords, system info |
| File Access | 📁 | File operations | Read, write, upload |
| Modules | 🧩 | Special modules | Shellshock |
| Misc | ⚙️ | General settings | Verbosity, session, logging |

## Essential Workflows

### Quick Test (30 seconds)
```
1. Enter URL in Target tab
2. Click "🚀 Start Attack"
3. Done!
```

### Authenticated Test
```
1. Target tab → URL
2. Request tab → Cookie
3. Injection tab → Test parameter
4. Start Attack
```

### Full Enumeration
```
1. Target tab → URL
2. Enumeration tab → ✓ Retrieve everything
3. Detection tab → Level 3
4. Start Attack
```

### WAF Bypass
```
1. Target tab → URL
2. Injection tab → Tamper: space2plus,randomcase
3. Misc tab → ✓ Skip WAF
4. Start Attack
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+N` | New project |
| `Ctrl+O` | Open project |
| `Ctrl+S` | Save project |
| `Ctrl+Q` | Quit |

## Common Options

### Injection Techniques
- `c` = Classic
- `e` = Eval-based
- `t` = Time-based blind
- `f` = File-based

### Test Levels
- `1` = Basic (fast)
- `2` = Medium (balanced)
- `3` = Thorough (slow)

### Verbosity Levels
- `0` = Minimal
- `1` = Normal
- `2` = Verbose
- `3` = Very verbose
- `4` = Debug

## Popular Tamper Scripts
```
space2plus       → Space to +
base64encode     → Base64 encoding
randomcase       → Random capitalization
doublequotes     → Add quotes
hexencode        → Hex encoding
nested           → Nested encoding
```

## Output Console Colors

| Color | Meaning |
|-------|---------|
| White | Normal output |
| Red | Errors |
| Green | Success |
| Yellow | Warnings |
| Blue | Information |

## Project Files

### Save Project
```
File → Save Project (Ctrl+S)
Extension: .cproj
Format: JSON
```

### Load Project
```
File → Open Project (Ctrl+O)
Select: .cproj file
Result: All settings restored
```

## Command Generation

```
Click: 📋 Generate Command
View: Exact CLI command
Copy: To clipboard
Use: In scripts or terminal
```

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Commix not found | Check `commix/` folder exists |
| PyQt6 error | `pip install PyQt6` |
| No output | Increase verbosity level |
| Not finding injection | Increase test level |
| GUI won't start | Check Python version (3.7+) |

## Example Commands Generated

### Basic Test
```bash
python commix.py -u "http://site.com/page?id=1"
```

### With Cookie
```bash
python commix.py -u "http://site.com/page?id=1" \
  --cookie="PHPSESSID=abc123"
```

### Full Enumeration
```bash
python commix.py -u "http://site.com/page?id=1" \
  --level=3 \
  --all \
  --batch
```

### With Tamper
```bash
python commix.py -u "http://site.com/page?id=1" \
  --tamper=space2plus,randomcase \
  --technique=c,t
```

## HTTP Methods
```
GET     → Default
POST    → With --data
PUT     → With --method=PUT
DELETE  → With --method=DELETE
```

## File Paths

### Unix/Linux
```
/etc/passwd           → Users
/var/www/html         → Web root
/tmp                  → Temp
```

### Windows
```
C:\Windows\System32\drivers\etc\hosts  → Hosts file
C:\inetpub\wwwroot                     → Web root
C:\Windows\Temp                        → Temp
```

## Status Bar Messages

| Message | Meaning |
|---------|---------|
| Ready | Waiting for action |
| Attack in progress... | Running scan |
| Attack completed | Finished successfully |
| Attack finished with errors | Completed with issues |

## Best Practices

1. ✅ Start with Level 1
2. ✅ Use batch mode for automation
3. ✅ Save projects frequently
4. ✅ Check generated command
5. ✅ Monitor output in real-time
6. ✅ Get authorization first
7. ✅ Add delays for slow sites
8. ✅ Use appropriate techniques

## Common Patterns

### Test Single Parameter
```
Test Parameter: id
Skip Parameter: csrf_token
```

### Time-Based Testing
```
Technique: t
Time Delay: 3
```

### All Techniques
```
Technique: c,e,t,f
```

### Smart Testing
```
Detection → ✓ Smart
Level: 2
```

## Resource Links

- 📖 README: Complete documentation
- 🚀 QUICKSTART: Get started fast
- 📚 USER_GUIDE: Full manual
- 📊 FEATURES: Feature comparison
- 🎯 Commix Docs: https://commixproject.com

## Quick Help

### In GUI
```
Help → About      → Version info
Help → Docs       → Online resources
```

### Command Line
```
python commix_gui.py --help
```

## Version Check
```bash
# Python version
python --version

# PyQt6 installed
python -c "import PyQt6; print('OK')"

# Commix exists
ls commix/commix.py
```

---

## 📞 Emergency Quick Start

**Got 60 seconds? Here's all you need:**

```bash
# 1. Install
pip install PyQt6

# 2. Run
python commix_gui.py

# 3. Use
# - Enter URL in Target tab
# - Click Start Attack
# - Done!
```

---

**Print this card and keep it handy! 📋**
