"""Split the open-questions document into one document per question.

A question is not a paragraph in a list. It is opened, argued, answered,
deferred or withdrawn, it has an owner, and it has a blast radius across the
corpus. Bundled into one file, twelve of them could only be cited, versioned
and closed together, which is the same argument that spread the framework out
in the first place - applied one level down.

This tool performs that split once, from the subsections of the original
document, and rewrites what remains as an introduction and an index.

Run from the repository root:

    python tools/split_questions.py --check  report what would be written
    python tools/split_questions.py --force  perform or redo the split

Like `tools/split_framework.py`, it is destructive after the fact: the
question documents are the editable source once written, so overwriting them
requires --force. It is kept as provenance for the `affects` mapping below,
which is authored judgement rather than anything derived from the text.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "governance" / "open-questions.md"
OUT = ROOT / "governance" / "open-questions"

OPENED = "2026-08-20"

# What each question would change if it were answered.
#
# This is the one authored part of the split. A question's blast radius is a
# judgement about the corpus, not something the text states, and it is what
# makes the index worth reading: it turns "twelve things we have not decided"
# into "these are the documents that move when we do".
AFFECTS: dict[int, list[str]] = {
    1: ["AI-PRIN-000", "AI-GOV-002"],
    2: ["AI-PRIN-002", "AI-KNOW-003"],
    3: ["AI-FND-004", "AI-AGT-004", "AI-AGT-005"],
    4: ["AI-PRIN-003", "AI-INT-004"],
    5: ["AI-GOV-003", "AI-PROF-003"],
    6: ["AI-INT-005", "AI-PROF-002"],
    7: ["AI-GOV-002", "AI-INT-005"],
    8: ["AI-SEC-001", "AI-AGT-003"],
    9: ["AI-GOV-001", "AI-GOV-005"],
    10: ["AI-FND-003", "AI-AGT-002"],
    11: ["AI-KNOW-005"],
    12: ["AI-GOV-004"],
}

CLOSES = """## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
"""


def slugify(text: str) -> str:
    kept = []
    for char in text:
        if unicodedata.category(char)[0] in "LN":
            kept.append(char)
        elif char in " -":
            kept.append("-")
    return re.sub(r"-+", "-", "".join(kept)).strip("-").lower()


def parse_questions(body: str) -> tuple[str, list[tuple[int, str, str, list[str], str]]]:
    preamble, _, rest = body.partition("### Q1 —")
    rest = "### Q1 —" + rest

    questions = []
    for block in re.split(r"\n(?=### Q\d+ —)", rest):
        head, _, content = block.partition("\n")
        m = re.match(r"### Q(\d+) — (.+)", head.strip())
        if not m:
            raise SystemExit(f"unparseable question heading: {head!r}")
        number, title = int(m.group(1)), m.group(2).strip()

        lines = [l for l in content.strip().splitlines() if l.strip()]
        question = lines[0].strip().strip("*")

        provisional = ""
        discussion = []
        for line in lines[1:]:
            if line.startswith("*Provisional position in this draft:*"):
                provisional = line.split(":*", 1)[1].strip()
            else:
                discussion.append(line)

        questions.append((number, title, question, discussion, provisional))
    return preamble.strip(), questions


def render_question(number: int, title: str, question: str, discussion: list[str], provisional: str) -> str:
    ident = f"OQ-{number:04d}"
    front = [
        "---",
        f"id: {ident}",
        f"title: {title}",
        "status: open",
        "domain: governance",
        f"opened: {OPENED}",
        "owners:",
        "  - engineering",
        f"question: {question}",
        "affects:",
    ]
    front += [f"  - {a}" for a in AFFECTS[number]]
    front += [
        "related:",
        "  - AI-GOV-006",
        "source:",
        f"  - draft EN202608161000, section 71 (Q{number} — {title})",
        "---",
    ]

    parts = [
        "\n".join(front),
        "",
        f"# {ident} — {title}",
        "",
        f"> {question}",
        "",
        "---",
        "",
        "## Discussion",
        "",
        "\n\n".join(discussion),
        "",
    ]
    if provisional:
        parts += ["## Provisional position", "", provisional, ""]
    parts.append(CLOSES)
    return "\n".join(parts)


def render_index(front_matter: str, preamble: str, questions) -> str:
    lines = [
        front_matter.rstrip("\n"),
        "",
        "# Open Questions",
        "",
        "What the framework deliberately leaves undecided. This is the agenda for "
        "review, not a list of gaps to be quietly filled in.",
        "",
        "---",
        "",
        preamble,
        "",
        "Each question is its own document, with its own status, its own owner and "
        "its own history. A question is not a paragraph in a list: it is opened, "
        "argued and eventually closed, and bundling twelve of them into one file "
        "meant they could only be cited, versioned and answered together.",
        "",
        "## Index",
        "",
        "| Question | Status | Documents it would change |",
        "|---|---|---|",
    ]
    for number, title, _q, _d, _p in questions:
        ident = f"OQ-{number:04d}"
        name = f"{ident}-{slugify(title)}.md"
        affects = " ".join(f"`{a}`" for a in AFFECTS[number])
        lines.append(f"| [`{ident}` {title}](open-questions/{name}) | `open` | {affects} |")

    lines += [
        "",
        "## Lifecycle",
        "",
        "```text",
        "open        stated, not answered",
        "answered    closed by an accepted decision record",
        "deferred    real, but deliberately not being decided yet",
        "withdrawn   no longer a question - the premise changed",
        "superseded  replaced by a better-framed question",
        "```",
        "",
        "A question is answered by accepting a decision record under `decisions/` "
        "and updating the documents it affects in the same change. Nothing else "
        "closes one; a question that quietly stops being mentioned is still open.",
        "",
        "A closed question keeps its document. What was asked is worth as much as "
        "what was answered, and deleting it would leave the decision record "
        "pointing at nothing.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    check = "--check" in sys.argv
    force = "--force" in sys.argv

    text = SRC.read_text(encoding="utf-8")
    parts = text.split("\n---\n", 2)
    if len(parts) < 3:
        raise SystemExit(f"{SRC.name}: expected front matter, header and body")
    front_matter = parts[0] + "\n---\n"
    body = parts[2]

    # Section 71 was captured up to the next level-two heading, and Part II
    # opens with a level-one one, so the annex header rode in with it.
    body = body.split("\n# Part II")[0].rstrip().rstrip("-").rstrip()

    preamble, questions = parse_questions(body)

    existing = sorted(OUT.glob("OQ-*.md")) if OUT.exists() else []
    if existing and not force and not check:
        print(f"{len(existing)} question documents already exist.")
        print("They are the editable source; rewriting them from the index would")
        print("destroy any edit made since the split. Re-run with --force only if")
        print("that is genuinely what you want.")
        return 1

    if check:
        print(f"{len(questions)} questions parsed from {SRC.relative_to(ROOT).as_posix()}")
        for number, title, _q, _d, _p in questions:
            print(f"  OQ-{number:04d}  {title}")
        return 0

    OUT.mkdir(exist_ok=True)
    for number, title, question, discussion, provisional in questions:
        name = f"OQ-{number:04d}-{slugify(title)}.md"
        (OUT / name).write_text(
            render_question(number, title, question, discussion, provisional),
            encoding="utf-8",
            newline="\n",
        )
        print(f"governance/open-questions/{name}")

    SRC.write_text(render_index(front_matter, preamble, questions), encoding="utf-8", newline="\n")
    print(f"\n{len(questions)} questions written; index rewritten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
