#!/usr/bin/env python
# encoding: UTF-8

"""
Session Manager - Comprehensive save/load for all GUI fields and output
"""

import json
import os
from datetime import datetime


class SessionManager:
    """Manage complete session data including all fields and output"""
    
    def __init__(self):
        self.current_file = None
        self.is_modified = False
        
    def save_session(self, filename, session_data):
        """
        Save complete session to file
        
        Args:
            filename: Path to save file (.cproj extension)
            session_data: Dictionary containing:
                - tabs_data: Data from all configuration tabs
                - output_data: Console output and metadata
                - metadata: Session info (timestamp, version, etc.)
        """
        try:
            # Add metadata
            full_data = {
                'version': '1.0.0',
                'saved_at': datetime.now().isoformat(),
                'session_data': session_data
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(full_data, f, indent=4, ensure_ascii=False)
            
            self.current_file = filename
            self.is_modified = False
            return True
            
        except Exception as e:
            raise Exception(f"Failed to save session: {str(e)}")
    
    def load_session(self, filename):
        """
        Load complete session from file
        
        Args:
            filename: Path to session file (.cproj)
            
        Returns:
            Dictionary containing session_data and metadata
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Session file not found: {filename}")
            
            with open(filename, 'r', encoding='utf-8') as f:
                full_data = json.load(f)
            
            # Validate file format
            if 'version' not in full_data or 'session_data' not in full_data:
                raise ValueError("Invalid session file format")
            
            self.current_file = filename
            self.is_modified = False
            
            return full_data
            
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON format: {str(e)}")
        except Exception as e:
            raise Exception(f"Failed to load session: {str(e)}")
    
    def collect_all_data(self, tabs, output_console):
        """
        Collect all data from tabs and output console
        
        Args:
            tabs: Dictionary of tab objects
            output_console: Output console widget
            
        Returns:
            Complete session data dictionary
        """
        session_data = {
            'tabs_data': {},
            'output_data': {},
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'tabs_count': len(tabs)
            }
        }
        
        # Collect data from all tabs
        for tab_name, tab_widget in tabs.items():
            if hasattr(tab_widget, 'get_options'):
                session_data['tabs_data'][tab_name] = tab_widget.get_options()
        
        # Collect output console data
        if output_console:
            session_data['output_data'] = {
                'text': output_console.get_output_text(),
                'stats': output_console.get_stats()
            }
        
        return session_data
    
    def restore_all_data(self, session_data, tabs, output_console):
        """
        Restore all data to tabs and output console
        
        Args:
            session_data: Complete session data
            tabs: Dictionary of tab objects
            output_console: Output console widget
        """
        # Restore tab data
        tabs_data = session_data.get('tabs_data', {})
        for tab_name, tab_widget in tabs.items():
            if tab_name in tabs_data and hasattr(tab_widget, 'set_options'):
                tab_widget.set_options(tabs_data[tab_name])
        
        # Restore output data
        output_data = session_data.get('output_data', {})
        if output_console and output_data:
            if 'text' in output_data:
                output_console.set_output_text(output_data['text'])
            if 'stats' in output_data:
                output_console.set_stats(output_data['stats'])
    
    def mark_modified(self):
        """Mark current session as modified"""
        self.is_modified = True
    
    def is_session_modified(self):
        """Check if session has unsaved changes"""
        return self.is_modified
    
    def get_current_file(self):
        """Get current session file path"""
        return self.current_file
    
    def clear_current_file(self):
        """Clear current file reference (for new session)"""
        self.current_file = None
        self.is_modified = False
