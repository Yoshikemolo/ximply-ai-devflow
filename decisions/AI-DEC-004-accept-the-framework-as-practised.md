---
id: AI-DEC-004
title: Accept the domain documents as practised, subject to review
status: accepted
created: 2026-09-19
owners:
  - jorge-rodriguez
supersedes: []
related:
  - AI-PRIN-000
  - AI-GOV-005
  - AI-GOV-007
---

<!-- nav:start -->
`AI-DEC-004` &middot; status **accepted** &middot; domain [`decisions/`](./)

**Related** &mdash; [Purpose, Scope and Normative Language `AI-PRIN-000`](../principles/purpose-and-scope.md) &middot; [Periodic AI Governance Review `AI-GOV-005`](../governance/periodic-review.md) &middot; [Decision Process `AI-GOV-007`](../governance/decision-process.md)
<!-- nav:end -->
# Context

Every domain document was `proposed`, which the decision process defined as
written down but not agreed. That no longer describes the framework. Ximplicity
Software Solutions applies it in its own products, such as EVIDENT App, and in
client projects that cannot be named under non-disclosure agreements. A status
that says nothing is agreed, attached to rules that are followed every day,
misleads both the people reading the corpus and the agents retrieving it.

# Options considered

1. **Keep `proposed` and redefine it** as applied but not yet settled. Honest
   about use, but it leaves the status vocabulary unable to distinguish a rule
   in daily use from an idea written down yesterday.
2. **Accept documents one by one** as each is argued and confirmed. The most
   rigorous path, and the slowest: the corpus would keep understating its own
   standing for as long as the review takes.
3. **Accept every domain document now, subject to review.** The status matches
   practice today, and the review that option 2 would require up front happens
   through periodic review and ordinary decision records instead.

# Decision

Option 3.

Every domain document moves from `proposed` to `accepted`. Accepted does not
mean final: each document remains subject to [Periodic Review](../governance/periodic-review.md)
and can be changed, deprecated or superseded through the
[decision process](../governance/decision-process.md). New material that has
not been applied yet enters as `proposed`.

Open questions under `governance/open-questions/` keep their own status. A
question that is `open` is still open; accepting the documents around it does
not answer it, and a `Discussion point` inside an accepted document remains
arguable.

Decision record AI-DEC-002 keeps its own status. Accepting it is a separate
question about the identifier scheme, not about the practice this record
settles.

# Evidence

Use in practice by Ximplicity Software Solutions across its own products and
client projects, as stated by the accountable owner of the framework.

# Consequences

Agents and readers may now say the framework requires something, rather than
proposes it, when quoting an accepted document.

A change that alters what an accepted document asks for now needs a decision
record, where before an editorial Pull Request could have been argued to be
enough. That is the intended cost.

The acceptance rests on practice rather than on a document-by-document review.
Where practice and a document disagree, the disagreement is a defect to be
raised through the decision process, not a licence to ignore the document.
