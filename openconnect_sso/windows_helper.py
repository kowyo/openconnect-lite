"""Windows-specific helper utilities."""

import ctypes
import os
import sys

import structlog

logger = structlog.get_logger()


def check_admin_on_windows():
    """Check if the application is running with administrator privileges on Windows.
    
    Uses ctypes to call the Windows Shell API's IsUserAnAdmin() function.
    
    Returns:
        bool: True if running on non-Windows systems or as administrator, False otherwise.
    
    Raises:
        SystemExit: Exits with code 21 if running on Windows without administrator privileges.
    """
    if os.name != "nt":
        return True
    
    try:
        # Shell32.IsUserAnAdmin returns 1 if user is admin, 0 otherwise
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        
        if not is_admin:
            logger.error(
                "This application requires administrator privileges on Windows. "
                "Please run the application as Administrator."
            )
            sys.exit(21)
    except Exception as e:
        logger.warning(f"Could not verify administrator privileges: {e}")
    
    return True
