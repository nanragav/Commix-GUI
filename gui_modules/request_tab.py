#!/usr/bin/env python
# encoding: UTF-8

"""
Request Tab - Configure HTTP request options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit,
    QTextEdit, QPushButton, QGroupBox, QLabel, QSpinBox,
    QCheckBox, QFileDialog, QComboBox, QScrollArea
)
from PyQt6.QtCore import Qt


class RequestTab(QWidget):
    """Tab for HTTP request configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        
        # HTTP Headers Group
        headers_group = QGroupBox("HTTP Headers")
        headers_layout = QFormLayout()
        
        self.user_agent_input = QLineEdit()
        self.user_agent_input.setPlaceholderText("Custom User-Agent")
        headers_layout.addRow("User-Agent (--user-agent):", self.user_agent_input)
        
        self.random_agent_check = QCheckBox("Use random User-Agent")
        headers_layout.addRow("", self.random_agent_check)
        
        self.mobile_check = QCheckBox("Imitate smartphone")
        headers_layout.addRow("", self.mobile_check)
        
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("example.com")
        headers_layout.addRow("Host Header (--host):", self.host_input)
        
        self.referer_input = QLineEdit()
        self.referer_input.setPlaceholderText("http://example.com/")
        headers_layout.addRow("Referer (--referer):", self.referer_input)
        
        self.cookie_input = QLineEdit()
        self.cookie_input.setPlaceholderText("PHPSESSID=abcd1234; user=admin")
        headers_layout.addRow("Cookie (--cookie):", self.cookie_input)
        
        self.cookie_del_input = QLineEdit()
        self.cookie_del_input.setPlaceholderText(";")
        headers_layout.addRow("Cookie Delimiter (--cookie-del):", self.cookie_del_input)
        
        self.header_input = QLineEdit()
        self.header_input.setPlaceholderText("X-Forwarded-For: 127.0.0.1")
        headers_layout.addRow("Extra Header (-H, --header):", self.header_input)
        
        headers_layout.addRow(QLabel("Extra Headers (--headers):"), QLabel(""))
        self.headers_input = QTextEdit()
        self.headers_input.setPlaceholderText("Accept-Language: en-US\\nX-Custom-Header: value")
        self.headers_input.setMaximumHeight(60)
        headers_layout.addRow("", self.headers_input)
        
        headers_group.setLayout(headers_layout)
        layout.addWidget(headers_group)
        
        # Connection Options Group
        connection_group = QGroupBox("Connection Options")
        connection_layout = QFormLayout()
        
        self.timeout_spin = QSpinBox()
        self.timeout_spin.setMinimum(1)
        self.timeout_spin.setMaximum(3600)
        self.timeout_spin.setValue(30)
        connection_layout.addRow("Timeout (--timeout):", self.timeout_spin)
        
        self.retries_spin = QSpinBox()
        self.retries_spin.setMinimum(0)
        self.retries_spin.setMaximum(10)
        self.retries_spin.setValue(3)
        connection_layout.addRow("Retries (--retries):", self.retries_spin)
        
        self.delay_spin = QSpinBox()
        self.delay_spin.setMinimum(0)
        self.delay_spin.setMaximum(60)
        self.delay_spin.setValue(0)
        connection_layout.addRow("Delay (--delay):", self.delay_spin)
        
        self.http10_check = QCheckBox("Use HTTP/1.0")
        connection_layout.addRow("", self.http10_check)
        
        self.force_ssl_check = QCheckBox("Force SSL/HTTPS")
        connection_layout.addRow("", self.force_ssl_check)
        
        self.ignore_redirects_check = QCheckBox("Ignore redirects")
        connection_layout.addRow("", self.ignore_redirects_check)
        
        self.drop_set_cookie_check = QCheckBox("Ignore Set-Cookie header")
        connection_layout.addRow("", self.drop_set_cookie_check)
        
        connection_group.setLayout(connection_layout)
        layout.addWidget(connection_group)
        
        # Proxy Options Group
        proxy_group = QGroupBox("Proxy & Tor")
        proxy_layout = QFormLayout()
        
        self.proxy_input = QLineEdit()
        self.proxy_input.setPlaceholderText("http://127.0.0.1:8080")
        proxy_layout.addRow("Proxy (--proxy):", self.proxy_input)
        
        self.ignore_proxy_check = QCheckBox("Ignore system proxy")
        proxy_layout.addRow("", self.ignore_proxy_check)
        
        self.tor_check = QCheckBox("Use Tor network")
        proxy_layout.addRow("", self.tor_check)
        
        self.tor_port_input = QLineEdit()
        self.tor_port_input.setPlaceholderText("8118")
        proxy_layout.addRow("Tor Port (--tor-port):", self.tor_port_input)
        
        self.tor_check_box = QCheckBox("Check Tor usage")
        proxy_layout.addRow("", self.tor_check_box)
        
        proxy_group.setLayout(proxy_layout)
        layout.addWidget(proxy_group)
        
        # Error Handling Group
        error_group = QGroupBox("Error Handling")
        error_layout = QFormLayout()
        
        self.abort_code_input = QLineEdit()
        self.abort_code_input.setPlaceholderText("401,403")
        error_layout.addRow("Abort on Error Code (--abort-code):", self.abort_code_input)
        
        self.ignore_code_input = QLineEdit()
        self.ignore_code_input.setPlaceholderText("404,500")
        error_layout.addRow("Ignore Error Code (--ignore-code):", self.ignore_code_input)
        
        error_group.setLayout(error_layout)
        layout.addWidget(error_group)
        
        # Parameters Group
        params_group = QGroupBox("Parameters")
        params_layout = QFormLayout()
        
        self.param_del_input = QLineEdit()
        self.param_del_input.setPlaceholderText("&")
        params_layout.addRow("Parameter Delimiter (--param-del):", self.param_del_input)
        
        params_group.setLayout(params_layout)
        layout.addWidget(params_group)
        
        layout.addStretch()
        
        scroll.setWidget(container)
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
        
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.user_agent_input.text():
            options['agent'] = self.user_agent_input.text()
            
        if self.random_agent_check.isChecked():
            options['random_agent'] = True
            
        if self.mobile_check.isChecked():
            options['mobile'] = True
            
        if self.host_input.text():
            options['host'] = self.host_input.text()
            
        if self.referer_input.text():
            options['referer'] = self.referer_input.text()
            
        if self.cookie_input.text():
            options['cookie'] = self.cookie_input.text()
            
        if self.cookie_del_input.text():
            options['cdel'] = self.cookie_del_input.text()
            
        if self.header_input.text():
            options['header'] = self.header_input.text()
            
        if self.headers_input.toPlainText():
            options['headers'] = self.headers_input.toPlainText()
            
        if self.timeout_spin.value() != 30:
            options['timeout'] = self.timeout_spin.value()
            
        if self.retries_spin.value() != 3:
            options['retries'] = self.retries_spin.value()
            
        if self.delay_spin.value() > 0:
            options['delay'] = self.delay_spin.value()
            
        if self.http10_check.isChecked():
            options['http10'] = True
            
        if self.force_ssl_check.isChecked():
            options['force_ssl'] = True
            
        if self.ignore_redirects_check.isChecked():
            options['ignore_redirects'] = True
            
        if self.drop_set_cookie_check.isChecked():
            options['drop_set_cookie'] = True
            
        if self.proxy_input.text():
            options['proxy'] = self.proxy_input.text()
            
        if self.ignore_proxy_check.isChecked():
            options['ignore_proxy'] = True
            
        if self.tor_check.isChecked():
            options['tor'] = True
            
        if self.tor_port_input.text():
            options['tor_port'] = self.tor_port_input.text()
            
        if self.tor_check_box.isChecked():
            options['tor_check'] = True
            
        if self.abort_code_input.text():
            options['abort_code'] = self.abort_code_input.text()
            
        if self.ignore_code_input.text():
            options['ignore_code'] = self.ignore_code_input.text()
            
        if self.param_del_input.text():
            options['pdel'] = self.param_del_input.text()
            
        return options
        
    def reset(self):
        """Reset all fields to default"""
        self.user_agent_input.clear()
        self.random_agent_check.setChecked(False)
        self.mobile_check.setChecked(False)
        self.host_input.clear()
        self.referer_input.clear()
        self.cookie_input.clear()
        self.cookie_del_input.clear()
        self.header_input.clear()
        self.headers_input.clear()
        self.timeout_spin.setValue(30)
        self.retries_spin.setValue(3)
        self.delay_spin.setValue(0)
        self.http10_check.setChecked(False)
        self.force_ssl_check.setChecked(False)
        self.ignore_redirects_check.setChecked(False)
        self.drop_set_cookie_check.setChecked(False)
        self.proxy_input.clear()
        self.ignore_proxy_check.setChecked(False)
        self.tor_check.setChecked(False)
        self.tor_port_input.clear()
        self.tor_check_box.setChecked(False)
        self.abort_code_input.clear()
        self.ignore_code_input.clear()
        self.param_del_input.clear()
