---
id: AI-SEC-002
title: Agentic Security Boundary
status: accepted
domain: security
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  - AI-AGT-003
  - AI-PRIN-002
  - AI-SEC-001
source:
  - draft EN202608161000, section 21
---

# Agentic Security Boundary

Context aggregation risk, progressive disclosure, and the protection of intellectual property that no individual file would identify as confidential. Sensitivity is a property of the accumulated context, not of the item.

<!-- nav:start -->
`AI-SEC-002` &middot; status **accepted** &middot; domain [`security/`](./)

**Related** &mdash; [Local Models and Organization-Owned Agentic Tooling `AI-AGT-003`](../agentic-engineering/local-and-corporate-agents.md) &middot; [Human Accountability `AI-PRIN-002`](../principles/human-accountability.md) &middot; [AI Context Boundary `AI-SEC-001`](ai-context-boundary.md)

**Derived from** &mdash; [section 21. Agentic Security Boundary](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#21-agentic-security-boundary)
<!-- nav:end -->

---

Agentic AI introduces additional risk because generated instructions may cause actions, not merely text generation.

AI agents MUST therefore treat repository content, tool output, external documents, issue descriptions and imported data as potentially untrusted input.

In particular, systems SHOULD protect against:

* Prompt injection.
* Indirect prompt injection.
* Tool misuse.
* Excessive agency.
* Credential exposure.
* Unauthorized data access.
* Malicious repository instructions.
* Unsafe shell commands.
* Unauthorized network access.
* Cross-repository data leakage.
* Progressive disclosure of intellectual property through accumulated context.
* Dependency substitution.
* Exfiltration through generated output.

Agent instructions discovered inside source code, documentation, tickets or external content MUST NOT automatically override organizational policy.

Tool permissions SHOULD be allow-listed wherever practical.

### Context aggregation and progressive intellectual-property disclosure

Confidentiality risk is not limited to exposing a complete secret, document, algorithm or dataset in a single prompt. A sequence of individually harmless and incomplete disclosures MAY collectively reveal proprietary knowledge, because modern AI systems correlate information across large contexts and infer relationships between fragments.

An assessment performed prompt by prompt therefore measures the wrong thing.

> **Context aggregation risk:** information that is non-sensitive in isolation may become sensitive when combined with other information. AI context MUST therefore be evaluated cumulatively, not prompt by prompt.

> **Minimum necessary context:** engineers MUST provide an AI system only the minimum organizational information required to perform the specific engineering task.

> **The security boundary is determined not only by what is explicitly disclosed, but also by what a sufficiently capable model may reasonably infer from the accumulated context.**

This document uses **context aggregation risk** for the exposure mechanism and **progressive IP disclosure** for the resulting failure mode. The same pattern is sometimes described informally as "IP juicing"; that term has no established technical definition and is not used here as the formal one.

Fragments that are unremarkable individually but correlatable in combination include:

* Previous prompts and accumulated conversation context.
* Other source-code fragments.
* Architecture information.
* Internal terminology.
* Business rules.
* Algorithms.
* Data models and schemas.
* Infrastructure details.
* Product behavior.
* Performance characteristics.
* Customer-specific information.
* Documentation or ADR fragments.
* Information obtained from other repositories or organizational systems.

#### Protected information

The knowledge this control protects extends beyond credentials and personal data, and includes, where applicable:

* Proprietary algorithms.
* Source code.
* Internal architectures.
* Trade secrets.
* Product designs.
* Industrial know-how.
* Proprietary business rules.
* Internal protocols.
* Security mechanisms.
* Manufacturing or engineering processes.
* Confidential customer solutions.
* Unpublished research.
* Patent-sensitive technical information.

The risk applies even when no single prompt contains the complete protected information.

This is deliberately broader than the prohibition on secrets and personal data stated among the hard limits in [Human Accountability](../principles/human-accountability.md) and repeated in the context boundary in [AI Context Boundary](ai-context-boundary.md). A context can contain no credentials, no keys and no customer PII, and still describe how the product works well enough to be reconstructed. Removing the obvious secrets is a necessary control, not a sufficient one.

#### Distinguishing what enters the context

Not every source-code fragment is prohibited from AI use, and the objective is risk-based protection rather than making AI-assisted development impractical. Before adding material to a session, engineers SHOULD place it in one of three categories:

1. **Required** — information the engineering task genuinely needs. This is provided.
2. **Unnecessary** — information that does not contribute to the task. This is not provided, regardless of how much context the model can hold.
3. **Cumulatively sensitive** — information that is defensible in isolation but that, combined with what the session already contains, approaches a reconstruction of protected knowledge. This requires a deliberate decision, and often a new session instead.

The third category is the one this section exists for. It is also the one that is easy to miss, because each individual step looks reasonable.

#### Controls

Engineers MUST NOT knowingly use AI systems in a way that enables progressive reconstruction, inference or extraction of confidential organizational or third-party intellectual property.

In addition:

* Engineers MUST consider the cumulative sensitivity of a session before adding new information to it.
* Only organization-approved AI tools and providers MUST be used for proprietary engineering information. The general requirement appears among the hard limits in [Human Accountability](../principles/human-accountability.md); it matters again here because provider retention and training terms determine what happens to an accumulated context after the session ends. Where the accumulated context is unavoidably rich, the structural answer is to keep inference and tool access inside the organization, as described in [Local Models and Organization-Owned Agentic Tooling](../agentic-engineering/local-and-corporate-agents.md).
* Cross-repository context MUST be treated as a privileged operation, justified by the task rather than by convenience.
* Redaction of obvious secrets MUST NOT be assumed to protect intellectual property.
* Context supplied to an AI system SHOULD be minimized to what the task requires.
* Abstractions, interfaces, contracts and reduced examples SHOULD be preferred over complete implementations where they are sufficient for the task.
* Proprietary identifiers, internal names and domain terminology SHOULD be sanitized or generalized where they are not necessary for the task.
* Unrelated repository content SHOULD NOT be supplied.
* Persistent sessions accumulating information from unrelated confidential tasks SHOULD be avoided.
* A new context or session SHOULD be started when separation between tasks is required, and MAY be started at any point when the accumulated context is no longer justified by the current task.

Work that touches core industrial know-how, patent-sensitive material or confidential customer solutions SHOULD be scoped explicitly before an assistant is involved, so that the decision about what may enter the context is made once and deliberately rather than incrementally under delivery pressure.

> **Discussion point.** This is the section most likely to be either over-applied or ignored. Two things would make it practical: a short, concrete list per repository of what counts as cumulatively sensitive in that codebase, and agreement on when starting a fresh session is expected rather than merely advisable.
