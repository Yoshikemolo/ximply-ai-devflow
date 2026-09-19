---
id: AI-GOV-002
title: Compliance and Exceptions
status: accepted
domain: governance
owners:
  - engineering
applies_to:
  - this-corpus
related:
  []
source:
  - draft EN202608161000, section 68
---

# Compliance and Exceptions

How the framework is enforced, and how an exception is granted so that it stays explicit, owned and time-bounded rather than becoming silent erosion.

<!-- nav:start -->
`AI-GOV-002` &middot; status **accepted** &middot; domain [`governance/`](./)

**Derived from** &mdash; [section 68. Proposed Compliance and Enforcement Model](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#68-proposed-compliance-and-enforcement-model)
<!-- nav:end -->

---

If the team decides to adopt this, it needs a model for what happens when something does not comply. This section proposes one; the level of strictness is itself a decision, and a staged approach — visibility first, blocking checks later — is a reasonable alternative to everything at once.

> **Discussion point.** Strong preventive enforcement gives consistency but can block delivery in edge cases; a lighter model relies on discipline. Where to start, and how quickly to tighten, is an open question.

### Enforcement

* **Preventive rather than punitive.** The controls would live in branch protection, required status checks and quality gates. A Pull Request that fails a required check is corrected rather than waived — the control does the work, so that no individual has to police it.
* **Administrative bypass is an audited event.** Where an emergency merge is performed by bypassing protections, the event MUST be recorded with its justification and the accountable owner, and a remediation change MUST follow within the agreed window. Repeated bypasses are escalated to engineering management.
* **Reversion.** A change merged in breach of what the team agrees, or a change identified after merge as containing an unreviewed or unverified AI-generated defect, is reverted or remediated on a defined timeline according to its risk. Reversion is an engineering decision executed by an authorized human, never an automated action taken by an AI tool.
* **Repository onboarding.** A repository would be considered ready when branch protection, the agreed workflows and the Quality Gate are active. Configuring new repositories before AI-assisted work starts is cheaper than retrofitting.

### Exceptions

Any deviation from an agreed requirement would carry:

1. A documented justification.
2. Explicit approval by the accountable engineering owner.
3. A recorded expiry date or remediation plan.
4. An ADR where the deviation is architecturally significant.

Exceptions are time-bounded by design. An exception that never expires is a requirement nobody believed in, and the honest response is to change the requirement rather than to keep granting the exception.

### Audit trail

The organization SHOULD be able to reconstruct, for any change:

* Who owned it and who approved it.
* Which automated checks ran and what they reported.
* Whether AI assistance was used and in what scope.
* Which requirement or ticket it satisfies.
* Which artifact it produced and where that artifact was deployed.

This information comes from the Pull Request, the CI records and the artifact provenance, not from AI conversation logs. Prompts and AI conversations MUST NOT be archived where they would retain confidential content unnecessarily.

### Keeping the document alive

Part I is expected to be stable; Part II will drift with tooling. A proposed rhythm: review at least semi-annually, and additionally whenever AI tooling capability, framework versions, security standards or organizational risk change materially. Each review would look at, at minimum:

* Supported framework, SDK and runtime versions referenced in the harness templates.
* Linter, analyzer and Quality Gate rule sets, including new AI-specific failure modes observed in production.
* Approved AI tools, providers and data-handling terms.
* Autonomy levels permitted per repository class.
