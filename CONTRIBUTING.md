# Contributing

How to change this repository. For the reasoning behind these rules, see
[Decision Process](governance/decision-process.md); this page is the mechanics.

## What kind of change is this

**Editorial** — a typo, a broken link, a clearer sentence, a better example,
front matter that is wrong. Open a Pull Request against the document. No
ceremony.

**Substantive** — anything that changes what the framework asks for, moves a
document between domains, adds or removes a document, or changes a `status`.
Open a decision record under [`decisions/`](decisions/) first. The record
carries the argument; the domain documents are updated when it is accepted.

If you are unsure which one you have, write the decision record. It is cheap,
and a change that turns out to be editorial loses nothing by having been
explained.

## Rules that apply to every change

1. **One logical change per commit and per Pull Request.** Split a
   reorganisation from a rewording; they are reviewed differently.
2. **No copies.** A statement lives in exactly one document. If two documents
   need it, one links to the other. A copied paragraph is a future
   contradiction.
3. **Links, not paths, and identifiers, not titles.** Cite a document by its
   `id` in prose and decision records. Paths move.
4. **Front matter stays true.** If a document's `related`, `applies_to` or
   `source` no longer describes it, that is a defect in the same sense the
   framework means it.
5. **Do not hand-edit the navigation header.** The block between `nav:start`
   and `nav:end` is generated from the front matter by
   `python tools/render_headers.py`. Change the front matter and re-run it; the
   gate fails if the two disagree.
6. **No secrets, ever** — in a document, a commit message, an example or a
   fixture. Not credentials, tokens, keys, internal URLs, customer data or
   personal information.
7. **English.** The corpus is written in English so it reads consistently and
   can be cited without translation drift.

## Commits

The full rule is [`docs/ai/commits.md`](docs/ai/commits.md). In short:

```text
<type>(<scope>): <imperative summary, 72 chars or fewer>

Why the change was made. The diff already shows what.

Refs: AI-DEC-001
```

Types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`,
`security`, `chore`.

No emoji. No attribution or co-author trailers. Cite the decision record when
a change implements one.

Enable the commit-msg hook once per clone so a message that breaks the
convention is rejected locally rather than in CI:

```bash
git config core.hooksPath .githooks
```

## Branches

Work outside protected branches:

```text
feature/<short-description>
fix/<short-description>
refactor/<short-description>
technical/<short-description>
```

`main` is reached through a Pull Request reviewed by a human. Nothing merges
itself.

## Working with an AI assistant

Assistance is expected and welcome, under the framework the repository
describes:

- An assistant MAY draft a document, a decision record, a summary or a
  critique. It MUST NOT accept a decision, approve a Pull Request or merge one.
- Give it the minimum context the task needs. A large context window is not
  permission to paste the corpus.
- Verify what it produces against the source before committing it. Fluency is
  not evidence — that is the whole argument of
  [Agentic Bias](ai-foundations/agentic-bias.md).
- Reusable instructions for assistants belong in [`docs/ai/`](docs/ai/), in
  version control and under review. Private agent configuration, session state
  and credentials do not; `.claude/` is untracked apart from
  `.claude/skills/`.
- Use the skills rather than improvising. Finding knowledge is
  `navigate-engineering-knowledge`; deciding whether a change needs a
  documentation update is `documentation-impact-analysis`; making that update is
  `maintain-engineering-documentation`; auditing the corpus is
  `validate-knowledge-graph`. They are listed in the [README](README.md).
- A skill is engineering instruction like any other document here. If one is
  wrong, fix it in a Pull Request rather than working around it.

The history records what changed and why, not who or what typed it. That is a
deliberate position, recorded in
[AI Contribution Traceability](governance/ai-traceability.md) and still open.

## Reviewing

A reviewer is asked for two things beyond correctness:

- **Does this belong here?** Domain placement is the part of the corpus most
  likely to be wrong, and the cheapest to fix early.
- **Is it arguable?** A document that cannot be disagreed with usually is not
  saying anything. Provisional positions should be marked
  `> **Discussion point.**` rather than smoothed into apparent consensus.
