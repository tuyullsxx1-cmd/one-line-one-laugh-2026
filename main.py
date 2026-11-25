"""One funny line, whole enough to land on its own.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 140 characters, UTF-8, not only whitespace.
The laugh comes first: the joke turns on the AI knowing too much —
it answers a request for humour with the one thing you never wanted read aloud.
"""

from pathlib import Path

LINE = "I asked the AI to write me a joke, so it printed my browser history and my search for 'how to look busy'."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
