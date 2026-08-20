# AI-Assisted Software Engineering Framework

Working draft of an engineering standard for software development assisted by
AI systems. It proposes how AI participates in engineering work, where the
human boundary sits, and what verification a change must pass before it is
allowed to cross into a shared branch.

The document is the product of this repository. There is no application code.

## Contents

| Path | Description |
|------|-------------|
| `AI-Assisted Software Engineering Framework - draft EN202608161000.md` | Authoritative source of the framework |
| `AI-Assisted Software Engineering Framework - draft EN202608161000.docx` | Derived distribution format |
| `AI-Assisted Software Engineering Framework - draft EN202608161000.pdf` | Derived distribution format |
| `docs/ai/` | Versioned engineering instructions that govern work in this repository |
| `.claude/skills/` | Agent skills that apply those instructions |

The Markdown file is the only editable form. The DOCX and PDF are generated
from it and are committed so a reviewer can read the document without a
conversion toolchain; they are regenerated, never edited directly.

The document is structured in two parts:

- **Part I — Proposed Engineering Standard**, sections 1 to 71.
- **Part II — Implementation Profile**, annexes A to C: reference CI harness
  configurations, proposed quality gate baselines and a draft Pull Request
  declaration.

Section 71, *Open Questions and Decisions Required*, lists what the draft
deliberately leaves undecided.

## Working in this repository

This repository applies the framework to itself. The rules below are not
stylistic preferences; each one is the repository-level expression of a
section of the document.

**Commits.** English, no emoji, no attribution trailers, one logical change per
commit. The full rule is in [`docs/ai/commits.md`](docs/ai/commits.md).

**Branches.** Work happens outside protected branches, on `feature/*`,
`fix/*`, `refactor/*` or `technical/*`, and reaches `main` through a Pull
Request reviewed by a human. An AI assistant does not push to a protected
branch, merge into one, or approve a Pull Request.

**Documentation.** `/docs` is part of the product. A change that contradicts
documented behavior is incomplete until the documentation moves with it.

**Private configuration.** Local agent state, settings and credentials stay
out of version control. Reviewed, reusable engineering instructions belong in
`/docs/ai`, which is versioned with the work it governs.

**Context boundary.** Minimum required context. A large context window is not
permission to supply unnecessary information, and sensitivity is a property of
the accumulated context rather than of any single file in it.

## Status

Draft. The standard is under discussion and is not yet ratified. Normative
language in the document (`MUST`, `SHOULD`, `MAY`) states the proposal, not an
adopted obligation.
