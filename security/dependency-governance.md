---
id: AI-SEC-005
title: Dependency Governance
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - all-changes
related:
  []
source:
  - draft EN202608161000, section 24
---

# Dependency Governance

An assistant proposing a dependency is proposing a long-term maintenance and security commitment. This document states who accepts that commitment and on what evidence.

<!-- nav:start -->
`AI-SEC-005` &middot; status **proposed** &middot; domain [`security/`](./)

**Derived from** &mdash; [section 24. Dependency Governance](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#24-dependency-governance)
<!-- nav:end -->

---

AI MUST NOT introduce dependencies simply because a generated answer references them.

Every new dependency SHOULD be validated for:

* Actual existence.
* Correct package identity.
* Maintainer reputation.
* License compatibility.
* Security advisories.
* Maintenance activity.
* Compatibility.
* Necessity.
* Dependency-tree impact.

Typosquatting and hallucinated package names MUST be considered explicit AI-development risks.

Prefer existing project dependencies when they provide the required capability.
