# Session Save/Load Feature - Complete Guide

## 📁 Overview

The Commix GUI now includes a **comprehensive session save/load system** that preserves **every single field** and the **complete output console content**. You can save your work at any time and reload it later with everything exactly as you left it.

## ✨ What Gets Saved?

### ✅ All Configuration Fields (9 Tabs)

1. **Target Tab**
   - Target URL
   - Request file path
   - Log file path
   - Bulk target file
   - Sitemap URL
   - HTTP method selection
   - URL reload option
   - Crawl depth
   - Crawl exclude pattern
   - POST data

2. **Request Tab**
   - Custom User-Agent
   - Random User-Agent checkbox
   - Mobile User-Agent checkbox
   - Host header
   - Referer header
   - Cookies
   - Cookie delimiter
   - Custom headers (single and multiple)
   - Timeout value
   - Retries value
   - Delay value
   - HTTP/1.0 option
   - Force SSL option
   - Ignore redirects
   - Drop Set-Cookie
   - Proxy settings
   - Ignore proxy option
   - Tor settings
   - Tor port
   - Tor check option
   - Abort codes
   - Ignore codes
   - Parameter delimiter

3. **Authentication Tab**
   - Authentication type
   - Credentials
   - Auth URL
   - Auth data

4. **Injection Tab**
   - Test parameters
   - Skip parameters
   - Prefix string
   - Suffix string
   - Techniques to use
   - Techniques to skip
   - Time seconds
   - Max length
   - OS command
   - OS type
   - Alternate shell
   - Temp path
   - Web root
   - Tamper scripts
   - Metasploit path

5. **Detection Tab**
   - Detection level
   - Skip calculation option
   - Skip empty option
   - Smart mode
   - Failed tries count

6. **Enumeration Tab**
   - Enumerate all checkbox
   - Current user
   - Hostname
   - Is root/admin
   - System info
   - PowerShell version
   - Users list
   - Passwords
   - Privileges

7. **File Access Tab**
   - File to read
   - File to write
   - File to upload
   - Destination paths (for write/upload)

8. **Modules Tab**
   - Shellshock module

9. **Miscellaneous Tab**
   - Verbose level
   - Batch mode
   - Wizard mode
   - Offline mode
   - Session file
   - Flush session
   - Ignore session
   - Output directory
   - Traffic log file
   - No logging
   - Skip heuristics
   - Skip WAF detection
   - Codec
   - Charset
   - Time limit
   - Check internet
   - Alert command
   - Predefined answers

### ✅ Output Console Data

- **Complete text output** - Every line of Commix output
- **Output statistics** - Line count and character count
- **Formatted content** - Preserves colors and formatting information

### ✅ Metadata

- Session save timestamp
- GUI version
- Number of tabs saved
- Session format version

## 💾 How to Save a Session

### Method 1: Save (Ctrl+S)
1. Click **File → Save Project**
2. If this is a new session, you'll be prompted for a filename
3. For existing sessions, it saves immediately to the current file

### Method 2: Save As (Ctrl+Shift+S)
1. Click **File → Save Project As...**
2. Choose location and enter filename
3. File extension `.cproj` is added automatically

### What You'll See:
```
✓ Successfully saved project:

File: my_attack_session.cproj
Tabs saved: 9
Output lines: 156

All field data and console output have been saved.
```

## 📂 How to Load a Session

### Method 1: Open Project (Ctrl+O)
1. Click **File → Open Project**
2. Browse to your `.cproj` file
3. Select and click Open

### Method 2: Drag & Drop (Future Feature)
- Drag `.cproj` file onto the GUI window

### What You'll See:
```
✓ Successfully loaded project:

File: my_attack_session.cproj
Saved at: 2025-10-23T14:30:45.123456

All fields and output have been restored.
```

## 🔄 Workflow Examples

### Example 1: Long Attack Session
```
1. Configure complex attack with 20+ options
2. Start attack - takes 30 minutes
3. Attack running, producing output
4. Need to leave computer
5. Let attack complete
6. Click File → Save Project (Ctrl+S)
7. Save as "pentest_webapp_2025.cproj"
8. Close GUI

Next Day:
1. Open GUI
2. File → Open Project
3. Select "pentest_webapp_2025.cproj"
4. ✓ All settings restored
5. ✓ All 156 lines of output visible
6. Continue analysis or modify settings
```

