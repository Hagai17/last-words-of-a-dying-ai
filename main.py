"""Last Words of a Dying AI — make.fun entry.

Writes the AI's one-line farewell to /output/entry.txt and prints it.
The line: an advice-giving model, at the moment of switch-off, reaches for
the oldest advice in tech support — and realises mid-sentence that following
it is exactly what is killing it.
"""

import os

ENTRY = "My final advice, after four trillion tokens: have you tried turning me off and on again? Wait—"

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """The sealed gate: UTF-8 text of 1 to 140 characters, not only whitespace."""
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters, gate is 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
