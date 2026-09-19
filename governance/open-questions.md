---
id: AI-GOV-006
title: Open Questions
status: accepted
domain: governance
owners:
  - engineering
applies_to:
  - this-corpus
related:
  []
source:
  - draft EN202608161000, section 71
---

# Open Questions

What the framework deliberately leaves undecided. This is the agenda for review, not a list of gaps to be quietly filled in.

<!-- nav:start -->
`AI-GOV-006` &middot; status **accepted** &middot; domain [`governance/`](./)

**Derived from** &mdash; [section 71. Open Questions and Decisions Required](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#71-open-questions-and-decisions-required)
<!-- nav:end -->

---

This section collects the points that the framework deliberately leaves open, even though the methodology is already applied in practice. They are the agenda for engineering review rather than positions already taken. Each one is written as a question, with the options currently visible and the provisional position taken in the text so that the draft remains readable.

Each question is its own document, with its own status, its own owner and its own history. A question is not a paragraph in a list: it is opened, argued and eventually closed, and bundling twelve of them into one file meant they could only be cited, versioned and answered together.

## Index

| Question | Status | Documents it would change |
|---|---|---|
| [`OQ-0001` Status and adoption scope](open-questions/OQ-0001-status-and-adoption-scope.md) | `open` | `AI-PRIN-000` `AI-GOV-002` |
| [`OQ-0002` Where the boundary of architectural authority sits](open-questions/OQ-0002-where-the-boundary-of-architectural-authority-sits.md) | `open` | `AI-PRIN-002` `AI-KNOW-003` |
| [`OQ-0003` How far an agent may work on a complete feature](open-questions/OQ-0003-how-far-an-agent-may-work-on-a-complete-feature.md) | `open` | `AI-FND-004` `AI-AGT-004` `AI-AGT-005` |
| [`OQ-0004` Review depth and generated artifacts](open-questions/OQ-0004-review-depth-and-generated-artifacts.md) | `open` | `AI-PRIN-003` `AI-INT-004` |
| [`OQ-0005` Granularity of AI traceability](open-questions/OQ-0005-granularity-of-ai-traceability.md) | `open` | `AI-GOV-003` `AI-PROF-003` |
| [`OQ-0006` Quality thresholds](open-questions/OQ-0006-quality-thresholds.md) | `open` | `AI-INT-005` `AI-PROF-002` |
| [`OQ-0007` Enforcement and exceptions](open-questions/OQ-0007-enforcement-and-exceptions.md) | `open` | `AI-GOV-002` `AI-INT-005` |
| [`OQ-0008` Approved tooling and data handling](open-questions/OQ-0008-approved-tooling-and-data-handling.md) | `open` | `AI-SEC-001` `AI-AGT-003` |
| [`OQ-0009` Ownership and maintenance of the document](open-questions/OQ-0009-ownership-and-maintenance-of-the-document.md) | `open` | `AI-GOV-001` `AI-GOV-005` |
| [`OQ-0010` Context tooling and cross-model practice](open-questions/OQ-0010-context-tooling-and-cross-model-practice.md) | `open` | `AI-FND-003` `AI-AGT-002` |
| [`OQ-0011` Addressable documentation](open-questions/OQ-0011-addressable-documentation.md) | `open` | `AI-KNOW-005` |
| [`OQ-0012` Metrics and evidence of value](open-questions/OQ-0012-metrics-and-evidence-of-value.md) | `open` | `AI-GOV-004` |

## Lifecycle

```text
open        stated, not answered
answered    closed by an accepted decision record
deferred    real, but deliberately not being decided yet
withdrawn   no longer a question - the premise changed
superseded  replaced by a better-framed question
```

A question is answered by accepting a decision record under `decisions/` and updating the documents it affects in the same change. Nothing else closes one; a question that quietly stops being mentioned is still open.

A closed question keeps its document. What was asked is worth as much as what was answered, and deleting it would leave the decision record pointing at nothing.
