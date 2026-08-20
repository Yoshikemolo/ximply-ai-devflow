---
id: AI-AGT-001
title: Human-in-the-Loop: The Engineer's Role
status: proposed
domain: agentic-engineering
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 10
---

# Human-in-the-Loop: The Engineer's Role

Where engineering attention moves when implementation gets cheaper. The role expands rather than shrinks: design and definition before, integration and validation after.

---

In an AI-assisted environment the engineer's centre of gravity moves from producing lines of code to **designing, integrating and validating** them. The role expands; it does not shrink.

```mermaid
flowchart TD
    E1["SOFTWARE ENGINEER (Human)<br/>• Establishes the requirement and acceptance criteria<br/>• Defines architecture and applies existing ADRs<br/>• Defines the test strategy and the behavioural oracles"]
    AI["AI ASSISTANT (Tool)<br/>• Generates atomic functions, structures and test drafts<br/>• Accelerates repetitive and mechanical work"]
    E2["SOFTWARE ENGINEER (Human)<br/>• Integrates the change into the real architecture<br/>• Runs tests, harnesses, static and security analysis<br/>• Reviews the material changes and updates documentation<br/>• Owns the Pull Request and remains accountable for it"]
    G["Automated quality gates"]
    R["Independent human review"]
    I["Integration"]

    E1 -- "context-injected, scoped prompt" --> AI
    AI -- "proposed change, not a decision" --> E2
    E2 --> G --> R --> I
```

### Design and define

The engineer analyses the business objective, defines acceptance criteria, identifies affected components and security impact, and records architecturally significant decisions as ADRs. Prompts are derived from this work; they do not replace it.

### Integrate

Whether AI output arrives as isolated fragments or as a larger proposed change set, the engineer is responsible for how it lands in the platform: global error handling, centralized logging and telemetry conventions, dependency-injection lifetimes, transaction and concurrency semantics, configuration, resource limits and performance budgets.

### Validate

The engineer is the final authority on whether the change is correct. Validation includes interpreting automated results rather than merely observing that they are green, reviewing the material authored changes, and confirming that the change satisfies the acceptance criteria of the originating requirement.

Generated artifacts — scaffolding, lockfiles, generated clients, schemas, snapshots, bulk fixtures — are validated differently: through the generator and its inputs, the contract they implement and the tests that exercise them, rather than by reading every line. What matters is that somebody decided the generator, the inputs and the expected result, and can say why.

> **The engineer who submits the change is the engineer who answers for it.**

> **Discussion point.** The role description above is a proposal about where engineering attention should move, not a redefinition of anyone's job. It is worth checking against how the teams actually work today.
