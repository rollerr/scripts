import paramiko
import unittest

from ddns_client import runner, ssh_handler
from unittest.mock import patch, MagicMock


@patch.object(runner, "get_wan_ip")
@patch.object(paramiko.SSHClient, "exec_command")
@patch.object(ssh_handler, "setup_paramiko")
@patch.object(ssh_handler, "get_private_key")
def test_check_for_ipv4_change(
    mock_get_private_key, mock_setup_paramiko, mock_exec_command, mock_get_wan_ip
):
    mock_get_private_key.return_value = "mock_private_key_path"
    mock_setup_paramiko.return_value = paramiko.SSHClient()
    mock_exec_command.return_value = MagicMock()
    mock_get_wan_ip.return_value = "1.1.1.1"
    cloudfare_client = runner.CloudfareExecutionContext("tests/test_api_key.txt")

    with patch.object(
        cloudfare_client, "get_cloudfare_record_id"
    ) as mock_get_record_id:
        mock_get_record_id.return_value = 200

    with patch("ddns_client.runner.get_wan_ip") as mock_get_wan_ip:
        mock_get_wan_ip.return_value = "1.1.1.1"
        assert runner.check_for_ipv4_change(cloudfare_client) is False
    with patch.object(
        cloudfare_client, "get_cloudfare_record_id"
    ) as mock_get_record_id:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": {"content": "1.1.1.1"}}
        mock_get_record_id.return_value = mock_response
        assert runner.check_for_ipv4_change(cloudfare_client) is False


class TestCheckIPV4(unittest.TestCase):
    @patch.object(paramiko.SSHClient, "exec_command")
    @patch.object(ssh_handler, "setup_paramiko")
    @patch.object(ssh_handler, "get_private_key")
    def setUp(
        self,
        mock_get_private_key,
        mock_setup_paramiko,
        mock_exec_command,
    ):
        mock_get_private_key.return_value = "mock_private_key_path"
        mock_setup_paramiko.return_value = paramiko.SSHClient()
        mock_exec_command.return_value = MagicMock()
        self.cloudfare_client = runner.CloudfareExecutionContext(
            "tests/test_api_key.txt"
        )

    @patch.object(runner, "get_wan_ip")
    def test_1(self, mock_get_wan_ip):
        mock_get_wan_ip.return_value = "2.2.2.2"
        my_class = self.cloudfare_client
        with patch.object(
            my_class, "get_cloudfare_record_id"
        ) as mock_get_cloudfare_record_id:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"result": {"content": "1.1.1.1"}}
            mock_get_cloudfare_record_id.return_value = mock_response
            assert runner.check_for_ipv4_change(self.cloudfare_client) is True
