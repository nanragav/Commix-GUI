# Commix GUI - Mutually Exclusive Options Reference

## Overview

This document provides a complete reference for **mutually exclusive options** and **dependent options** in Commix GUI. These rules are based on the official Commix command-line tool and ensure you don't use incompatible option combinations.

## ✅ What is Option Validation?

The GUI now includes **automatic validation** that checks your configuration before running Commix. If you select incompatible options, you'll see clear error messages explaining what needs to be fixed.

## 🚫 Mutually Exclusive Options

These options **CANNOT** be used together:

### 1. User-Agent Options

**Rule**: Only ONE of these can be used at a time:
- `--mobile` (Mobile user agent)
- `--user-agent` (Custom user agent)
- `--random-agent` (Random user agent)

**Location**: Request tab

**Example Error**:
```
User-Agent options are mutually exclusive. Only one of '--mobile', '--user-agent', '--random-agent' can be used at a time.
```

**Why**: Commix can only use one User-Agent header value at a time.

---

### 2. Injection Technique Selection

**Rule**: Cannot use both:
- `--technique` (Specify techniques to use)
- `--skip-technique` (Specify techniques to skip)

**Location**: Injection tab

**Example Error**:
```
The options '--technique' and '--skip-technique' cannot be used simultaneously (i.e. only one option must be set).
```

**Why**: You either specify which techniques to use OR which to skip, not both.

---

### 3. Parameter Testing

**Rule**: Cannot use both:
- `-p` / `--test-parameter` (Test specific parameters)
- `--skip` / `--skip-parameter` (Skip specific parameters)

**Location**: Injection tab

**Example Error**:
```
The options '-p' (test parameter) and '--skip' (skip parameter) cannot be used simultaneously (i.e. only one option must be set).
```

**Why**: You either test specific parameters OR skip specific ones, not both.

---

### 4. Proxy vs Tor

**Rule**: Cannot use both:
- `--proxy` (HTTP/SOCKS proxy)
- `--tor` (Use Tor network)

**Location**: Request tab

**Example Error**:
```
The switch '--tor' is incompatible with option '--proxy'.
```

**Why**: Tor is itself a proxy system - you use one or the other.

---

### 5. Proxy vs Ignore Proxy

**Rule**: Cannot use both:
- `--proxy` (Specify proxy)
- `--ignore-proxy` (Ignore system proxy)

**Location**: Request tab

**Example Error**:
```
The option '--proxy' is incompatible with switch '--ignore-proxy'.
```

**Why**: Contradictory - can't specify a proxy and ignore proxies at the same time.

---

### 6. Target Input Methods

**Rule**: Cannot use both:
- `-r` / `--requestfile` (Request from file)
- `-u` / `--url` (Direct URL)

**Location**: Target tab

**Example Error**:
```
The '-r' option (request file) is incompatible with option '-u' ('--url').
```

**Why**: Target is either from a file OR a direct URL, not both.

---

**Rule**: Unlikely combination:
- `-r` / `--requestfile` (Request from file)
- `-l` / `--logfile` (Parse from log file)

**Location**: Target tab

**Example Error**:
```
The '-r' option (request file) is unlikely to work combined with the '-l' option (log file).
```

**Why**: Different input formats that conflict.

---

## 🔗 Dependent Options

These options **REQUIRE** other options to be set:

### 1. Tor Check Requires Tor

**Rule**: If you use `--tor-check`, you MUST also enable `--tor`

**Location**: Request tab

**Example Error**:
```
The switch '--tor-check' requires usage of '--tor' switch.
```

**Fix**: Enable the "Use Tor" option first.

---

### 2. Authentication Options (Must Be Paired)

**Rule**: Both options required together:
- `--auth-cred` (Credentials) requires `--auth-type` (Type)
- `--auth-type` (Type) requires `--auth-cred` (Credentials)

**Location**: Authentication tab

**Example Error**:
```
You must specify both '--auth-cred' and '--auth-type' options.
```

**Fix**: Set BOTH the authentication type AND credentials.

---

### 3. File Access Dependencies

**Rule**: If you use `--file-write` OR `--file-upload`, you MUST set `--file-dest`

**Location**: File Access tab

**Example Error**:
```
Host's absolute filepath to write and/or upload must be specified (i.e. '--file-dest'). The '--file-write' or '--file-upload' option requires '--file-dest' to be set.
```

**Fix**: Specify the destination path on the target server.

---

**Rule**: If you use `--file-dest`, you MUST use `--file-write` OR `--file-upload`

**Example Error**:
```
You must enter the '--file-write' or '--file-upload' parameter when using '--file-dest'.
```

**Fix**: Specify which file to write or upload.

---

## 📊 Option Validation Flow

