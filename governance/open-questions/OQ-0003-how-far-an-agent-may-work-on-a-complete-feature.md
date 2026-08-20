---
id: OQ-0003
title: How far an agent may work on a complete feature
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: Is feature-scale agent work acceptable when it is planned and checkpointed?
affects:
  - AI-FND-004
  - AI-AGT-004
  - AI-AGT-005
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q3 — How far an agent may work on a complete feature)
---

# OQ-0003 — How far an agent may work on a complete feature

> Is feature-scale agent work acceptable when it is planned and checkpointed?

<!-- nav:start -->
`OQ-0003` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [AI Autonomy Levels `AI-FND-004`](../../ai-foundations/autonomy-levels.md) &middot; [Implementation Planning `AI-AGT-004`](../../agentic-engineering/implementation-planning.md) &middot; [Small-Batch AI Development `AI-AGT-005`](../../agentic-engineering/small-batch-development.md)

**Derived from** &mdash; [Q3 — How far an agent may work on a complete feature](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q3-%E2%80%94-how-far-an-agent-may-work-on-a-complete-feature)
<!-- nav:end -->

---

## Discussion

The draft says yes, provided the work is decomposed, a plan exists, checkpoints are verified and the human controls the result; what it rules out is a single unconstrained generation step accepted wholesale. The question for review is what a "checkpoint" needs to be in practice, and whether [the autonomy levels in this document](../../ai-foundations/autonomy-levels.md) map cleanly onto the agent tooling the teams actually use.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
