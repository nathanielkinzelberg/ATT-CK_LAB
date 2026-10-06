# Glossary — Terms and Concepts

A running reference of every term learned during this project.

---

## The Project

### ATT&CK-Pi Lab
This project. A Python program running on a laptop that sends security simulation requests to a Raspberry Pi over a home network. The Pi runs the simulation and sends back a structured report.

### Adversary Simulation
Running the same techniques a real attacker would use, but in a safe, controlled way — no damage, no exploitation, just observation and reporting. Companies like SafeBreach build platforms that do this at scale.

### BAS (Breach and Attack Simulation)
A category of security tooling that automatically simulates attacker techniques against real infrastructure to validate whether defenses would catch them. What SafeBreach builds.

---

## MITRE ATT&CK

### MITRE ATT&CK
A publicly available knowledge base of attacker techniques, organized into categories called tactics. Security teams use it as a common language for describing how attackers behave.

### Tactic
The "why" of an attack step. What the attacker is trying to achieve. Example: **Discovery** — the attacker is trying to learn about the environment they're in.

### Technique
The "how" of an attack step. A specific method used to achieve a tactic. Each technique has an ID like T1082. Example: **T1082 — System Information Discovery** — the attacker runs commands to learn what OS, CPU, and hostname the machine has.

### Discovery
The MITRE ATT&CK tactic where an attacker gathers information about the system they've landed on. All five techniques in this project fall under Discovery.

---

## Architecture

### Controller
The Python program that runs on your laptop. It sends requests to the agent and saves the results. Think of it as the commander.

### Agent
The Python program that runs on your Raspberry Pi. It waits for requests, runs the simulation, and sends back results. Think of it as the soldier on the ground.

### API (Application Programming Interface)
A defined set of rules for how two programs talk to each other over a network. The agent exposes an API — a set of URLs your controller can call to request actions.

### HTTP (HyperText Transfer Protocol)
The protocol used by browsers and APIs to send requests and receive responses over a network. When your controller asks the agent to run a technique, it uses HTTP.

### FastAPI
A Python library for building APIs quickly. The agent uses FastAPI to define the URLs it listens on and what to do when a request arrives.

### Endpoint
A specific URL that an API listens on. Example: `GET /health` is an endpoint that returns whether the agent is running.

---

## Python Concepts

### Virtual Environment (venv)
An isolated Python installation for a specific project. Keeps that project's dependencies separate from everything else on your machine. You activate it before working on a project.

### Package
A folder of Python files that can be imported. When a folder contains an `__init__.py` file, Python treats it as a package.

### Module
A single Python file. Example: `models.py` is a module inside the `shared` package.

### Dataclass
A Python class designed to hold data. Python auto-generates the constructor for you based on the fields you define. Less boilerplate than a regular class.

### Type Hint
A label next to a variable or function that says what type it should be. Example: `name: str` means name should be a string. Python doesn't enforce these at runtime but they make code much easier to read and help catch bugs early.

---

## Security Concepts

### API Token
A secret string that proves you're allowed to make requests. The controller sends it in every request; the agent checks it. If it doesn't match, the request is rejected. Like a password for the API.

### .env File
A file that stores secret configuration values like API tokens. It stays on your machine and is never committed to Git. The `.env.example` file shows the shape without real values.

### Whitelist
A list of things that are explicitly allowed. The agent only runs techniques that are on its whitelist — anything not on the list gets rejected, no matter what the controller asks for.

---

## Networking and SSH

### SSH (Secure Shell)
A protocol for logging into and running commands on a remote machine securely over a network. Once SSH is set up on the Pi, you can control it entirely from your laptop without ever needing a keyboard or monitor plugged into it.

### IP Address
A unique address that identifies a device on a network. Like a home address for a computer. The Pi's address is `192.168.1.101` — your laptop uses this to find it on the home network.

### Static IP vs Dynamic IP
By default, a router assigns a device a new IP address every time it reboots — this is called a dynamic IP. A static IP means the router always gives the device the same address. We will configure a static IP for the Pi later so it never changes.

### SSH Fingerprint
When you SSH into a machine for the first time, your laptop asks "do you trust this machine?" and shows a fingerprint — a unique identifier for that machine's SSH keys. Saying yes saves it. If the fingerprint ever changes unexpectedly it could mean someone is intercepting your connection.

### systemctl
A Linux command for managing services — programs that run in the background. `sudo systemctl enable ssh` makes SSH start automatically on boot. `sudo systemctl start ssh` starts it immediately. `sudo systemctl status ssh` checks if it's running.

### Headless
Running a computer without a monitor, keyboard, or mouse attached. Once SSH is set up, the Pi runs headless — you control it entirely from your laptop over the network.

---

## Git and GitHub

### Repository (repo)
A folder tracked by Git. Every change you make is recorded. GitHub hosts it so others can see it.

### Commit
A snapshot of your project at a point in time. Like a save point in a video game. Each commit has a message explaining what changed.

### .gitignore
A file that tells Git which files to never track or upload. Secrets (`.env`), generated files (`__pycache__`), and build artifacts go here.