```
User clicks "Start Attack"
         ↓
GUI collects all options
         ↓
Validator checks rules
         ↓
    ┌─────────┴─────────┐
    ↓                   ↓
✅ Valid           ❌ Invalid
    ↓                   ↓
Commix runs      Error displayed
                 (with fix suggestions)
```

## 🔧 How to Use in GUI

### Automatic Validation

1. Configure your options in the GUI tabs
2. Click "🚀 Start Attack"
3. **Validation runs automatically**
4. If errors found:
   - ❌ Commix won't run
   - Error messages displayed in Output Console
   - Each error numbered and explained
5. Fix the errors and try again

### Example Validation Error Output

```
❌ VALIDATION ERRORS FOUND:
================================================================================
1. User-Agent options are mutually exclusive. Only one of '--mobile', 
   '--user-agent' can be used at a time.
   
2. You must specify both '--auth-cred' and '--auth-type' options. 
   '--auth-cred' requires '--auth-type' to be set.
================================================================================

⚠️  Please fix the above errors before running Commix.
```

## 💡 Quick Fix Guide

| Error Message Contains | Quick Fix |
|------------------------|-----------|
| "User-Agent options are mutually exclusive" | Uncheck all but ONE User-Agent option |
| "technique" and "skip-technique" cannot be used simultaneously" | Use only ONE of these |
| "'-p' and '--skip' cannot be used simultaneously" | Use only ONE of these |
| "'--proxy' is incompatible with '--tor'" | Use only ONE of these |
| "'--tor-check' requires '--tor'" | Enable "Use Tor" option |
| "both '--auth-cred' and '--auth-type'" | Set BOTH authentication options |
| "'--file-write' requires '--file-dest'" | Set the destination path |
| "'-r' is incompatible with '-u'" | Use only ONE target input method |

## 🧪 Testing Your Configuration

### Test Scenario 1: Valid Configuration
```
✅ Target URL: http://example.com?id=1
✅ Custom User-Agent: "MyBot/1.0"
✅ Technique: classic
✅ Test Parameter: id
```
**Result**: ✅ Passes validation

### Test Scenario 2: Invalid Configuration
```
❌ Target URL: http://example.com?id=1
❌ Mobile User-Agent: ✓ (enabled)
❌ Random User-Agent: ✓ (enabled)
```
**Result**: ❌ Validation Error - Multiple User-Agents

### Test Scenario 3: Missing Dependencies
```
❌ Authentication Type: Basic
❌ Authentication Credentials: (empty)
```
**Result**: ❌ Validation Error - Missing credentials

## 📝 Implementation Details

### Validator Location
- **File**: `gui_modules/option_validator.py`
- **Class**: `OptionValidator`
- **Integration**: Runs automatically in `CommixRunner` before execution

### Validation Rules

Each rule is implemented as a dedicated method:

1. `validate_user_agent_options()` - User-Agent exclusivity
2. `validate_technique_options()` - Technique selection
3. `validate_parameter_options()` - Parameter testing
4. `validate_proxy_options()` - Proxy configurations
5. `validate_tor_options()` - Tor dependencies
6. `validate_auth_options()` - Authentication pairing
7. `validate_target_options()` - Target input methods
8. `validate_file_access_options()` - File operation dependencies

### How It Works

```python
# Pseudo-code
validator = OptionValidator()
is_valid, errors, warnings = validator.validate_all(options)

if not is_valid:
    # Show errors, don't run Commix
    display_errors(errors)
else:
    # All good, run Commix
    execute_commix(options)
```

## 🆘 Troubleshooting

### Problem: Validation error but I think it's wrong

**Solution**:
1. Check the official Commix documentation
2. These rules come directly from Commix source code
3. The CLI tool enforces the same restrictions

### Problem: Can I disable validation?

**Answer**: No. Validation prevents Commix from failing with cryptic errors. It's better to catch issues in the GUI than have Commix crash during execution.

### Problem: Validation passes but Commix still errors

**Possible Causes**:
1. **Input format errors** (e.g., invalid URL format)
2. **Target unreachable**
3. **Permission issues**
4. **Commix bugs** (rare)

**Solution**: Check the Commix error output in the console for specific details.

## 📚 References

- **Commix Source**: https://github.com/commixproject/commix
- **Rules Source**: `src/core/main.py` (lines 95-909)
- **Official Wiki**: https://github.com/commixproject/commix/wiki

## ✨ Summary

The option validator ensures:
- ✅ **100% accuracy** - Rules match official Commix behavior
- ✅ **Clear errors** - Know exactly what's wrong
- ✅ **Time saved** - Catch mistakes before execution
- ✅ **Better UX** - User-friendly error messages
- ✅ **Prevents crashes** - No conflicting options reach Commix

**Remember**: If you see a validation error, it means Commix itself would reject the same combination. The validator is helping you succeed! 🎯
