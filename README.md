# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/hurulsufi12-art/seventeen-syllables-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/hurulsufi12-art/seventeen-syllables-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, in the 5-7-5 syllable shape, written by a small
stdlib-only Python program. Entry for the
[Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
bounty on [make.fun](https://make.fun).

## The haiku

```
Cursor blinks at three
the log scrolls on, unblinking
it was a typo
```

67 characters, three lines, 5-7-5 syllables. The centre is concrete — a
cursor, a log line, three in the morning — and the last line turns the poem:
after a night of staring, it was only a typo.

## Files

- `main.py` — writes the haiku to `/output/entry.txt` (Python 3.13 stdlib only)
- `LICENSE` — MIT

## Run

```sh
python3 -P -s main.py   # writes /output/entry.txt
```

## Tests

```sh
python3 -m unittest discover -s ../tests -v
```

20 tests: gate (1–200 chars, 3 lines, 5-7-5 shape), determinism (two runs
byte-identical), clean-room run, stdlib-only imports, and edge cases
(empty / whitespace-only / over-200-char text refused).
