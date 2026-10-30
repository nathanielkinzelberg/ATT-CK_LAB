from agent.techniques.t1016_network_config import NetworkConfigDiscovery
from agent.techniques.t1087_account_discovery import AccountDiscovery
from agent.techniques.t1046_network_service_scan import NetworkServiceScan
from agent.techniques.t1082_system_info import SystemInfoDiscovery
from agent.techniques.t1057_process_discovery import ProcessDiscovery

from unittest.mock import patch, mock_open, MagicMock
# mock_open: creates a fake file with whatever content we give it
# patch: temporarily swaps the real open() with our fake one
# MagicMock: creates a fake object that pretends to be what you need — in this case a fake socket

def test_hex_to_ip_default_gateway():
    """_hex_to_ip should convert little-endian hex to a dotted IP adress."""
    t = NetworkConfigDiscovery()
    assert t._hex_to_ip("0101A8C0") == "192.168.1.1"

def test_hex_to_ip_localhost():
    """_hex_to_ip should correctly convert the loopback address."""
    t = NetworkConfigDiscovery()
    assert t._hex_to_ip("0100007F") == "127.0.0.1"

FAKE_PASSWD = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
nathaniel:x:1000:1000::/home/nathaniel:/bin/bash"""

def test_parse_passwd_returns_list():
    """_parse_passwd should return a list of account dicts."""
    t = AccountDiscovery()
    with patch("builtins.open", mock_open(read_data=FAKE_PASSWD)):
        result = t._parse_passwd()
    assert isinstance(result, list)
    assert len(result) == 3

def test_parse_passwd_fields():
    """_parse_passwd should correctly extract username, uid, and shell."""
    t = AccountDiscovery()
    with patch("builtins.open", mock_open(read_data=FAKE_PASSWD)):
        result = t._parse_passwd()
    nathaniel = next(a for a in result if a["username"] == "nathaniel")
    assert nathaniel["uid"] == 1000
    assert nathaniel["shell"] == "/bin/bash"

def test_scan_port_open():
    """_scan_port should return a dict when port is open (connect_ex returns 0)."""
    t = NetworkServiceScan()
    mock_socket = MagicMock()              # create a fake socket — no real network connection
    mock_socket.connect_ex.return_value = 0  # tell the fake socket: return 0 meaning port is open
    with patch("socket.socket", return_value=mock_socket):  # swap real socket with our fake one
        result = t._scan_port("192.168.1.101", 22)          # _scan_port now gets our fake socket
    assert result is not None
    assert result["port"] == 22
    assert result["service"] == "SSH"
    assert result["state"] == "open"

def test_scan_port_closed():
    """_scan_port should return None when port is closed (connect_ex returns non-zero)."""
    t = NetworkServiceScan()
    mock_socket = MagicMock()                 # create a fake socket — no real network connection
    mock_socket.connect_ex.return_value = 111 # tell the fake socket: return 111 meaning port is closed
    with patch("socket.socket", return_value=mock_socket):  # swap real socket with our fake one
        result = t._scan_port("192.168.1.101", 9999)        # _scan_port now gets our fake socket
    assert result is None

FAKE_MEMINFO = "MemTotal:       8000000 kB" \
"MemAvailable:      4000000 kB"

def test_read_proc_meminfo():
    """_read_proc_meminfo should parse total and avalible RAM from /proc/meminfo."""
    t = SystemInfoDiscovery()
    with patch("builtins.open", mock_open(read_data=FAKE_MEMINFO)):
        result = t._read_proc_meminfo()
    assert result["total_kb"] == 8000000
    assert result["available_kb"] == 4000000

def test_get_processes_returns_list():
    """_get_processes should return a list of process dicts with pid, name, and uid."""
    t = ProcessDiscovery()
    fake_comm = mock_open(read_data="bach\n")
    fake_status = mock_open(read_date="Uid:\t1000\t1000\t1000\t1000\n")

    def open_side_effect(path, *args, **kwargs):
        if "comm" in path:
            return fake_comm()
        return fake_status()

    with patch("os.listdir", return_value=["1","2", "self", "net"]):
        with patch("builtins.open", side_effect=open_side_effect):
            result = t._get_processes()

    assert isinstance(result, list)
    assert len(result) == 2         # only "1" and "2" are numeric
    assert result[0]["pid"] == 1
    assert result[0]["name"] == "bash"
    assert result[0]["uid"] == 1000