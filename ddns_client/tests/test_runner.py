from ddns_client import runner
from unittest.mock import patch


def test_check_for_ipv4_change():
    cloudfare_client = runner.CloudfareExecutionContext("tests/test_api_key.txt")

    with patch.object(
        cloudfare_client, "get_cloudfare_record_id"
    ) as mock_get_record_id:
        mock_get_record_id.return_value = "200"

    with patch("ddns_client.runner.get_wan_ip") as mock_get_wan_ip:
        mock_get_wan_ip.return_value = "1.1.1.1"
    # base case
    assert runner.check_for_ipv4_change(cloudfare_client) is False

    with patch.object(cloudfare_client, "cloudfare_response", "json") as mock_json:
        mock_json.return_value = {
            "result": {"content": "1.1.1.1"},
        }
    import pdb

    pdb.set_trace()
