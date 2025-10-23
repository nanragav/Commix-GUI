#!/usr/bin/env python
# encoding: UTF-8

"""
Command Dialog - Display generated command
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTextEdit, QPushButton,
    QHBoxLayout, QLabel, QApplication
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class CommandDialog(QDialog):
    """Dialog to display and copy generated command"""
    
    def __init__(self, command, parent=None):
        super().__init__(parent)
        self.command = command
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle("Generated Commix Command")
        self.setMinimumWidth(600)
        self.setMinimumHeight(300)
        
        layout = QVBoxLayout(self)
        
        # Label
        label = QLabel("Generated Command:")
        label.setStyleSheet("font-weight: bold; font-size: 12px;")
        layout.addWidget(label)
        
        # Command text
        self.command_text = QTextEdit()
        self.command_text.setPlainText(self.command)
        self.command_text.setFont(QFont("Courier New", 10))
        self.command_text.setReadOnly(True)
        layout.addWidget(self.command_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        copy_btn = QPushButton("Copy to Clipboard")
        copy_btn.clicked.connect(self.copy_command)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        
        button_layout.addWidget(copy_btn)
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
    def copy_command(self):
        """Copy command to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.command)
        
        # Change button text temporarily
        sender = self.sender()
        original_text = sender.text()
        sender.setText("✓ Copied!")
        sender.setEnabled(False)
        
        # Reset after 1 second
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(1000, lambda: (sender.setText(original_text), sender.setEnabled(True)))
