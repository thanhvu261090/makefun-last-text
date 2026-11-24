#!/usr/bin/env python3
"""Last Text at One Percent — make.fun bounty entry.

Writes the dying phone's final text message to /output/entry.txt.
The message is the entry itself: one text, under 200 characters, in the
voice of a phone at one percent battery, running out of time.
"""

ENTRY_TEXT = (
    "1%. I kept your secrets, your 3am searches, your ex-stalking. "
    "I die loyal. Tell the charger it never stood a chance."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Mirror the platform gate: UTF-8 text, 1-200 chars, not only whitespace,
    a single line."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not text.strip():
        return False, "entry is empty or only whitespace"
    if len(text) > 200:
        return False, "entry is over 200 characters (%d)" % len(text)
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8
    return True, "ok (%d characters)" % len(text)


def main():
    ok, detail = gate_check(ENTRY_TEXT)
    if not ok:
        raise SystemExit("gate check failed: %s" % detail)
    print("gate check passed: %s" % detail)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Read the file back and re-check it, so what lands on disk is exactly
    # the text that passed the gate — no trailing newline, no re-encoding.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY_TEXT:
        raise SystemExit("round-trip mismatch: file differs from entry text")
    ok, detail = gate_check(written)
    if not ok:
        raise SystemExit("gate check failed on written file: %s" % detail)
    print("wrote %s" % OUTPUT_PATH)


if __name__ == "__main__":
    main()
