#!/usr/bin/env python
# encoding: UTF-8

"""
Commix Runner - Execute Commix with specified options
"""

import os
import sys
import subprocess
from PyQt6.QtCore import QThread, pyqtSignal
from gui_modules.option_validator import get_validator


class CommixRunner(QThread):
    """Thread for running Commix"""
    
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(int)
    
    def __init__(self, options, commix_manager=None):
        super().__init__()
        self.options = options
        self.commix_manager = commix_manager
        self.process = None
        self.should_stop = False
        
    def run(self):
        """Execute Commix"""
        try:
            # Validate options before execution
            validator = get_validator()
            is_valid, errors, warnings = validator.validate_all(self.options)
            
            if not is_valid:
                # Emit validation errors
                self.error_signal.emit("\n❌ VALIDATION ERRORS FOUND:\n")
                self.error_signal.emit("=" * 80 + "\n")
                for i, error in enumerate(errors, 1):
                    self.error_signal.emit(f"{i}. {error}\n")
                self.error_signal.emit("=" * 80 + "\n")
                self.error_signal.emit("\n⚠️  Please fix the above errors before running Commix.\n")
                self.finished_signal.emit(1)
                return
            
            # Emit warnings if any
            if warnings:
                self.output_signal.emit("\n⚠️  WARNINGS:\n")
                for i, warning in enumerate(warnings, 1):
                    self.output_signal.emit(f"{i}. {warning}\n")
                self.output_signal.emit("\n")
            
            # Build command
            cmd = self.build_command()
            
            # Emit command being executed
            self.output_signal.emit(f"Executing: {' '.join(cmd)}\n")
            self.output_signal.emit("=" * 80 + "\n")
            
            # Get Commix command from manager
            if self.commix_manager:
                full_cmd = self.commix_manager.get_commix_command() + cmd[2:]  # Skip 'python' and 'commix.py'
            else:
                # Fallback to local commix folder
                commix_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commix")
                commix_script = os.path.join(commix_path, "commix.py")
                
                if not os.path.exists(commix_script):
                    self.error_signal.emit(f"Error: Commix not found at {commix_script}")
                    self.finished_signal.emit(1)
                    return
                
                full_cmd = [sys.executable, commix_script] + cmd[2:]  # Skip 'python' and 'commix.py' from cmd
            
            # Execute process
            self.process = subprocess.Popen(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Read output in real-time
            while True:
                if self.should_stop:
                    self.process.terminate()
                    self.process.wait(timeout=5)
                    break
                    
                output = self.process.stdout.readline()
                if output:
                    self.output_signal.emit(output.rstrip())
                    
                error = self.process.stderr.readline()
                if error:
                    self.error_signal.emit(error.rstrip())
                    
                # Check if process has finished
                if output == '' and error == '' and self.process.poll() is not None:
                    break
            
            # Get remaining output
            stdout, stderr = self.process.communicate()
            if stdout:
                self.output_signal.emit(stdout)
            if stderr:
                self.error_signal.emit(stderr)
            
            exit_code = self.process.returncode
            self.finished_signal.emit(exit_code)
            
        except Exception as e:
            self.error_signal.emit(f"Error executing Commix: {str(e)}")
            self.finished_signal.emit(1)
            
    def build_command(self):
        """Build Commix command from options"""
        cmd = ["python", "commix/commix.py"]
        
        for key, value in self.options.items():
            if value is None or value == "" or value is False:
                continue
                
            # Convert underscores to hyphens for command line
            param_name = key.replace('_', '-')
            
            if value is True:
                cmd.append(f"--{param_name}")
            else:
                cmd.append(f"--{param_name}")
                cmd.append(str(value))
                
        return cmd
        
    def stop(self):
        """Stop the running process"""
        self.should_stop = True
        if self.process and self.process.poll() is None:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                self.process.kill()
