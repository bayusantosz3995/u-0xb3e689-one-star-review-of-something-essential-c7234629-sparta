"""One-line entry for make.fun's "One-Star Review of Something Essential" bounty.

A deadpan one-star review of Mondays, filed in earnest against a thing
that cannot be fixed. The grievance is the sharpest true one: Monday
arrives every single week, on time, with no refund, no unsubscribe
button, and no apology — a delivery that cannot be refused. The turn
lands in the last few words, where the cost is priced in concrete
terms: Monday took the whole weekend and left an alarm clock in its
place, so the reviewer has paid in full and received nothing back.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: Mondays — the weekly delivery that cannot be refused, and it
# charges a whole weekend while leaving an alarm clock behind.
TEXT = (
    "Monday arrives every week, on time, with no refund, "
    "no unsubscribe button, and no apology. "
    "It took my whole weekend and left an alarm clock in its place."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
