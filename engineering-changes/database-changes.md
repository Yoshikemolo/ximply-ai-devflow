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

---

Database changes MUST include:

* Explicit migration.
* Migration test.
* Migration review.
* Compatibility analysis.
* Rollback consideration.
* Appropriate integration testing.

Production database manipulation MUST remain outside autonomous AI authority.
