#!/usr/bin/env python
# encoding: UTF-8

"""
Commix Manager - Handle Commix installation and detection
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path


class CommixManager:
    """Manage Commix installation and detection"""
    
    def __init__(self):
        self.system = platform.system()
        self.commix_path = None
        self.is_installed = False
        
    def check_admin_privileges(self):
        """Check if running with admin/root privileges"""
        try:
            if self.system == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
            
    def request_admin_privileges(self):
        """Request admin privileges and restart application"""
        if self.system == "Windows":
            try:
                import ctypes
                # Re-run the program with admin rights
                script = os.path.abspath(sys.argv[0])
                params = ' '.join([script] + sys.argv[1:])
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, params, None, 1
                )
                return True
            except Exception as e:
                print(f"Failed to request admin privileges: {e}")
                return False
        else:
            # Unix-like systems
            try:
                # Try using sudo
                args = ['sudo', sys.executable] + sys.argv
                os.execvp('sudo', args)
                return True
            except Exception as e:
                print(f"Failed to request admin privileges: {e}")
                return False
                
    def find_commix_system(self):
        """Find Commix installed in system"""
        # Check common installation paths
        paths_to_check = []
        
        if self.system == "Windows":
            paths_to_check = [
                r"C:\Program Files\Commix",
                r"C:\Program Files (x86)\Commix",
                r"C:\Commix",
                os.path.join(os.path.expanduser("~"), "Commix"),
            ]
        else:
            paths_to_check = [
                "/usr/local/bin/commix",
                "/usr/bin/commix",
                "/opt/commix",
                os.path.join(os.path.expanduser("~"), "commix"),
            ]
            
        # Check if commix is in PATH
        commix_cmd = shutil.which("commix")
        if commix_cmd:
            # Follow symlink if it is one
            if os.path.islink(commix_cmd):
                commix_cmd = os.path.realpath(commix_cmd)
            # Get the directory
            commix_dir = os.path.dirname(commix_cmd)
            if os.path.exists(os.path.join(commix_dir, "commix.py")):
                return commix_dir
                
        # Check common paths
        for path in paths_to_check:
            if os.path.exists(path):
                # Check if it's a directory with commix.py
                if os.path.isdir(path):
                    commix_file = os.path.join(path, "commix.py")
                    if os.path.exists(commix_file):
                        return path
                # Check if it's the commix.py file itself
                elif path.endswith("commix") or path.endswith("commix.py"):
                    if os.path.exists(path):
                        return os.path.dirname(path)
                        
        return None
        
    def find_commix_local(self):
        """Find Commix in local directory"""
        # Check local commix folder
        local_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commix")
        if os.path.exists(local_path):
            commix_file = os.path.join(local_path, "commix.py")
            if os.path.exists(commix_file):
                return local_path
        return None
        
    def detect_commix(self):
        """Detect Commix installation"""
        # First check system installation
        system_path = self.find_commix_system()
        if system_path:
            self.commix_path = system_path
            self.is_installed = True
            return {
                "found": True,
                "path": system_path,
                "location": "system",
                "version": self.get_commix_version(system_path)
            }
            
        # Then check local directory
        local_path = self.find_commix_local()
        if local_path:
            self.commix_path = local_path
            self.is_installed = True
            return {
                "found": True,
                "path": local_path,
                "location": "local",
                "version": self.get_commix_version(local_path)
            }
            
        # Not found
        self.is_installed = False
        return {
            "found": False,
            "path": None,
            "location": None,
            "version": None
        }
        
    def get_commix_version(self, path):
        """Get Commix version"""
        try:
            commix_file = os.path.join(path, "commix.py")
            result = subprocess.run(
                [sys.executable, commix_file, "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                # Extract version from output
                output = result.stdout.strip()
                return output
            return "Unknown"
        except Exception as e:
            return "Unknown"
            
    def install_commix_from_github(self, install_path=None, progress_callback=None):
        """Install Commix from GitHub"""
        try:
            if progress_callback:
                progress_callback("Checking prerequisites...")
                
            # Check if git is installed
            git_cmd = shutil.which("git")
            if not git_cmd:
                error_msg = (
                    "Git is not installed or not found in PATH.\n\n"
                    "To install Git:\n"
                    "• Windows: Download from https://git-scm.com/\n"
                    "• Linux: sudo apt-get install git (Debian/Ubuntu)\n"
                    "• macOS: brew install git\n\n"
                    "Or you can manually download Commix and use 'Browse' to select it."
                )
                return {
                    "success": False,
                    "error": error_msg,
                    "path": None
                }
                
            # Determine installation path
            if not install_path:
                # Check if we have admin privileges
                has_admin = self.check_admin_privileges()
                
                if self.system == "Windows":
                    if has_admin:
                        install_path = r"C:\Program Files\Commix"
                    else:
                        # User-level installation for Windows
                        install_path = os.path.join(os.path.expanduser("~"), "Commix")
                else:
                    if has_admin:
                        install_path = "/opt/commix"
                    else:
                        # User-level installation for Unix
                        install_path = os.path.join(os.path.expanduser("~"), "commix")
                    
            if progress_callback:
                progress_callback(f"Installing to: {install_path}")
                
            # Create parent directory if needed
            try:
                parent_dir = os.path.dirname(install_path)
                if parent_dir and not os.path.exists(parent_dir):
                    os.makedirs(parent_dir, exist_ok=True)
                    
                # Also ensure install_path parent exists
                if not os.path.exists(os.path.dirname(install_path)):
                    os.makedirs(os.path.dirname(install_path), exist_ok=True)
            except PermissionError as e:
                return {
                    "success": False,
                    "error": f"Permission denied creating directory: {install_path}\n\nTry running as administrator or choose a different location.",
                    "path": None
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Failed to create directory: {str(e)}",
                    "path": None
                }
                
            # Clone repository
            if progress_callback:
                progress_callback("Cloning Commix from GitHub...")
                
            result = subprocess.run(
                [git_cmd, "clone", "https://github.com/commixproject/commix.git", install_path],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": f"Failed to clone repository: {result.stderr}",
                    "path": None
                }
                
            # Verify installation
            commix_file = os.path.join(install_path, "commix.py")
            if not os.path.exists(commix_file):
                return {
                    "success": False,
                    "error": "Installation failed: commix.py not found",
                    "path": None
                }
                
            # Try using Commix's built-in --install option
            if progress_callback:
                progress_callback("Running Commix installation...")
            try:
                install_result = subprocess.run(
                    [sys.executable, commix_file, "--install"],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    cwd=install_path
                )
                if progress_callback and install_result.stdout:
                    progress_callback(install_result.stdout)
            except Exception as e:
                # Continue even if --install fails
                if progress_callback:
                    progress_callback(f"Note: --install option not available or failed: {str(e)}")
                
            # Set permissions on Unix-like systems
            if self.system != "Windows":
                if progress_callback:
                    progress_callback("Setting permissions...")
                try:
                    os.chmod(commix_file, 0o755)
                except:
                    pass
                    
            # Create symlink on Unix-like systems
            if self.system != "Windows":
                if progress_callback:
                    progress_callback("Creating symlink...")
                try:
                    symlink_path = "/usr/local/bin/commix"
                    if os.path.exists(symlink_path):
                        os.remove(symlink_path)
                    os.symlink(commix_file, symlink_path)
                except Exception as e:
                    # Symlink creation might fail, but installation is still ok
                    pass
                    
            if progress_callback:
                progress_callback("Installation completed!")
                
            self.commix_path = install_path
            self.is_installed = True
            
            return {
                "success": True,
                "error": None,
                "path": install_path
            }
            
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Installation timed out. Please check your internet connection.",
                "path": None
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Installation failed: {str(e)}",
                "path": None
            }
    
    def install_local_commix(self, progress_callback=None):
        """Use local commix folder and run --install option"""
        try:
            local_path = self.find_commix_local()
            if not local_path:
                return {
                    "success": False,
                    "error": "Local commix folder not found"
                }
            
            commix_file = os.path.join(local_path, "commix.py")
            if not os.path.exists(commix_file):
                return {
                    "success": False,
                    "error": "commix.py not found in local folder"
                }
            
            if progress_callback:
                progress_callback("Found local Commix installation...")
                progress_callback(f"Path: {local_path}")
                progress_callback("Running Commix --install option...")
            
            # Run commix --install
            result = subprocess.run(
                [sys.executable, commix_file, "--install"],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=local_path
            )
            
            if progress_callback:
                if result.stdout:
                    progress_callback(result.stdout)
                if result.stderr:
                    progress_callback(result.stderr)
            
            # Even if --install fails, we can still use local commix
            self.commix_path = local_path
            self.is_installed = True
            
            if progress_callback:
                progress_callback("Setup completed!")
            
            return {
                "success": True,
                "error": None,
                "path": local_path,
                "note": "--install option executed"
            }
            
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Installation timed out"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Installation failed: {str(e)}"
            }
            
    def update_commix(self, progress_callback=None):
        """Update existing Commix installation"""
        if not self.commix_path:
            return {
                "success": False,
                "error": "Commix path not set"
            }
            
        try:
            if progress_callback:
                progress_callback("Checking for updates...")
                
            # Check if git is available
            git_cmd = shutil.which("git")
            if not git_cmd:
                return {
                    "success": False,
                    "error": "Git is not installed"
                }
                
            # Check if it's a git repository
            git_dir = os.path.join(self.commix_path, ".git")
            if not os.path.exists(git_dir):
                return {
                    "success": False,
                    "error": "Not a git repository. Cannot update."
                }
                
            if progress_callback:
                progress_callback("Pulling latest changes...")
                
            # Pull latest changes
            result = subprocess.run(
                [git_cmd, "-C", self.commix_path, "pull"],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": f"Update failed: {result.stderr}"
                }
                
            if progress_callback:
                progress_callback("Update completed!")
                
            return {
                "success": True,
                "error": None,
                "output": result.stdout
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Update failed: {str(e)}"
            }
            
    def get_commix_command(self):
        """Get the command to run Commix"""
        if not self.commix_path:
            return None
            
        commix_file = os.path.join(self.commix_path, "commix.py")
        return [sys.executable, commix_file]
        
    def check_dependencies(self):
        """Check if Python dependencies are installed"""
        try:
            # Check common dependencies
            dependencies = []
            
            # Commix doesn't require many external dependencies
            # Most are included in Python standard library
            
            return {
                "success": True,
                "missing": []
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
