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

<!-- nav:start -->
`AI-KNOW-001` &middot; status **proposed** &middot; domain [`knowledge/`](./)

**Derived from** &mdash; [section 12. Repository as Engineering Source of Truth](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#12-repository-as-engineering-source-of-truth) &middot; [section 14. README](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#14-readme)
<!-- nav:end -->

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
