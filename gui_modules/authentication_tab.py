#!/usr/bin/env python
# encoding: UTF-8

"""
Authentication Tab - Configure authentication options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QGroupBox, QComboBox, QCheckBox
)


class AuthenticationTab(QWidget):
    """Tab for authentication configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # HTTP Authentication Group
        http_auth_group = QGroupBox("HTTP Authentication")
        http_auth_layout = QFormLayout()
        
        self.auth_type_combo = QComboBox()
        self.auth_type_combo.addItems(["None", "Basic", "Digest", "Bearer"])
        http_auth_layout.addRow("Auth Type (--auth-type):", self.auth_type_combo)
        
        self.auth_cred_input = QLineEdit()
        self.auth_cred_input.setPlaceholderText("username:password")
        http_auth_layout.addRow("Credentials (--auth-cred):", self.auth_cred_input)
        
        http_auth_group.setLayout(http_auth_layout)
        layout.addWidget(http_auth_group)
        
        # Form-based Authentication Group
        form_auth_group = QGroupBox("Form-based Authentication")
        form_auth_layout = QFormLayout()
        
        self.auth_url_input = QLineEdit()
        self.auth_url_input.setPlaceholderText("http://example.com/login.php")
        form_auth_layout.addRow("Login URL (--auth-url):", self.auth_url_input)
        
        self.auth_data_input = QLineEdit()
        self.auth_data_input.setPlaceholderText("username=admin&password=pass&submit=Login")
        form_auth_layout.addRow("Login Data (--auth-data):", self.auth_data_input)
        
        form_auth_group.setLayout(form_auth_layout)
        layout.addWidget(form_auth_group)
        
        layout.addStretch()
        
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.auth_type_combo.currentText() != "None":
            options['auth_type'] = self.auth_type_combo.currentText()
            
        if self.auth_cred_input.text():
            options['auth_cred'] = self.auth_cred_input.text()
            
        if self.auth_url_input.text():
            options['auth_url'] = self.auth_url_input.text()
            
        if self.auth_data_input.text():
            options['auth_data'] = self.auth_data_input.text()
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.auth_type_combo.setCurrentIndex(0)
        self.auth_cred_input.clear()
        self.auth_url_input.clear()
        self.auth_data_input.clear()
