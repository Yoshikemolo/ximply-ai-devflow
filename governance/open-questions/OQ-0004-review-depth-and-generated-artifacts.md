---
id: OQ-0004
title: Review depth and generated artifacts
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: What must be read line by line, and what is validated differently?
affects:
  - AI-PRIN-003
  - AI-INT-004
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q4 — Review depth and generated artifacts)
---

# OQ-0004 — Review depth and generated artifacts

> What must be read line by line, and what is validated differently?

<!-- nav:start -->
`OQ-0004` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Evidence and Verification `AI-PRIN-003`](../../principles/evidence-and-verification.md) &middot; [Human Review `AI-INT-004`](../../integration/human-review.md)

**Derived from** &mdash; [Q4 — Review depth and generated artifacts](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q4-%E2%80%94-review-depth-and-generated-artifacts)
<!-- nav:end -->

---

## Discussion

The draft distinguishes material authored changes, which are reviewed and must be explainable, from generated artifacts — scaffolding, lockfiles, generated clients, schemas, snapshots, bulk fixtures — which are validated through their generator, their input contract and their tests. The open question is where the line falls for each stack, and how the review checklist should express it without becoming a formality.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
