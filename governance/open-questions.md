---
id: AI-GOV-006
title: Open Questions
status: proposed
domain: governance
owners:
  - engineering
applies_to:
  - this-corpus
related:
  - AI-FND-003
  - AI-FND-004
  - AI-PROF-002
source:
  - draft EN202608161000, section 71
---

# Open Questions

What the framework deliberately leaves undecided. This is the agenda for review, not a list of gaps to be quietly filled in. Each question that closes should close as a decision record.

---

This section collects the points that this draft deliberately leaves open. They are the agenda for engineering review rather than positions already taken. Each one is written as a question, with the options currently visible and the provisional position taken in the text so that the draft remains readable.

### Q1 — Status and adoption scope

*Which repositories would this apply to, and from when?*

Options range from applying it to new repositories only, through applying it to repositories that already use AI assistance, to organization-wide adoption with a transition period. A phased approach — principles first, automated enforcement later — is probably easier to sustain than a single cut-over.

*Provisional position in this draft:* nothing is enforced until agreed; Part I is proposed first, Part II follows per stack.

### Q2 — Where the boundary of architectural authority sits

*What exactly is reserved to human decision?*

The draft proposes that AI may analyse, propose alternatives, challenge a decision, surface conflicts with existing ADRs and draft ADR candidates, but does not hold decision authority. The open part is the operational one: which categories of change require an ADR before implementation begins, and who accepts an ADR in each team.

### Q3 — How far an agent may work on a complete feature

*Is feature-scale agent work acceptable when it is planned and checkpointed?*

The draft says yes, provided the work is decomposed, a plan exists, checkpoints are verified and the human controls the result; what it rules out is a single unconstrained generation step accepted wholesale. The question for review is what a "checkpoint" needs to be in practice, and whether [the autonomy levels in this document](../ai-foundations/autonomy-levels.md) map cleanly onto the agent tooling the teams actually use.

### Q4 — Review depth and generated artifacts

*What must be read line by line, and what is validated differently?*

The draft distinguishes material authored changes, which are reviewed and must be explainable, from generated artifacts — scaffolding, lockfiles, generated clients, schemas, snapshots, bulk fixtures — which are validated through their generator, their input contract and their tests. The open question is where the line falls for each stack, and how the review checklist should express it without becoming a formality.

### Q5 — Granularity of AI traceability

*Is a yes/no declaration still meaningful?*

If most development carries some degree of assistance within a couple of years, a boolean loses its information value. The alternative in the draft is to record the kind of intervention that actually matters for risk — substantial agent-generated change, generated tests, generated synthetic data, assisted migration, assisted security-sensitive code — rather than assistance in general. This needs agreement on the categories before it is put into a Pull Request template, otherwise it becomes noise that everybody ticks.

### Q6 — Quality thresholds

*Which numbers, and who owns them?*

Coverage percentages, duplication limits and rating requirements are in [Annex B](../profiles/quality-gates/baselines.md) precisely so that they can be discussed and changed without reopening the standard. The questions are the values themselves, whether they differ per stack or per repository class, whether they apply to new code only, and how existing repositories converge without blocking delivery.

### Q7 — Enforcement and exceptions

*How strict should the integration boundary be at the start?*

The draft proposes preventive controls, audited administrative bypass and time-bounded exceptions. There is a real trade-off: strong preventive enforcement gives consistency but can block delivery in edge cases, while a lighter model depends on discipline. A staged tightening, starting with visibility and moving to blocking checks, is one option.

### Q8 — Approved tooling and data handling

*Which assistants, models and providers are approved, under what data terms?*

This draft states the requirement but not the list, because the list is an organizational decision with contractual implications. It also affects what "minimum necessary context" means in practice for each tool.

### Q9 — Ownership and maintenance of the document

*Who maintains Part I and Part II, and at what cadence?*

Part I is expected to be stable for years; Part II tracks framework, SDK and tooling versions and will drift faster. A named owner and a review rhythm for each are needed for the document to stay credible.

### Q10 — Context tooling and cross-model practice

*What do we invest in, and what stays discretionary?*

Two items from [the context-economy section](../ai-foundations/context-economy.md) need a decision rather than a recommendation: whether we build or adopt a structural index — a symbol and call graph, or a ranked repository map — for the main codebases, and whether confronting output across different models becomes an expected step for architectural and security-relevant work or is left to each engineer. The first has a cost and an owner; the second has a token cost and only pays off where the decision matters.

### Q11 — Addressable documentation

*Is it worth giving every documentation piece a stable identifier?*

The conceptual-architecture section sketches identifiers such as `ADR-0042` or `SEC-0017`, with relations like `supersedes` and `applies-to`, turning the documentation set into a versioned knowledge graph that both agents and Pull Requests can cite precisely. The open part is whether the discipline is worth its cost: an identifier scheme is cheap to start, useful only if maintained, and awkward to abandon once things reference each other. It also needs an owner, a numbering convention and a decision about what to do with the documents that already exist.

### Q12 — Metrics and evidence of value

*How do we know whether this is helping?*

The draft proposes delivery and quality metrics rather than AI-activity counters. Before adoption it is worth agreeing on a small baseline set that can actually be measured with current tooling, so that the effect of the standard is observable rather than assumed.

---

# Part II — Implementation Profile

*Non-normative annexes. Expected to change with tooling; versioned separately from Part I.*
