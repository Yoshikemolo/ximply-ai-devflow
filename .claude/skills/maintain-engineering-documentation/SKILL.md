---
name: maintain-engineering-documentation
description: Update the framework corpus so it stays true after a change - editing the right existing document, keeping front matter and relationships correct, and re-running the generators and gate. Use when documentation must be written or corrected, when a change altered documented behaviour, or when asked to add, move or restructure a document in this repository.
---

# Maintain engineering documentation

Keep the corpus true. Documentation that contradicts reality is a defect, and
this is the procedure for fixing it without creating a worse one.

The characteristic failure of an assistant here is not laziness. It is
enthusiasm: writing a new document because one seemed missing, and leaving the
corpus with two documents that will eventually disagree.

## The rule that matters most

> **Do not create a new document if an existing authoritative document should
> be updated instead.**

Before writing anything new, find what already covers the subject. Creating a
document is justified only when the subject genuinely has no home and would
distort whatever document it were forced into. If in doubt, update.

Equally: **no statement lives in two places.** If two documents need the same
fact, one states it and the other links to it.

## Procedure

### 1. Establish the impact first

Run `documentation-impact-analysis`. Do not update a document because it looks
related; update it because the analysis says it is contradicted or incomplete.

### 2. Edit the smallest thing that makes it true

Change the sentence that is now false. Resist rewriting the surrounding
section, restructuring the document, or improving prose you were not sent to
improve - that turns a reviewable correction into a diff nobody can check.

### 3. Keep the front matter true

Front matter is not decoration; the gate reads it and other documents resolve
against it.

```yaml
id:          stable, never changes, never reused
title:       what the document is
status:      proposed | accepted | deprecated | superseded | rejected
domain:      must equal the directory the file is in
owners:      who answers for it
applies_to:  scope tag - where it bites
related:     identifiers this document links to
source:      where in the trunk document it came from
```

Open questions under `governance/open-questions/` use `OQ-NNNN`, carry
`question`, `opened` and `affects`, and take their status from `open`,
`answered`, `deferred`, `withdrawn`, `superseded`.

If you add a link to another document, add its identifier to `related`. If you
remove the link, remove the identifier.

### 4. Never hand-edit generated content

The block between `<!-- nav:start -->` and `<!-- nav:end -->` is derived from
front matter. Change the front matter, then regenerate:

```bash
python tools/render_headers.py
```

`compiled/` is a frozen snapshot, not a source. Never edit it. See `AI-DEC-003`.

### 5. Validate before committing

```bash
python tools/check_corpus.py
python tools/render_headers.py --check
python tools/split_framework.py --check
```

All three must pass. If one fails, fix the cause - never work around the gate.

### 6. Report what moved

Say which documents changed, by identifier, and which you decided not to
change and why. The second half is the part a reviewer cannot reconstruct.

## Moving or adding a document

Adding one:

1. Choose the domain by the question it answers, not by keyword.
2. Take the next free number in that domain's prefix.
3. Link it from an index, or from a document reachable from `README.md` - the
   gate fails on a document nothing points at, and rightly: a document that
   cannot be found cannot be retrieved.
4. Regenerate headers, run the gate.

Moving one between domains changes its identifier prefix, which breaks every
citation of it. That is a substantive change: open a decision record first,
per `CONTRIBUTING.md`.

## Rules

1. **Update, do not duplicate.** Restated above because it is the one an
   assistant breaks.
2. **One logical change per commit.** Split a restructure from a rewording.
3. **Editorial or substantive.** A correction goes straight to a Pull Request.
   Anything that changes what the framework asks for opens a decision record
   first - use `manage-engineering-decisions` when it exists, or follow
   `governance/decision-process.md`.
4. **Do not change `status` casually.** Moving a document from `proposed` to
   `accepted` claims a consensus. Only a decision record does that.
5. **Preserve the discussion points.** A passage marked
   `> **Discussion point.**` is a provisional position deliberately left
   arguable. Do not smooth it into apparent agreement.
6. **English, no emoji**, and commits per `docs/ai/commits.md`.
7. **Never invent a fact about the trunk document.** If a `source` entry needs
   changing, verify it against `compiled/` rather than reasoning about it.

## Do not

- Create a document to avoid the harder work of editing one.
- Copy a paragraph between documents. Link instead.
- Edit the navigation block, `compiled/`, or anything else that is generated.
- Use `--force` on the split tools. After the source inversion they destroy
  edits rather than build anything.
- Mark a question answered without an accepted decision record behind it.
