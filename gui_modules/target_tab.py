#!/usr/bin/env python
# encoding: UTF-8

"""
Target Tab - Configure target URL and related options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit,
    QTextEdit, QPushButton, QGroupBox, QLabel, QSpinBox,
    QCheckBox, QFileDialog, QComboBox
)
from PyQt6.QtCore import Qt


class TargetTab(QWidget):
    """Tab for target configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # Target URL Group
        target_group = QGroupBox("Target Configuration")
        target_layout = QFormLayout()
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("http://example.com/page.php?id=1")
        target_layout.addRow("Target URL (-u):", self.url_input)
        
        # Request file
        req_file_layout = QHBoxLayout()
        self.request_file_input = QLineEdit()
        self.request_file_input.setPlaceholderText("Path to HTTP request file")
        req_file_btn = QPushButton("Browse...")
        req_file_btn.clicked.connect(self.browse_request_file)
        req_file_layout.addWidget(self.request_file_input)
        req_file_layout.addWidget(req_file_btn)
        target_layout.addRow("Request File (-r):", req_file_layout)
        
        # Log file
        log_file_layout = QHBoxLayout()
        self.log_file_input = QLineEdit()
        self.log_file_input.setPlaceholderText("Path to HTTP proxy log file")
        log_file_btn = QPushButton("Browse...")
        log_file_btn.clicked.connect(self.browse_log_file)
        log_file_layout.addWidget(self.log_file_input)
        log_file_layout.addWidget(log_file_btn)
        target_layout.addRow("Proxy Log File (-l):", log_file_layout)
        
        # Bulk file
        bulk_file_layout = QHBoxLayout()
        self.bulk_file_input = QLineEdit()
        self.bulk_file_input.setPlaceholderText("File with multiple targets")
        bulk_file_btn = QPushButton("Browse...")
        bulk_file_btn.clicked.connect(self.browse_bulk_file)
        bulk_file_layout.addWidget(self.bulk_file_input)
        bulk_file_layout.addWidget(bulk_file_btn)
        target_layout.addRow("Bulk File (-m):", bulk_file_layout)
        
        # Sitemap URL
        self.sitemap_input = QLineEdit()
        self.sitemap_input.setPlaceholderText("http://example.com/sitemap.xml")
        target_layout.addRow("Sitemap URL (-x):", self.sitemap_input)
        
        # HTTP Method
        self.method_combo = QComboBox()
        self.method_combo.addItems(["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"])
        target_layout.addRow("HTTP Method:", self.method_combo)
        
        # URL Reload
        self.url_reload_check = QCheckBox("Reload target URL after command execution")
        target_layout.addRow("", self.url_reload_check)
        
        target_group.setLayout(target_layout)
        layout.addWidget(target_group)
        
        # Crawler Group
        crawler_group = QGroupBox("Web Crawler")
        crawler_layout = QFormLayout()
        
        self.crawl_depth_spin = QSpinBox()
        self.crawl_depth_spin.setMinimum(0)
        self.crawl_depth_spin.setMaximum(10)
        self.crawl_depth_spin.setValue(0)
        self.crawl_depth_spin.setToolTip("0 means disabled")
        crawler_layout.addRow("Crawl Depth (--crawl):", self.crawl_depth_spin)
        
        self.crawl_exclude_input = QLineEdit()
        self.crawl_exclude_input.setPlaceholderText("e.g., 'logout|admin'")
        crawler_layout.addRow("Exclude Pattern (--crawl-exclude):", self.crawl_exclude_input)
        
        crawler_group.setLayout(crawler_layout)
        layout.addWidget(crawler_group)
        
        # POST Data Group
        data_group = QGroupBox("POST Data")
        data_layout = QVBoxLayout()
        
        self.data_input = QTextEdit()
        self.data_input.setPlaceholderText("username=admin&password=test&submit=Login")
        self.data_input.setMaximumHeight(80)
        data_layout.addWidget(QLabel("POST Data (-d, --data):"))
        data_layout.addWidget(self.data_input)
        
        data_group.setLayout(data_layout)
        layout.addWidget(data_group)
        
        layout.addStretch()
        
    def browse_request_file(self):
        """Browse for request file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Request File", "", "All Files (*)"
        )
        if filename:
            self.request_file_input.setText(filename)
            
    def browse_log_file(self):
        """Browse for log file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Log File", "", "Log Files (*.log);;All Files (*)"
        )
        if filename:
            self.log_file_input.setText(filename)
            
    def browse_bulk_file(self):
        """Browse for bulk file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Bulk Target File", "", "Text Files (*.txt);;All Files (*)"
        )
        if filename:
            self.bulk_file_input.setText(filename)
            
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.url_input.text():
            options['url'] = self.url_input.text()
            
        if self.request_file_input.text():
            options['requestfile'] = self.request_file_input.text()
            
        if self.log_file_input.text():
            options['logfile'] = self.log_file_input.text()
            
        if self.bulk_file_input.text():
            options['bulkfile'] = self.bulk_file_input.text()
            
        if self.sitemap_input.text():
            options['sitemap_url'] = self.sitemap_input.text()
            
        if self.method_combo.currentText() != "GET":
            options['method'] = self.method_combo.currentText()
            
        if self.url_reload_check.isChecked():
            options['url_reload'] = True
            
        if self.crawl_depth_spin.value() > 0:
            options['crawldepth'] = self.crawl_depth_spin.value()
            
        if self.crawl_exclude_input.text():
            options['crawl_exclude'] = self.crawl_exclude_input.text()
            
        if self.data_input.toPlainText():
            options['data'] = self.data_input.toPlainText()
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.url_input.clear()
        self.request_file_input.clear()
        self.log_file_input.clear()
        self.bulk_file_input.clear()
        self.sitemap_input.clear()
        self.method_combo.setCurrentIndex(0)
        self.url_reload_check.setChecked(False)
        self.crawl_depth_spin.setValue(0)
        self.crawl_exclude_input.clear()
        self.data_input.clear()
