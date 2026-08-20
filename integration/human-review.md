---
id: AI-INT-004
title: Human Review
status: proposed
domain: integration
owners:
  - engineering
applies_to:
  - all-changes
related:
  []
source:
  - draft EN202608161000, section 61
  - draft EN202608161000, section 57
---

# Human Review

What a human reviewer is responsible for that no automated check covers, and the place AI review occupies alongside it rather than instead of it.

<!-- nav:start -->
`AI-INT-004` &middot; status **proposed** &middot; domain [`integration/`](./)

**Derived from** &mdash; [section 61. Human Review](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#61-human-review) &middot; [section 57. AI Review as Additional Review](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#57-ai-review-as-additional-review)
<!-- nav:end -->

---

## Human Review

Human review is mandatory.

A reviewer MUST NOT merely confirm that CI is green.

Review SHOULD evaluate:

* Correctness.
* Domain behavior.
* Architectural alignment.
* Security.
* Maintainability.
* Error handling.
* Performance.
* Test quality.
* Complexity.
* Observability.
* Dependency impact.

Particular attention SHOULD be paid to AI-specific failure modes including:

* Invented APIs.
* Hallucinated packages.
* Incorrect library usage.
* Hidden assumptions.
* Security bypasses.
* Missing edge cases.
* Overengineering.
* Incorrect concurrency assumptions.
* Silent behavior changes.
* Tests that merely mirror implementation assumptions.

---

## AI Review as Additional Review

AI code review MAY complement human review.

It MUST NOT replace required human approval.

AI review is useful for:

* Suspicious patterns.
* Missing validation.
* Repetition.
* Potential bugs.
* Documentation inconsistencies.
* Test suggestions.

The human reviewer remains responsible for architectural and domain correctness.
