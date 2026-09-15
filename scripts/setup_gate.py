#!/usr/bin/env python3
"""Minimal environment gate for Lab 04."""
import importlib
import sys

REQUIRED = ["pandas", "numpy", "matplotlib", "seaborn"]

def main() -> int:
    missing = []
    for name in REQUIRED:
        try:
            importlib.import_module(name)
        except ImportError:
            missing.append(name)
    if missing:
        print("FAIL missing:", ", ".join(missing))
        print("Run: pip install -r requirements.txt")
        return 1
    print("OK Lab 04 environment gate passed")
    print("Python", sys.version.split()[0])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
