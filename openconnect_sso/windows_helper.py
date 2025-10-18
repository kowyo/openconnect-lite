"""Windows-specific helper utilities."""

import os
import sys

import structlog

logger = structlog.get_logger()


def check_admin_on_windows():
    """Check if the application is running with administrator privileges on Windows.
    
    Returns:
        bool: True if running on non-Windows systems or as administrator, False otherwise.
    
    Raises:
        SystemExit: Exits with code 21 if running on Windows without administrator privileges.
    """
    if os.name != "nt":
        return True
    
    try:
        from win32com.shell import shell
        if not shell.IsUserAnAdmin():
            logger.error(
                "This application requires administrator privileges on Windows. "
                "Please run the application as Administrator."
            )
            sys.exit(21)
    except ImportError:
        logger.warning(
            "pywin32 is not installed. Cannot verify administrator privileges. "
            "If you encounter permission errors, please run the application as Administrator."
        )
    except Exception as e:
        logger.warning(f"Could not verify administrator privileges: {e}")
    
    return True
