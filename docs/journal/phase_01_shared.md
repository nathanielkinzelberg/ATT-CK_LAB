# Phase 1 — Shared Models and Base Class

**Date started:** 2026-10-06
**Date completed:** 2026-10-06

---

## Goal

Build the shared foundation that every other part of the project depends on. Define the standard result format and the template every ATT&CK technique must follow.

---

## What I Built

- `shared/__init__.py` — marks the shared folder as a Python package
- `shared/models.py` — the TechniqueResult dataclass, the standard result format
- `shared/base.py` — the AttackTechnique abstract base class, the template every technique must follow
- `shared/logging_config.py` — a shared logging setup used by both the agent and controller
- `tests/unit/test_models.py` — unit tests for the result model
- `tests/unit/test_base.py` — unit tests for the base class
- `tests/conftest.py` — tells pytest where to find the shared package

---

## Key Concepts Learned

### Python Package
A folder that contains an `__init__.py` file. That file is what tells Python the folder is importable code and not just a regular folder.

### Dataclass
A Python class designed to hold data. The `@dataclass` decorator automatically generates the constructor so you don't have to write one. Fields are defined with type hints.

### Type Hints
Labels that say what type a variable should be. `name: str` means name is a string. `success: bool` means success is True or False. Python doesn't enforce these at runtime but they make code easier to read and catch bugs early.

### field(default_factory=...)
Used on dataclass fields that need a fresh default value each time. `field(default_factory=dict)` gives each instance its own empty dictionary. Using `= {}` directly would cause all instances to share the same dictionary — a classic Python bug.

### UTC Timestamps
Always use UTC for timestamps in systems where multiple machines are involved. Each machine may be in a different timezone. UTC is the universal clock everyone agrees on.

### Abstract Base Class (ABC)
A class that cannot be used directly — it is only a template for other classes to inherit from. Marked with `ABC`. Methods marked `@abstractmethod` must be implemented by any class that inherits from it. If they are not, Python raises a TypeError immediately.

### @abstractmethod
A decorator that marks a method as required. Any class that inherits from the base class must implement this method or Python will refuse to create an instance of it.

### Separation of Concerns
Each file has one job. `models.py` defines the result shape. `base.py` defines the technique template. `logging_config.py` defines logging. Mixing these into one file would make the code harder to read and maintain.

### Logging vs print()
Python's built-in `logging` module is preferred over `print()` because it automatically adds timestamps and severity levels (INFO, ERROR, DEBUG) to every message, and can be configured in one place for the entire project.

### pytest
A Python testing framework. Tests are functions that start with `test_`. Running `pytest` automatically discovers and runs all of them. `assert` checks that a condition is true — if it isn't, the test fails.

### conftest.py
A special pytest file that runs before any tests. Used here to add the project root to Python's path so tests can import from the shared package.

---

## Test Results

```
8 passed in 0.01s
```

---

## Problems Encountered

*(Fill in any issues you ran into.)*

---

## Files Changed

- `shared/__init__.py`
- `shared/models.py`
- `shared/base.py`
- `shared/logging_config.py`
- `tests/conftest.py`
- `tests/unit/test_models.py`
- `tests/unit/test_base.py`
