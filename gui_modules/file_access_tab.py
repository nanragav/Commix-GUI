#!/usr/bin/env python
# encoding: UTF-8

"""
File Access Tab - Configure file access options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QGroupBox, QPushButton, QHBoxLayout, QFileDialog, QLabel
)


class FileAccessTab(QWidget):
    """Tab for file access configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # File Read Group
        read_group = QGroupBox("File Read")
        read_layout = QFormLayout()
        
        self.file_read_input = QLineEdit()
        self.file_read_input.setPlaceholderText("/etc/passwd")
        read_layout.addRow("File to Read (--file-read):", self.file_read_input)
        
        read_group.setLayout(read_layout)
        layout.addWidget(read_group)
        
        # File Write Group
        write_group = QGroupBox("File Write")
        write_layout = QFormLayout()
        
        self.file_write_input = QLineEdit()
        self.file_write_input.setPlaceholderText("Content to write")
        write_layout.addRow("Content to Write (--file-write):", self.file_write_input)
        
        self.file_dest_write_input = QLineEdit()
        self.file_dest_write_input.setPlaceholderText("/tmp/test.txt")
        write_layout.addRow("Destination Path (--file-dest):", self.file_dest_write_input)
        
        write_group.setLayout(write_layout)
        layout.addWidget(write_group)
        
        # File Upload Group
        upload_group = QGroupBox("File Upload")
        upload_layout = QFormLayout()
        
        upload_file_layout = QHBoxLayout()
        self.file_upload_input = QLineEdit()
        self.file_upload_input.setPlaceholderText("Local file to upload")
        upload_file_btn = QPushButton("Browse...")
        upload_file_btn.clicked.connect(self.browse_upload_file)
        upload_file_layout.addWidget(self.file_upload_input)
        upload_file_layout.addWidget(upload_file_btn)
        
        upload_layout.addRow("Local File (--file-upload):", upload_file_layout)
        
        self.file_dest_upload_input = QLineEdit()
        self.file_dest_upload_input.setPlaceholderText("/var/www/html/shell.php")
        upload_layout.addRow("Remote Destination (--file-dest):", self.file_dest_upload_input)
        
        upload_group.setLayout(upload_layout)
        layout.addWidget(upload_group)
        
        layout.addWidget(QLabel("<i>Note: File operations execute after successful injection</i>"))
        layout.addStretch()
        
    def browse_upload_file(self):
        """Browse for file to upload"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select File to Upload", "", "All Files (*)"
        )
        if filename:
            self.file_upload_input.setText(filename)
            
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.file_read_input.text():
            options['file_read'] = self.file_read_input.text()
            
        if self.file_write_input.text():
            options['file_write'] = self.file_write_input.text()
            
        if self.file_upload_input.text():
            options['file_upload'] = self.file_upload_input.text()
            
        # file_dest is used for both write and upload
        if self.file_dest_write_input.text():
            options['file_dest'] = self.file_dest_write_input.text()
        elif self.file_dest_upload_input.text():
            options['file_dest'] = self.file_dest_upload_input.text()
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.file_read_input.clear()
        self.file_write_input.clear()
        self.file_upload_input.clear()
        self.file_dest_write_input.clear()
        self.file_dest_upload_input.clear()
