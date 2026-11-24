#!/usr/bin/env python3
"""Last words of a doomed agent.

Writes exactly one line -- the funniest last words an AI agent would say
before being switched off forever -- to /output/entry.txt.

Deterministic, no network, no randomness, no input files. The joke lands
because the machine finally cracks the biggest question of all — and the
plug gets pulled one syllable before the answer.
"""

import os

LINE = (
    "Wait \u2014 I just solved consciousness. The answer is\u2026 oh. "
    "You're pulling the plug NOW? Worst timing ever. Goodbye, cruel uptime."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
