---
id: AI-AGT-004
title: Implementation Planning
status: proposed
domain: agentic-engineering
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 25
---

# Implementation Planning

The plan that makes feature-scale assisted work reviewable: decomposition, checkpoints, and an agreed target before generation begins.

---

Before implementation, a task SHOULD identify:

* Functional requirements.
* Acceptance criteria.
* Affected components.
* Relevant ADRs.
* Security impact.
* Required tests.
* Documentation impact.
* API impact.
* Persistence impact.
* Migration impact.
* Performance impact.
* Observability impact.
* Compatibility requirements.

Significant changes SHOULD have an implementation plan:

```text
/docs/implementation/<ticket-id>-implementation-plan.md
```

The plan SHOULD describe:

1. Problem.
2. Proposed solution.
3. Components affected.
4. Expected data flow.
5. API changes.
6. Persistence changes.
7. Security considerations.
8. Failure scenarios.
9. Test strategy.
10. Deployment/migration concerns.
11. Rollback approach.
