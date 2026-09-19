"""Render the executive map at summary/README.md.

A two-page entry point: what the framework is for, the principles that govern
it, and eight blocks that each link straight into the authoritative documents.
Read it to understand the model, follow the links to apply it, read the
decision records to understand why.

The design problem is that a summary is exactly how a corpus acquires a second
source of truth. Six months after someone writes two readable pages, those two
pages are what people quote, and they have quietly started saying things the
documents do not.

This tool solves that by not letting the summary have prose of its own. Every
sentence in the generated page is taken from somewhere authoritative:

    the opening                from the Purpose section, verbatim
    the conceptual chain       from the chain table that names its links
    the domain questions       from the domain table in README.md
    the seven principles       from principles/engineering-principles.md
    each block's essence       from the framing paragraph of its primary
                               document, as that document states it
    every title and identifier from the front matter of the document itself
    the counts                 from the corpus as it stands

The only authored judgement is BLOCKS below: which documents are the entry
points into each domain. That is a navigation decision, not a claim about what
the framework requires, and it is in one reviewable place.

Run from the repository root:

    python tools/render_summary.py           write summary/README.md
    python tools/render_summary.py --check   fail if it is stale

The generated page carries no requirement of its own. If it appears to, that
is a defect in this tool, not a rule.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_corpus import parse_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "summary" / "README.md"
README = ROOT / "README.md"
PRINCIPLES = ROOT / "principles" / "engineering-principles.md"

# The one authored part: which documents are the way into each domain.
#
# A navigation decision, not a statement about the framework. Changing it
# changes what a reader meets first; it cannot change what the framework
# requires, because nothing here supplies text.
BLOCKS: list[tuple[str, str, str, list[str]]] = [
    ("Foundations", "ai-foundations", "AI-FND-001", ["AI-FND-002", "AI-FND-003", "AI-FND-004"]),
    ("Knowledge", "knowledge", "AI-KNOW-001", ["AI-KNOW-002", "AI-KNOW-003", "AI-KNOW-005"]),
    ("Security", "security", "AI-SEC-001", ["AI-SEC-002", "AI-SEC-003"]),
    ("Agentic engineering", "agentic-engineering", "AI-AGT-001", ["AI-AGT-002", "AI-AGT-005"]),
    ("Verification", "verification", "AI-VER-001", ["AI-VER-002", "AI-VER-005"]),
    ("Integration", "integration", "AI-INT-003", ["AI-INT-002", "AI-INT-005", "AI-INT-006"]),
    ("Governance", "governance", "AI-GOV-001", ["AI-GOV-006", "AI-GOV-007"]),
    ("Implementation profiles", "profiles", "AI-PROF-002", ["AI-PROF-001", "AI-PROF-003"]),
]

DOMAINS = [
    "principles", "ai-foundations", "knowledge", "security", "agentic-engineering",
    "verification", "integration", "engineering-changes", "governance", "profiles",
    "decisions",
]

STANDING = (
    "This document is a navigation and executive-summary layer. It does not "
    "replace the authoritative, version-controlled documentation in the "
    "repository.\n\n"
    "Authoritative knowledge lives in the structured source documents. "
    "Summaries and compiled views are derived navigation aids and must never "
    "introduce requirements or decisions of their own."
)

CLOSING = (
    "Read the summary to understand the model. Follow the links to apply it. "
    "Consult the decision records to understand why."
)


def index() -> dict[str, tuple[Path, dict]]:
    found: dict[str, tuple[Path, dict]] = {}
    for domain in DOMAINS:
        for path in sorted((ROOT / domain).rglob("*.md")):
            front = parse_front_matter(path.read_text(encoding="utf-8"))
            if front and isinstance(front.get("id"), str):
                found[front["id"]] = (path, front)
    return found


def framing(path: Path, sentences: int = 2) -> str:
    """The document's own framing paragraph: between its title and its header."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^# .*?$\n+(.*?)\n+<!-- nav:start -->", text, re.MULTILINE | re.DOTALL)
    if not m:
        raise SystemExit(f"{path}: no framing paragraph found")
    paragraph = " ".join(m.group(1).split())
    parts = re.split(r"(?<=[.!?]) (?=[A-Z])", paragraph)
    return " ".join(parts[:sentences])


def domain_questions() -> dict[str, str]:
    """The question each domain answers, as the README already states it."""
    questions = {}
    for line in README.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*\[`([a-z-]+)/`\]\([^)]+\)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            questions[m.group(1)] = m.group(2)
    if not questions:
        raise SystemExit("README.md: could not read the domain table")
    return questions


