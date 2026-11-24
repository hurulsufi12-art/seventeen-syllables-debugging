"""Seventeen Syllables of Debugging — entry program.

Writes one haiku about debugging (5-7-5 syllables, 66 characters) to
/output/entry.txt. Stdlib only, deterministic, no network, no model calls.
"""
import os

TEXT = (
    "Cursor blinks at three\n"
    "the log scrolls on, unblinking\n"
    "it was a typo"
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 characters,
    # three lines in the 5-7-5 shape, not whitespace-only. Fail loudly
    # instead of writing an invalid entry. Also refuse control characters
    # other than the two line breaks: a stray \x00-\x1f would fail the
    # scorer's UTF-8 text check.
    lines = TEXT.split("\n")
    if not 1 <= len(TEXT) <= 200 or len(lines) != 3 or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char / 3-line gate")
    if any(ord(c) < 0x20 and c != "\n" for c in TEXT):
        raise SystemExit("entry text contains a control character")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
