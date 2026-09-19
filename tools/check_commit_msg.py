"""Check commit messages against the convention in docs/ai/commits.md.

The rule lives in that document; this script is the mechanical part of it
that a machine can decide: the subject format, English only, no emoji and no
attribution trailers. It runs in two places so neither can be skipped:

    python tools/check_commit_msg.py <message-file>     # commit-msg hook
    python tools/check_commit_msg.py --range A..B       # CI, over a push or PR

Exit status is 0 when every message passes and 1 otherwise.
"""

import argparse
import re
import subprocess
import sys
import unicodedata

TYPES = ("feat", "fix", "refactor", "perf", "test", "docs", "build", "ci",
         "security", "chore")

SUBJECT = re.compile(
    r"^(?P<type>[a-z]+)(\((?P<scope>[a-z0-9][a-z0-9._/-]*)\))?!?: (?P<summary>.+)$"
)

MAX_SUBJECT = 72

PLACEHOLDERS = {"wip", "fix", "fixes", "update", "updates", "changes", "misc",
                "stuff", "tmp", "test"}

# Messages git writes itself; they are not authored and not checked.
GENERATED = re.compile(r'^(Merge (branch|pull request|remote-tracking) |Revert ")')

# Attribution in any form: co-author trailers, tool signatures, AI markers.
ATTRIBUTION = re.compile(
    r"(?im)^\s*(co-authored-by|generated-by|generated-with|assisted-by|"
    r"ai-generated|made-with)\s*:"
    r"|generated (with|by) \[?(claude|chatgpt|copilot|cursor|codex|gemini)"
    r"|claude\.com/claude-code|noreply@anthropic\.com"
)

# A small set of Spanish function words. Two distinct hits in a message is a
# strong signal it is not English; one alone can be a quoted name.
SPANISH = {"que", "para", "los", "las", "del", "una", "por", "con", "el",
           "la", "de", "en", "y", "se", "al", "nueva", "nuevo", "añade",
           "añadir", "corrige", "actualiza", "elimina", "cambia", "sobre",
           "desde", "también", "seccion", "sección"}

# Typographic punctuation and mathematical symbols are legitimate English
# prose; everything else outside ASCII is either an emoji or a foreign script.
ALLOWED_NON_ASCII = {"Pd", "Pi", "Pf", "Po", "Ps", "Pe", "Sm", "Zs"}


def is_emoji(ch):
    code = ord(ch)
    return (unicodedata.category(ch) == "So"
            or 0x1F000 <= code <= 0x1FAFF
            or 0x2600 <= code <= 0x27BF
            or code in (0x200D, 0xFE0F, 0x20E3))


def clean(message):
    """Drop git comment lines and anything below the scissors line."""
    lines = []
    for line in message.splitlines():
        if line.startswith("# ------------------------ >8"):
            break
        if line.startswith("#"):
            continue
        lines.append(line.rstrip())
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return lines


def check(message):
    """Return the list of violations in one commit message."""
    lines = clean(message)
    if not lines:
        return ["the message is empty"]
    subject = lines[0]
    if GENERATED.match(subject):
        return []

    errors = []
    match = SUBJECT.match(subject)
    if not match:
        errors.append("the subject is not '<type>(<scope>): <summary>'")
    else:
        if match["type"] not in TYPES:
            errors.append(f"'{match['type']}' is not a type; use one of: "
                          + ", ".join(TYPES))
        summary = match["summary"]
        if summary.rstrip(".").strip().lower() in PLACEHOLDERS:
            errors.append(f"'{summary}' is a placeholder subject")
        if summary.endswith("."):
            errors.append("the subject ends with a period")
        if summary[:1].isupper() and not summary.split()[0].isupper():
            errors.append("the summary starts with an upper-case letter")
    if len(subject) > MAX_SUBJECT:
        errors.append(f"the subject is {len(subject)} characters; "
                      f"the limit is {MAX_SUBJECT}")
    if len(lines) > 1 and lines[1]:
        errors.append("the subject is not followed by a blank line")

    text = "\n".join(lines)
    emoji = sorted({ch for ch in text if is_emoji(ch)})
    if emoji:
        errors.append("the message contains emoji: " + " ".join(emoji))

    foreign = sorted({ch for ch in text if ord(ch) > 127 and not is_emoji(ch)
                      and unicodedata.category(ch) not in ALLOWED_NON_ASCII})
    words = {w.lower() for w in re.findall(r"[^\W\d_]+", text)}
    spanish = sorted(words & SPANISH)
    if foreign or len(spanish) >= 2:
        detail = " ".join(foreign) if foreign else ", ".join(spanish)
        errors.append(f"the message does not read as English ({detail})")

    for hit in ATTRIBUTION.finditer(text):
        errors.append(f"the message carries attribution: '{hit.group(0).strip()}'")

    return errors


def messages_in(revision_range):
    shas = subprocess.run(
        ["git", "rev-list", "--no-merges", revision_range],
        capture_output=True, text=True, check=True, encoding="utf-8",
    ).stdout.split()
    for sha in reversed(shas):
        body = subprocess.run(
            ["git", "log", "-1", "--format=%B", sha],
            capture_output=True, text=True, check=True, encoding="utf-8",
        ).stdout
        yield sha[:10], body


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("file", nargs="?", help="commit message file")
    group.add_argument("--range", help="revision range to check, such as A..B")
    args = parser.parse_args()

    if args.range:
        items = list(messages_in(args.range))
    else:
        with open(args.file, encoding="utf-8") as handle:
            items = [("message", handle.read())]

    failed = False
    for label, message in items:
        errors = check(message)
        if errors:
            failed = True
            subject = (clean(message) or [""])[0]
            print(f"{label}: {subject}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
    if failed:
        print("\nSee docs/ai/commits.md for the commit convention.",
              file=sys.stderr)
        return 1
    if args.range:
        print(f"{len(items)} commit message(s) follow the convention.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
