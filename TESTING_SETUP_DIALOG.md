# Testing the Commix Setup Dialog

## Changes Made

### 1. launch.py
- **Fixed**: QApplication is now created BEFORE importing/creating CommixGUI
- **Added**: Better exception handling for SystemExit (when user cancels setup)
- **Why**: Qt dialogs require QApplication to exist first

### 2. commix_setup_dialog.py
- **Added**: `setModal(True)` to ensure dialog is modal
- **Added**: `WindowStaysOnTopHint` flag to keep dialog visible
- **Removed**: Debug print statement
- **Why**: Ensures dialog appears on top and blocks interaction with parent

## How It Works

### When Commix IS Found (Normal Mode - No Admin):
1. Dialog appears showing "✓ Commix found ({location} installation)"
2. Shows admin warning (recommending elevation)
3. Shows only "Continue" button (Update button hidden)
4. **Waits for user to click Continue** (no auto-close)
5. GUI launches after user clicks Continue

### When Commix IS Found (Admin Mode):
1. Dialog appears showing "✓ Commix found - Running as Administrator"
2. Shows both "Update Commix" and "Continue" buttons
3. **Waits for user to click Continue or Update** (no auto-close)
4. User can review settings or update Commix
5. GUI launches after user clicks Continue

### When Commix IS NOT Found:
1. Dialog appears showing "✗ Commix not found on this system"
2. Shows installation options:
   - Install from GitHub
   - Browse for existing installation
3. User MUST take action:
   - Click "Install Commix" button
   - Click "Browse" to locate existing installation
   - Click "Cancel" to exit
4. Dialog stays open until user acts
5. NO auto-close (requires user input)

## Testing

### Test 1: With Commix Installed (Normal Mode)
```cmd
python launch.py
# When prompted: select 'n' for no admin
```
**Expected**: 
- Dialog appears and stays open
- Shows green checkmark
- Shows admin warning
- Shows only "Continue" button (no Update button)
- **Waits for user to click Continue**
- GUI launches after Continue clicked

### Test 1b: With Commix Installed (Admin Mode)
```cmd
# Right-click Command Prompt → Run as administrator
python launch.py
# OR when prompted: select 'y' for admin
```
**Expected**: 
- Dialog appears showing "Running as Administrator"
- Shows both "Update Commix" and "Continue" buttons
- **Waits for user to click Continue or Update**
- GUI launches after user action

### Test 2: Without Commix (Simulated)
To test the "not found" scenario, you have two options:

**Option A: Rename Commix temporarily**
```cmd
# Rename to hide it
ren "C:\Program Files\Commix" "Commix_temp"

# Run launcher
python launch.py

# Expected: Dialog shows "not found" with install options

# Restore
ren "C:\Program Files\Commix_temp" "Commix"
```

**Option B: Use test script**
```cmd
# Just test the dialog directly
python test_dialog.py
```

### Test 3: Test the dialog standalone
```cmd
python test_dialog.py
```
**Expected**:
- Dialog appears immediately
- Shows current Commix status
- Prints result to console

## What Should Happen

### Correct Behavior (FIXED):
✅ Dialog appears centered on screen
✅ Dialog is modal (can't interact with background)
✅ Dialog stays on top
✅ Shows installation UI when Commix not found
✅ Install/Browse/Cancel buttons visible and clickable
✅ **No auto-close** - always waits for user input
✅ When running as admin, shows both Update and Continue buttons
✅ When running as normal user, shows only Continue button (Update hidden)

### Previous Issue:
❌ Dialog might not appear
❌ Dialog might appear behind other windows
❌ Dialog might not block properly

## Key Files Changed

1. **launch.py** (Lines 122-157)
   - QApplication created before GUI import
   - Better exception handling

2. **commix_setup_dialog.py** (Lines 38-47)
   - Added `setModal(True)`
   - Added `WindowStaysOnTopHint` flag

## Platform Differences

### Windows:
- Dialog should appear on top
- Modal behavior works well
- UAC prompt may appear if installing

### Linux/Mac:
- Dialog should appear on top
- May need window manager support for "stay on top"
- sudo prompt appears in terminal if elevating

## Troubleshooting

**If dialog still doesn't appear:**

1. Check QApplication is created first:
```python
app = QApplication(sys.argv)  # MUST be first
dialog = CommixSetupDialog()   # Then create dialog
```

2. Verify PyQt6 is installed:
```cmd
python -c "import PyQt6; print('OK')"
```

3. Try test script:
```cmd
python test_dialog.py
```

4. Check for exceptions:
```cmd
python launch.py 2>&1 | more
```

**If dialog appears but doesn't stay on top:**
- This is a window manager issue
- Dialog is still modal (blocks interaction)
- Click on it in taskbar to bring forward

**If installation buttons don't work:**
- Check git is installed: `git --version`
- Check internet connection
- Check admin privileges if installing system-wide

## Success Criteria

✅ Dialog appears when running `python launch.py`
✅ Dialog shows correct status (found/not found)
✅ Dialog is modal (can't click past it)
✅ Install button visible when Commix not found
✅ **No auto-close** - dialog always waits for user input
✅ When running as admin, shows Update button
✅ When running as normal user, Update button is hidden
✅ User must click Continue/Cancel/Update/Install buttons
✅ GUI launches after setup completes

---

**Status**: FIXED ✓

**Tested on**: Windows (needs testing on Linux/Mac)

**Related Issues**: 
- GUI not launching after selecting 'n' (FIXED)
- Dialog not appearing from launch.py (FIXED)
