---
id: OQ-0005
title: Granularity of AI traceability
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: Is a yes/no declaration still meaningful?
affects:
  - AI-GOV-003
  - AI-PROF-003
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q5 — Granularity of AI traceability)
---

# OQ-0005 — Granularity of AI traceability

> Is a yes/no declaration still meaningful?

<!-- nav:start -->
`OQ-0005` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [AI Contribution Traceability `AI-GOV-003`](../ai-traceability.md) &middot; [Draft Pull Request Declaration `AI-PROF-003`](../../profiles/pull-request/declaration.md)

**Derived from** &mdash; [Q5 — Granularity of AI traceability](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q5-%E2%80%94-granularity-of-ai-traceability)
<!-- nav:end -->

---

## Discussion

If most development carries some degree of assistance within a couple of years, a boolean loses its information value. The alternative in the draft is to record the kind of intervention that actually matters for risk — substantial agent-generated change, generated tests, generated synthetic data, assisted migration, assisted security-sensitive code — rather than assistance in general. This needs agreement on the categories before it is put into a Pull Request template, otherwise it becomes noise that everybody ticks.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