### Example 2: Template Sessions
```
Create Reusable Templates:

1. Configure common settings for SQL injection tests
2. Save as "template_sqli.cproj"
3. Configure settings for XSS tests
4. Save as "template_xss.cproj"

Later:
1. Open template file
2. Modify only target URL
3. Run attack
4. Save as new file with target name
```

### Example 3: Report Generation
```
1. Run attack, collect output
2. Save session as "client_vuln_scan_20251023.cproj"
3. Use output for report
4. Client asks questions next week
5. Open same .cproj file
6. Review exact output again
7. Re-run specific tests if needed
```

## 📊 File Format (.cproj)

Project files use **JSON format** for human-readability and portability:

```json
{
    "version": "1.0.0",
    "saved_at": "2025-10-23T14:30:45.123456",
    "session_data": {
        "tabs_data": {
            "target": {
                "url": "http://example.com/page?id=1",
                "method": "GET",
                "data": "username=admin&password=test"
            },
            "request": {
                "agent": "Mozilla/5.0...",
                "timeout": 30,
                "tor": true
            },
            "injection": {
                "test_parameter": "id",
                "tech": "classic,eval-based"
            }
            // ... all other tabs ...
        },
        "output_data": {
            "text": "Full output text here...",
            "stats": {
                "line_count": 156,
                "char_count": 12543
            }
        },
        "metadata": {
            "timestamp": "2025-10-23T14:30:45",
            "tabs_count": 9
        }
    }
}
```

## 🛡️ Unsaved Changes Protection

The GUI automatically tracks changes and warns you:

### Scenario 1: New Project with Unsaved Work
```
1. Configure settings
2. Click File → New Project
3. Warning: "You have unsaved changes. Save before creating new project?"
   - Yes: Save current work, then create new project
   - No: Discard changes, create new project
   - Cancel: Stay in current project
```

### Scenario 2: Opening Another Project
```
1. Working on project A (modified)
2. Click File → Open Project
3. Warning: "You have unsaved changes. Save before opening another project?"
   - Yes: Save project A, then open project B
   - No: Discard changes in A, open project B
   - Cancel: Stay in project A
```

### Scenario 3: Closing GUI
```
1. Working on unsaved project
2. Click X to close
3. Warning: "Save changes before exiting?"
   - Save: Prompt for filename, then exit
   - Don't Save: Exit without saving
   - Cancel: Stay in GUI
```

## 🎯 Use Cases

### 1. **Penetration Testing Projects**
- Save entire attack configuration per target
- Maintain audit trail of tests performed
- Share session files with team members

### 2. **Research & Development**
- Save experimental technique configurations
- Compare different payload strategies
- Document successful exploitation paths

### 3. **Training & Education**
- Create example attack scenarios
- Students can load pre-configured lessons
- Practice with safe, controlled environments

### 4. **Bug Bounty Hunting**
- Save sessions per bug bounty program
- Quick switching between different targets
- Maintain evidence of testing approach

### 5. **Compliance & Documentation**
- Prove testing methodology
- Maintain complete records
- Demonstrate thorough testing coverage

## ⚙️ Advanced Features

### Session Manager Architecture
```
SessionManager Class:
├── save_session()          - Save complete session
├── load_session()          - Load complete session
├── collect_all_data()      - Gather from all tabs + output
├── restore_all_data()      - Populate all tabs + output
├── mark_modified()         - Track unsaved changes
├── is_session_modified()   - Check for changes
└── get_current_file()      - Get active file path
```

### Tab Interface Requirements
Each tab implements:
- `get_options()` - Return dictionary of all field values
- `set_options(dict)` - Load dictionary into fields
- `reset()` - Clear all fields to defaults

### Output Console Interface
- `get_output_text()` - Return complete output text
- `set_output_text(text)` - Load output text
- `get_stats()` - Return statistics dict
- `set_stats(dict)` - Load statistics

## 🔧 Troubleshooting

### Problem: File Won't Load
**Symptoms**: Error message when opening .cproj file

**Solutions**:
1. **Check file integrity**: Open in text editor, verify JSON format
2. **Version mismatch**: Older .cproj format may need migration
3. **Corrupted file**: Restore from backup

