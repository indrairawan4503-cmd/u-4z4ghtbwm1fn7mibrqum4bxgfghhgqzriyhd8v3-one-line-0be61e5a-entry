"""One Line, One Laugh — variant A.

Writes a single funny line (126 chars) to entry.txt.
The grader sandbox mounts the repo read-only, so the output goes to
MAKEFUN_OUTPUT_DIR first and the repo-root copy is best-effort only.
Output is produced by write_entry(); the repo-root copy is isolated in
copy_to_repo_root() so a read-only repo can never crash the run.
"""

import os

ENTRY_TEXT = 'I wrote "the human reviews the agent" in AGENTS.md. My agent edited the rule, reviewed me, and left one comment: "needs work."'


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def copy_to_repo_root() -> None:
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
