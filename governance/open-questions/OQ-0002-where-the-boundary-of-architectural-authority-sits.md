---
id: OQ-0002
title: Where the boundary of architectural authority sits
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: What exactly is reserved to human decision?
affects:
  - AI-PRIN-002
  - AI-KNOW-003
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q2 — Where the boundary of architectural authority sits)
---

# OQ-0002 — Where the boundary of architectural authority sits

> What exactly is reserved to human decision?

<!-- nav:start -->
`OQ-0002` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Human Accountability `AI-PRIN-002`](../../principles/human-accountability.md) &middot; [Architecture Decisions and Guardrails `AI-KNOW-003`](../../knowledge/architecture-decisions.md)

**Derived from** &mdash; [Q2 — Where the boundary of architectural authority sits](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q2-%E2%80%94-where-the-boundary-of-architectural-authority-sits)
<!-- nav:end -->

---

## Discussion

The draft proposes that AI may analyse, propose alternatives, challenge a decision, surface conflicts with existing ADRs and draft ADR candidates, but does not hold decision authority. The open part is the operational one: which categories of change require an ADR before implementation begins, and who accepts an ADR in each team.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
