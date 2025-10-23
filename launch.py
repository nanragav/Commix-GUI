#!/usr/bin/env python
# encoding: UTF-8

"""
Commix GUI Launcher - Python-based launcher with admin detection
This launcher handles privilege detection and can be run directly without batch files
"""

import sys
import os
import platform
import subprocess


def check_admin():
    """Check if running with admin/root privileges"""
    system = platform.system()
    
    try:
        if system == "Windows":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            # Unix-like systems
            return os.geteuid() == 0
    except:
        return False


def request_admin():
    """Request admin privileges and restart"""
    system = platform.system()
    
    try:
        if system == "Windows":
            import ctypes
            # Get the script path
            script = os.path.abspath(__file__)
            # Add flag to prevent re-prompting after elevation
            params = ' '.join([script, '--skip-admin-prompt'] + sys.argv[1:])
            
            # Use ShellExecute to run with admin rights
            ret = ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, params, None, 1
            )
            return ret > 32  # Success
        else:
            # Unix-like systems - use sudo
            script = os.path.abspath(__file__)
            # Add flag to prevent re-prompting after elevation
            args = ['sudo', '-E', sys.executable, script, '--skip-admin-prompt'] + sys.argv[1:]
            subprocess.call(args)
            return True
    except Exception as e:
        print(f"Failed to request privileges: {e}")
        return False


def main():
    """Main launcher function"""
    print("=" * 50)
    print(" Commix GUI - Command Injection Tool")
    print("=" * 50)
    print()
    
    # Check admin status
    is_admin = check_admin()
    
    if is_admin:
        print("[*] Running with Administrator/Root privileges")
    else:
        print("[!] Running without Administrator/Root privileges")
        print("[!] Some features may require elevation:")
        print("    - System-wide Commix installation")
        print("    - Certain scan types")
        print("    - Network operations")
    
    print()
    
    # Check if we should skip the prompt (already tried or declined)
    skip_prompt = '--skip-admin-prompt' in sys.argv
    
    if not is_admin and not skip_prompt:
        try:
            response = input("[?] Do you want to restart with admin privileges? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                print()
                print("[*] Requesting elevation...")
                if request_admin():
                    print("[*] Restarting with elevated privileges...")
                    sys.exit(0)
                else:
                    print("[!] Failed to elevate. Continuing without admin...")
            else:
                # User declined elevation, add flag to prevent issues
                if '--skip-admin-prompt' not in sys.argv:
                    sys.argv.append('--skip-admin-prompt')
        except (EOFError, KeyboardInterrupt):
            print()
            print("[*] Continuing without elevation...")
            if '--skip-admin-prompt' not in sys.argv:
                sys.argv.append('--skip-admin-prompt')
    
    print()
    print("[*] Starting Commix GUI...")
    print()
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gui_file = os.path.join(script_dir, "commix_gui.py")
    
    # Check if GUI file exists
    if not os.path.exists(gui_file):
        print(f"[X] Error: {gui_file} not found")
        print(f"[!] Current directory: {script_dir}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Launch the GUI
    try:
        # Import and run the GUI directly
        sys.path.insert(0, script_dir)
        
        # Check dependencies
        try:
            import PyQt6
        except ImportError:
            print("[!] PyQt6 not installed. Installing dependencies...")
            print()
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print()
            print("[*] Dependencies installed successfully")
            print()
        
        # Create QApplication FIRST - required for any Qt widgets including dialogs
        from PyQt6.QtWidgets import QApplication
        app = QApplication(sys.argv)
        
        # Now import and create GUI (this will show dialogs if needed)
        import commix_gui
        
        # Create main window - this will trigger Commix check dialog if needed
        window = commix_gui.CommixGUI()
        window.show()
        
        # Run event loop
        sys.exit(app.exec())
        
    except SystemExit as e:
        # Handle sys.exit() calls from GUI (e.g., user cancelled setup)
        if e.code != 0:
            print()
            print("[!] Application exited")
            print()
        sys.exit(e.code)
    except Exception as e:
        print()
        print(f"[X] Error: {e}")
        print()
        import traceback
        traceback.print_exc()
        print()
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()
