---
id: AI-CHG-001
title: API Changes
status: proposed
domain: engineering-changes
owners:
  - engineering
applies_to:
  - public-contracts
related:
  []
source:
  - draft EN202608161000, section 53
---

# API Changes

Playbook for changing a published contract without breaking its consumers.

---

API changes MUST include:

* Implementation.
* Automated tests.
* OpenAPI update where applicable.
* Contract validation.
* Compatibility evaluation.
* Integration documentation.

Breaking API changes SHOULD normally require architectural review and potentially an ADR.
