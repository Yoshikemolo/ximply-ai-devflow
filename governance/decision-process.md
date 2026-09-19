---
id: AI-GOV-007
title: Decision Process
status: proposed
domain: governance
owners:
  - engineering
applies_to:
  - this-corpus
related:
  - AI-GOV-001
  - AI-GOV-006
  - AI-KNOW-003
  - AI-KNOW-005
source:
  - authored for this repository
---

# Decision Process

How a question in this corpus stops being open. The framework asks a lot of
engineering practice; the mechanism by which the framework itself changes
deserves the same treatment, and it was the one thing the draft did not write
down.

<!-- nav:start -->
`AI-GOV-007` &middot; status **proposed** &middot; domain [`governance/`](./)

**Related** &mdash; [Engineering Governance Model `AI-GOV-001`](governance-model.md) &middot; [Open Questions `AI-GOV-006`](open-questions.md) &middot; [Architecture Decisions and Guardrails `AI-KNOW-003`](../knowledge/architecture-decisions.md) &middot; [Addressable Knowledge `AI-KNOW-005`](../knowledge/addressable-knowledge.md)

**Derived from** &mdash; authored for this repository
<!-- nav:end -->

---

## Two kinds of document

The distinction matters more than any rule below.

**Domain documents** — everything under `principles/`, `ai-foundations/`,
`knowledge/`, `security/`, `agentic-engineering/`, `verification/`,
`integration/`, `engineering-changes/`, `governance/` and `profiles/` —
describe the framework as it currently stands: proposed, accepted or
superseded.

**Decision records** under `decisions/` describe how it got there. They are
append-only history. A decision record is never edited to reflect a change of
mind; a new record supersedes it.

A domain document answers *what do we do*. A decision record answers *why is
that what we do, and what did we reject*. Losing the second is how a framework
becomes a set of rules nobody can defend three years later.

## Status

A domain document carries one of:

```text
proposed     applied in practice, not yet settled by a decision record
accepted     settled by a decision record, agreed by the people it applies to
deprecated   still true, no longer recommended
superseded   replaced, kept for the record
rejected     considered and declined
```

Everything in this corpus is currently `proposed` unless its front matter says
otherwise. That describes how settled a document is, not whether it is used:
the methodology as a whole is applied in practice by
[Ximplicity Software Solutions](https://ximplicity.es), and a `proposed`
document is followed as written until a decision changes it.

## How a question closes

1. **Raise it.** Open a decision record under `decisions/` with status
   `proposed`, stating the question, the options visible and the evidence
   available. Drafting one is cheap and is explicitly a good use of AI
   assistance.
2. **Argue it.** In review, in the record, in whatever forum the team uses.
   The record accumulates the argument; it is not a summary written afterwards.
3. **Decide it.** An accountable human accepts the record. AI MAY draft a
   decision and MUST NOT accept one.
4. **Apply it.** Update the domain documents the decision affects, in the same
   change that flips the record to `accepted`, and cite the record identifier
   in the commit. A decision that is not reflected in the domain documents has
   not been applied, whatever its status says.

## Participation

Participation remains open throughout the process. Lack of prior participation
does not remove anyone's voice, and it does not create a retrospective veto
either.

The practical reading: an objection raised late is still an objection and is
answered on its merits. It is not, on its own, grounds to reopen a decision
that was made in the open while the objector was not looking. Reopening
requires an argument or evidence that was not already considered.

## What a decision record looks like

```markdown
---
id: AI-DEC-0NN
title: <the question, stated as a thing decided>
status: proposed | accepted | rejected | superseded
created: YYYY-MM-DD
owners:
  - <accountable human>
supersedes: []
related:
  - <identifiers of affected domain documents>
---

# Context
Why this question exists now.

# Options considered
The alternatives, each stated well enough that someone who preferred it would
recognise their position.

# Decision
What was chosen, or "pending".

# Evidence
What the decision rests on. "It seemed cleaner" is evidence of a preference,
which is a legitimate thing to record as long as it is not dressed as more.

# Consequences
What this now commits us to, including the parts that are worse.
```

Architectural decisions inside a product repository use the fuller template in
[Architecture Decisions and Guardrails](../knowledge/architecture-decisions.md).
The lighter shape above is for decisions about this corpus, where most of the
impact headings would be answered "not applicable" and a form full of "not
applicable" trains people to stop reading it.

> **Discussion point.** Whether decision records and architecture decision
> records should share one template and one numbering space. Two schemes is a
> cost; a template whose headings are mostly empty is also a cost.
