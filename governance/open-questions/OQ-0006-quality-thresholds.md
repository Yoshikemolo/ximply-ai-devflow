---
id: OQ-0006
title: Quality thresholds
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: Which numbers, and who owns them?
affects:
  - AI-INT-005
  - AI-PROF-002
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q6 — Quality thresholds)
---

# OQ-0006 — Quality thresholds

> Which numbers, and who owns them?

<!-- nav:start -->
`OQ-0006` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Automated Quality Gates and CI Pipeline `AI-INT-005`](../../integration/quality-gates.md) &middot; [Proposed Quality Gate Baselines `AI-PROF-002`](../../profiles/quality-gates/baselines.md)

**Derived from** &mdash; [Q6 — Quality thresholds](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q6-%E2%80%94-quality-thresholds)
<!-- nav:end -->

---

## Discussion

Coverage percentages, duplication limits and rating requirements are in [Annex B](../../profiles/quality-gates/baselines.md) precisely so that they can be discussed and changed without reopening the standard. The questions are the values themselves, whether they differ per stack or per repository class, whether they apply to new code only, and how existing repositories converge without blocking delivery.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
