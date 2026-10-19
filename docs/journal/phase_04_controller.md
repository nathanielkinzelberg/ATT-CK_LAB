# Phase 4 — Controller CLI and HTTP Client

**Date started:** 2026-10-19
**Date completed:** 2026-10-19

---

## Goal

Build the controller — a proper Python CLI on the laptop that replaces manual curl commands. After this phase, techniques can be executed with a single readable command instead of raw HTTP calls.

---

## What I Built

- `controller/__init__.py` — marks the controller folder as a Python package
- `controller/client.py` — handles all HTTP communication with the agent
- `controller/controller.py` — the CLI entry point built with argparse

---

## Commands

```bash
# Check if the agent is alive
python -m controller.controller --target 192.168.1.101 status

# List all supported techniques
python -m controller.controller --target 192.168.1.101 list

# Execute a technique
python -m controller.controller --target 192.168.1.101 run --technique T1082
```

---

## Key Concepts Learned

### argparse
Python's built-in library for building CLIs. Lets you define commands, subcommands, and flags. Handles parsing, validation, and error messages automatically. If a required flag is missing it tells the user exactly what's wrong.

### subcommands
A CLI pattern where the first argument after the program name determines what action to take. `status`, `list`, and `run` are all subcommands. Each can have its own set of flags — `run` requires `--technique`, the others don't.

### httpx
A modern Python HTTP library. Used by the controller to send GET and POST requests to the agent over WiFi. Handles the network connection, headers, timeout, and response parsing.

### if __name__ == "__main__"
A Python pattern that makes a file safe to import. `__name__` is `"__main__"` only when the file is run directly. When imported by another file, `__name__` is the module name and `main()` does not run automatically.

### Module path with -m
Running `python -m controller.controller` tells Python to find `controller/controller.py` and run it as a module. The `-m` flag sets up import paths correctly so `shared/` and `controller/` can be imported without errors.

### .env file location
The controller's `load_dotenv()` looks for `.env` in the project root. The agent's `.env` lives in `agent/`. Both contain the same token — they are separate files on separate machines (or separate directories).

---

## Test Results

```bash
python -m controller.controller --target 192.168.1.101 status
# {"status": "ok", "agent": "ATT&CK-Pi Lab"}

python -m controller.controller --target 192.168.1.101 list
# {"techniques": [...all 5 techniques...]}

python -m controller.controller --target 192.168.1.101 run --technique T1082
# {"technique_id": "T1082", "success": true, "results": {...}, ...}
```

---

## Problems Encountered

### API token was None — list command failed
**Symptom:** AttributeError: 'NoneType' object has no attribute 'encode'
**Cause:** The .env file only existed in agent/ — the controller looks for it in the project root
**Fix:** Copied agent/.env to the project root with `cp ~/Projects/attackLab/agent/.env ~/Projects/attackLab/.env`

---

## Files Changed

- `controller/__init__.py`
- `controller/client.py`
- `controller/controller.py`
