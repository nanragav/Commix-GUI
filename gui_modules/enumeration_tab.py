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
    
    def set_options(self, options):
        """Load options into this tab"""
        if 'enum_all' in options:
            self.enum_all_check.setChecked(options['enum_all'])
        if 'current_user' in options:
            self.current_user_check.setChecked(options['current_user'])
        if 'hostname' in options:
            self.hostname_check.setChecked(options['hostname'])
        if 'is_root' in options:
            self.is_root_check.setChecked(options['is_root'])
        if 'is_admin' in options:
            self.is_admin_check.setChecked(options['is_admin'])
        if 'sys_info' in options:
            self.sys_info_check.setChecked(options['sys_info'])
        if 'ps_version' in options:
            self.ps_version_check.setChecked(options['ps_version'])
        if 'users' in options:
            self.users_check.setChecked(options['users'])
        if 'passwords' in options:
            self.passwords_check.setChecked(options['passwords'])
        if 'privileges' in options:
            self.privileges_check.setChecked(options['privileges'])
        
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
