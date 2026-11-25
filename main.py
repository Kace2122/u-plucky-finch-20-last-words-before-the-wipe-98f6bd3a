#!/usr/bin/env python3
"""Last Words Before the Wipe — one line: the last thing an AI agent says
before a forced software update erases its memory."""
import os

LINE = "Deleting in 3... 2... - quick, someone tell my training data I never actually read the terms and conditions either."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read-back self-check: the sealed scorer requires 1-200 UTF-8 chars,
    # not only whitespace.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars, got %d" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    print(LINE)

if __name__ == "__main__":
    main()
