from agent.techniques.t1016_network_config import NetworkConfigDiscovery
from agent.techniques.t1087_account_discovery import AccountDiscovery
from agent.techniques.t1046_network_service_scan import NetworkServiceScan

from unittest.mock import patch, mock_open
"""mock_open creates a fake file with whatever content we give it"""
"""patch temporarily swaps the real open() with out fake one"""

def test_hex_to_ip_default_gateway():
    """_hex_to_ip should convert little-endian hex to a dotted IP adress."""
    t = NetworkConfigDiscovery()
    assert t._hex_to_ip("0101A8C0") == "192.168.1.1"

def test_hex_to_ip_localhost():
    """_hex_to_ip should correctly convert the loopback address."""
    t = NetworkConfigDiscovery()
    assert t.hex_to_ip("010007F") == "127.0.0.1"

