# Phase 2 — Agent: FastAPI Server and Authentication

**Date started:** 2026-10-07
**Date completed:** 2026-10-07

---

## Goal

Build the program that runs on the Raspberry Pi. It exposes a small web API that listens for requests from the controller, validates the API token, and responds with data.

---

## What I Built

- `agent/__init__.py` — marks the agent folder as a Python package
- `agent/auth.py` — validates the API token on every protected request
- `agent/main.py` — FastAPI server with /health and /techniques endpoints
- `.env` on the Pi — stores the API token securely
- Virtual environment on the Pi with fastapi, uvicorn, python-dotenv installed

---

## Endpoints

| Method | URL | Auth Required | Purpose |
|---|---|---|---|
| GET | /health | No | Check if the agent is running |
| GET | /techniques | Yes | List all supported ATT&CK techniques |

---

## Key Concepts Learned

### FastAPI
A Python library for building APIs. You define URLs and the functions that handle them. FastAPI handles the HTTP layer automatically.

### Endpoint
A specific URL that the API listens on. Each endpoint has a method (GET or POST) and a function that runs when it is called.

### GET vs POST
GET requests ask for information — no data sent, just a request. POST requests send data along with the request. Used for executing techniques because we are telling the Pi to do something.

### API Token Authentication
A long random string stored in a .env file on both the laptop and the Pi. The controller sends it in every request as an HTTP header (X-API-Token). The agent checks it — wrong token returns 401 Unauthorized.

### Depends()
FastAPI's way of attaching a check to an endpoint. `Depends(verify_token)` means "run verify_token before this endpoint — if it fails, stop and return 401."

### async def
FastAPI requires functions to be defined with `async def`. This allows FastAPI to handle multiple requests efficiently without blocking.

### scp
A command for securely copying files from one machine to another over SSH. Used to transfer agent and shared files from the laptop to the Pi.

### uvicorn
The server that actually runs the FastAPI app. FastAPI defines the routes — uvicorn handles the network connections and serves the app.

### 0.0.0.0
When running uvicorn with `--host 0.0.0.0`, it means "listen on all network interfaces." This allows the laptop to reach the agent over WiFi. Using `127.0.0.1` (localhost) would only allow connections from the Pi itself.

---

## Test Results

```bash
# Health check — no token needed
curl http://192.168.1.101:8000/health
# {"status": "ok", "agent": "ATT&CK-Pi Lab"}

# Techniques — no token, rejected
curl http://192.168.1.101:8000/techniques
# {"detail": [{"type": "missing", "loc": ["header", "x-api-token"], ...}]}

# Techniques — wrong token, rejected
curl http://192.168.1.101:8000/techniques -H "X-API-Token: wrong"
# {"detail": "Unauthorized"}

# Techniques — correct token, success
curl http://192.168.1.101:8000/techniques -H "X-API-Token: <real_token>"
# {"techniques": [...all 5 techniques...]}
```

---

## Problems Encountered

*(Fill in any issues you ran into.)*

---

## Files Changed

- `agent/__init__.py`
- `agent/auth.py`
- `agent/main.py`
