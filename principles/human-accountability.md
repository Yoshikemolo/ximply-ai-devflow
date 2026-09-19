---
id: AI-PRIN-002
title: Human Accountability
status: accepted
domain: principles
owners:
  - engineering
applies_to:
  - all-changes
related:
  - AI-AGT-003
  - AI-GOV-002
  - AI-GOV-006
  - AI-INT-004
source:
  - draft EN202608161000, section 8 (8.1 Human ownership; 8.2 Human-controlled integration)
  - draft EN202608161000, section 9
---

# Human Accountability

Who answers for a change, and which decisions are not delegable. This document draws the line between what an AI system may contribute and what only an accountable engineer may decide.

<!-- nav:start -->
`AI-PRIN-002` &middot; status **accepted** &middot; domain [`principles/`](./)

**Related** &mdash; [Local Models and Organization-Owned Agentic Tooling `AI-AGT-003`](../agentic-engineering/local-and-corporate-agents.md) &middot; [Compliance and Exceptions `AI-GOV-002`](../governance/compliance-and-exceptions.md) &middot; [Open Questions `AI-GOV-006`](../governance/open-questions.md) &middot; [Human Review `AI-INT-004`](../integration/human-review.md)

**Derived from** &mdash; [8.1 Human ownership](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#81-human-ownership) &middot; [8.2 Human-controlled integration](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#82-human-controlled-integration) &middot; [section 9. Operational Boundaries: Where AI Fits and Where It Should Not Decide](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#9-operational-boundaries-where-ai-fits-and-where-it-should-not-decide)
<!-- nav:end -->

---

## Human ownership

Every code change MUST have an identifiable human owner.

The human owner remains accountable for:

* The requirement.
* The technical solution.
* Architectural alignment.
* Security implications.
* Test adequacy.
* Documentation.
* Publication of the change.
* Pull Request submission.
* Acceptance of review comments.
* Final integration.

AI assistance does not transfer accountability.

---

## Human-controlled integration

AI MUST NOT independently:

* Approve a Pull Request.
* Merge a Pull Request.
* Promote code to a shared development branch.
* Promote code to a release branch.
* Release software.
* Deploy software to production.
* Disable a quality gate.
* Override branch protection.
* Suppress security controls.
* Decide that a failed mandatory check can be ignored.

The decision that software is ready for integration always belongs to an authorized human engineer.

---

## Operational Boundaries: Where AI Fits and Where It Should Not Decide

This section sketches the practical envelope of AI-assisted development. It is the part of the proposal most likely to need adjustment from experience, and is offered on that basis.

### Uses proposed as unproblematic

The following uses seem safe for all teams, subject to the review, testing and security expectations described in the rest of Part I:

* **Boilerplate and scaffolding** — standard code structures, DTOs, mappers, configuration files and project skeletons that follow existing project conventions.
* **Test construction support** — repetitive test setup, fixtures, mocks and parameterized cases derived from human-defined business rules and acceptance criteria.
* **Legacy comprehension** — explaining undocumented legacy code, dense regular expressions, low-level bitwise operations, build scripts or unfamiliar framework behaviour.
* **Syntactic translation** — porting isolated helper functions or data-transformation scripts between languages (for example, converting a shell automation routine into a maintainable Python script).
* **Documentation drafting** — docstrings, README structure, `/docs` pages, changelog entries and initial API descriptions, subject to human factual verification.
* **Refactoring assistance** — mechanical, behaviour-preserving transformations protected by existing regression tests.
* **Review assistance** — a non-authoritative additional review pass, as defined in [the section on AI review](../integration/human-review.md).
* **Analysis and options** — explaining trade-offs, drafting ADR candidates, proposing test scenarios and identifying risks for human decision.

### Proposed hard limits

The following are put forward as the short list of things that should hold regardless of tool, model, vendor, autonomy level or deadline pressure. The question for review is whether this list is correctly drawn and whether it is complete — a long list of prohibitions tends to be ignored, so it is deliberately short.

* **Architectural decision authority.** AI MUST NOT hold architectural decision authority. Service boundaries, persistence strategy, state-management paradigm, authentication and authorization models, messaging topology and comparable choices are accepted by the accountable engineers and recorded as ADRs.

  This is a limit on *authority*, not on contribution. AI is often genuinely good at the work that precedes the decision, and the proposal encourages using it there: identifying alternatives, challenging a proposed design, analysing trade-offs, surfacing consequences nobody had considered, detecting that a change conflicts with an existing ADR, and drafting an ADR candidate for humans to argue over. AI proposes; the team decides.
* **Secret and personal-data ingestion.** Real API keys, tokens, cryptographic material, certificates, connection strings, production configuration, production data extracts and real customer personal data MUST NOT be entered into any AI prompt, tool context, agent workspace or attachment. Sanitized or synthetic equivalents MUST be used instead.
* **Unreviewed execution and integration.** AI tooling MUST NOT be wired into pipelines that perform automatic merges, automatic releases, automatic deployments or automatic changes to protected branches, quality gates or infrastructure without human-in-the-loop approval.
* **Delegation of accountability.** "The AI generated it this way" would not be an acceptable explanation for a defect, vulnerability, outage or architectural regression. The human owner of the change remains accountable for its content.
* **Use of unapproved tools and models.** Only AI tools and providers approved by the organization, under the applicable data-handling terms, may be used for work on organizational code, data or documentation. Approval is a property of the deployment, not only of the vendor; [Local Models and Organization-Owned Agentic Tooling](../agentic-engineering/local-and-corporate-agents.md) describes the internally hosted option, which is the preferred one for proprietary context.
* **Bypassing controls.** AI MUST NOT be used to generate code, configuration or scripts whose purpose is to weaken, disable or circumvent branch protection, quality gates, security scanning, licensing controls or audit logging.

### Handling a boundary conflict

When a task appears to require crossing one of these limits, the suggested response is to stop and escalate to the accountable owner rather than quietly reduce the control. Exceptions would be explicit, owned and time-bounded, as described in [the proposed compliance model](../governance/compliance-and-exceptions.md).

> **Discussion point.** Two things are worth arguing about here: whether the "unproblematic" list is too conservative for the tooling the teams actually use, and whether the hard limits are drawn at the right level of abstraction. See also [[the open questions](../governance/open-questions.md) at the end of Part I](../governance/open-questions.md).