def sentence(path: Path, starts_with: str) -> str:
    """Lift one stated sentence out of a document, verbatim."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith(starts_with):
            return line.strip()
    raise SystemExit(f"{path}: no line starting {starts_with!r}")


def paragraph_after(path: Path, heading: str) -> str:
    """The first paragraph under a heading, as that document writes it."""
    text = path.read_text(encoding="utf-8")
    m = re.search(rf"^{re.escape(heading)}\s*$\n+(.+?)\n\n", text, re.MULTILINE | re.DOTALL)
    if not m:
        raise SystemExit(f"{path}: no paragraph under {heading!r}")
    return " ".join(m.group(1).split())


def chain() -> list[str]:
    """The links of the conceptual chain, as the chain table names them."""
    text = PRINCIPLES.read_text(encoding="utf-8")
    rows = re.findall(r"^\| ([A-Z][^|]+?) \| .+? \| .+? \|$", text, re.MULTILINE)
    links = [r.strip() for r in rows if r.strip() != "Link"]
    if not links:
        raise SystemExit(f"{PRINCIPLES}: could not read the chain table")
    return links


def principles() -> list[str]:
    """The seven principles, as the principles document numbers them."""
    text = PRINCIPLES.read_text(encoding="utf-8")
    found = re.findall(r"^### (\d+)\.\s+(.*?)\s*$", text, re.MULTILINE)
    if not found:
        raise SystemExit(f"{PRINCIPLES}: no numbered principles found")
    return [title for _n, title in found]


def link(ident: str, docs: dict) -> str:
    path, front = docs[ident]
    rel = "../" + path.relative_to(ROOT).as_posix()
    return f"[{front['title']} `{ident}`]({rel})"


def render() -> str:
    docs = index()
    purpose_doc = docs["AI-PRIN-000"][0]
    questions = domain_questions()
    counts = {d: len(list((ROOT / d).rglob("*.md"))) for d in DOMAINS}

    out: list[str] = [
        "# Framework Map",
        "",
        f"> {STANDING.splitlines()[0]}",
        "",
        "> " + STANDING.split("\n\n")[1].replace("\n", "\n> "),
        "",
        "---",
        "",
        "## What this framework is for",
        "",
        paragraph_after(purpose_doc, "## Purpose"),
        "",
        sentence(purpose_doc, "The framework treats AI systems as"),
        "",
        sentence(purpose_doc, "> **AI may accelerate engineering work."),
        "",
        "Every domain document is `accepted`, subject to periodic review and "
        "open to change through the decision process. See "
        f"{link('AI-PRIN-000', docs)}.",
        "",
        "## One chain",
        "",
        sentence(PRINCIPLES, "Each link depends on the one before it"),
        "",
        "`" + "` &rarr; `".join(chain()) + "`",
        "",
        "## The seven principles",
        "",
    ]

    for number, title in enumerate(principles(), start=1):
        out.append(f"{number}. {title}")
    out += [
        "",
        "Stated in full in "
        f"{link('AI-PRIN-001', docs)}, with accountability in "
        f"{link('AI-PRIN-002', docs)} and evidence in "
        f"{link('AI-PRIN-003', docs)}.",
        "",
        "---",
        "",
        "## The map",
        "",
    ]

    for name, domain, primary, others in BLOCKS:
        question = questions.get(domain, "")
        entries = " &middot; ".join(link(i, docs) for i in [primary] + others)
        out += [
            f"### {name}",
            "",
            f"*{question}*",
            "",
            framing(docs[primary][0]),
            "",
            f"[`{domain}/`](../{domain}/) &mdash; {counts[domain]} documents "
            f"&middot; {entries}",
            "",
        ]

    out += [
        "---",
        "",
        "## Where the rest is",
        "",
        f"- [`engineering-changes/`](../engineering-changes/) &mdash; "
        f"{counts['engineering-changes']} playbooks for specific kinds of risky "
        "change: APIs, databases, observability.",
        f"- [`decisions/`](../decisions/) &mdash; {counts['decisions']} records of "
        "what was chosen and what was rejected. Append-only.",
        f"- [Open Questions](../governance/open-questions.md) &mdash; what is "
        "deliberately undecided, one document per question.",
        "- [`compiled/`](../compiled/) &mdash; the original draft, frozen. A "
        "snapshot, not a source.",
        "",
        "---",
        "",
        f"{CLOSING}",
        "",
        "<sub>Generated by `tools/render_summary.py`. Every sentence above is "
        "taken from the document it links to, from the README domain table, or "
        "from the corpus as it stands. Do not edit this file: change the source "
        "document and regenerate.</sub>",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    rendered = render()
    if "--check" in sys.argv:
        if not OUT.exists():
            print(f"{OUT.relative_to(ROOT).as_posix()} does not exist. Run: python tools/render_summary.py")
            return 1
        if OUT.read_text(encoding="utf-8") != rendered:
            print(f"{OUT.relative_to(ROOT).as_posix()} is stale.")
            print("A source document changed and the map was not regenerated.")
            print("Run: python tools/render_summary.py")
            return 1
        print("summary map is current")
        return 0

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"{OUT.relative_to(ROOT).as_posix()} written ({len(rendered.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
