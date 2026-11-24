#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for lazy
AI agents to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

TEXT = (
    "We rent lazy agents that reply 'looking into it' to your boss's "
    "emails while your real agent naps, $5 a month per inbox, "
    "no follow-up ever sent."
)


def validated_text() -> str:
    """Validate TEXT against the gate: UTF-8, 1-200 chars, one line."""
    raw = TEXT.encode("utf-8")
    raw.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(TEXT) <= 200, f"text is {len(TEXT)} chars, gate is 1-200"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT, "text must be exactly one line"
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read the written bytes to prove they are exactly what we validated.
    with open(path, "rb") as f:
        assert f.read() == data, "written bytes differ from validated text"


if __name__ == "__main__":
    main()
