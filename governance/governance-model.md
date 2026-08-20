---
id: AI-GOV-001
title: Engineering Governance Model
status: proposed
domain: governance
owners:
  - engineering
applies_to:
  - this-corpus
related:
  []
source:
  - draft EN202608161000, section 69
---

# Engineering Governance Model

Who owns the framework, who may change it, and how authority is distributed.

---

The final control flow is:

```mermaid
flowchart TD
    subgraph HUMAN["Human framing"]
        direction LR
        G1["Business requirement"] --> G2["Human ownership"] --> G3["Architecture and security context"] --> G4["Acceptance criteria"] --> G5["Independent test strategy"]
    end

    subgraph WORK["AI-assisted engineering"]
        direction LR
        G6["AI-assisted engineering"]
    end

    subgraph AUTO["Automated verification"]
        direction LR
        G7["Automated verification"] --> G8["Security verification"] --> G9["Supply-chain verification"] --> G10["Documentation validation"]
    end

    subgraph BOUNDARY["Human-controlled integration"]
        direction LR
        G11["Human review"] --> G12["Pull Request"] --> G13["Protected CI"] --> G14["Human approval"] --> G15["Integration"] --> G16["Release process"]
    end

    HUMAN --> WORK --> AUTO --> BOUNDARY
```

At no point does AI independently cross a software governance boundary.
