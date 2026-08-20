---
id: AI-PROF-002
title: Proposed Quality Gate Baselines
status: proposed
domain: profiles
owners:
  - engineering
applies_to:
  - implementation-profile
related:
  []
source:
  - draft EN202608161000, Annex B
---

# Proposed Quality Gate Baselines

The concrete numbers, kept out of the domain documents on purpose so that discussing a coverage percentage does not mean reopening the framework.

<!-- nav:start -->
`AI-PROF-002` &middot; status **proposed** &middot; domain [`profiles/`](../)

**Derived from** &mdash; [Annex B — Proposed Quality Gate Baselines](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#annex-b-%E2%80%94-proposed-quality-gate-baselines)
<!-- nav:end -->

---

Non-normative. These numbers are a **proposed starting baseline**, not a decision. They live here, apart from Part I, precisely so that they can be discussed, adjusted per stack and revised over time without touching the principles.

They would apply to **new code** in the Pull Request, so that existing debt does not block delivery and new debt does not accumulate silently.

| Condition (new code)                | Baseline threshold | Notes |
|-------------------------------------|--------------------|-------|
| New blocker or critical issues      | 0                  | Merge-blocking. |
| New vulnerabilities                 | 0                  | Merge-blocking. |
| Security hotspots reviewed          | 100 %              | Review is a human action. |
| Reliability rating                  | A                  | |
| Security rating                     | A                  | |
| Maintainability rating              | A                  | |
| Duplicated lines                    | ≤ 3 %              | |
| Coverage — .NET, Python             | ≥ 80 %             | Business logic; excludes generated code. |
| Coverage — Angular                  | ≥ 70 %             | Excludes generated and pure-markup files. |
| Coverage — Embedded C/C++           | ≥ 60 %             | Host-testable logic; hardware-coupled code covered by harnesses. |

Coverage appears as a floor rather than a goal: it measures execution, not verification. The mutation-testing and harness sections of Part I are what actually speak to assertion strength.

### What is open here

* Whether the values are right, and whether they should differ per stack or per repository class.
* Whether coverage floors help at all, or whether they mostly produce tests written to satisfy a percentage.
* How existing repositories converge on them without a period of blocked delivery.
* Who owns these numbers and revises them, and how often.

> **Discussion point.** Coverage is the number most likely to be argued about, and rightly so. If the team prefers no numeric floor at the start — measuring and publishing coverage without blocking on it — that is a reasonable position and easy to tighten later.
