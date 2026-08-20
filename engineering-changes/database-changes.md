---
id: AI-CHG-002
title: Database Changes
status: proposed
domain: engineering-changes
owners:
  - engineering
applies_to:
  - persistence
related:
  []
source:
  - draft EN202608161000, section 54
---

# Database Changes

Playbook for schema and data migration, where assisted work carries irreversible risk.

<!-- nav:start -->
`AI-CHG-002` &middot; status **proposed** &middot; domain [`engineering-changes/`](./)

**Derived from** &mdash; [section 54. Database Changes](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#54-database-changes)
<!-- nav:end -->

---

Database changes MUST include:

* Explicit migration.
* Migration test.
* Migration review.
* Compatibility analysis.
* Rollback consideration.
* Appropriate integration testing.

Production database manipulation MUST remain outside autonomous AI authority.
