# ATT&CK-Pi Lab

**A Raspberry Pi–based Python adversary simulation framework for safely reproducing MITRE ATT&CK discovery techniques in a controlled Linux lab.**

---

## What This Is

ATT&CK-Pi Lab is a two-component adversary simulation platform built on a Raspberry Pi 5.

The controller runs on a laptop and sends authenticated requests to the agent running on the Pi. The agent executes safe, predefined MITRE ATT&CK discovery simulations and returns structured JSON results.

This project demonstrates the kind of engineering work involved in building and validating attack simulations: modular technique execution, structured telemetry, safety controls, and automated testing.

---

## Architecture

```
Laptop / Controller
        │
        │  HTTP + API token
        │
        ▼
Raspberry Pi 5 / Agent  (FastAPI)
        │
        │  executes whitelisted technique module
        │
        ▼
ATT&CK simulation result
        │
        ▼
JSON report  ·  terminal output  ·  logs
```

| Component | Location | Responsibility |
|---|---|---|
| Controller | Laptop | CLI, HTTP client, report saving |
| Agent | Raspberry Pi 5 | FastAPI server, technique whitelist, execution |
| Shared | Both | Result models, logging config |

---

## MITRE ATT&CK Techniques

| Technique ID | Name | Tactic | Status |
|---|---|---|---|
| T1082 | System Information Discovery | Discovery | Planned |
| T1057 | Process Discovery | Discovery | Planned |
| T1087 | Account Discovery | Discovery | Planned |
| T1016 | System Network Configuration Discovery | Discovery | Planned |
| T1046 | Network Service Scanning | Discovery | Planned |

---

## Project Status

> **Phase 0 — Scaffolding** (current)

This project is under active development. See the roadmap below.

---

## Repository Structure

```
attack-pi-lab/
├── controller/          # Laptop-side CLI and HTTP client
├── agent/               # Raspberry Pi FastAPI server
│   └── techniques/      # One module per ATT&CK technique
├── shared/              # Shared models and logging config
├── tests/
│   ├── unit/            # Module-level tests
│   └── integration/     # Controller → Agent end-to-end tests
├── reports/             # Generated execution reports (gitignored)
├── docs/                # Architecture notes and diagrams
├── .env.example         # Environment variable template
└── README.md
```

---

## Setup

### Requirements

- Python 3.11+
- Raspberry Pi 5 running Raspberry Pi OS (Bookworm)
- Both devices on the same local network

### Controller Setup (Laptop)

```bash
cd controller
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Agent Setup (Raspberry Pi)

```bash
cd agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env and set ATTACK_PI_API_TOKEN, AGENT_HOST, AGENT_PORT
```

---

## Usage

```bash
# Check agent health
python controller.py status --target 192.168.1.50

# List available techniques
python controller.py list --target 192.168.1.50

# Execute a technique
python controller.py run --target 192.168.1.50 --technique T1082
```

---

## Safety Model

- The agent does **not** accept arbitrary commands
- Only explicitly registered technique modules can execute
- Network scanning (T1046) is restricted to RFC1918 private addresses only
- API token required for all requests
- No destructive operations — discovery only

---

## Testing

```bash
cd tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

---

## Roadmap

- [x] Phase 0 — Project scaffolding, directory structure, README
- [ ] Phase 1 — Shared models and base technique class
- [ ] Phase 2 — Agent: FastAPI server, health endpoint, auth
- [ ] Phase 3 — First technique: T1082 System Information Discovery
- [ ] Phase 4 — Controller CLI and HTTP client
- [ ] Phase 5 — Remaining techniques: T1057, T1087, T1016, T1046
- [ ] Phase 6 — Automated tests
- [ ] Phase 7 — Reporting and structured output
- [ ] Phase 8 — Deploy agent as a Raspberry Pi service

---

## Why I Built This

This project was built to demonstrate the engineering skills relevant to adversary simulation and Red Team tooling development: Python, Linux internals, networking, MITRE ATT&CK, modular architecture, safety controls, and automated testing.
