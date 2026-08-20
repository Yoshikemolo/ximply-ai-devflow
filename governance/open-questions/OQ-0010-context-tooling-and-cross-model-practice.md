---
id: OQ-0010
title: Context tooling and cross-model practice
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: What do we invest in, and what stays discretionary?
affects:
  - AI-FND-003
  - AI-AGT-002
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q10 — Context tooling and cross-model practice)
---

# OQ-0010 — Context tooling and cross-model practice

> What do we invest in, and what stays discretionary?

<!-- nav:start -->
`OQ-0010` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Context Economy `AI-FND-003`](../../ai-foundations/context-economy.md) &middot; [Context-Informed Prompting Protocol `AI-AGT-002`](../../agentic-engineering/context-informed-prompting.md)

**Derived from** &mdash; [Q10 — Context tooling and cross-model practice](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q10-%E2%80%94-context-tooling-and-cross-model-practice)
<!-- nav:end -->

---

## Discussion

Two items from [the context-economy section](../../ai-foundations/context-economy.md) need a decision rather than a recommendation: whether we build or adopt a structural index — a symbol and call graph, or a ranked repository map — for the main codebases, and whether confronting output across different models becomes an expected step for architectural and security-relevant work or is left to each engineer. The first has a cost and an owner; the second has a token cost and only pays off where the decision matters.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
