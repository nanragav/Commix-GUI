#!/usr/bin/env python
# encoding: UTF-8

"""
Miscellaneous Tab - Configure general and misc options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QGroupBox, QCheckBox, QSpinBox, QLabel, QPushButton,
    QHBoxLayout, QFileDialog, QScrollArea, QTextEdit
)
from PyQt6.QtCore import Qt


class MiscTab(QWidget):
    """Tab for miscellaneous configuration"""
    
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
        
        # General Options Group
        general_group = QGroupBox("General Options")
        general_layout = QFormLayout()
        
        self.verbose_spin = QSpinBox()
        self.verbose_spin.setMinimum(0)
        self.verbose_spin.setMaximum(4)
        self.verbose_spin.setValue(0)
        general_layout.addRow("Verbosity Level (-v):", self.verbose_spin)
        
        self.batch_check = QCheckBox("Never ask for user input (batch mode)")
        general_layout.addRow("", self.batch_check)
        
        self.wizard_check = QCheckBox("Simple wizard interface for beginners")
        general_layout.addRow("", self.wizard_check)
        
        self.offline_check = QCheckBox("Work in offline mode")
        general_layout.addRow("", self.offline_check)
        
        general_group.setLayout(general_layout)
        layout.addWidget(general_group)
        
        # Session Options Group
        session_group = QGroupBox("Session Management")
        session_layout = QFormLayout()
        
        session_file_layout = QHBoxLayout()
        self.session_file_input = QLineEdit()
        self.session_file_input.setPlaceholderText("session.sqlite")
        session_file_btn = QPushButton("Browse...")
        session_file_btn.clicked.connect(self.browse_session_file)
        session_file_layout.addWidget(self.session_file_input)
        session_file_layout.addWidget(session_file_btn)
        
        session_layout.addRow("Session File (-s):", session_file_layout)
        
        self.flush_session_check = QCheckBox("Flush session files for current target")
        session_layout.addRow("", self.flush_session_check)
        
        self.ignore_session_check = QCheckBox("Ignore results stored in session file")
        session_layout.addRow("", self.ignore_session_check)
        
        session_group.setLayout(session_layout)
        layout.addWidget(session_group)
        
        # Output Options Group
        output_group = QGroupBox("Output & Logging")
        output_layout = QFormLayout()
        
        output_dir_layout = QHBoxLayout()
        self.output_dir_input = QLineEdit()
        self.output_dir_input.setPlaceholderText("Custom output directory")
        output_dir_btn = QPushButton("Browse...")
        output_dir_btn.clicked.connect(self.browse_output_dir)
        output_dir_layout.addWidget(self.output_dir_input)
        output_dir_layout.addWidget(output_dir_btn)
        
        output_layout.addRow("Output Directory (--output-dir):", output_dir_layout)
        
        traffic_file_layout = QHBoxLayout()
        self.traffic_file_input = QLineEdit()
        self.traffic_file_input.setPlaceholderText("traffic.log")
        traffic_file_btn = QPushButton("Browse...")
        traffic_file_btn.clicked.connect(self.browse_traffic_file)
        traffic_file_layout.addWidget(self.traffic_file_input)
        traffic_file_layout.addWidget(traffic_file_btn)
        
        output_layout.addRow("Traffic Log File (-t):", traffic_file_layout)
        
        self.no_logging_check = QCheckBox("Disable logging to file")
        output_layout.addRow("", self.no_logging_check)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Detection Options Group
        detection_group = QGroupBox("Detection & Filtering")
        detection_layout = QFormLayout()
        
        self.skip_heuristics_check = QCheckBox("Skip heuristic detection for code injection")
        detection_layout.addRow("", self.skip_heuristics_check)
        
        self.skip_waf_check = QCheckBox("Skip heuristic detection of WAF/IPS")
        detection_layout.addRow("", self.skip_waf_check)
        
        detection_group.setLayout(detection_layout)
        layout.addWidget(detection_group)
        
        # Advanced Options Group
        advanced_group = QGroupBox("Advanced Options")
        advanced_layout = QFormLayout()
        
        self.codec_input = QLineEdit()
        self.codec_input.setPlaceholderText("utf-8, ascii, etc.")
        advanced_layout.addRow("Character Encoding (--codec):", self.codec_input)
        
        self.charset_input = QLineEdit()
        self.charset_input.setPlaceholderText("0123456789abcdef")
        advanced_layout.addRow("Injection Charset (--charset):", self.charset_input)
        
        self.time_limit_spin = QSpinBox()
        self.time_limit_spin.setMinimum(0)
        self.time_limit_spin.setMaximum(86400)
        self.time_limit_spin.setValue(0)
        self.time_limit_spin.setToolTip("0 means no limit")
        advanced_layout.addRow("Time Limit in seconds (--time-limit):", self.time_limit_spin)
        
        self.check_internet_check = QCheckBox("Check internet connection before testing")
        advanced_layout.addRow("", self.check_internet_check)
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
        # Alerts Group
        alert_group = QGroupBox("Alerts")
        alert_layout = QFormLayout()
        
        alert_layout.addRow(QLabel("Alert Command (--alert):"), QLabel(""))
        self.alert_input = QTextEdit()
        self.alert_input.setPlaceholderText("Command to run when injection point is found")
        self.alert_input.setMaximumHeight(60)
        alert_layout.addRow("", self.alert_input)
        
        alert_group.setLayout(alert_layout)
        layout.addWidget(alert_group)
        
        # Answers Group
        answers_group = QGroupBox("Predefined Answers")
        answers_layout = QFormLayout()
        
        self.answers_input = QLineEdit()
        self.answers_input.setPlaceholderText("quit=N,follow=N")
        answers_layout.addRow("Answers (--answers):", self.answers_input)
        
        answers_group.setLayout(answers_layout)
        layout.addWidget(answers_group)
        
        layout.addStretch()
        
        scroll.setWidget(container)
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
        
    def browse_session_file(self):
        """Browse for session file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Session File", "", "SQLite Files (*.sqlite);;All Files (*)"
        )
        if filename:
            self.session_file_input.setText(filename)
            
    def browse_output_dir(self):
        """Browse for output directory"""
        dirname = QFileDialog.getExistingDirectory(
            self, "Select Output Directory"
        )
        if dirname:
            self.output_dir_input.setText(dirname)
            
    def browse_traffic_file(self):
        """Browse for traffic log file"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Select Traffic Log File", "", "Log Files (*.log);;All Files (*)"
        )
        if filename:
            self.traffic_file_input.setText(filename)
            
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.verbose_spin.value() > 0:
            options['verbose'] = self.verbose_spin.value()
            
        if self.batch_check.isChecked():
            options['batch'] = True
            
        if self.wizard_check.isChecked():
            options['wizard'] = True
            
        if self.offline_check.isChecked():
            options['offline'] = True
            
        if self.session_file_input.text():
            options['session_file'] = self.session_file_input.text()
            
        if self.flush_session_check.isChecked():
            options['flush_session'] = True
            
        if self.ignore_session_check.isChecked():
            options['ignore_session'] = True
            
        if self.output_dir_input.text():
            options['output_dir'] = self.output_dir_input.text()
            
        if self.traffic_file_input.text():
            options['traffic_file'] = self.traffic_file_input.text()
            
        if self.no_logging_check.isChecked():
            options['no_logging'] = True
            
        if self.skip_heuristics_check.isChecked():
            options['skip_heuristics'] = True
            
        if self.skip_waf_check.isChecked():
            options['skip_waf'] = True
            
        if self.codec_input.text():
            options['codec'] = self.codec_input.text()
            
        if self.charset_input.text():
            options['charset'] = self.charset_input.text()
            
        if self.time_limit_spin.value() > 0:
            options['time_limit'] = self.time_limit_spin.value()
            
        if self.check_internet_check.isChecked():
            options['check_internet'] = True
            
        if self.alert_input.toPlainText():
            options['alert'] = self.alert_input.toPlainText()
            
        if self.answers_input.text():
            options['answers'] = self.answers_input.text()
            
        return options
    
    def set_options(self, options):
        """Load options into this tab"""
        if 'verbose' in options:
            self.verbose_spin.setValue(options['verbose'])
        if 'batch' in options:
            self.batch_check.setChecked(options['batch'])
        if 'wizard' in options:
            self.wizard_check.setChecked(options['wizard'])
        if 'offline' in options:
            self.offline_check.setChecked(options['offline'])
        if 'session_file' in options:
            self.session_file_input.setText(options['session_file'])
        if 'flush_session' in options:
            self.flush_session_check.setChecked(options['flush_session'])
        if 'ignore_session' in options:
            self.ignore_session_check.setChecked(options['ignore_session'])
        if 'output_dir' in options:
            self.output_dir_input.setText(options['output_dir'])
        if 'traffic_file' in options:
            self.traffic_file_input.setText(options['traffic_file'])
        if 'no_logging' in options:
            self.no_logging_check.setChecked(options['no_logging'])
        if 'skip_heuristics' in options:
            self.skip_heuristics_check.setChecked(options['skip_heuristics'])
        if 'skip_waf' in options:
            self.skip_waf_check.setChecked(options['skip_waf'])
        if 'codec' in options:
            self.codec_input.setText(options['codec'])
        if 'charset' in options:
            self.charset_input.setText(options['charset'])
        if 'time_limit' in options:
            self.time_limit_spin.setValue(options['time_limit'])
        if 'check_internet' in options:
            self.check_internet_check.setChecked(options['check_internet'])
        if 'alert' in options:
            self.alert_input.setPlainText(options['alert'])
        if 'answers' in options:
            self.answers_input.setText(options['answers'])
        
    def reset(self):
        """Reset all fields to default"""
        self.verbose_spin.setValue(0)
        self.batch_check.setChecked(False)
        self.wizard_check.setChecked(False)
        self.offline_check.setChecked(False)
        self.session_file_input.clear()
        self.flush_session_check.setChecked(False)
        self.ignore_session_check.setChecked(False)
        self.output_dir_input.clear()
        self.traffic_file_input.clear()
        self.no_logging_check.setChecked(False)
        self.skip_heuristics_check.setChecked(False)
        self.skip_waf_check.setChecked(False)
        self.codec_input.clear()
        self.charset_input.clear()
        self.time_limit_spin.setValue(0)
        self.check_internet_check.setChecked(False)
        self.alert_input.clear()
        self.answers_input.clear()
