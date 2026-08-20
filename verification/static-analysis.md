---
id: AI-VER-006
title: Static Analysis and Code Quality
status: proposed
domain: verification
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 45
  - draft EN202608161000, section 47
---

# Static Analysis and Code Quality

The properties a machine can check without running the code, and the clean-code expectations that generated output is held to.

<!-- nav:start -->
`AI-VER-006` &middot; status **proposed** &middot; domain [`verification/`](./)

**Derived from** &mdash; [section 45. Static Quality Analysis](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#45-static-quality-analysis) &middot; [section 47. Clean Code Requirements](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#47-clean-code-requirements)
<!-- nav:end -->

---

## Static Quality Analysis

Static analysis SHOULD form part of the mandatory quality boundary.

Where SonarQube is used, the Pull Request MUST satisfy its configured Quality Gate.

Particular emphasis SHOULD be placed on **new code**.

Controls SHOULD include:

* Bugs.
* Vulnerabilities.
* Security hotspots.
* Maintainability.
* Reliability.
* Duplication.
* Complexity.
* Coverage.

Existing legacy debt SHOULD not justify introducing new debt.

---

## Clean Code Requirements

AI-generated code MUST follow the same standards as manually produced code.

Expected characteristics include:

* Small cohesive functions.
* Explicit intent.
* Clear naming.
* Single responsibility.
* Appropriate abstraction.
* Clear domain boundaries.
* Controlled side effects.
* Explicit error handling.
* Dependency inversion where appropriate.
* Minimal duplication.
* No dead code.
* No commented-out code.
* No speculative abstractions.
* No unnecessary dependencies.

Prefer:

> **The simplest design that correctly satisfies the known requirements and existing architecture.**

Avoid speculative architecture generated to solve hypothetical future requirements.
