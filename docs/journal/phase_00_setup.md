# Phase 0 — Project Setup and Scaffolding

**Date started:** 2026-10-06
**Date completed:**

---

## Goal

Set up the complete project structure before writing any real code. Create the folder layout, configuration files, documentation skeleton, and Git repository so that every future phase has a clean foundation to build on.

---

## What I Built

- Created the full project directory structure (controller, agent, shared, tests, docs, reports)
- Created `.gitignore` — tells Git which files to never track
- Created `.env.example` — a template showing what secret variables are needed, without any real secrets
- Created `requirements.txt` for controller, agent, and tests
- Created the initial `README.md`
- Created `CLAUDE.md` — instructions for how Claude Code should work in this project
- Created `docs/glossary.md` — running reference of terms learned
- Created `docs/skills.md` — tracker of skills learned per phase
- Created this journal file

---

## Environment Details

| Item | Value |
|---|---|
| Laptop OS | Ubuntu Linux |
| Python version | 3.12.3 |
| Git version | 2.43.0 |
| Raspberry Pi model | Raspberry Pi 5 8GB |
| Pi OS | Debian GNU/Linux 12 (Bookworm) |
| Pi Python version | 3.11.2 |
| Pi IP address | 192.168.1.101 |
| Pi username | nathanielkinzelberg |
| GitHub repo | https://github.com/nathanielkinzelberg/ATT-CK_LAB |

---

## Key Concepts Learned

### Virtual Environment
An isolated Python installation scoped to one project. When you run `python3 -m venv venv`, Python creates a new folder called `venv` containing its own Python interpreter and its own set of installed packages. You activate it with `source venv/bin/activate`. After that, any package you install with `pip install` goes into that folder only — it doesn't affect the rest of your machine.

Why this matters: if two projects need different versions of the same library, virtual environments keep them from conflicting.

### .gitignore
A file at the root of a repository that tells Git which files and folders to completely ignore. They won't appear in `git status`, won't be staged by `git add .`, and will never be committed. Common entries include: `__pycache__/` (Python bytecode files generated automatically), `.env` (secrets), and `venv/` (the virtual environment — each person creates their own).

### .env and .env.example
`.env` is a file containing real secret values — like an API token — that only exists on your machine. It is never committed to Git. `.env.example` is a template showing the shape of the file (which variables exist) but with placeholder values instead of real ones. You commit `.env.example` so anyone cloning the repo knows exactly what they need to fill in.

Why this matters: if you accidentally commit a real API token or password to a public GitHub repo, it can be found by automated scanners within seconds and used to access your accounts.

### Python Package
A folder of Python files that can be imported by other Python files. The key requirement is that the folder must contain a file called `__init__.py` (even if it's empty). That file is what tells Python "this folder is a package, not just a folder."

### requirements.txt
A plain text file listing the Python packages a project depends on. Running `pip install -r requirements.txt` installs everything listed. We have three — one for the controller, one for the agent, and one for the tests — because each component runs on different hardware and needs different libraries.

---

## SSH Setup Process

### Enabling SSH on the Pi
Opened a terminal on the Pi and ran:
```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

### Finding the Pi's IP address
```bash
hostname -I
# returned: 192.168.1.101
```

### Connecting from the laptop
```bash
ssh nathanielkinzelberg@192.168.1.101
```

---

## Problems Encountered

### Keyboard layout was Hebrew on first boot
**Symptom:** Lowercase letters produced no output. Uppercase worked with Caps Lock.
**Fix:** Went into Pi settings and changed the country to US. Keyboard layout corrected immediately.

### Bluetooth mouse would not pair
**Symptom:** `bluetoothctl scan on` found nearby devices but not the mouse.
**Fix:** Never resolved. Proceeded with keyboard only. Mouse is not needed once SSH is set up.

### SSH connection hung with no response
**Symptom:** Running `ssh nathanielkinzelberg@192.168.1.101` produced no output and hung indefinitely.
**Cause:** SSH service needed a restart after being enabled.
**Fix:** Ran `sudo systemctl restart ssh` on the Pi, then SSH connected immediately from the laptop.

### SSH asked to confirm key fingerprint on first connect
**Symptom:** Message saying the host is not known and asking to confirm.
**This is normal.** Type `yes`. The fingerprint is saved and the prompt never appears again for this host.

---

## Git Commit

```
git add .
git commit -m "Phase 0: Initialize ATT&CK-Pi Lab project structure"
git push
```

Files committed:
- `.gitignore`
- `.env.example`
- `README.md`
- `CLAUDE.md`
- `controller/requirements.txt`
- `agent/requirements.txt`
- `tests/requirements.txt`
- `docs/glossary.md`
- `docs/skills.md`
- `docs/journal/phase_00_setup.md`
- All `.gitkeep` files
