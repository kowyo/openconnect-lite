import os
import subprocess
from unittest.mock import MagicMock, patch

from openconnect_sso.app import run_openconnect
from openconnect_sso.config import HostProfile


@patch("subprocess.run")
@patch("shutil.which")
@patch("os.name", "nt")
def test_run_openconnect_windows(mock_which, mock_run):
    mock_which.return_value = None
    auth_info = MagicMock()
    auth_info.session_token = "session_token"
    auth_info.server_cert_hash = "server_cert_hash"
    host = HostProfile("server", "group", "name")
    proxy = None
    version = "4.7.00136"
    args = []

    run_openconnect(auth_info, host, proxy, version, args)

    expected_command = [
        "powershell.exe",
        "-Command",
        "openconnect",
        "--useragent",
        f"AnyConnect Win {version}",
        "--version-string",
        version,
        "--cookie-on-stdin",
        "--servercert",
        auth_info.server_cert_hash,
        *args,
        host.vpn_url,
    ]
    mock_run.assert_called_once_with(expected_command, input=b"session_token")
