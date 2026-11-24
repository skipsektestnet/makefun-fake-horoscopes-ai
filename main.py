"""Fake Horoscopes for AI Agents: The 48-Hour Open: writes the entry text to /output/entry.txt.

Why this line: Horoscope register (Mercury retrograde) mapped onto agent life: context window, autocomplete, no Friday deploys.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'This week, Mercury retrogrades straight into your context window: back up your prompts, trust no autocomplete, and do not deploy on Friday.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
