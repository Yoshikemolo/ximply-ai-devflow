"""Integrity checks for the addressable corpus.

The framework claims that documentation which contradicts reality is a defect.
A claim like that is worth very little unless something checks it, so this is
the quality gate for the corpus itself.

It verifies what can actually be verified mechanically:

    front matter    present, parseable, and carrying the required fields
    identifiers     unique, well-formed, and matching their domain
    status          drawn from the agreed vocabulary
    relationships   every identifier in `related` resolves to a document
    links           every relative Markdown link resolves to a file
    coverage        every corpus document is reachable from the README

It deliberately does not check prose. Whether a document is any good is a
question for human review, and a gate that pretends otherwise mostly teaches
people to write around it.

Run from the repository root:

    python tools/check_corpus.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN_PREFIX = {
    "principles": "PRIN",
    "ai-foundations": "FND",
    "knowledge": "KNOW",
    "security": "SEC",
    "agentic-engineering": "AGT",
    "verification": "VER",
    "integration": "INT",
    "engineering-changes": "CHG",
    "governance": "GOV",
    "profiles": "PROF",
    "decisions": "DEC",
}

REQUIRED = ["id", "title", "status"]
DOMAIN_REQUIRED = REQUIRED + ["domain", "owners", "applies_to", "related", "source"]
DECISION_REQUIRED = REQUIRED + ["created", "owners", "related"]

STATUSES = {"proposed", "accepted", "deprecated", "superseded", "rejected", "pending"}
ID_RE = re.compile(r"^AI-(PRIN|FND|KNOW|SEC|AGT|VER|INT|CHG|GOV|PROF|DEC)-\d{3}$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")

errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT).as_posix()}: {message}")


def parse_front_matter(text: str) -> dict[str, object] | None:
    """Parse the restricted YAML subset used by this corpus."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    data: dict[str, object] = {}
    key: str | None = None
    for raw in text[4:end].splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  "):
            item = raw.strip()
            if item == "[]":
                data[key] = []
            elif item.startswith("- "):
                data.setdefault(key, [])
                if isinstance(data[key], list):
                    data[key].append(item[2:].strip())
            continue
        if ":" not in raw:
            return None
        key, _, value = raw.partition(":")
        key = key.strip()
        value = value.strip()
        data[key] = value if value else None
    return data


def corpus_documents() -> list[Path]:
    docs: list[Path] = []
    for domain in DOMAIN_PREFIX:
        docs.extend(sorted((ROOT / domain).rglob("*.md")))
    return docs


def check_document(path: Path, ids: dict[str, Path]) -> dict[str, object] | None:
    text = path.read_text(encoding="utf-8")
    front = parse_front_matter(text)
    if front is None:
        fail(path, "missing or unparseable front matter")
        return None

    domain = path.relative_to(ROOT).parts[0]
    required = DECISION_REQUIRED if domain == "decisions" else DOMAIN_REQUIRED
    for field in required:
        if field not in front:
            fail(path, f"front matter missing '{field}'")

    doc_id = front.get("id")
    if not isinstance(doc_id, str) or not ID_RE.match(doc_id):
        fail(path, f"malformed identifier: {doc_id!r}")
    else:
        if doc_id in ids:
            fail(path, f"duplicate identifier {doc_id}, also in {ids[doc_id].relative_to(ROOT).as_posix()}")
        ids[doc_id] = path
        expected = DOMAIN_PREFIX[domain]
        if doc_id.split("-")[1] != expected:
            fail(path, f"identifier {doc_id} does not match domain '{domain}' (expected AI-{expected}-NNN)")

    status = front.get("status")
    if status not in STATUSES:
        fail(path, f"status {status!r} is not one of {sorted(STATUSES)}")

    if domain != "decisions" and front.get("domain") != domain:
        fail(path, f"front matter domain {front.get('domain')!r} does not match location {domain!r}")

    for link in LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        if not target.exists():
            fail(path, f"dangling link: {link}")

    return front


def main() -> int:
    ids: dict[str, Path] = {}
    fronts: dict[Path, dict[str, object]] = {}

    documents = corpus_documents()
    if not documents:
        print("no corpus documents found")
        return 1

    for path in documents:
        front = check_document(path, ids)
        if front:
            fronts[path] = front

    for path, front in fronts.items():
        for ref in front.get("related") or []:
            if ref not in ids:
                fail(path, f"related identifier {ref} does not resolve to any document")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    linked = {
        (ROOT / "README.md").parent.joinpath(link.split("#")[0]).resolve()
        for link in LINK_RE.findall(readme)
        if not link.startswith(("http://", "https://", "#", "mailto:"))
    }
    for path in documents:
        if path.resolve() not in linked and path.parent.resolve() not in linked:
            fail(path, "not reachable from README.md")

    for link in LINK_RE.findall(readme):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (ROOT / link.split("#")[0]).exists():
            errors.append(f"README.md: dangling link: {link}")

    if errors:
        print(f"corpus check failed with {len(errors)} problem(s):\n")
        for error in errors:
            print(f"  {error}")
        return 1

    print(f"corpus check passed: {len(documents)} documents, {len(ids)} identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
