#!/usr/bin/env python
# encoding: UTF-8

"""
Output Console - Display output with syntax highlighting
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QLabel, QFileDialog
from PyQt6.QtGui import QTextCursor, QColor, QTextCharFormat, QFont
from PyQt6.QtCore import Qt


class OutputConsole(QWidget):
    """Console widget for displaying Commix output"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        
        # Add header with stats
        header_layout = QHBoxLayout()
        
        self.title_label = QLabel("📟 Command Output Console")
        self.title_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font-weight: bold;
                font-size: 14px;
                padding: 5px;
            }
        """)
        
        self.stats_label = QLabel("Ready")
        self.stats_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                padding: 5px;
            }
        """)
        
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.stats_label)
        
        layout.addLayout(header_layout)
        
        # Create text display - larger and more readable
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        
        # Use monospace font for better code readability
        try:
            # Try Consolas first (Windows), then fallback to others
            self.output_text.setFont(QFont("Consolas", 10))
        except:
            try:
                self.output_text.setFont(QFont("Monaco", 10))  # macOS
            except:
                self.output_text.setFont(QFont("Courier New", 10))  # Fallback
        
        self.output_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 2px solid #3e3e3e;
                border-radius: 4px;
                padding: 10px;
                line-height: 1.4;
            }
        """)
        
        layout.addWidget(self.output_text)
        
        # Create control buttons - more prominent
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.clear_btn = QPushButton("🗑️ Clear Output")
        self.clear_btn.setMinimumHeight(35)
        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        
        self.save_btn = QPushButton("💾 Save to File")
        self.save_btn.setMinimumHeight(35)
        self.save_btn.clicked.connect(self.save_output)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        
        self.copy_btn = QPushButton("📋 Copy All")
        self.copy_btn.setMinimumHeight(35)
        self.copy_btn.clicked.connect(self.copy_all)
        self.copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
        """)
        
        # Add line count indicator
        self.line_count_label = QLabel("Lines: 0")
        self.line_count_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                padding: 8px;
            }
        """)
        
        button_layout.addWidget(self.clear_btn)
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.copy_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.line_count_label)
        
        layout.addLayout(button_layout)
        
    def append_output(self, text):
        """Append normal output text"""
        self.append_colored_text(text, QColor("#d4d4d4"))
        
    def append_error(self, text):
        """Append error text in red"""
        self.append_colored_text(text, QColor("#f48771"))
        
    def append_success(self, text):
        """Append success text in green"""
        self.append_colored_text(text, QColor("#4ec9b0"))
        
    def append_warning(self, text):
        """Append warning text in yellow"""
        self.append_colored_text(text, QColor("#dcdcaa"))
        
    def append_info(self, text):
        """Append info text in blue"""
        self.append_colored_text(text, QColor("#569cd6"))
        
    def append_colored_text(self, text, color):
        """Append text with specified color"""
        cursor = self.output_text.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        
        format = QTextCharFormat()
        format.setForeground(color)
        
        cursor.insertText(text + "\n", format)
        
        # Auto-scroll to bottom
        self.output_text.setTextCursor(cursor)
        self.output_text.ensureCursorVisible()
        
        # Update line count
        self.update_line_count()
        
    def update_line_count(self):
        """Update the line count display"""
        line_count = self.output_text.document().blockCount()
        self.line_count_label.setText(f"Lines: {line_count}")
        self.stats_label.setText(f"Lines: {line_count}")
        
    def clear(self):
        """Clear all output"""
        self.output_text.clear()
        self.update_line_count()
        
    def save_output(self):
        """Save output to file"""
        from PyQt6.QtWidgets import QFileDialog
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Output", "", "Text Files (*.txt);;Log Files (*.log);;All Files (*)"
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.output_text.toPlainText())
                self.append_success(f"✓ Output saved to: {filename}")
            except Exception as e:
                self.append_error(f"✗ Failed to save output: {str(e)}")
                
    def copy_all(self):
        """Copy all output to clipboard"""
        from PyQt6.QtWidgets import QApplication
        
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text.toPlainText())
        self.append_info("✓ Output copied to clipboard")
    
    def get_output_text(self):
        """Get all output text for saving"""
        return self.output_text.toPlainText()
    
    def set_output_text(self, text):
        """Set output text from loaded session"""
        self.output_text.setPlainText(text)
        self.update_line_count()
    
    def get_stats(self):
        """Get current stats for saving"""
        return {
            'line_count': self.output_text.document().blockCount(),
            'char_count': len(self.output_text.toPlainText())
        }
    
    def set_stats(self, stats):
        """Restore stats from session"""
        if stats:
            line_count = stats.get('line_count', 0)
            self.stats_label.setText(f"Lines: {line_count}")

