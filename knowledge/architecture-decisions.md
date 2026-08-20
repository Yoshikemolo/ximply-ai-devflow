---
id: AI-KNOW-003
title: Architecture Decisions and Guardrails
status: proposed
domain: knowledge
owners:
  - engineering
applies_to:
  - software-repositories
related:
  []
source:
  - draft EN202608161000, section 15
  - draft EN202608161000, section 16
---

# Architecture Decisions and Guardrails

How architectural decisions are recorded so they can be cited, superseded and checked against, and what an assistant must inspect before changing a system. AI may draft a decision; it may not accept one.

<!-- nav:start -->
`AI-KNOW-003` &middot; status **proposed** &middot; domain [`knowledge/`](./)

**Derived from** &mdash; [section 15. Architecture Decision Records](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#15-architecture-decision-records) &middot; [section 16. Architecture Guardrails](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#16-architecture-guardrails)
<!-- nav:end -->

---

## Architecture Decision Records

Significant architectural decisions MUST be recorded under:

```text
/ADR
```

An ADR SHOULD contain:

```text
Title
Status
Date
Owners

Context
Problem
Decision
Alternatives Considered
Decision Drivers
Consequences
Security Impact
Operational Impact
Performance Impact
Migration Impact
Observability Impact
Superseded Decisions
References
```

Supported statuses SHOULD include:

```text
Proposed
Accepted
Deprecated
Superseded
Rejected
```

Architectural decisions MUST NOT exist exclusively in:

* AI conversations.
* Chat systems.
* Emails.
* Meeting conversations.
* Developer memory.
* Temporary notes.

AI MAY draft an ADR.

AI MUST NOT accept an ADR.

Architectural authority remains human.

---

## Architecture Guardrails

Before modifying a system, the engineer and AI assistant SHOULD inspect:

1. `README.md`.
2. Relevant architecture documentation.
3. Relevant ADRs.
4. Existing implementation.
5. Existing tests.
6. Public contracts.
7. Domain models.
8. Security constraints.

The AI MUST NOT silently introduce:

* A new architectural pattern.
* A new persistence strategy.
* A new message transport.
* A new authentication mechanism.
* A new authorization model.
* A new dependency injection strategy.
* A new major framework.
* A new cross-cutting abstraction.

When implementation conflicts with an accepted ADR, the conflict MUST be resolved before proceeding.
