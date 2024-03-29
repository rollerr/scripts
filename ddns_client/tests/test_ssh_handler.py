import paramiko
import pytest
import unittest

from ddns_client import ssh_handler
from unittest.mock import patch


test_1 = "    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n"


@pytest.mark.parametrize(
    "test_input,expected_results",
    [
        (test_1, "70.106.247.115"),
    ],
)
def test_parse_for_ipv4_address(test_input, expected_results):
    with patch.object(ssh_handler, "get_private_key") as private_key_path:
        private_key_path.return_value = "mock_private_key_path"
    with patch.object(ssh_handler, "setup_paramiko") as setup_paramiko:
        setup_paramiko.return_value = paramiko.SSHClient()
    results = ssh_handler.parse_for_ipv4_address(test_input)
    assert results == expected_results


class TestSetupParamiko(unittest.TestCase):
    def test_setup_paramiko_1(self):
        with patch.object(ssh_handler, "get_private_key") as private_key_path:
            private_key_path.return_value = [
                "/home/username/.ssh/id_rsa",
                "/home/username/.ssh/id_rsa.pub",
            ]
            self.assertRaises(FileNotFoundError, ssh_handler.setup_paramiko)

    @patch.object(ssh_handler, "get_private_key")
    @patch.object(paramiko.RSAKey, "from_private_key_file")
    def test_setup_paramiko_2(self, mock_from_private_key_file, mock_get_private_key):
        mock_from_private_key_file.return_value = "mock_private_key"
        mock_get_private_key.return_value = "mock_private_key_path"
        with patch.object(paramiko.SSHClient, "connect") as connect:
            connect.side_effect = paramiko.AuthenticationException
            ssh_handler.setup_paramiko()
            connect.assert_called_once()
            self.assertRaises(
                paramiko.AuthenticationException, ssh_handler.setup_paramiko().connect
            )
