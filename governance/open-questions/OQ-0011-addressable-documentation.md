---
id: OQ-0011
title: Addressable documentation
status: open
domain: governance
opened: 2026-08-20
owners:
  - engineering
question: Is it worth giving every documentation piece a stable identifier?
affects:
  - AI-KNOW-005
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 71 (Q11 — Addressable documentation)
---

# OQ-0011 — Addressable documentation

> Is it worth giving every documentation piece a stable identifier?

<!-- nav:start -->
`OQ-0011` &middot; status **open** &middot; domain [`governance/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../open-questions.md)

**Would change** &mdash; [Addressable Knowledge `AI-KNOW-005`](../../knowledge/addressable-knowledge.md)

**Derived from** &mdash; [Q11 — Addressable documentation](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#q11-%E2%80%94-addressable-documentation)
<!-- nav:end -->

---

## Discussion

The conceptual-architecture section sketches identifiers such as `ADR-0042` or `SEC-0017`, with relations like `supersedes` and `applies-to`, turning the documentation set into a versioned knowledge graph that both agents and Pull Requests can cite precisely. The open part is whether the discipline is worth its cost: an identifier scheme is cheap to start, useful only if maintained, and awkward to abandon once things reference each other. It also needs an owner, a numbering convention and a decision about what to do with the documents that already exist.

## How this closes

A decision record under [`decisions/`](../../decisions/), accepted by the
people it applies to, with the affected documents updated in the same change.

Until then this question is `open`, and any provisional position above is a
reading aid rather than an answer.
