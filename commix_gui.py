#!/usr/bin/env python
# encoding: UTF-8

"""
Commix GUI - A comprehensive GUI wrapper for Commix
Cross-platform PyQt6-based interface for command injection testing
"""

import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QTextEdit, QPushButton, QStatusBar, QToolBar,
    QSplitter, QMessageBox, QFileDialog, QMenuBar, QMenu
)
from PyQt6.QtCore import Qt, pyqtSignal, QThread, QTimer
from PyQt6.QtGui import QAction, QIcon, QFont, QTextCursor, QGuiApplication

# Import custom modules
from gui_modules.target_tab import TargetTab
from gui_modules.request_tab import RequestTab
from gui_modules.authentication_tab import AuthenticationTab
from gui_modules.enumeration_tab import EnumerationTab
from gui_modules.file_access_tab import FileAccessTab
from gui_modules.injection_tab import InjectionTab
from gui_modules.detection_tab import DetectionTab
from gui_modules.modules_tab import ModulesTab
from gui_modules.misc_tab import MiscTab
from gui_modules.commix_runner import CommixRunner
from gui_modules.output_console import OutputConsole
from gui_modules.project_manager import ProjectManager
from gui_modules.commix_manager import CommixManager
from gui_modules.commix_setup_dialog import CommixSetupDialog


