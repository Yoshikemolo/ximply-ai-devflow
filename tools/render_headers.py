"""Render the navigable header of every corpus document.

Front matter is machine-readable and GitHub renders it as a flat table, so
`related`, `domain` and `source` arrive as inert text: a reader who wants the
document behind an identifier has to go and look for it. That friction is
exactly what the corpus was spread out to remove.

This tool derives a rendered header from the front matter of each document and
writes it between the `nav:start` and `nav:end` markers:

    identifier, status and a link to the domain folder
    every `related` and `affects` identifier, as a link to that document
    every `source` entry, as a link to the section of the trunk document

Nothing here is authored. The front matter remains the single place a fact is
stated, the header is derived from it, and `tools/check_corpus.py` fails the
build if the two disagree - so the duplication cannot rot into a
contradiction.

Run from the repository root:

    python tools/render_headers.py           write the headers
    python tools/render_headers.py --check   report documents that are stale
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_corpus import DOMAIN_PREFIX, parse_front_matter, slug  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TRUNK = ROOT / "compiled" / "AI-Assisted Software Engineering Framework - draft EN202608161000.md"

START = "<!-- nav:start -->"
END = "<!-- nav:end -->"

SECTION_SOURCE = re.compile(r"^draft \S+, section (\d+)(?:\s*\((excluding )?(.+)\))?$")
ANNEX_SOURCE = re.compile(r"^draft \S+, (Annex [ABC])$")


def trunk_headings() -> dict[str, str]:
    """Map a lookup key to the full heading text it appears under in the trunk."""
    headings: dict[str, str] = {}
    for line in TRUNK.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            text = line[3:].strip()
            m = re.match(r"^(\d+)\.\s", text)
            if m:
                headings[m.group(1)] = text
            elif text.startswith("Annex "):
                headings[text.split(" —")[0]] = text
        elif line.startswith("### "):
            text = line[4:].strip()
            headings[text] = text
    return headings


def relative(from_doc: Path, target: Path) -> str:
    rel = os.path.relpath(target, from_doc.parent)
    return "/".join(quote(part) for part in Path(rel).parts)


def trunk_link(from_doc: Path, anchor: str) -> str:
    fragment = quote(anchor, safe="-_")
    return f"{relative(from_doc, TRUNK)}#{fragment}"


def domain_link(from_doc: Path, domain: str) -> str:
    rel = os.path.relpath(ROOT / domain, from_doc.parent).replace(os.sep, "/")
    return "./" if rel == "." else rel + "/"


def render_sources(doc: Path, sources: list[str], headings: dict[str, str]) -> list[str]:
    rendered: list[str] = []
    for entry in sources:
        m = SECTION_SOURCE.match(entry)
        if m:
            number, excluding, names = m.group(1), m.group(2), m.group(3)
            if names and not excluding:
                for name in [n.strip() for n in names.split(";")]:
                    heading = headings.get(name)
                    if heading is None:
                        raise SystemExit(f"{doc}: no trunk heading for subsection {name!r}")
                    rendered.append(f"[{heading}]({trunk_link(doc, slug(heading))})")
                continue
            heading = headings.get(number)
            if heading is None:
                raise SystemExit(f"{doc}: no trunk heading for section {number}")
            label = f"section {heading}"
            if excluding:
                label += f" (excluding {names})"
            rendered.append(f"[{label}]({trunk_link(doc, slug(heading))})")
            continue

        m = ANNEX_SOURCE.match(entry)
        if m:
            heading = headings.get(m.group(1))
            if heading is None:
                raise SystemExit(f"{doc}: no trunk heading for {m.group(1)}")
            rendered.append(f"[{heading}]({trunk_link(doc, slug(heading))})")
            continue

        rendered.append(entry)
    return rendered


def build_index() -> dict[str, tuple[Path, str]]:
    index: dict[str, tuple[Path, str]] = {}
    for domain in DOMAIN_PREFIX:
        for path in sorted((ROOT / domain).rglob("*.md")):
            front = parse_front_matter(path.read_text(encoding="utf-8"))
            if front and isinstance(front.get("id"), str):
                index[front["id"]] = (path, str(front.get("title", front["id"])))
    return index


def render_block(doc: Path, front: dict, index: dict[str, tuple[Path, str]], headings: dict[str, str]) -> str:
    domain = doc.relative_to(ROOT).parts[0]
    lines = [
        f"`{front['id']}` &middot; status **{front['status']}** &middot; "
        f"domain [`{domain}/`]({domain_link(doc, domain)})"
    ]

    related = front.get("related") or []
    if related:
        items = []
        for ref in related:
            target = index.get(ref)
            if target is None:
                raise SystemExit(f"{doc}: related identifier {ref} does not resolve")
            path, title = target
            items.append(f"[{title} `{ref}`]({relative(doc, path)})")
        lines.append("**Related** &mdash; " + " &middot; ".join(items))

    affects = front.get("affects") or []
    if affects:
        items = []
        for ref in affects:
            target = index.get(ref)
            if target is None:
                raise SystemExit(f"{doc}: affects identifier {ref} does not resolve")
            items.append(f"[{target[1]} `{ref}`]({relative(doc, target[0])})")
        lines.append("**Would change** &mdash; " + " &middot; ".join(items))

    supersedes = front.get("supersedes") or []
    if not isinstance(supersedes, list):
        raise SystemExit(f"{doc}: supersedes must be a list, got {supersedes!r}")
    if supersedes:
        items = []
        for ref in supersedes:
            target = index.get(ref)
            items.append(
                f"[{target[1]} `{ref}`]({relative(doc, target[0])})" if target else f"`{ref}`"
            )
        lines.append("**Supersedes** &mdash; " + " &middot; ".join(items))

    sources = front.get("source") or []
    if sources:
        rendered = render_sources(doc, [str(s) for s in sources], headings)
        lines.append("**Derived from** &mdash; " + " &middot; ".join(rendered))

    return f"{START}\n" + "\n\n".join(lines) + f"\n{END}"


def apply_block(text: str, block: str) -> str:
    if START in text and END in text:
        start = text.index(START)
        end = text.index(END) + len(END)
        return text[:start] + block + text[end:]

    end_of_front = text.index("\n---\n", 4) + len("\n---\n")
    head, body = text[:end_of_front], text[end_of_front:]

    if body.lstrip().startswith("# "):
        marker = "\n\n---\n"
        cut = body.find(marker)
        if cut != -1:
            return head + body[:cut] + "\n\n" + block + body[cut:]
    return head + "\n" + block + "\n" + body.lstrip("\n")


def main() -> int:
    check = "--check" in sys.argv
    index = build_index()
    headings = trunk_headings()

    stale: list[str] = []
    for _id, (path, _title) in sorted(index.items()):
        text = path.read_text(encoding="utf-8")
        front = parse_front_matter(text)
        block = render_block(path, front, index, headings)
        updated = apply_block(text, block)
        if updated == text:
            continue
        if check:
            stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.write_text(updated, encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT).as_posix())

    if check:
        if stale:
            print(f"{len(stale)} document(s) with a stale or missing navigation header:\n")
            for path in stale:
                print(f"  {path}")
            print("\nRun: python tools/render_headers.py")
            return 1
        print(f"navigation headers current in {len(index)} documents")
    else:
        print(f"\n{len(index)} documents checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
