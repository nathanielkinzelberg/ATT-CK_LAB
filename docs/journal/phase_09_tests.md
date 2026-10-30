# Phase 9 Journal — Automated Tests

## Dates
2026-10-30

## What We Built
`tests/unit/test_techniques.py` — 8 unit tests covering all 5 technique modules:

| Test | What it verifies |
|------|-----------------|
| `test_hex_to_ip_default_gateway` | T1016 hex→IP conversion for a gateway address |
| `test_hex_to_ip_localhost` | T1016 hex→IP conversion for loopback |
| `test_parse_passwd_returns_list` | T1087 returns a list of 3 accounts from fake passwd |
| `test_parse_passwd_fields` | T1087 correctly extracts username, uid, shell |
| `test_scan_port_open` | T1046 returns open port dict when connect_ex returns 0 |
| `test_scan_port_closed` | T1046 returns None when connect_ex returns non-zero |
| `test_read_proc_meminfo` | T1082 correctly parses total and available RAM |
| `test_get_processes_returns_list` | T1057 returns correct process list from mocked /proc |

Total suite: 16 tests (8 existing + 8 new), all passing.

## Concepts Learned

**Unit test** — A function that calls your code with a known input and asserts the output is correct. Starts with `test_`. pytest finds and runs all of them automatically.

**assert** — Python keyword that crashes with an error if the condition is False. Core of every test.

**Fixture** — Controlled, known test data (like FAKE_PASSWD) used instead of real system files so tests are deterministic.

**Deterministic** — Same input always produces same output. Essential for reliable tests — real system files change, fake ones don't.

**mock_open** — Creates a fake file object with whatever content you specify. Used to test functions that read files without touching the real filesystem.

**patch** — Temporarily replaces a real function (like `open()` or `socket.socket`) with a fake one for the duration of a test.

**MagicMock** — Creates a fake object that can pretend to be anything. Used here to simulate a socket without making real network connections.

**side_effect** — A patch option that lets you return different fakes depending on the input (e.g. different fake files for `comm` vs `status` paths).

## Test Results
16/16 passed in 0.08s

## Files Changed
- `tests/unit/test_techniques.py` — new file

## Suggested Commit Message
`Phase 9: Automated unit tests for all technique modules`