class CommixGUI(QMainWindow):
    """Main GUI window for Commix"""
    
    def __init__(self):
        super().__init__()
        self.project_manager = ProjectManager()
        self.commix_runner = None
        self.commix_manager = None
        
        # Check for Commix installation
        if not self.check_commix_installation():
            sys.exit(1)  # Exit if user cancels setup
            
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Commix GUI - Command Injection Exploitation Tool")
        
        # Make window responsive to screen size
        screen = QGuiApplication.primaryScreen().availableGeometry()
        
        # Calculate optimal window size based on screen
        screen_width = screen.width()
        screen_height = screen.height()
        
        # Use percentage of screen, but cap at reasonable maximums
        if screen_width >= 1920:  # Large screens (Full HD+)
            width = int(screen_width * 0.75)  # 75% of screen
            height = int(screen_height * 0.80)
        elif screen_width >= 1366:  # Medium screens (HD)
            width = int(screen_width * 0.85)  # 85% of screen
            height = int(screen_height * 0.85)
        else:  # Small screens (below HD)
            width = int(screen_width * 0.95)  # 95% of screen
            height = int(screen_height * 0.90)
        
        # Ensure minimum readable size, but don't exceed screen
        min_width = min(900, screen_width - 100)
        min_height = min(600, screen_height - 100)
        width = max(width, min_width)
        height = max(height, min_height)
        
        # Ensure window fits on screen
        width = min(width, screen_width - 50)
        height = min(height, screen_height - 50)
        
        # Center the window
        x = max(0, int((screen_width - width) / 2))
        y = max(0, int((screen_height - height) / 2))
        
        self.setGeometry(x, y, width, height)
        
        # Set minimum size based on screen capabilities
        self.setMinimumSize(min_width, min_height)
        
        # Create output console first (needed by menu bar)
        self.output_console = OutputConsole()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create main tab widget (includes both config and output)
        self.main_tab_widget = QTabWidget()
        self.main_tab_widget.setTabPosition(QTabWidget.TabPosition.North)
        
        # Create configuration tabs container
        self.config_widget = QWidget()
        config_layout = QVBoxLayout(self.config_widget)
        config_layout.setContentsMargins(5, 5, 5, 5)
        
        # Create tab widget for configuration
        self.tab_widget = QTabWidget()
        self.create_tabs()
        config_layout.addWidget(self.tab_widget)
        
        # Add configuration and output as main tabs
        self.main_tab_widget.addTab(self.config_widget, "⚙️ Configuration")
        self.main_tab_widget.addTab(self.output_console, "📟 Output Console")
        
        # Set tab bar style for better visibility (responsive)
        # Calculate responsive sizes
        screen = QGuiApplication.primaryScreen().availableGeometry()
        if screen.width() < 1366:
            tab_padding = "8px 15px"
            tab_font_size = "11px"
        else:
            tab_padding = "12px 25px"
            tab_font_size = "13px"
        
        self.main_tab_widget.setStyleSheet(f"""
            QTabWidget::pane {{
                border: none;
            }}
            QTabBar::tab {{
                background-color: #e0e0e0;
                padding: {tab_padding};
                margin-right: 2px;
                font-size: {tab_font_size};
                font-weight: bold;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }}
            QTabBar::tab:selected {{
                background-color: #ffffff;
                color: #007bff;
            }}
            QTabBar::tab:hover {{
                background-color: #d0d0d0;
            }}
        """)
        
        main_layout.addWidget(self.main_tab_widget)
        
        # Create control panel
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Apply stylesheet
        self.apply_stylesheet()
        
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        new_action = QAction("&New Project", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_project)
        file_menu.addAction(new_action)
        
        open_action = QAction("&Open Project", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_project)
        file_menu.addAction(open_action)
        
        save_action = QAction("&Save Project", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_project)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("Save Project &As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_project_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        clear_output = QAction("&Clear Output", self)
        clear_output.triggered.connect(self.output_console.clear)
        edit_menu.addAction(clear_output)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        # Tools menu
        tools_menu = menubar.addMenu("&Tools")
        
        check_commix = QAction("&Check Commix Installation", self)
        check_commix.triggered.connect(self.check_installation)
        tools_menu.addAction(check_commix)
        
        update_commix = QAction("&Update Commix", self)
        update_commix.triggered.connect(self.update_commix)
        tools_menu.addAction(update_commix)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        docs_action = QAction("&Documentation", self)
        docs_action.triggered.connect(self.show_documentation)
        help_menu.addAction(docs_action)
        
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # Add toolbar actions
        new_btn = QAction("New", self)
        new_btn.triggered.connect(self.new_project)
        toolbar.addAction(new_btn)
        
        open_btn = QAction("Open", self)
        open_btn.triggered.connect(self.open_project)
        toolbar.addAction(open_btn)
        
        save_btn = QAction("Save", self)
        save_btn.triggered.connect(self.save_project)
        toolbar.addAction(save_btn)
        
        toolbar.addSeparator()
        
    def check_commix_installation(self):
        """Check if Commix is installed and handle setup"""
        dialog = CommixSetupDialog(self)
        result = dialog.exec()
        
        if result == dialog.DialogCode.Accepted:
            self.commix_manager = dialog.get_manager()
            return True
        else:
            # User cancelled
            QMessageBox.warning(
                self,
                "Commix Required",
                "Commix is required to use this application.\n"
                "The application will now exit."
            )
            return False
        
    def create_tabs(self):
        """Create all configuration tabs"""
        self.target_tab = TargetTab()
        self.request_tab = RequestTab()
        self.auth_tab = AuthenticationTab()
        self.enumeration_tab = EnumerationTab()
        self.file_access_tab = FileAccessTab()
        self.injection_tab = InjectionTab()
        self.detection_tab = DetectionTab()
        self.modules_tab = ModulesTab()
        self.misc_tab = MiscTab()
        
        self.tab_widget.addTab(self.target_tab, "🎯 Target")
        self.tab_widget.addTab(self.request_tab, "📡 Request")
        self.tab_widget.addTab(self.auth_tab, "🔐 Authentication")
        self.tab_widget.addTab(self.injection_tab, "💉 Injection")
        self.tab_widget.addTab(self.detection_tab, "🔍 Detection")
        self.tab_widget.addTab(self.enumeration_tab, "📊 Enumeration")
        self.tab_widget.addTab(self.file_access_tab, "📁 File Access")
        self.tab_widget.addTab(self.modules_tab, "🧩 Modules")
        self.tab_widget.addTab(self.misc_tab, "⚙️ Miscellaneous")
        
    def create_control_panel(self):
        """Create the control panel with action buttons"""
        panel = QWidget()
        layout = QHBoxLayout(panel)
        
        # Calculate responsive button sizes
        screen = QGuiApplication.primaryScreen().availableGeometry()
        if screen.width() < 1366:
            btn_font_size = "12px"
            btn_padding = "8px 15px"
            btn_min_height = 35
        else:
            btn_font_size = "14px"
            btn_padding = "10px 20px"
            btn_min_height = 40
        
        # Start button
        self.start_btn = QPushButton("🚀 Start Attack")
        self.start_btn.setMinimumHeight(btn_min_height)
        self.start_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #28a745;
                color: white;
                font-size: {btn_font_size};
                font-weight: bold;
                padding: {btn_padding};
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #218838;
            }}
            QPushButton:disabled {{
                background-color: #6c757d;
            }}
        """)
        self.start_btn.clicked.connect(self.start_attack)
        
        # Stop button
        self.stop_btn = QPushButton("⏹️ Stop")
        self.stop_btn.setEnabled(False)
        self.stop_btn.setMinimumHeight(btn_min_height)
        self.stop_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #dc3545;
                color: white;
                font-size: {btn_font_size};
                font-weight: bold;
                padding: {btn_padding};
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #c82333;
            }}
            QPushButton:disabled {{
                background-color: #6c757d;
            }}
        """)
        self.stop_btn.clicked.connect(self.stop_attack)
        
        # Generate command button
        self.gen_cmd_btn = QPushButton("📋 Generate Command")
        self.gen_cmd_btn.setMinimumHeight(btn_min_height)
        self.gen_cmd_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #007bff;
                color: white;
                font-size: {btn_font_size};
                font-weight: bold;
                padding: {btn_padding};
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #0069d9;
            }}
        """)
        self.gen_cmd_btn.clicked.connect(self.generate_command)
        
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.gen_cmd_btn)
        layout.addStretch()
        
        return panel
        
    def start_attack(self):
        """Start Commix attack with current configuration"""
        try:
            # Check if Commix is available
            if not self.commix_manager or not self.commix_manager.is_installed:
                QMessageBox.warning(
                    self,
                    "Commix Not Available",
                    "Commix is not installed. Please restart the application."
                )
                return
            
            # Collect all options from tabs
            options = self.collect_options()
            
            # Validate required options
            if not options.get('url') and not options.get('requestfile'):
                QMessageBox.warning(self, "Missing Target", 
                                  "Please specify a target URL or request file.")
                return
            
            # Check if needs admin privileges
            if not self.commix_manager.check_admin_privileges():
                reply = QMessageBox.question(
                    self,
                    "Administrator Privileges",
                    "Some scans may require administrator privileges for full functionality.\n\n"
                    "Would you like to restart the application as administrator?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | 
                    QMessageBox.StandardButton.Cancel
                )
                
                if reply == QMessageBox.StandardButton.Yes:
                    if self.commix_manager.request_admin_privileges():
                        # Application will restart
                        sys.exit(0)
                    else:
                        QMessageBox.warning(
                            self,
                            "Error",
                            "Failed to request administrator privileges."
                        )
                    return
                elif reply == QMessageBox.StandardButton.Cancel:
                    return
                # If No, continue without admin
            
            # Switch to Output Console tab
            self.main_tab_widget.setCurrentIndex(1)
            
            # Disable start button, enable stop button
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.status_bar.showMessage("Attack in progress...")
            
            # Clear previous output
            self.output_console.clear()
            
            # Create and start Commix runner with CommixManager
            self.commix_runner = CommixRunner(options, self.commix_manager)
            self.commix_runner.output_signal.connect(self.output_console.append_output)
            self.commix_runner.error_signal.connect(self.output_console.append_error)
            self.commix_runner.finished_signal.connect(self.attack_finished)
            self.commix_runner.start()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to start attack: {str(e)}")
            self.attack_finished(1)
            
    def stop_attack(self):
        """Stop the running attack"""
        if self.commix_runner and self.commix_runner.isRunning():
            reply = QMessageBox.question(self, "Confirm Stop", 
                                        "Are you sure you want to stop the attack?",
                                        QMessageBox.StandardButton.Yes | 
                                        QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.commix_runner.stop()
                self.output_console.append_warning("Attack stopped by user")
                
    def attack_finished(self, exit_code):
        """Handle attack completion"""
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        
        if exit_code == 0:
            self.status_bar.showMessage("Attack completed successfully")
            self.output_console.append_success("\n=== Attack completed successfully ===")
        else:
            self.status_bar.showMessage("Attack finished with errors")
            self.output_console.append_error(f"\n=== Attack finished with exit code: {exit_code} ===")
            
    def generate_command(self):
        """Generate and display the Commix command"""
        try:
            options = self.collect_options()
            command = self.build_command(options)
            
            # Show command in a dialog
            from gui_modules.command_dialog import CommandDialog
            dialog = CommandDialog(command, self)
            dialog.exec()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate command: {str(e)}")
            
    def collect_options(self):
        """Collect all options from all tabs"""
        options = {}
        options.update(self.target_tab.get_options())
        options.update(self.request_tab.get_options())
        options.update(self.auth_tab.get_options())
        options.update(self.injection_tab.get_options())
        options.update(self.detection_tab.get_options())
        options.update(self.enumeration_tab.get_options())
        options.update(self.file_access_tab.get_options())
        options.update(self.modules_tab.get_options())
        options.update(self.misc_tab.get_options())
        return options
        
    def build_command(self, options):
        """Build Commix command from options"""
        cmd_parts = ["python", "commix/commix.py"]
        
        for key, value in options.items():
            if value is None or value == "" or value is False:
                continue
            if value is True:
                cmd_parts.append(f"--{key}")
            else:
                cmd_parts.append(f"--{key}")
                cmd_parts.append(str(value))
                
        return " ".join(cmd_parts)
        
    def new_project(self):
        """Create a new project"""
        reply = QMessageBox.question(self, "New Project", 
                                    "Create a new project? Unsaved changes will be lost.",
                                    QMessageBox.StandardButton.Yes | 
                                    QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.reset_all_tabs()
            self.output_console.clear()
            self.status_bar.showMessage("New project created")
            
    def open_project(self):
        """Open an existing project"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "", "Commix Project Files (*.cproj);;All Files (*)"
        )
        if filename:
            try:
                project_data = self.project_manager.load_project(filename)
                self.load_project_data(project_data)
                self.status_bar.showMessage(f"Project loaded: {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open project: {str(e)}")
                
    def save_project(self):
        """Save the current project"""
        if hasattr(self, 'current_project_file'):
            self.save_project_to_file(self.current_project_file)
        else:
            self.save_project_as()
            
    def save_project_as(self):
        """Save project with a new name"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Project As", "", "Commix Project Files (*.cproj);;All Files (*)"
        )
        if filename:
            if not filename.endswith('.cproj'):
                filename += '.cproj'
            self.save_project_to_file(filename)
            self.current_project_file = filename
            
    def save_project_to_file(self, filename):
        """Save project data to file"""
        try:
            project_data = self.collect_options()
            self.project_manager.save_project(filename, project_data)
            self.status_bar.showMessage(f"Project saved: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save project: {str(e)}")
            
    def load_project_data(self, data):
        """Load project data into tabs"""
        # Implementation depends on tab structure
        pass
        
    def reset_all_tabs(self):
        """Reset all tabs to default values"""
        self.target_tab.reset()
        self.request_tab.reset()
        self.auth_tab.reset()
        self.injection_tab.reset()
        self.detection_tab.reset()
        self.enumeration_tab.reset()
        self.file_access_tab.reset()
        self.modules_tab.reset()
        self.misc_tab.reset()
        
    def show_about(self):
        """Show about dialog"""
        about_text = """
        <h2>Commix GUI</h2>
        <p>A comprehensive GUI wrapper for Commix</p>
        <p><b>Version:</b> 1.0.0</p>
        <p><b>Commix:</b> Command Injection Exploitation Tool</p>
        <p>Copyright © 2014-2025 Anastasios Stasinopoulos</p>
        <p>GUI Wrapper: Cross-platform PyQt6 Interface</p>
        """
        QMessageBox.about(self, "About Commix GUI", about_text)
    
    def check_installation(self):
        """Check Commix installation status"""
        if not self.commix_manager:
            QMessageBox.warning(self, "Error", "Commix manager not initialized.")
            return
            
        result = self.commix_manager.detect_commix()
        
        if result["found"]:
            QMessageBox.information(
                self,
                "Commix Installation",
                f"✓ Commix is installed\n\n"
                f"Location: {result['location']}\n"
                f"Path: {result['path']}\n"
                f"Version: {result['version']}"
            )
        else:
            reply = QMessageBox.question(
                self,
                "Commix Not Found",
                "Commix is not installed on this system.\n\n"
                "Would you like to install it now?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                # Show setup dialog again
                dialog = CommixSetupDialog(self)
                dialog.exec()
                
    def update_commix(self):
        """Update Commix to latest version"""
        if not self.commix_manager:
            QMessageBox.warning(self, "Error", "Commix manager not initialized.")
            return
            
        if not self.commix_manager.is_installed:
            QMessageBox.warning(
                self,
                "Not Installed",
                "Commix is not installed. Please install it first."
            )
            return
            
        from PyQt6.QtWidgets import QProgressDialog
        
        # Create progress dialog
        progress = QProgressDialog("Updating Commix...", "Cancel", 0, 0, self)
        progress.setWindowTitle("Update Commix")
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.show()
        
        def progress_callback(message):
            progress.setLabelText(message)
            QApplication.processEvents()
        
        result = self.commix_manager.update_commix(progress_callback)
        
        progress.close()
        
        if result["success"]:
            QMessageBox.information(
                self,
                "Update Complete",
                "Commix has been updated successfully!"
            )
        else:
            QMessageBox.warning(
                self,
                "Update Failed",
                f"Failed to update Commix:\n\n{result['error']}"
            )
        
    def show_documentation(self):
        """Show documentation"""
        doc_text = """
        <h3>Commix GUI Documentation</h3>
        <p>For detailed documentation, visit:</p>
        <p><a href='https://commixproject.com'>https://commixproject.com</a></p>
        <p><a href='https://github.com/commixproject/commix'>GitHub Repository</a></p>
        """
        QMessageBox.information(self, "Documentation", doc_text)
        
    def apply_stylesheet(self):
        """Apply custom stylesheet to the application"""
        stylesheet = """
        QMainWindow {
            background-color: #f5f5f5;
        }
        QTabWidget::pane {
            border: 1px solid #cccccc;
            background-color: white;
            border-radius: 5px;
        }
        QTabBar::tab {
            background-color: #e0e0e0;
            padding: 10px 15px;
            margin-right: 2px;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }
        QTabBar::tab:selected {
            background-color: white;
            font-weight: bold;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px;
        }
        """
        self.setStyleSheet(stylesheet)
    
    def resizeEvent(self, event):
        """Handle window resize events for responsive UI"""
        super().resizeEvent(event)
        
        # Update button sizes based on new window size
        if hasattr(self, 'start_btn'):
            window_width = self.width()
            
            # Adjust button styling based on window width
            if window_width < 1000:
                btn_font_size = "11px"
                btn_padding = "6px 12px"
                tab_padding = "6px 12px"
                tab_font_size = "10px"
            elif window_width < 1366:
                btn_font_size = "12px"
                btn_padding = "8px 15px"
                tab_padding = "8px 15px"
                tab_font_size = "11px"
            else:
                btn_font_size = "14px"
                btn_padding = "10px 20px"
                tab_padding = "12px 25px"
                tab_font_size = "13px"
            
            # Update main tab widget style
            if hasattr(self, 'main_tab_widget'):
                self.main_tab_widget.setStyleSheet(f"""
                    QTabWidget::pane {{
                        border: none;
                    }}
                    QTabBar::tab {{
                        background-color: #e0e0e0;
                        padding: {tab_padding};
                        margin-right: 2px;
                        font-size: {tab_font_size};
                        font-weight: bold;
                        border-top-left-radius: 5px;
                        border-top-right-radius: 5px;
                    }}
                    QTabBar::tab:selected {{
                        background-color: #ffffff;
                        color: #007bff;
                    }}
                    QTabBar::tab:hover {{
                        background-color: #d0d0d0;
                    }}
                """)


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Set application info
    app.setApplicationName("Commix GUI")
    app.setOrganizationName("Commix Project")
    app.setApplicationVersion("1.0.0")
    
    window = CommixGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
