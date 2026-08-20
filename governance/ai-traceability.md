---
id: AI-GOV-003
title: AI Contribution Traceability
status: proposed
domain: governance
owners:
  - engineering
applies_to:
  - all-changes
related:
  - AI-PROF-003
source:
  - draft EN202608161000, section 56
---

# AI Contribution Traceability

What is worth recording about how a change came to be. The purpose is auditability rather than attribution, and the categories below are an open proposal rather than a decision.

<!-- nav:start -->
`AI-GOV-003` &middot; status **proposed** &middot; domain [`governance/`](./)

**Related** &mdash; [Draft Pull Request Declaration `AI-PROF-003`](../profiles/pull-request/declaration.md)

**Derived from** &mdash; [section 56. AI Contribution Traceability: Options](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#56-ai-contribution-traceability-options)
<!-- nav:end -->

---

Some traceability of AI-assisted development is useful for auditability and for understanding how a change came to be. The open question is what to record.

**A simple boolean has a short shelf life.** Recording `AI assistance: yes / no` works while assistance is the exception. If, within a couple of years, nearly all development carries some degree of assistance, the field stops discriminating anything and becomes a box everyone ticks.

**Recording the kind and degree of intervention is likely to age better.** Categories that would actually change how a reviewer approaches the change:

```text
AI agent generated a substantial part of this change
AI-generated tests
AI-generated synthetic or fixture data
AI-assisted data or schema migration
AI-assisted change to security-sensitive code
AI-assisted change to CI, infrastructure or deployment configuration

Human owner: <developer>
Verification performed: <checks executed and evidence reviewed>
```

Whatever is chosen, two things seem worth keeping in view: the declaration should be cheap for the author, and anything derivable automatically — from commit trailers, agent tooling or branch metadata — is better derived than asked.

The purpose would be auditability rather than attribution: understanding how a change came to be, and being able to look again at the changes where the process carried more risk. Prompts and confidential AI conversations are not what should be archived.

[Annex C](../profiles/pull-request/declaration.md) sketches how this could look in a Pull Request template, as material for the discussion.

> **Discussion point.** This needs consensus before it goes into a template. The categories above are a first proposal, not a decision, and the alternative of recording nothing at all — relying on review and ownership instead — is also a legitimate position to argue.
