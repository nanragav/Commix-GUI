#!/usr/bin/env python
# encoding: UTF-8

"""
Option Validator - Validates mutually exclusive and dependent Commix options
Based on Commix source code analysis from: https://github.com/commixproject/commix
"""

class OptionValidator:
    """Validates Commix options for mutual exclusivity and dependencies"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_all(self, options_dict):
        """
        Validate all option combinations
        
        Args:
            options_dict: Dictionary of all GUI options with their values
            
        Returns:
            tuple: (is_valid, errors_list, warnings_list)
        """
        self.errors = []
        self.warnings = []
        
        # Validate each rule
        self.validate_user_agent_options(options_dict)
        self.validate_technique_options(options_dict)
        self.validate_parameter_options(options_dict)
        self.validate_proxy_options(options_dict)
        self.validate_auth_options(options_dict)
        self.validate_target_options(options_dict)
        self.validate_file_access_options(options_dict)
        self.validate_tor_options(options_dict)
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def validate_user_agent_options(self, opts):
        """
        User-Agent options are mutually exclusive:
        --mobile, --user-agent, --random-agent
        """
        mobile = opts.get('mobile', False)
        custom_agent = opts.get('user_agent', '').strip()
        random_agent = opts.get('random_agent', False)
        
        # Count how many are enabled
        enabled_count = sum([
            mobile,
            bool(custom_agent),
            random_agent
        ])
        
        if enabled_count > 1:
            conflicting = []
            if mobile:
                conflicting.append("'--mobile'")
            if custom_agent:
                conflicting.append("'--user-agent'")
            if random_agent:
                conflicting.append("'--random-agent'")
            
            self.errors.append(
                f"User-Agent options are mutually exclusive. "
                f"Only one of {', '.join(conflicting)} can be used at a time."
            )
    
    def validate_technique_options(self, opts):
        """
        --technique and --skip-technique cannot be used simultaneously
        """
        technique = opts.get('technique', '').strip()
        skip_technique = opts.get('skip_technique', '').strip()
        
        if technique and skip_technique:
            self.errors.append(
                "The options '--technique' and '--skip-technique' cannot be used "
                "simultaneously (i.e. only one option must be set)."
            )
    
    def validate_parameter_options(self, opts):
        """
        -p (test_parameter) and --skip (skip_parameter) cannot be used simultaneously
        """
        test_param = opts.get('test_parameter', '').strip()
        skip_param = opts.get('skip_parameter', '').strip()
        
        if test_param and skip_param:
            self.errors.append(
                "The options '-p' (test parameter) and '--skip' (skip parameter) cannot be used "
                "simultaneously (i.e. only one option must be set)."
            )
    
    def validate_proxy_options(self, opts):
        """
        Proxy-related mutually exclusive options:
        - --proxy vs --tor
        - --proxy vs --ignore-proxy
        """
        proxy = opts.get('proxy', '').strip()
        tor = opts.get('tor', False)
        ignore_proxy = opts.get('ignore_proxy', False)
        
        if proxy and tor:
            self.errors.append(
                "The switch '--tor' is incompatible with option '--proxy'."
            )
        
        if proxy and ignore_proxy:
            self.errors.append(
                "The option '--proxy' is incompatible with switch '--ignore-proxy'."
            )
    
    def validate_tor_options(self, opts):
        """
        --tor-check requires --tor to be enabled
        """
        tor_check = opts.get('tor_check', False)
        tor = opts.get('tor', False)
        
        if tor_check and not tor:
            self.errors.append(
                "The switch '--tor-check' requires usage of '--tor' switch."
            )
    
    def validate_auth_options(self, opts):
        """
        Authentication options must be used together:
        --auth-cred requires --auth-type and vice versa
        """
        auth_cred = opts.get('auth_cred', '').strip()
        auth_type = opts.get('auth_type', '').strip()
        
        if auth_cred and not auth_type:
            self.errors.append(
                "You must specify both '--auth-cred' and '--auth-type' options. "
                "'--auth-cred' requires '--auth-type' to be set."
            )
        
        if auth_type and not auth_cred:
            self.errors.append(
                "You must specify both '--auth-cred' and '--auth-type' options. "
                "'--auth-type' requires '--auth-cred' to be set."
            )
    
    def validate_target_options(self, opts):
        """
        Target options mutual exclusivity:
        - -r (requestfile) vs -u (url)
        - -r (requestfile) vs -l (logfile)
        """
        requestfile = opts.get('requestfile', '').strip()
        url = opts.get('url', '').strip()
        logfile = opts.get('logfile', '').strip()
        
        if requestfile and url:
            self.errors.append(
                "The '-r' option (request file) is incompatible with option '-u' ('--url')."
            )
        
        if requestfile and logfile:
            self.errors.append(
                "The '-r' option (request file) is unlikely to work combined with the '-l' option (log file)."
            )
    
    def validate_file_access_options(self, opts):
        """
        File access options dependencies:
        --file-write or --file-upload require --file-dest
        """
        file_write = opts.get('file_write', '').strip()
        file_upload = opts.get('file_upload', '').strip()
        file_dest = opts.get('file_dest', '').strip()
        
        if (file_write or file_upload) and not file_dest:
            self.errors.append(
                "Host's absolute filepath to write and/or upload must be specified (i.e. '--file-dest'). "
                "The '--file-write' or '--file-upload' option requires '--file-dest' to be set."
            )
        
        if file_dest and not (file_write or file_upload):
            self.errors.append(
                "You must enter the '--file-write' or '--file-upload' parameter when using '--file-dest'."
            )
    
    def get_validation_message(self):
        """
        Get a formatted validation message
        
        Returns:
            str: Formatted error and warning messages
        """
        messages = []
        
        if self.errors:
            messages.append("❌ Validation Errors:\n")
            for i, error in enumerate(self.errors, 1):
                messages.append(f"  {i}. {error}\n")
        
        if self.warnings:
            messages.append("\n⚠️  Warnings:\n")
            for i, warning in enumerate(self.warnings, 1):
                messages.append(f"  {i}. {warning}\n")
        
        return "".join(messages) if messages else "✅ All options are valid"


# Singleton instance
_validator_instance = None

def get_validator():
    """Get the singleton validator instance"""
    global _validator_instance
    if _validator_instance is None:
        _validator_instance = OptionValidator()
    return _validator_instance
