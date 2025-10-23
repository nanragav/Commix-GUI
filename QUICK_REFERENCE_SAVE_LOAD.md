# Quick Reference: Session Save/Load

## What Gets Saved?
✅ **ALL 9 configuration tabs** - Every single field  
✅ **Complete output console** - All text and formatting  
✅ **Session metadata** - Timestamps and stats  

## Quick Actions

### Save Session
```
Keyboard: Ctrl+S
Menu: File → Save Project
```
- First time: Choose filename
- Subsequent: Saves immediately
- Format: .cproj (JSON)

### Load Session
```
Keyboard: Ctrl+O
Menu: File → Open Project
```
- Browse for .cproj file
- Everything restored instantly
- Output console included

### New Session
```
Keyboard: Ctrl+N
Menu: File → New Project
```
- Warns if unsaved changes
- Clears all fields
- Clears output console

### Save As
```
Keyboard: Ctrl+Shift+S
Menu: File → Save Project As...
```
- Choose new filename
- Keep original unchanged
- Create copies/variants

## What's Included in Save?

### Target Tab (10 fields)
- URL, request file, log file, bulk file
- Sitemap, method, reload, crawl settings
- POST data

### Request Tab (24 fields)
- User agents, headers, cookies
- Timeouts, retries, delays
- Proxy, Tor, HTTP options

### Authentication Tab (4 fields)
- Type, credentials, URL, data

### Injection Tab (13 fields)
- Parameters, prefix/suffix
- Techniques, timing
- OS commands, paths, tamper scripts

### Detection Tab (5 fields)
- Level, skip options, smart mode
- Failed tries

### Enumeration Tab (10 fields)
- All enum checkboxes
- User, system, password options

### File Access Tab (5 fields)
- Read, write, upload paths
- Destination paths

### Modules Tab (1 field)
- Shellshock module

### Misc Tab (18 fields)
- Verbose, batch, wizard
- Session management
- Output options
- Codec, limits, alerts

### Output Console
- Complete text output
- Line/character counts
- All formatting preserved

## File Format

```json
{
  "version": "1.0.0",
  "saved_at": "2025-10-23T14:30:45",
  "session_data": {
    "tabs_data": { /* all tabs */ },
    "output_data": { /* console */ },
    "metadata": { /* info */ }
  }
}
```

## Typical Workflow

```
1. Configure attack settings
2. Run attack (output generated)
3. Ctrl+S to save
4. Name: "target_scan_2025-10-23.cproj"
5. Close GUI

Next time:
1. Ctrl+O to open
2. Select .cproj file
3. ✓ All settings restored
4. ✓ All output visible
5. Continue work
```

## Protection Features

### Unsaved Changes Warning
- New project while modified → Asks to save
- Open project while modified → Asks to save  
- Close GUI while modified → Asks to save

### Window Title Indicator
```
Normal: "Commix GUI - Command Injection Tool"
With file: "Commix GUI - mysession.cproj"
Modified: "Commix GUI - mysession.cproj *"
```

## Use Cases

🎯 **Penetration Testing** - Save per target  
📚 **Training** - Create lesson templates  
🐛 **Bug Bounty** - Quick target switching  
🔬 **Research** - Document experiments  
📋 **Compliance** - Audit trail  

## File Size Guide

| Type | Size | Example |
|------|------|---------|
| Config only | ~5-20 KB | Just settings |
| Short attack | ~50-200 KB | Few minutes |
| Long attack | ~500 KB-5 MB | Extended test |
| Very long | ~5-50 MB | Hours of output |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+N` | New Project |
| `Ctrl+O` | Open Project |
| `Ctrl+S` | Save Project |
| `Ctrl+Shift+S` | Save Project As |
| `Ctrl+Q` | Quit |

## Tips

💡 **Templates**: Save common configs as templates  
💡 **Naming**: Use descriptive names with dates  
💡 **Backup**: Keep important sessions backed up  
💡 **Share**: Send .cproj files to teammates  

## Troubleshooting

**File won't load?**
- Check JSON syntax (open in text editor)
- Verify .cproj extension
- Check file permissions

**Fields not restored?**
- Update GUI to latest version
- Resave with new format

**Output missing?**
- Switch to Output Console tab
- Check file size (may be large)

---

**For complete documentation, see: SESSION_SAVE_LOAD.md**
