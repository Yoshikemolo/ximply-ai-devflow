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
    anchors         every link fragment resolves to a heading in its target
    coverage        every document is reachable by following links from README

It deliberately does not check prose. Whether a document is any good is a
question for human review, and a gate that pretends otherwise mostly teaches
people to write around it.

Run from the repository root:

    python tools/check_corpus.py

The navigation headers the documents carry are generated rather than authored;
`tools/render_headers.py --check` verifies they still agree with the front
matter they were derived from.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

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
QUESTION_REQUIRED = REQUIRED + ["domain", "opened", "owners", "question", "affects", "related", "source"]

STATUSES = {"proposed", "accepted", "deprecated", "superseded", "rejected", "pending"}
# A question has its own lifecycle. It is not proposed or accepted; it is asked,
# and it stays asked until a decision record closes it.
QUESTION_STATUSES = {"open", "answered", "deferred", "withdrawn", "superseded"}
ID_RE = re.compile(r"^AI-(PRIN|FND|KNOW|SEC|AGT|VER|INT|CHG|GOV|PROF|DEC)-\d{3}$")
QUESTION_ID_RE = re.compile(r"^OQ-\d{4}$")
QUESTIONS_DIR = ROOT / "governance" / "open-questions"
LINK_RE = re.compile(r"\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


def slug(heading: str) -> str:
    """Approximate the anchor GitHub generates for a heading.

    Letters, numbers, marks and connector or dash punctuation survive;
    everything else is dropped, spaces become hyphens, and the result is
    lower-cased. Kept here rather than in the renderer because the check is
    what makes the anchors trustworthy.
    """
    kept = []
    for char in heading:
        category = unicodedata.category(char)
        if category[0] in "LN" or category in ("Pc", "Pd", "Mn", "Mc"):
            kept.append(char)
        elif char == " ":
            kept.append("-")
    return "".join(kept).lower()


_anchors: dict[Path, set[str]] = {}


def anchors_of(path: Path) -> set[str]:
    if path not in _anchors:
        text = path.read_text(encoding="utf-8", errors="replace")
        _anchors[path] = {slug(h.strip()) for h in HEADING_RE.findall(text)}
    return _anchors[path]


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
                # The key line that opened this list parsed to None, so replace
                # it rather than setdefault, which would leave the None in place
                # and silently drop every item.
                if not isinstance(data.get(key), list):
                    data[key] = []
                data[key].append(item[2:].strip())
            continue
        if ":" not in raw:
            return None
        key, _, value = raw.partition(":")
        key = key.strip()
        value = value.strip()
        # An inline "[]" is an empty list, not the two-character string. Left as
        # a string it iterates as its own brackets wherever a list is expected.
        data[key] = [] if value == "[]" else (value if value else None)
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
    is_question = path.parent == QUESTIONS_DIR

    if is_question:
        required = QUESTION_REQUIRED
    elif domain == "decisions":
        required = DECISION_REQUIRED
    else:
        required = DOMAIN_REQUIRED
    for field in required:
        if field not in front:
            fail(path, f"front matter missing '{field}'")

    doc_id = front.get("id")
    pattern = QUESTION_ID_RE if is_question else ID_RE
    if not isinstance(doc_id, str) or not pattern.match(doc_id):
        fail(path, f"malformed identifier: {doc_id!r}")
    else:
        if doc_id in ids:
            fail(path, f"duplicate identifier {doc_id}, also in {ids[doc_id].relative_to(ROOT).as_posix()}")
        ids[doc_id] = path
        if not is_question:
            expected = DOMAIN_PREFIX[domain]
            if doc_id.split("-")[1] != expected:
                fail(path, f"identifier {doc_id} does not match domain '{domain}' (expected AI-{expected}-NNN)")

    status = front.get("status")
    allowed = QUESTION_STATUSES if is_question else STATUSES
    if status not in allowed:
        fail(path, f"status {status!r} is not one of {sorted(allowed)}")

    if domain != "decisions" and front.get("domain") != domain:
        fail(path, f"front matter domain {front.get('domain')!r} does not match location {domain!r}")

    for link in LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        location, _, fragment = link.partition("#")
        target = (path.parent / unquote(location)).resolve()
        if not target.exists():
            fail(path, f"dangling link: {link}")
        elif fragment and target.suffix == ".md":
            anchor = unquote(fragment)
            if anchor not in anchors_of(target):
                fail(path, f"anchor not found in {target.name}: #{anchor}")

    return front


def reachable(start: Path) -> set[Path]:
    """Every document a reader can arrive at by following links from `start`.

    A link to a directory reaches the documents directly inside it, which is
    how the README indexes a domain; anything deeper has to be linked by a
    document that was itself reached. Selective retrieval is the argument the
    corpus rests on, and a document nothing points at cannot be retrieved.
    """
    seen = {start.resolve()}
    queue = [start]
    while queue:
        current = queue.pop()
        try:
            text = current.read_text(encoding="utf-8")
        except OSError:
            continue
        for link in LINK_RE.findall(text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (current.parent / unquote(link.partition("#")[0])).resolve()
            found = sorted(target.glob("*.md")) if target.is_dir() else [target]
            for item in found:
                if item.suffix == ".md" and item.exists() and item not in seen:
                    seen.add(item)
                    queue.append(item)
    return seen


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
        for field in ("related", "affects", "supersedes"):
            for ref in front.get(field) or []:
                if ref not in ids:
                    fail(path, f"{field} identifier {ref} does not resolve to any document")

    readme = ROOT / "README.md"
    reached = reachable(readme)
    for path in documents:
        if path.resolve() not in reached:
            fail(path, "not reachable by following links from README.md")

    for link in LINK_RE.findall(readme.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (ROOT / unquote(link.split("#")[0])).exists():
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
