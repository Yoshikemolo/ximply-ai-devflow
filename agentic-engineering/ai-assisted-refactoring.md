---
id: AI-AGT-006
title: AI-Assisted Refactoring
status: proposed
domain: agentic-engineering
owners:
  - engineering
applies_to:
  - all-changes
related:
  []
source:
  - draft EN202608161000, section 55
---

# AI-Assisted Refactoring

Behaviour-preserving transformation is among the strongest uses of assistance, and it depends entirely on the regression tests that protect it.

<!-- nav:start -->
`AI-AGT-006` &middot; status **proposed** &middot; domain [`agentic-engineering/`](./)

**Derived from** &mdash; [section 55. AI-Assisted Refactoring](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#55-ai-assisted-refactoring)
<!-- nav:end -->

---

AI is particularly effective at systematic refactoring, but refactoring MUST preserve behavior unless requirements explicitly change.

Before significant refactoring:

1. Establish or verify regression tests.
2. Identify behavioral invariants.
3. Perform small changes.
4. Re-run tests after each meaningful step.
5. Inspect the resulting diff.

A large AI rewrite without behavioral protection SHOULD NOT be accepted as routine refactoring.
