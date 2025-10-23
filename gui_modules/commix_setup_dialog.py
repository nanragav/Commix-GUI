#!/usr/bin/env python
# encoding: UTF-8

"""
Commix Setup Dialog - Handle Commix detection and installation
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTextEdit, QProgressBar, QMessageBox, QFileDialog, QGroupBox,
    QRadioButton, QButtonGroup
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont
from gui_modules.commix_manager import CommixManager


class InstallThread(QThread):
    """Thread for installing Commix"""
    progress_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(dict)
    
    def __init__(self, manager, install_path=None):
        super().__init__()
        self.manager = manager
        self.install_path = install_path
        
    def run(self):
        result = self.manager.install_commix_from_github(
            self.install_path,
            self.progress_signal.emit
        )
        self.finished_signal.emit(result)


class CommixSetupDialog(QDialog):
    """Dialog for Commix setup and installation"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set dialog as modal and ensure it stays on top
        self.setModal(True)
        from PyQt6.QtCore import Qt
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        
        self.manager = CommixManager()
        self.detection_result = None
        self.init_ui()
        self.detect_commix()
        
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle("Commix Setup - Detection & Installation")
        
        # Make dialog responsive to screen size
        from PyQt6.QtGui import QGuiApplication
        screen = QGuiApplication.primaryScreen().availableGeometry()
        
        # Calculate appropriate size for dialog
        screen_width = screen.width()
        screen_height = screen.height()
        
        # Dialog should be smaller than main window
        if screen_width >= 1920:
            dialog_width = 800
            dialog_height = 600
        elif screen_width >= 1366:
            dialog_width = 700
            dialog_height = 550
        else:
            dialog_width = min(600, screen_width - 100)
            dialog_height = min(500, screen_height - 100)
        
        # Set size
        self.resize(dialog_width, dialog_height)
        
        # Set minimum size that works on small screens
        min_width = min(550, screen_width - 100)
        min_height = min(450, screen_height - 100)
        self.setMinimumSize(min_width, min_height)
        
        # Center dialog on screen
        x = int((screen_width - dialog_width) / 2)
        y = int((screen_height - dialog_height) / 2)
        self.move(max(0, x), max(0, y))
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("🔍 Commix Detection & Setup")
        title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333333;
                padding: 10px;
            }
        """)
        layout.addWidget(title)
        
        # Status group
        status_group = QGroupBox("Current Status")
        status_layout = QVBoxLayout()
        
        self.status_label = QLabel("Detecting Commix installation...")
        self.status_label.setWordWrap(True)
        status_layout.addWidget(self.status_label)
        
        self.path_label = QLabel("")
        self.path_label.setWordWrap(True)
        self.path_label.setStyleSheet("QLabel { color: #666666; font-size: 11px; }")
        status_layout.addWidget(self.path_label)
        
        self.version_label = QLabel("")
        self.version_label.setStyleSheet("QLabel { color: #666666; font-size: 11px; }")
        status_layout.addWidget(self.version_label)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # Admin privileges warning
        self.admin_warning = QLabel()
        self.admin_warning.setWordWrap(True)
        self.admin_warning.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                color: #856404;
                border: 1px solid #ffc107;
                border-radius: 4px;
                padding: 10px;
                font-weight: bold;
            }
        """)
        self.admin_warning.hide()
        layout.addWidget(self.admin_warning)
        
        # Installation options
        self.install_group = QGroupBox("Installation Options")
        install_layout = QVBoxLayout()
        
        # Check if local commix exists
        local_commix = self.manager.find_commix_local()
        
        if local_commix:
            self.local_radio = QRadioButton(f"Use local Commix folder and run --install\n({local_commix})")
            self.local_radio.setChecked(True)
            install_layout.addWidget(self.local_radio)
            
            self.install_radio = QRadioButton("Install Commix from GitHub to system")
            install_layout.addWidget(self.install_radio)
        else:
            self.local_radio = None
            self.install_radio = QRadioButton("Install Commix from GitHub (Recommended)")
            self.install_radio.setChecked(True)
            install_layout.addWidget(self.install_radio)
        
        self.custom_radio = QRadioButton("Specify custom Commix path")
        install_layout.addWidget(self.custom_radio)
        
        self.install_group.setLayout(install_layout)
        self.install_group.hide()
        layout.addWidget(self.install_group)
        
        # Progress area
        self.progress_area = QGroupBox("Installation Progress")
        progress_layout = QVBoxLayout()
        
        self.progress_text = QTextEdit()
        self.progress_text.setReadOnly(True)
        self.progress_text.setMaximumHeight(150)
        self.progress_text.setFont(QFont("Consolas", 9))
        progress_layout.addWidget(self.progress_text)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate
        self.progress_bar.hide()
        progress_layout.addWidget(self.progress_bar)
        
        self.progress_area.setLayout(progress_layout)
        self.progress_area.hide()
        layout.addWidget(self.progress_area)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.install_btn = QPushButton("📥 Install Commix")
        self.install_btn.setMinimumHeight(35)
        self.install_btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:disabled {
                background-color: #6c757d;
            }
        """)
        self.install_btn.clicked.connect(self.install_commix)
        self.install_btn.hide()
        
        self.update_btn = QPushButton("🔄 Update Commix")
        self.update_btn.setMinimumHeight(35)
        self.update_btn.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        self.update_btn.clicked.connect(self.update_commix)
        self.update_btn.hide()
        
        self.browse_btn = QPushButton("📁 Browse")
        self.browse_btn.setMinimumHeight(35)
        self.browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
        """)
        self.browse_btn.clicked.connect(self.browse_commix)
        self.browse_btn.hide()
        
        self.continue_btn = QPushButton("✓ Continue")
        self.continue_btn.setMinimumHeight(35)
        self.continue_btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.continue_btn.clicked.connect(self.accept)
        self.continue_btn.hide()
        
        self.cancel_btn = QPushButton("✗ Cancel")
        self.cancel_btn.setMinimumHeight(35)
        self.cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(self.install_btn)
        button_layout.addWidget(self.update_btn)
        button_layout.addWidget(self.browse_btn)
        button_layout.addWidget(self.continue_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(button_layout)
        
    def detect_commix(self):
        """Detect Commix installation"""
        self.detection_result = self.manager.detect_commix()
        
        if self.detection_result["found"]:
            # Commix found
            location = self.detection_result["location"]
            path = self.detection_result["path"]
            version = self.detection_result["version"]
            
            # Check if running as admin
            is_admin = self.manager.check_admin_privileges()
            
            if is_admin:
                # Running as admin - show update option
                self.status_label.setText(f"✓ Commix found ({location} installation) - Running as Administrator")
                self.status_label.setStyleSheet("QLabel { color: green; font-weight: bold; }")
                # Show update button for admin users
                self.update_btn.show()
            else:
                # Not admin - no update option
                self.status_label.setText(f"✓ Commix found ({location} installation)")
                self.status_label.setStyleSheet("QLabel { color: green; font-weight: bold; }")
                # Don't show update button for normal users
                self.update_btn.hide()
                
                # Show admin warning
                self.admin_warning.setText(
                    "⚠️ Not running with administrator privileges. "
                    "Some Commix scans may require admin rights. "
                    "Consider restarting the application as administrator."
                )
                self.admin_warning.show()
            
            self.path_label.setText(f"Path: {path}")
            self.version_label.setText(f"Version: {version}")
            
            # Always show continue button
            self.continue_btn.show()
            
            # No auto-close - user must click Continue
            
        else:
            # Commix not found
            self.status_label.setText("✗ Commix not found on this system")
            self.status_label.setStyleSheet("QLabel { color: red; font-weight: bold; }")
            self.path_label.setText("Commix needs to be installed to use this GUI.")
            
            # Show installation options
            self.install_group.show()
            self.install_btn.show()
            self.browse_btn.show()
            
            # Check admin privileges
            if not self.manager.check_admin_privileges():
                self.admin_warning.setText(
                    "⚠️ Administrator privileges required for installation. "
                    "Click below to restart with admin rights."
                )
                self.admin_warning.show()
                
    def install_commix(self):
        """Install Commix"""
        # Check which option is selected
        use_local = hasattr(self, 'local_radio') and self.local_radio and self.local_radio.isChecked()
        
        # Local installation doesn't always need admin
        if not use_local:
            # Check if needs admin for system installation
            if not self.manager.check_admin_privileges():
                reply = QMessageBox.question(
                    self,
                    "Administrator Rights Required",
                    "Installing Commix to system directories requires administrator privileges.\n\n"
                    "Would you like to restart the application as administrator?\n\n"
                    "Note: You can also choose 'No' to continue and install to a user directory instead.",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                
                if reply == QMessageBox.StandardButton.Yes:
                    # Show message before restarting
                    QMessageBox.information(
                        self,
                        "Restarting",
                        "The application will now restart with administrator privileges.\n\n"
                        "Please accept the UAC prompt that appears.\n\n"
                        "After restarting, the installation will continue automatically."
                    )
                    
                    if self.manager.request_admin_privileges():
                        # Application will restart
                        import sys
                        sys.exit(0)
                    else:
                        QMessageBox.critical(
                            self,
                            "Error",
                            "Failed to request administrator privileges.\n\n"
                            "You can try:\n"
                            "1. Run the launcher as administrator manually\n"
                            "2. Choose a user-level installation directory\n"
                            "3. Use the local commix folder if available"
                        )
                        return
                else:
                    # User chose not to elevate, continue with user-level installation
                    pass
            
        # Disable buttons
        self.install_btn.setEnabled(False)
        self.browse_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        
        # Show progress
        self.progress_area.show()
        self.progress_bar.show()
        self.progress_text.clear()
        
        # Start installation based on selection
        if use_local:
            # Use local commix with --install
            self.progress_text.append("Using local Commix folder...")
            result = self.manager.install_local_commix(self.progress_text.append)
            self.on_install_finished(result)
        else:
            # Install from GitHub
            self.install_thread = InstallThread(self.manager)
            self.install_thread.progress_signal.connect(self.on_install_progress)
            self.install_thread.finished_signal.connect(self.on_install_finished)
            self.install_thread.start()
        
    def on_install_progress(self, message):
        """Handle installation progress"""
        self.progress_text.append(message)
        
    def on_install_finished(self, result):
        """Handle installation completion"""
        self.progress_bar.hide()
        self.install_btn.setEnabled(True)
        self.browse_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)
        
        if result["success"]:
            self.progress_text.append("\n✓ Installation completed successfully!")
            QMessageBox.information(
                self,
                "Success",
                f"Commix has been installed successfully!\n\nLocation: {result['path']}"
            )
            # Re-detect
            self.detect_commix()
        else:
            self.progress_text.append(f"\n✗ Installation failed: {result['error']}")
            QMessageBox.critical(
                self,
                "Installation Failed",
                f"Failed to install Commix:\n\n{result['error']}"
            )
            
    def update_commix(self):
        """Update Commix"""
        reply = QMessageBox.question(
            self,
            "Update Commix",
            "Do you want to update Commix to the latest version from GitHub?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.progress_area.show()
            self.progress_bar.show()
            self.progress_text.clear()
            
            result = self.manager.update_commix(self.progress_text.append)
            
            self.progress_bar.hide()
            
            if result["success"]:
                QMessageBox.information(self, "Success", "Commix updated successfully!")
                self.detect_commix()
            else:
                QMessageBox.warning(self, "Update Failed", f"Failed to update:\n\n{result['error']}")
                
    def browse_commix(self):
        """Browse for Commix directory"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Commix Directory",
            "",
            QFileDialog.Option.ShowDirsOnly
        )
        
        if directory:
            # Verify it's a valid Commix directory
            commix_file = os.path.join(directory, "commix.py")
            if os.path.exists(commix_file):
                self.manager.commix_path = directory
                self.manager.is_installed = True
                self.detect_commix()
            else:
                QMessageBox.warning(
                    self,
                    "Invalid Directory",
                    "The selected directory does not contain commix.py"
                )
                
    def get_commix_path(self):
        """Get the detected Commix path"""
        return self.manager.commix_path
        
    def get_manager(self):
        """Get the Commix manager"""
        return self.manager


import os
