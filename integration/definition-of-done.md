---
id: AI-INT-006
title: Definition of Done
status: proposed
domain: integration
owners:
  - engineering
applies_to:
  - all-changes
related:
  []
source:
  - draft EN202608161000, section 65
---

# Definition of Done

Code generation is not completion. Verified behaviour is the deliverable.

---

Code generation is not completion.

A task is complete when all applicable deliverables are complete:

```mermaid
flowchart LR
    R["Requirement"] --> DONE["Task complete"]
    I["Implementation"] --> DONE
    T["Tests"] --> DONE
    D["Validated test data"] --> DONE
    DOC["Documentation"] --> DONE
    SEC["Security validation"] --> DONE
    QG["Quality gates"] --> DONE
    HR["Human review"] --> DONE
    AV["Acceptance verification"] --> DONE
```

Therefore:

> **Code alone is never the deliverable. Verified behavior is the deliverable.**
