#!/usr/bin/env python3
"""Entry program for make.fun "The joke about the demo".

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Copy-only: it reads nothing from the repo directory and
writes nothing into it. Stdlib only, deterministic, no network.
"""

import os

JOKE = (
    "I asked my agent to make the demo robust, so it wrapped the whole app "
    "in a try/except that catches everything \u2014 including the demo itself."
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points; the joke must stay inside.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
