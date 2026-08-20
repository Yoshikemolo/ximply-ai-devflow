---
id: AI-DEC-003
title: Invert the source of truth from the document to the corpus
status: accepted
created: 2026-08-20
owners:
  - jorge-rodriguez
supersedes: []
related:
  - AI-KNOW-001
  - AI-KNOW-002
  - AI-DEC-001
---

# Context

AI-DEC-001 produced fifty domain documents derived from the draft. That leaves
two texts saying the same thing, which is the precondition for them saying
different things. One of them has to be authoritative.

The draft is not disposable. It is the artifact that made the discussion
possible, it reads end to end in a way the corpus does not, and it is the form
in which the framework can be handed to someone outside engineering.

# Options considered

1. **Keep the draft authoritative, regenerate the corpus from it.** The corpus
   stays a view. Every discussion still edits one large file, so the problem
   AI-DEC-001 set out to solve returns intact.
2. **Delete the draft.** Removes the ambiguity at the cost of the only readable
   end-to-end form of the framework, and of its history.
3. **Invert the derivation.** The corpus becomes the editable source; the draft
   is frozen as a snapshot and later regenerated from the corpus as a compiled
   view.

# Decision

Option 3.

The draft moves to `compiled/` and is frozen at revision EN202608161000. The
domain documents are now the source. `tools/split_framework.py` refuses to
overwrite existing corpus documents without `--force`, because after this
inversion running it is a destructive act rather than a build step.

The compile step that regenerates the document from the corpus does not exist
yet. Until it does, `compiled/` holds a snapshot, not an output.

# Evidence

The framework's own position: the repository contains the authoritative
account, and documentation that contradicts the implementation is a defect.
Two copies of the same text with no declared direction of derivation is that
defect waiting to happen.

# Consequences

Between now and the compile step, the draft under `compiled/` will drift out of
date. It is labelled as a snapshot rather than kept accurate, and anyone
reading it is reading the state of 2026-08-20.

The DOCX and PDF cannot be regenerated faithfully without deciding on a
toolchain, which is not yet chosen. Building it is now on the critical path for
anyone who needs to circulate the framework outside the repository.

`tools/split_framework.py` becomes provenance rather than a build tool. It is
kept because it makes the split checkable against the draft, and it is
explicitly documented as retiring once the compile step exists.
