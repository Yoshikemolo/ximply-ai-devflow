"""Derive the addressable framework corpus from the monolithic draft.

The draft document is the historical source. This tool splits it into one
document per conceptual unit, grouped by domain, and rewrites the internal
"section N" cross-references into links between the resulting files.

The split is conceptual rather than mechanical: sections that answer the same
engineering question end up in the same document, and no section is copied
into two places. Every target document records which source sections it was
derived from, so the derivation stays auditable.

Run from the repository root:

    python tools/split_framework.py          write the corpus
    python tools/split_framework.py --check  report coverage and dangling refs

The tool is kept in the repository as provenance for the corpus. It will be
retired once the domain documents become the editable source and the draft
becomes a compiled view rather than the origin.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from corpus_map import MAP  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DRAFT_NAME = "AI-Assisted Software Engineering Framework - draft EN202608161000.md"
STATUS = "proposed"
OWNERS = ["engineering"]


def source_path() -> Path:
    for candidate in (ROOT / "compiled" / DRAFT_NAME, ROOT / DRAFT_NAME):
        if candidate.exists():
            return candidate
    raise SystemExit(f"draft not found: {DRAFT_NAME}")


# ---------------------------------------------------------------------------
# Source parsing
# ---------------------------------------------------------------------------

SECTION_RE = re.compile(r"^## (?:(\d+)\.\s+(.*)|(Annex [ABC])\s+—\s+(.*))$")


def parse_sections(text: str) -> dict[str, tuple[str, str]]:
    """Return {key: (title, body)} for every numbered section and annex."""
    lines = text.splitlines()
    starts: list[tuple[int, str, str]] = []
    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            if m.group(1):
                starts.append((i, m.group(1), m.group(2).strip()))
            else:
                starts.append((i, m.group(3), m.group(4).strip()))

    sections: dict[str, tuple[str, str]] = {}
    for idx, (start, key, title) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body = lines[start + 1 : end]
        sections[key] = (title, trim("\n".join(body)))
    return sections


def trim(block: str) -> str:
    lines = block.splitlines()
    while lines and lines[-1].strip() in ("", "---"):
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines)


def split_subsections(body: str) -> dict[str, str]:
    """Return {subsection title: block} for every level-three heading."""
    lines = body.splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("### ")]
    subs: dict[str, str] = {}
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        subs[lines[start][4:].strip()] = trim("\n".join(lines[start:end]))
    return subs


def drop_subsections(body: str, names: tuple[str, ...]) -> str:
    lines = body.splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("### ")]
    keep = [True] * len(lines)
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        if lines[start][4:].strip() in names:
            for i in range(start, end):
                keep[i] = False
    return trim("\n".join(l for l, k in zip(lines, keep) if k))


def promote(block: str) -> str:
    """Promote a subsection block one heading level and strip its number."""
    out = []
    for line in block.splitlines():
        if line.startswith("#### "):
            out.append("### " + line[5:])
        elif line.startswith("### "):
            title = re.sub(r"^\d+(\.\d+)*\s+", "", line[4:].strip())
            out.append("## " + title)
        else:
            out.append(line)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Cross-reference rewriting
# ---------------------------------------------------------------------------

# Prose references that name a section without numbering it. Each maps to the
# source section key that now lives in a target document.
PHRASES: list[tuple[str, str]] = [
    (r"the section on automated quality gates", "46"),
    (r"the section on AI review", "57"),
    (r"the section on quality gates", "46"),
    (r"the proposed compliance model", "68"),
    (r"the compliance model", "68"),
    (r"the context-economy section", "7"),
    (r"the context economy section", "7"),
    (r"the prompting section", "20"),
    (r"the tooling section", "23"),
    (r"the open questions at the end of Part I", "71"),
    (r"the open questions", "71"),
    (r"the autonomy levels in this document", "11"),
    (r"the section on synthetic data", "36"),
]

ANNEX_RE = re.compile(r"\bAnnex ([ABC])\b")
NUMBER_RE = re.compile(r"\b([Ss])ections?\s+(\d+)\b")


def build_index() -> dict[str, dict]:
    """Map every source section key to the target document that now holds it."""
    index: dict[str, dict] = {}
    for entry in MAP:
        for key, _mode, _names in entry["sources"]:
            index[key] = entry
    return index


def link(from_path: str, target: dict, text: str) -> str:
    rel = os.path.relpath(target["path"], os.path.dirname(from_path)).replace(os.sep, "/")
    return f"[{text}]({rel})"


def rewrite(body: str, from_path: str, index: dict[str, dict]) -> tuple[str, set[str]]:
    """Rewrite internal references into links; return the body and the ids used."""
    referenced: set[str] = set()

    def register(entry: dict) -> None:
        if entry["path"] != from_path:
            referenced.add(entry["id"])

    for pattern, key in PHRASES:
        target = index.get(key)
        if not target or target["path"] == from_path:
            continue

        def repl(m: re.Match, target=target) -> str:
            register(target)
            return link(from_path, target, m.group(0))

        body = re.sub(pattern, repl, body)

    def annex_repl(m: re.Match) -> str:
        target = index.get(f"Annex {m.group(1)}")
        if not target or target["path"] == from_path:
            return m.group(0)
        register(target)
        return link(from_path, target, m.group(0))

    body = ANNEX_RE.sub(annex_repl, body)

    def number_repl(m: re.Match) -> str:
        target = index.get(m.group(2))
        if not target or target["path"] == from_path:
            return m.group(0)
        register(target)
        return link(from_path, target, target["title"])

    body = NUMBER_RE.sub(number_repl, body)
    return body, referenced


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def collect_blocks(entry: dict, sections: dict[str, tuple[str, str]]) -> list[tuple[str | None, str]]:
    blocks: list[tuple[str | None, str]] = []
    for key, mode, names in entry["sources"]:
        if key not in sections:
            raise SystemExit(f"{entry['path']}: unknown source section {key!r}")
        title, body = sections[key]
        if mode == "only":
            subs = split_subsections(body)
            for name in names:
                if name not in subs:
                    raise SystemExit(f"{entry['path']}: unknown subsection {name!r} in section {key}")
                promoted = promote(subs[name])
                heading, _, rest = promoted.partition("\n")
                blocks.append((heading[3:].strip(), trim(rest)))
        elif mode == "except":
            blocks.append((title, drop_subsections(body, names)))
        else:
            blocks.append((title, body))
    return blocks


def front_matter(entry: dict, related: list[str]) -> str:
    domain = entry["path"].split("/")[0]
    lines = [
        "---",
        f"id: {entry['id']}",
        f"title: {entry['title']}",
        f"status: {STATUS}",
        f"domain: {domain}",
        "owners:",
    ]
    lines += [f"  - {o}" for o in OWNERS]
    lines.append("applies_to:")
    lines += [f"  - {a}" for a in entry["applies_to"]]
    lines.append("related:")
    lines += [f"  - {r}" for r in related] if related else ["  []"]
    lines.append("source:")
    for key, mode, names in entry["sources"]:
        label = f"draft EN202608161000, section {key}" if key.isdigit() else f"draft EN202608161000, {key}"
        if mode == "only":
            label += " (" + "; ".join(names) + ")"
        elif mode == "except":
            label += " (excluding " + "; ".join(names) + ")"
        lines.append(f"  - {label}")
    lines.append("---")
    return "\n".join(lines)


def render(entry: dict, sections: dict[str, tuple[str, str]], index: dict[str, dict]) -> str:
    blocks = collect_blocks(entry, sections)
    parts: list[str] = []
    single = len(blocks) == 1
    for heading, body in blocks:
        if not single and heading:
            parts.append(f"## {heading}\n\n{body}")
        else:
            parts.append(body)
    body = "\n\n---\n\n".join(parts)
    body, referenced = rewrite(body, entry["path"], index)
    related = sorted(referenced)
    return f"{front_matter(entry, related)}\n\n# {entry['title']}\n\n{entry['intro']}\n\n---\n\n{body}\n"


def main() -> int:
    text = source_path().read_text(encoding="utf-8")
    sections = parse_sections(text)
    index = build_index()

    check = "--check" in sys.argv
    if check:
        covered = set(index)
        missing = sorted(set(sections) - covered, key=lambda k: (not k.isdigit(), int(k) if k.isdigit() else k))
        print(f"sections parsed: {len(sections)}")
        print(f"sections mapped: {len(covered)}")
        print(f"documents:       {len(MAP)}")
        if missing:
            print("NOT MAPPED: " + ", ".join(missing))
        else:
            print("NOT MAPPED: none")
        return 1 if missing else 0

    for entry in MAP:
        target = ROOT / entry["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(entry, sections, index), encoding="utf-8", newline="\n")
        print(entry["path"])
    print(f"\n{len(MAP)} documents written from {len(sections)} source sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
