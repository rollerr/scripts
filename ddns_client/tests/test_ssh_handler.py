import pytest
from ddns_client.src.ssh_handler import parse_for_ipv4_address


test_1 = "    inet 70.106.247.115/24 brd 70.106.247.255 scope global eth0\n"


@pytest.mark.parametrize(
    "test_input,expected_results",
    [
        (test_1, "70.106.247.115"),
    ],
)
def test_parse_for_ipv4_address(test_input, expected_results):
    results = parse_for_ipv4_address(test_input)
    assert results == expected_results
