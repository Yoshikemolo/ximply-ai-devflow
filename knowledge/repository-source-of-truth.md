---
id: AI-KNOW-001
title: Repository as Engineering Source of Truth
status: proposed
domain: knowledge
owners:
  - engineering
applies_to:
  - software-repositories
related:
  []
source:
  - draft EN202608161000, section 12
  - draft EN202608161000, section 14
---

# Repository as Engineering Source of Truth

The authoritative account of a system lives in its repository, not in conversations, tickets or memory. This is the first link of the conceptual chain: without it there is nothing authoritative to retrieve.

---

## Repository as Engineering Source of Truth

The repository MUST contain sufficient authoritative information for both developers and AI systems to understand the software.

Recommended structure:

```text
/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
│
├── docs/
│   ├── architecture/
│   ├── implementation/
│   ├── testing/
│   ├── security/
│   ├── operations/
│   ├── integration/
│   └── ai/
│
├── ADR/
│
├── src/
├── tests/
├── harness/
├── scripts/
├── tools/
│
├── test-data/
│   ├── fixtures/
│   ├── generators/
│   └── schemas/
│
└── .github/
    └── workflows/
```

The repository SHOULD explain:

* What the system does.
* Its architecture.
* Domain boundaries.
* How it is built.
* How it is tested.
* How it is executed locally.
* How it is deployed.
* Security assumptions.
* External integrations.
* Observability conventions.
* Architectural decisions.
* Engineering constraints.
* AI development rules.

---

## README

The root `README.md` MUST remain the entry point for engineers.

It SHOULD contain:

* Product purpose.
* Architecture summary.
* Repository structure.
* Local setup.
* Build instructions.
* Test execution.
* Required tooling.
* Runtime requirements.
* Configuration.
* Development workflow.
* Links to `/docs`.
* Links to `/ADR`.
* Links to `CONTRIBUTING.md`.
* Quality expectations.

Detailed explanations belong in `/docs`.
