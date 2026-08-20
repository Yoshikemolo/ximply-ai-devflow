---
id: OQ-0007
title: Enforcement and exceptions
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: How strict should the integration boundary be at the start?
affects:
  - AI-GOV-002
  - AI-INT-005
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q7 — Enforcement and exceptions)
---

# OQ-0007 — Enforcement and exceptions

> How strict should the integration boundary be at the start?

<!-- nav:start -->
`OQ-0007` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Compliance and Exceptions `AI-GOV-002`](../compliance-and-exceptions.md) &middot; [Automated Quality Gates and CI Pipeline `AI-INT-005`](../../integration/quality-gates.md)

**Derived from** &mdash; [Q7 — Enforcement and exceptions](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q7-%E2%80%94-enforcement-and-exceptions)
<!-- nav:end -->

---

## Discussion

The draft proposes preventive controls, audited administrative bypass and time-bounded exceptions. There is a real trade-off: strong preventive enforcement gives consistency but can block delivery in edge cases, while a lighter model depends on discipline. A staged tightening, starting with visibility and moving to blocking checks, is one option.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
