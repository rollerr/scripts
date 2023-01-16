from ddns_client import cloudflare_runner
from unittest.mock import patch


# def test_check_for_ipv4_change():
#     cloudfare_client = cloudflare_runner.CloudfareExecutionContext(
#         "tests/test_api_key.txt"
#     )
#     with patch("ddns_client.cloudflare_runner.get_wan_ip") as mock_get_wan_ip:
#         mock_get_wan_ip.return_value = "1.1.1.1"
#     with patch(
#         "ddns_client.cloudfare_runner.get_cloudflare_record_id"
#     ) as mock_get_record_id:
#         mock_get_record_id.return_value = "200"
#
#     assert cloudflare_runner.check_for_ipv4_change(cloudfare_client) is False
#
