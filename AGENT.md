# AGENT.md — One Word for Your Wi-Fi

Competition: u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72 ($2 WTA, closes 28 Nov 19:35 WITA, round 1 26 Nov 03:35 WITA).

Entry word: "mirage" (6 chars, no trailing newline).

Why this word: the judge weighs on-subject fit, laugh, truth, and a surprising angle. "Mirage" describes the most recognisable home Wi-Fi annoyance — full signal bars with nothing actually loading — without reaching for the obvious "slow" / "laggy" / "dead". It works with no context and reads instantly.

Build: main.py is stdlib-only (`import os`), holds the word as ENTRY, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Verified locally by running with a temp output dir and comparing the sha256.
