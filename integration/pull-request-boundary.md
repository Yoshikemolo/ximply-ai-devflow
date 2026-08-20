---
id: AI-INT-003
title: Pull Request Boundary
status: proposed
domain: integration
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 58
  - draft EN202608161000, section 59
  - draft EN202608161000, section 60
---

# Pull Request Boundary

The Pull Request is the principal integration quality boundary: what a change must satisfy to be considered for acceptance, and what its author declares.

---

## Pull Request Boundary

Every change entering a protected shared development branch MUST use a Pull Request.

Direct pushes SHOULD be technically disabled.

The Pull Request is the principal integration quality boundary.

---

## Pull Request Acceptance Criteria

A Pull Request may be merged only when all applicable criteria are satisfied:

* Code builds.
* Required tests pass.
* Integration tests pass.
* Contract tests pass where required.
* Harnesses pass.
* Static analysis passes.
* SonarQube Quality Gate passes where applicable.
* Security checks pass.
* No secrets are introduced.
* Documentation is updated.
* ADRs are updated if architecture changed.
* OpenAPI is updated if contracts changed.
* Database migrations are reviewed.
* Observability impact is considered.
* Compatibility is evaluated.
* Ticket acceptance criteria are verified.
* Human review is complete.

---

## Pull Request Checklist

```text
[ ] AI assistance declared (scope and human owner)
[ ] Material authored changes reviewed and explainable by the author
[ ] Generated artifacts identified and validated by generator, contract or tests
[ ] Requirement implemented
[ ] Acceptance criteria verified
[ ] Architecture respected
[ ] Relevant ADRs reviewed
[ ] Unit tests added or updated
[ ] Integration tests added or updated
[ ] Contract tests added where applicable
[ ] E2E tests added where applicable
[ ] Security cases considered
[ ] Tests pass
[ ] Required harnesses pass
[ ] Quality Gate passes
[ ] No credentials or secrets introduced
[ ] New dependencies reviewed
[ ] Documentation updated
[ ] README updated if required
[ ] API documentation updated if required
[ ] Database migration reviewed
[ ] Observability reviewed
[ ] Compatibility reviewed
[ ] Human code review complete
```

The checklist would be automated wherever possible rather than depending on developer memory. It is also long: part of the review is deciding which items earn their place and which are ceremony.
