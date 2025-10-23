#!/usr/bin/env python
# encoding: UTF-8

"""
Modules Tab - Configure detection and injection modules
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QGroupBox, QCheckBox, QLabel
)


class ModulesTab(QWidget):
    """Tab for modules configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # Modules Group
        modules_group = QGroupBox("Detection/Injection Modules")
        modules_layout = QFormLayout()
        
        self.shellshock_check = QCheckBox("Enable Shellshock module")
        modules_layout.addRow("", self.shellshock_check)
        
        modules_layout.addRow("", QLabel("<i>The Shellshock module tests for the Shellshock vulnerability</i>"))
        modules_layout.addRow("", QLabel("<i>(CVE-2014-6271) via HTTP headers and CGI scripts</i>"))
        
        modules_group.setLayout(modules_layout)
        layout.addWidget(modules_group)
        
        layout.addStretch()
        
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.shellshock_check.isChecked():
            options['shellshock'] = True
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.shellshock_check.setChecked(False)
