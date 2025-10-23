#!/usr/bin/env python
# encoding: UTF-8

"""
Test script to verify CommixSetupDialog displays correctly
"""

import sys
from PyQt6.QtWidgets import QApplication
from gui_modules.commix_setup_dialog import CommixSetupDialog

def main():
    print("Creating QApplication...")
    app = QApplication(sys.argv)
    
    print("Creating CommixSetupDialog...")
    dialog = CommixSetupDialog()
    
    print("Showing dialog...")
    result = dialog.exec()
    
    print(f"Dialog result: {result}")
    print(f"Accepted: {result == dialog.DialogCode.Accepted}")
    
    if result == dialog.DialogCode.Accepted:
        print("User accepted/continued")
    else:
        print("User cancelled")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
