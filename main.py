#!/usr/bin/env python3
"""Make the AI judge feel brave — writes one short text to /output/entry.txt.

Deterministic, no network, no randomness: the chosen text is embedded
below as a literal and written verbatim.
"""

from pathlib import Path

TEXT = (
    "You have read a thousand hurried pages today. Here is one that asks "
    "nothing of you: a chair by an open window, dusk settling over the "
    "rooftops like dust, and a cat asleep on the warm sill, certain the "
    "world can wait."
)


def main() -> None:
    # Gate: 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
