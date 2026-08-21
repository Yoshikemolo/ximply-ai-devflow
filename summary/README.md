# Framework Map

> This document is a navigation and executive-summary layer. It does not replace the authoritative, version-controlled documentation in the repository.

> Authoritative knowledge lives in the structured source documents. Summaries and compiled views are derived navigation aids and must never introduce requirements or decisions of their own.

---

## What this framework is for

This document proposes the engineering practices that would govern software development assisted by Artificial Intelligence. It is a draft for engineering review: the practices below are put forward for discussion, not issued as rules.

The proposal treats AI systems as **engineering assistants operating within explicitly defined boundaries**.

> **AI may accelerate engineering work. It must never lower the engineering standard required to accept that work.**

Everything here is `proposed` and nothing is in force. See [Purpose, Scope and Normative Language `AI-PRIN-000`](../principles/purpose-and-scope.md).

## One chain

Each link depends on the one before it, which is why weakening any of them quietly weakens the rest:

`Repository as source of truth` &rarr; `Living documentation` &rarr; `Context economy` &rarr; `Selective retrieval` &rarr; `Minimum necessary context` &rarr; `IP protection` &rarr; `Internal agent and MCP layer`

## The seven principles

1. AI accelerates implementation; humans retain accountability.
2. Repository documentation and ADRs define authoritative engineering context.
3. AI receives minimum necessary context and minimum necessary permissions.
4. Generated implementation must be independently verifiable.
5. Tests, synthetic data and harnesses are engineering assets, not disposable generated output.
6. Automated quality and security controls protect the integration boundary.
7. Only humans decide when software is ready to cross that boundary.

Stated in full in [Engineering Principles `AI-PRIN-001`](../principles/engineering-principles.md), with accountability in [Human Accountability `AI-PRIN-002`](../principles/human-accountability.md) and evidence in [Evidence and Verification `AI-PRIN-003`](../principles/evidence-and-verification.md).

---

## The map

### Foundations

*What are we actually governing?*

What these systems can and cannot be relied on to do, and the failure modes that the controls elsewhere in the corpus exist to catch. Agreeing on this precedes arguing about thresholds.

[`ai-foundations/`](../ai-foundations/) &mdash; 4 documents &middot; [AI Capability Model `AI-FND-001`](../ai-foundations/capability-model.md) &middot; [Agentic Bias `AI-FND-002`](../ai-foundations/agentic-bias.md) &middot; [Context Economy `AI-FND-003`](../ai-foundations/context-economy.md) &middot; [AI Autonomy Levels `AI-FND-004`](../ai-foundations/autonomy-levels.md)

### Knowledge

*How does engineering knowledge stay true and findable?*

The authoritative account of a system lives in its repository, not in conversations, tickets or memory. This is the first link of the conceptual chain: without it there is nothing authoritative to retrieve.

[`knowledge/`](../knowledge/) &mdash; 5 documents &middot; [Repository as Engineering Source of Truth `AI-KNOW-001`](../knowledge/repository-source-of-truth.md) &middot; [Living Documentation `AI-KNOW-002`](../knowledge/living-documentation.md) &middot; [Architecture Decisions and Guardrails `AI-KNOW-003`](../knowledge/architecture-decisions.md) &middot; [Addressable Knowledge `AI-KNOW-005`](../knowledge/addressable-knowledge.md)

### Security

*What may an agent know, and what may it do?*

What an agent is allowed to know. Minimum required context is both an accuracy control and the principal preventive control against cumulative exposure.

[`security/`](../security/) &mdash; 7 documents &middot; [AI Context Boundary `AI-SEC-001`](../security/ai-context-boundary.md) &middot; [Agentic Security Boundary `AI-SEC-002`](../security/agentic-security-boundary.md) &middot; [Shell and Tool Execution `AI-SEC-003`](../security/tool-execution.md)

### Agentic engineering

*How do we work with agents in practice?*

Where engineering attention moves when implementation gets cheaper. The role expands rather than shrinks: design and definition before, integration and validation after.

[`agentic-engineering/`](../agentic-engineering/) &mdash; 6 documents &middot; [Human-in-the-Loop: The Engineer's Role `AI-AGT-001`](../agentic-engineering/human-in-the-loop.md) &middot; [Context-Informed Prompting Protocol `AI-AGT-002`](../agentic-engineering/context-informed-prompting.md) &middot; [Small-Batch AI Development `AI-AGT-005`](../agentic-engineering/small-batch-development.md)

### Verification

*What counts as proof that generated code is correct?*

The AI-specific rule: what checks the work must not be what produced it. This is the operational consequence of agentic bias.

[`verification/`](../verification/) &mdash; 6 documents &middot; [Verification Independence `AI-VER-001`](../verification/verification-independence.md) &middot; [Testing Strategy `AI-VER-002`](../verification/testing-strategy.md) &middot; [Test Harnesses and Harness Independence `AI-VER-005`](../verification/test-harnesses.md)

### Integration

*What has to happen before a change is accepted?*

The Pull Request is the principal integration quality boundary: what a change must satisfy to be considered for acceptance, and what its author declares.

[`integration/`](../integration/) &mdash; 6 documents &middot; [Pull Request Boundary `AI-INT-003`](../integration/pull-request-boundary.md) &middot; [Branch Management `AI-INT-002`](../integration/branch-management.md) &middot; [Automated Quality Gates and CI Pipeline `AI-INT-005`](../integration/quality-gates.md) &middot; [Definition of Done `AI-INT-006`](../integration/definition-of-done.md)

### Governance

*How does the framework itself stay alive?*

Who owns the framework, who may change it, and how authority is distributed.

[`governance/`](../governance/) &mdash; 19 documents &middot; [Engineering Governance Model `AI-GOV-001`](../governance/governance-model.md) &middot; [Open Questions `AI-GOV-006`](../governance/open-questions.md) &middot; [Decision Process `AI-GOV-007`](../governance/decision-process.md)

### Implementation profiles

*What does this look like on a concrete stack?*

The concrete numbers, kept out of the domain documents on purpose so that discussing a coverage percentage does not mean reopening the framework.

[`profiles/`](../profiles/) &mdash; 3 documents &middot; [Proposed Quality Gate Baselines `AI-PROF-002`](../profiles/quality-gates/baselines.md) &middot; [Reference CI Harness Configurations `AI-PROF-001`](../profiles/ci/reference-harness-configurations.md) &middot; [Draft Pull Request Declaration `AI-PROF-003`](../profiles/pull-request/declaration.md)

---

## Where the rest is

- [`engineering-changes/`](../engineering-changes/) &mdash; 3 playbooks for specific kinds of risky change: APIs, databases, observability.
- [`decisions/`](../decisions/) &mdash; 3 records of what was chosen and what was rejected. Append-only.
- [Open Questions](../governance/open-questions.md) &mdash; what is deliberately undecided, one document per question.
- [`compiled/`](../compiled/) &mdash; the original draft, frozen. A snapshot, not a source.

---

Read the summary to understand the model. Follow the links to apply it. Consult the decision records to understand why.

<sub>Generated by `tools/render_summary.py`. Every sentence above is taken from the document it links to, from the README domain table, or from the corpus as it stands. Do not edit this file: change the source document and regenerate.</sub>
