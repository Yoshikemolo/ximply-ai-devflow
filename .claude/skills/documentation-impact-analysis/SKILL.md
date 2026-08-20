---
name: documentation-impact-analysis
description: Determine whether a change affects documented behaviour, and which documents it would touch, without editing anything. Use when reviewing a diff, a Pull Request or a proposed change; when asked "does this need a doc update"; or as the first step before maintaining documentation. Read-only - it reports impact and stops.
---

# Documentation impact analysis

Given a change, determine whether it affects documented behaviour and which
documents would have to move with it.

**This skill is read-only.** It reports; it does not edit. That separation is
the point: the same analysis has to work during a review, where nothing may be
written, and before maintenance, where something will be. Use
`maintain-engineering-documentation` to act on the result.

## Triggers

Run this analysis whenever a change touches any of:

```text
architecture or module boundaries      security boundaries or authorization
public APIs and contracts              engineering conventions
database schemas and migrations        deployment or release behaviour
observability, logs, metrics           dependencies
AI tooling, prompts or autonomy        testing strategy
documented operational behaviour       anything a document currently describes
```

The last row is the one that catches what the list misses. If a document
states how something behaves and the change makes that statement false, the
change has documentation impact regardless of category.

## Procedure

### 1. Read the actual change

```bash
git diff                    # working tree
git diff --stat main...HEAD # a branch
gh pr diff <number>         # a Pull Request
```

Work from the diff, never from the description of the diff. A commit message
says what the author intended; the diff says what happened.

### 2. Name the concepts, not the files

For each hunk, state what changed in engineering terms: "the authorization
check moved from the gateway to the service", not "12 lines in `auth.ts`". A
file path finds a file; a concept finds a document.

### 3. Find the authoritative documents

Use `navigate-engineering-knowledge`. For each concept, resolve which document
currently states something about it, by identifier.

### 4. Classify each hit

```text
CONTRADICTED   the document now states something untrue. Must be updated.
INCOMPLETE     still true, but silent about the new behaviour. Should be updated.
CITED          constrains the change but needs no edit. Cite it.
UNAFFECTED     matched on a keyword, not on substance. Drop it, do not list it.
```

Dropping the `UNAFFECTED` hits is what makes the report worth reading. A list
of everything that mentions "authentication" is a search result, not an
analysis.

### 5. Check whether the change already carries its documentation

```bash
git diff --name-only main...HEAD | grep -E "\.md$"
```

A change that alters documented behaviour and updates no document is
incomplete - see `knowledge/living-documentation.md`. Say so.

## Output

```text
Documentation impact

CONTRADICTED
  AI-SEC-001  AI Context Boundary
    States that tool credentials never enter agent context. The change passes
    a scoped token through the agent workspace.

INCOMPLETE
  AI-CHG-001  API Changes
    Silent on how a deprecated field is signalled to consumers.

CITED
  AI-PRIN-002  Human Accountability - the change does not alter the boundary.

No documentation change found in this diff.

Recommendation: update AI-SEC-001 and AI-CHG-001, or state explicitly why no
documentation change is required.
```

If there is no impact, say that in one line. A clean result is a useful result.

## Rules

1. **Audit the artifact, not the author.** Write "this change modifies a public
   contract and no corresponding documentation update was found", never "the
   author forgot the documentation". The finding is about the change.
2. **Report, do not edit.** Not even a typo. This skill has no write step.
3. **Do not speculate about intent.** If the diff is ambiguous, say what is
   ambiguous and what would resolve it.
4. **Uncertainty is a finding.** "This may affect AI-SEC-002; I could not
   determine whether the token crosses the boundary" is more useful than a
   confident guess, and far more useful than silence.
5. **No documentation change can be the right answer.** Say so plainly when it
   is. A skill that always finds impact gets ignored.
6. **Cite by identifier.** Every document named in the report is one you opened.

## Do not

- Recommend creating a new document. If something needs saying, an existing
  authoritative document almost always needs updating instead - that judgement
  belongs to `maintain-engineering-documentation`.
- Report a document as affected because a word matched.
- Approve, block or merge anything. This produces a finding, not a verdict.
