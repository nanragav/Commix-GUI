#!/usr/bin/env python
# encoding: UTF-8

"""
Injection Tab - Configure injection options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QGroupBox, QSpinBox, QDoubleSpinBox, QTextEdit,
    QPushButton, QHBoxLayout, QFileDialog, QLabel, QScrollArea
)
from PyQt6.QtCore import Qt


class InjectionTab(QWidget):
    """Tab for injection configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        
        # Parameter Testing Group
        param_group = QGroupBox("Parameter Testing")
        param_layout = QFormLayout()
        
        self.test_param_input = QLineEdit()
        self.test_param_input.setPlaceholderText("id,name,user")
        param_layout.addRow("Test Parameter(s) (-p):", self.test_param_input)
        
        self.skip_param_input = QLineEdit()
        self.skip_param_input.setPlaceholderText("csrf_token,session")
        param_layout.addRow("Skip Parameter(s) (--skip):", self.skip_param_input)
        
        param_group.setLayout(param_layout)
        layout.addWidget(param_group)
        
        # Injection Payload Group
        payload_group = QGroupBox("Injection Payload")
        payload_layout = QFormLayout()
        
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("'")
        payload_layout.addRow("Prefix (--prefix):", self.prefix_input)
        
        self.suffix_input = QLineEdit()
        self.suffix_input.setPlaceholderText("'")
        payload_layout.addRow("Suffix (--suffix):", self.suffix_input)
        
        payload_group.setLayout(payload_layout)
        layout.addWidget(payload_group)
        
        # Technique Group
        technique_group = QGroupBox("Injection Techniques")
        technique_layout = QFormLayout()
        
        self.technique_input = QLineEdit()
        self.technique_input.setPlaceholderText("c,e,t,f (classic,eval,time,file)")
        technique_layout.addRow("Technique(s) (--technique):", self.technique_input)
        
        self.skip_technique_input = QLineEdit()
        self.skip_technique_input.setPlaceholderText("f")
        technique_layout.addRow("Skip Technique(s) (--skip-technique):", self.skip_technique_input)
        
        technique_layout.addRow(QLabel("<i>c=classic, e=eval, t=time-based, f=file-based</i>"), QLabel(""))
        
        technique_group.setLayout(technique_layout)
        layout.addWidget(technique_group)
        
        # Time-Based Options Group
        time_group = QGroupBox("Time-Based Injection Options")
        time_layout = QFormLayout()
        
        self.timesec_spin = QDoubleSpinBox()
        self.timesec_spin.setMinimum(0.1)
        self.timesec_spin.setMaximum(10.0)
        self.timesec_spin.setValue(1.0)
        self.timesec_spin.setSingleStep(0.1)
        time_layout.addRow("Time Delay (--time-sec):", self.timesec_spin)
        
        self.maxlen_spin = QSpinBox()
        self.maxlen_spin.setMinimum(1)
        self.maxlen_spin.setMaximum(10000)
        self.maxlen_spin.setValue(10000)
        time_layout.addRow("Max Output Length (--maxlen):", self.maxlen_spin)
        
        time_group.setLayout(time_layout)
        layout.addWidget(time_group)
        
        # OS Options Group
        os_group = QGroupBox("Operating System Options")
        os_layout = QFormLayout()
        
        self.os_cmd_input = QLineEdit()
        self.os_cmd_input.setPlaceholderText("whoami")
        os_layout.addRow("Single OS Command (--os-cmd):", self.os_cmd_input)
        
        self.os_input = QLineEdit()
        self.os_input.setPlaceholderText("Windows or Unix")
        os_layout.addRow("Force OS (--os):", self.os_input)
        
        self.alter_shell_input = QLineEdit()
        self.alter_shell_input.setPlaceholderText("Python")
        os_layout.addRow("Alternative Shell (--alter-shell):", self.alter_shell_input)
        
        os_group.setLayout(os_layout)
        layout.addWidget(os_group)
        
        # File-Based Options Group
        file_group = QGroupBox("File-Based Injection Options")
        file_layout = QFormLayout()
        
        self.tmp_path_input = QLineEdit()
        self.tmp_path_input.setPlaceholderText("/tmp")
        file_layout.addRow("Temp Path (--tmp-path):", self.tmp_path_input)
        
        self.web_root_input = QLineEdit()
        self.web_root_input.setPlaceholderText("/var/www/html")
        file_layout.addRow("Web Root (--web-root):", self.web_root_input)
        
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)
        
        # Tamper Scripts Group
        tamper_group = QGroupBox("Tamper Scripts")
        tamper_layout = QVBoxLayout()
        
        tamper_layout.addWidget(QLabel("Tamper Script(s) (--tamper):"))
        self.tamper_input = QTextEdit()
        self.tamper_input.setPlaceholderText("space2plus,base64encode")
        self.tamper_input.setMaximumHeight(60)
        tamper_layout.addWidget(self.tamper_input)
        
        tamper_layout.addWidget(QLabel("<i>Available: backslashes, backticks, base64encode, caret, dollaratsigns,</i>"))
        tamper_layout.addWidget(QLabel("<i>doublequotes, hexencode, multiplespaces, nested, printf2echo,</i>"))
        tamper_layout.addWidget(QLabel("<i>randomcase, rev, singlequotes, slash2env, sleep2timeout,</i>"))
        tamper_layout.addWidget(QLabel("<i>sleep2usleep, space2htab, space2ifs, space2plus, space2vtab,</i>"))
        tamper_layout.addWidget(QLabel("<i>uninitializedvariable, xforwardedfor</i>"))
        
        tamper_group.setLayout(tamper_layout)
        layout.addWidget(tamper_group)
        
        # Metasploit Group
        msf_group = QGroupBox("Metasploit Integration")
        msf_layout = QFormLayout()
        
        msf_path_layout = QHBoxLayout()
        self.msf_path_input = QLineEdit()
        self.msf_path_input.setPlaceholderText("/usr/share/metasploit-framework")
        msf_path_btn = QPushButton("Browse...")
        msf_path_btn.clicked.connect(self.browse_msf_path)
        msf_path_layout.addWidget(self.msf_path_input)
        msf_path_layout.addWidget(msf_path_btn)
        
        msf_layout.addRow("MSF Path (--msf-path):", msf_path_layout)
        
        msf_group.setLayout(msf_layout)
        layout.addWidget(msf_group)
        
        layout.addStretch()
        
        scroll.setWidget(container)
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
        
    def browse_msf_path(self):
        """Browse for Metasploit path"""
        dirname = QFileDialog.getExistingDirectory(
            self, "Select Metasploit Directory"
        )
        if dirname:
            self.msf_path_input.setText(dirname)
            
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.test_param_input.text():
            options['test_parameter'] = self.test_param_input.text()
            
        if self.skip_param_input.text():
            options['skip_parameter'] = self.skip_param_input.text()
            
        if self.prefix_input.text():
            options['prefix'] = self.prefix_input.text()
            
        if self.suffix_input.text():
            options['suffix'] = self.suffix_input.text()
            
        if self.technique_input.text():
            options['tech'] = self.technique_input.text()
            
        if self.skip_technique_input.text():
            options['skip_tech'] = self.skip_technique_input.text()
            
        if self.timesec_spin.value() != 1.0:
            options['timesec'] = self.timesec_spin.value()
            
        if self.maxlen_spin.value() != 10000:
            options['maxlen'] = self.maxlen_spin.value()
            
        if self.os_cmd_input.text():
            options['os_cmd'] = self.os_cmd_input.text()
            
        if self.os_input.text():
            options['os'] = self.os_input.text()
            
        if self.alter_shell_input.text():
            options['alter_shell'] = self.alter_shell_input.text()
            
        if self.tmp_path_input.text():
            options['tmp_path'] = self.tmp_path_input.text()
            
        if self.web_root_input.text():
            options['web_root'] = self.web_root_input.text()
            
        if self.tamper_input.toPlainText():
            options['tamper'] = self.tamper_input.toPlainText()
            
        if self.msf_path_input.text():
            options['msf_path'] = self.msf_path_input.text()
            
        return options
    
    def set_options(self, options):
        """Load options into this tab"""
        if 'test_parameter' in options:
            self.test_param_input.setText(options['test_parameter'])
        if 'skip_parameter' in options:
            self.skip_param_input.setText(options['skip_parameter'])
        if 'prefix' in options:
            self.prefix_input.setText(options['prefix'])
        if 'suffix' in options:
            self.suffix_input.setText(options['suffix'])
        if 'tech' in options:
            self.technique_input.setText(options['tech'])
        if 'skip_tech' in options:
            self.skip_technique_input.setText(options['skip_tech'])
        if 'timesec' in options:
            self.timesec_spin.setValue(options['timesec'])
        if 'maxlen' in options:
            self.maxlen_spin.setValue(options['maxlen'])
        if 'os_cmd' in options:
            self.os_cmd_input.setText(options['os_cmd'])
        if 'os' in options:
            self.os_input.setText(options['os'])
        if 'alter_shell' in options:
            self.alter_shell_input.setText(options['alter_shell'])
        if 'tmp_path' in options:
            self.tmp_path_input.setText(options['tmp_path'])
        if 'web_root' in options:
            self.web_root_input.setText(options['web_root'])
        if 'tamper' in options:
            self.tamper_input.setPlainText(options['tamper'])
        if 'msf_path' in options:
            self.msf_path_input.setText(options['msf_path'])
        
    def reset(self):
        """Reset all fields to default"""
        self.test_param_input.clear()
        self.skip_param_input.clear()
        self.prefix_input.clear()
        self.suffix_input.clear()
        self.technique_input.clear()
        self.skip_technique_input.clear()
        self.timesec_spin.setValue(1.0)
        self.maxlen_spin.setValue(10000)
        self.os_cmd_input.clear()
        self.os_input.clear()
        self.alter_shell_input.clear()
        self.tmp_path_input.clear()
        self.web_root_input.clear()
        self.tamper_input.clear()
        self.msf_path_input.clear()
