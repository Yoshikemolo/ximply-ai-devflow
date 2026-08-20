# Commit Convention

Versioned engineering instruction. It governs every commit in this repository,
whether the author is a human or an AI assistant.

This document holds the rule. The agent skill under `.claude/skills/commit`
only implements it; when the two disagree, this document wins.

## Principles this rule derives from

- **Repository as engineering source of truth.** The commit history is part of
  the authoritative record of how the software came to be. It is written for a
  future reader who was not present when the change was made.
- **Small-batch development.** A change is accepted at the speed it can be
  understood. One commit carries one logical change.
- **Living documentation.** A change that alters documented behavior is
  incomplete until the documentation moves with it, in the same commit.
- **Auditability rather than attribution.** The history explains what changed
  and why. It does not record who or what typed it.

## Format

```text
<type>(<scope>): <summary>

<body>

<trailers>
```

- **Subject line.** Imperative mood, lower case after the colon, no trailing
  period, 72 characters or fewer. It completes the sentence "This commit
  will ...".
- **Scope.** Optional. The area touched, such as a module, a document or a
  pipeline stage. Omit it rather than inventing one.
- **Body.** Required for anything that is not trivial. Wrapped at 72 columns.
  It states what changed and, above all, **why** — the constraint, the defect
  or the decision behind the change. What the diff already shows does not need
  to be restated.
- **Trailers.** Optional machine-readable lines at the end.

## Types

| Type       | Use for                                                    |
|------------|------------------------------------------------------------|
| `feat`     | New behavior visible to a user or a caller                 |
| `fix`      | Correction of defective behavior                           |
| `refactor` | Behavior-preserving restructuring                          |
| `perf`     | Change made for performance, behavior preserved            |
| `test`     | Tests, harnesses, fixtures and test data                   |
| `docs`     | Documentation, ADRs and engineering instructions           |
| `build`    | Build system, dependencies, packaging                      |
| `ci`       | Pipelines, quality gates, workflow configuration           |
| `security` | Change made for a security reason                          |
| `chore`    | Repository maintenance with no product effect              |

## Trailers

```text
Refs: <issue or ticket identifier>
ADR: <ADR identifier the change implements or is constrained by>
BREAKING CHANGE: <contract broken and the migration required>
```

A commit that breaks a public contract MUST carry `BREAKING CHANGE:`. A commit
that implements or contradicts an accepted architectural decision SHOULD carry
`ADR:`.

## Rules

Every commit MUST:

1. Be written in **English**.
2. Contain **no emoji**, in any position.
3. Carry **no attribution trailers** — no `Co-Authored-By`, no
   `Generated-with`, no tool signature, no AI marker. Traceability of
   AI-assisted development remains an open question in the framework and is
   not settled by convention in the commit body.
4. Cover **one logical change**. Unrelated fixes are separate commits.
5. Leave the tree in a **verifiable state**. Do not commit a change that is
   known to break the build or the test suite in order to fix it later in the
   same branch.
6. Update the documentation that the change contradicts, in the same commit.
7. Contain **no secrets**: no credentials, tokens, private keys, certificates,
   production endpoints, customer data or personal information. This applies to
   the message as much as to the diff.

Every commit MUST NOT:

1. Use a placeholder subject such as `wip`, `fixes`, `update`, `changes` or
   `misc`.
2. Bundle a mechanical reformat with a behavioral change. Split them.
3. Amend or rewrite a commit that has already been published to a shared
   branch.

## Branch boundary

AI-assisted work happens outside protected shared branches. Commits are made on
`feature/*`, `fix/*`, `refactor/*` or `technical/*` branches and reach a
protected branch only through a Pull Request reviewed by a human.

An AI assistant MUST NOT push to a protected branch, merge into one, approve a
Pull Request or bypass branch protection.

## Examples

Accepted:

```text
docs: record the decision to keep PDF and DOCX as derived artifacts

The Markdown source is the single editable form of the framework. Storing
the generated formats alongside it lets a reviewer read the document without
a conversion toolchain, at the cost of a regeneration step on every edit.

ADR: ADR-0002
```

```text
fix(context-economy): correct the model-fit table row for long-context review

The row stated the opposite recommendation to the surrounding text, which
would have led a reader to select the smaller context window for exactly the
task the section argues against.
```

Rejected:

```text
Update docs                                    <- placeholder subject
docs: added section 21                         <- not imperative, past tense
docs: improve wording of the security section. <- trailing period
feat: nueva seccion de gobernanza              <- not English
docs: polish the executive summary

Co-Authored-By: Claude <noreply@anthropic.com>  <- attribution trailer
```
