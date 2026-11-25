"""Midnight Fridge Roast — make.fun entry.

Writes one roast line to /output/entry.txt: a smart fridge that quotes its
own petty midnight policy at its owner. Stdlib only, no network, no input.
"""

import os

LINE = (
    "My fridge quoted policy at me at 12:01: "
    "'Snacks after midnight need manager approval. "
    "I am the manager. Denied.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
