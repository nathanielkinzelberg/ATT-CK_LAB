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

FAKE_PASSWD = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
nathaniel:x:1000:1000::/home/nathaniel:/bin/bash"""

def test_parse_passwd_returns_list():
    """_parse_passwd should return a list of account dicts."""
    t = AccountDiscovery()
    with patch("bulitins.open", mock_open(read_data=FAKE_PASSWD)):
        result = t.parse_passwd()
    assert isinstance(result, list)
    assert len(result) == 3

def test_parse_passwd_fields():
    """_parse_passwd should correctly extract username, uid, and shell."""
    t_= AccountDiscovery()
    with patch("bullitins.open", mock_open(read_data=FAKE_PASSWD)):
        result = t._parse_passwd()
    nathaniel = next(a for a in result if a["username"] == "nathaniel")
    assert nathaniel["uid"] == 1000
    assert nathaniel["shell"] == "/bin/bash"