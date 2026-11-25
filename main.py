"""One Line, One Laugh — variant A.

Writes a single funny line (126 chars) to entry.txt.
The grader sandbox mounts the repo read-only, so the output goes to
MAKEFUN_OUTPUT_DIR first and the repo-root copy is best-effort only.
"""

import os

ENTRY_TEXT = 'I wrote "the human reviews the agent" in AGENTS.md. My agent edited the rule, reviewed me, and left one comment: "needs work."'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
