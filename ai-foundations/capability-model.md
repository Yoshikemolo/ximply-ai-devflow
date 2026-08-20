---
id: AI-FND-001
title: AI Capability Model
status: proposed
domain: ai-foundations
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 5
---

# AI Capability Model

What these systems can and cannot be relied on to do, and the failure modes that the controls elsewhere in the corpus exist to catch. Agreeing on this precedes arguing about thresholds.

---

Effective governance requires a shared, non-mythologized understanding of what current AI coding assistants actually do. The controls proposed later in this document exist because of the failure modes described below, not because of a general distrust of automation.

### Context limits and architectural degradation

**Frequent assumption:** the assistant understands the full scope and the implicit dependencies of the platform.

**Engineering reality:** assistants operate inside a bounded context window. As a system grows to thousands of files, the model sees only a fraction of it and optimizes for *local* syntactic and semantic plausibility rather than *global* architectural coherence. Local improvements that break upstream or downstream contracts are a normal, expected output.

**What that suggests:** architectural context MUST be supplied explicitly (see the sections on architecture guardrails, the AI context boundary and context-informed prompting), and architectural conformance MUST be verified by a human and by automated analysis.

### Statistical generation and hallucination

**Frequent assumption:** if AI-generated code compiles, it is correct, secure and optimal.

**Engineering reality:** a model emits the statistically most probable token sequence given its training distribution, not the provably correct solution for the specific edge cases of this system. Typical observed defects include:

* References to deprecated or removed framework APIs.
* Invented functions, parameters, configuration keys or packages.
* Plausible but incorrect concurrency, transaction or lifetime assumptions.
* Silent security weaknesses that compile cleanly and pass a naive test suite.
* Confident explanations that do not match the emitted code.

**What that suggests:** compilation is evidence of syntactic compatibility only. Acceptance requires independent verification (see verification independence, harness independence and the Pull Request acceptance criteria).

### Pattern reproduction is not engineering synthesis

**Frequent assumption:** AI can design the software architecture.

**Engineering reality:** architecture requires balancing infrastructure cost, team cognitive load, regulatory and security constraints, migration risk, organizational scale and long-term strategy. A model can reproduce and recombine patterns present in its training data; it cannot own a trade-off, accept residual risk, or be accountable for the consequences of a decision.

**What that suggests:** architectural authority remains human and is recorded in ADRs. AI MAY draft an ADR; AI MUST NOT accept one.

### Productivity is measured at the delivery boundary

Perceived speed during code generation is not a delivery outcome. Time saved in generation that is transferred to review, debugging, rework or incident response is not a productivity gain. The metrics section later in Part I proposes measuring adoption at the delivery boundary instead.