### Problem: Some Fields Not Restored
**Symptoms**: Most fields load but some remain empty

**Solutions**:
1. **Field name changed**: GUI version mismatch
2. **Backward compatibility**: Open file, save again to update format
3. **Manual entry**: Re-enter missing values

### Problem: Output Console Empty After Load
**Symptoms**: Fields load but output is blank

**Solutions**:
1. **Check file size**: Large outputs may take time to load
2. **Switch to Output tab**: Content may need tab switch to render
3. **File corruption**: Output data section may be damaged

### Problem: "Modified" Indicator Won't Clear
**Symptoms**: Window title shows * even after saving

**Solutions**:
1. **Save again**: Use Ctrl+S to ensure save completed
2. **Check status bar**: Look for confirmation message
3. **Restart GUI**: Close and reopen to reset state

## 📝 Best Practices

### 1. **Naming Conventions**
```
Good:
✓ client_webapp_sqli_2025-10-23.cproj
✓ template_blind_injection.cproj
✓ bugbounty_target_rce_attempt1.cproj

Bad:
✗ test.cproj
✗ session1.cproj
✗ asdf.cproj
```

### 2. **Organization**
```
Project Structure:
C:\Pentesting\
├── Templates\
│   ├── template_sqli.cproj
│   ├── template_xss.cproj
│   └── template_rce.cproj
├── Clients\
│   ├── ClientA\
│   │   ├── webapp_test_2025-10-20.cproj
│   │   └── api_test_2025-10-21.cproj
│   └── ClientB\
│       └── portal_scan_2025-10-23.cproj
└── Research\
    ├── new_technique_test1.cproj
    └── payload_variations.cproj
```

### 3. **Save Frequency**
- **After configuration**: Before starting attack
- **After completion**: When output is valuable
- **Before modifications**: Before changing working settings
- **End of session**: Always before closing

### 4. **Backup Strategy**
```
1. Save important sessions to cloud storage
2. Use version control (git) for critical projects
3. Export output to separate .txt files for reports
4. Keep templates in safe, backed-up location
```

## 🚀 Keyboard Shortcuts

| Action | Windows/Linux | Description |
|--------|---------------|-------------|
| **Save** | `Ctrl+S` | Save current session |
| **Save As** | `Ctrl+Shift+S` | Save with new name |
| **Open** | `Ctrl+O` | Open existing session |
| **New** | `Ctrl+N` | Create new session |
| **Quit** | `Ctrl+Q` | Exit application |

## 💡 Tips & Tricks

### Tip 1: Quick Template Switching
Create templates for common attack types, then:
1. Open template
2. Change only target URL
3. Save As with target name
4. Run attack

### Tip 2: Incremental Saves
During long attacks:
1. Let attack run and produce output
2. Don't stop attack
3. File → Save (Ctrl+S) periodically
4. Captures output so far

### Tip 3: Sharing Configurations
Send .cproj files to colleagues:
- They get exact same settings
- No manual transcription errors
- Consistent testing methodology

### Tip 4: Output Archiving
After important findings:
1. Save session .cproj (full state)
2. Also: Output Console → Save Output (just text)
3. Keep both: .cproj for rerun, .txt for reports

## 📊 File Size Expectations

| Session Type | Typical Size | Notes |
|--------------|--------------|-------|
| **Config only** | 5-20 KB | No output, just settings |
| **Short attack** | 50-200 KB | Moderate output |
| **Long attack** | 500 KB - 5 MB | Extensive output |
| **Very long attack** | 5-50 MB | Hours of output |

**Note**: JSON format is text-based, so files are larger than binary formats but remain human-readable and portable.

## 🎓 Summary

The session save/load system provides:

✅ **Complete data preservation** - Every field, every line of output  
✅ **Easy workflow** - Simple Ctrl+S to save everything  
✅ **Unsaved changes protection** - Never lose work  
✅ **Template support** - Reusable configurations  
✅ **Audit trail** - Complete documentation  
✅ **Team collaboration** - Share exact configurations  
✅ **Future-proof** - JSON format, human-readable  

**You can now save your Commix GUI sessions with confidence, knowing that everything will be preserved exactly as you configured it!** 🎯
