#!/usr/bin/env python
# encoding: UTF-8

"""
Enumeration Tab - Configure enumeration options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QGroupBox, QCheckBox, QLabel
)


class EnumerationTab(QWidget):
    """Tab for enumeration configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # System Information Group
        system_group = QGroupBox("System Information Enumeration")
        system_layout = QFormLayout()
        
        self.enum_all_check = QCheckBox("Retrieve everything")
        system_layout.addRow("", self.enum_all_check)
        
        self.current_user_check = QCheckBox("Retrieve current user name")
        system_layout.addRow("", self.current_user_check)
        
        self.hostname_check = QCheckBox("Retrieve current hostname")
        system_layout.addRow("", self.hostname_check)
        
        self.is_root_check = QCheckBox("Check if current user has root privileges")
        system_layout.addRow("", self.is_root_check)
        
        self.is_admin_check = QCheckBox("Check if current user has admin privileges")
        system_layout.addRow("", self.is_admin_check)
        
        self.sys_info_check = QCheckBox("Retrieve system information")
        system_layout.addRow("", self.sys_info_check)
        
        self.ps_version_check = QCheckBox("Retrieve PowerShell version (Windows)")
        system_layout.addRow("", self.ps_version_check)
        
        system_group.setLayout(system_layout)
        layout.addWidget(system_group)
        
        # User Information Group
        user_group = QGroupBox("User Information Enumeration")
        user_layout = QFormLayout()
        
        self.users_check = QCheckBox("Retrieve system users")
        user_layout.addRow("", self.users_check)
        
        self.passwords_check = QCheckBox("Retrieve system user password hashes")
        user_layout.addRow("", self.passwords_check)
        
        self.privileges_check = QCheckBox("Retrieve system user privileges")
        user_layout.addRow("", self.privileges_check)
        
        user_group.setLayout(user_layout)
        layout.addWidget(user_group)
        
        layout.addWidget(QLabel("<i>Note: Enumeration options execute after successful injection</i>"))
        layout.addStretch()
        
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.enum_all_check.isChecked():
            options['enum_all'] = True
            
        if self.current_user_check.isChecked():
            options['current_user'] = True
            
        if self.hostname_check.isChecked():
            options['hostname'] = True
            
        if self.is_root_check.isChecked():
            options['is_root'] = True
            
        if self.is_admin_check.isChecked():
            options['is_admin'] = True
            
        if self.sys_info_check.isChecked():
            options['sys_info'] = True
            
        if self.ps_version_check.isChecked():
            options['ps_version'] = True
            
        if self.users_check.isChecked():
            options['users'] = True
            
        if self.passwords_check.isChecked():
            options['passwords'] = True
            
        if self.privileges_check.isChecked():
            options['privileges'] = True
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.enum_all_check.setChecked(False)
        self.current_user_check.setChecked(False)
        self.hostname_check.setChecked(False)
        self.is_root_check.setChecked(False)
        self.is_admin_check.setChecked(False)
        self.sys_info_check.setChecked(False)
        self.ps_version_check.setChecked(False)
        self.users_check.setChecked(False)
        self.passwords_check.setChecked(False)
        self.privileges_check.setChecked(False)
