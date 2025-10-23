#!/usr/bin/env python
# encoding: UTF-8

"""
Detection Tab - Configure detection options
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QGroupBox, QSpinBox, QCheckBox, QLabel
)


class DetectionTab(QWidget):
    """Tab for detection configuration"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        
        # Detection Level Group
        level_group = QGroupBox("Detection Configuration")
        level_layout = QFormLayout()
        
        self.level_spin = QSpinBox()
        self.level_spin.setMinimum(1)
        self.level_spin.setMaximum(3)
        self.level_spin.setValue(1)
        level_layout.addRow("Test Level (--level):", self.level_spin)
        level_layout.addRow("", QLabel("<i>1=basic, 2=medium, 3=thorough</i>"))
        
        self.skip_calc_check = QCheckBox("Skip mathematic calculation during detection")
        level_layout.addRow("", self.skip_calc_check)
        
        self.skip_empty_check = QCheckBox("Skip testing parameters with empty values")
        level_layout.addRow("", self.skip_empty_check)
        
        self.smart_check = QCheckBox("Perform thorough tests only if positive heuristic")
        level_layout.addRow("", self.smart_check)
        
        level_group.setLayout(level_layout)
        layout.addWidget(level_group)
        
        # Failed Tries Group
        tries_group = QGroupBox("File-Based Technique")
        tries_layout = QFormLayout()
        
        self.failed_tries_spin = QSpinBox()
        self.failed_tries_spin.setMinimum(1)
        self.failed_tries_spin.setMaximum(100)
        self.failed_tries_spin.setValue(20)
        tries_layout.addRow("Failed Tries (--failed-tries):", self.failed_tries_spin)
        
        tries_group.setLayout(tries_layout)
        layout.addWidget(tries_group)
        
        layout.addStretch()
        
    def get_options(self):
        """Get all options from this tab"""
        options = {}
        
        if self.level_spin.value() != 1:
            options['level'] = self.level_spin.value()
            
        if self.skip_calc_check.isChecked():
            options['skip_calc'] = True
            
        if self.skip_empty_check.isChecked():
            options['skip_empty'] = True
            
        if self.smart_check.isChecked():
            options['smart'] = True
            
        if self.failed_tries_spin.value() != 20:
            options['failed_tries'] = self.failed_tries_spin.value()
            
        return options
    
    def set_options(self, options):
        """Load options into this tab"""
        if 'level' in options:
            self.level_spin.setValue(options['level'])
        if 'skip_calc' in options:
            self.skip_calc_check.setChecked(options['skip_calc'])
        if 'skip_empty' in options:
            self.skip_empty_check.setChecked(options['skip_empty'])
        if 'smart' in options:
            self.smart_check.setChecked(options['smart'])
        if 'failed_tries' in options:
            self.failed_tries_spin.setValue(options['failed_tries'])
        
    def reset(self):
        """Reset all fields to default"""
        self.level_spin.setValue(1)
        self.skip_calc_check.setChecked(False)
        self.skip_empty_check.setChecked(False)
        self.smart_check.setChecked(False)
        self.failed_tries_spin.setValue(20)
