---
id: AI-DEC-002
title: Stable identifiers and relationships for corpus documents
status: proposed
created: 2026-08-20
owners:
  - engineering
supersedes: []
related:
  - AI-KNOW-005
  - AI-GOV-006
  - OQ-0011
---

<!-- nav:start -->
`AI-DEC-002` &middot; status **proposed** &middot; domain [`decisions/`](./)

**Related** &mdash; [Addressable Knowledge `AI-KNOW-005`](../knowledge/addressable-knowledge.md) &middot; [Open Questions `AI-GOV-006`](../governance/open-questions.md) &middot; [Addressable documentation `OQ-0011`](../governance/open-questions/OQ-0011-addressable-documentation.md)
<!-- nav:end -->
# Context

The draft proposes that documentation pieces carry stable identifiers and
declare relationships - supersedes, depends-on, applies-to, conflicts-with -
so that Markdown in Git behaves as a versioned knowledge graph. It lists this
among the open questions rather than settling it.

Spreading the corpus forced a provisional answer, because fifty documents
without identifiers are fifty documents that can only be cited by path, and a
path changes.

# Options considered

1. **No identifiers.** Cite by path and title. Zero ceremony. Paths change,
   citations rot silently, and a superseded document keeps being quoted.
2. **Identifiers only, no relationships.** Half the value for most of the cost.
3. **Identifiers plus declared relationships in front matter.** What the draft
   sketches. Buys citation stability, supersession that is visible, and
   detectable contradiction.

# Decision

Pending. Option 3 is in provisional use so that the corpus is usable, with the
scheme `AI-<DOMAIN>-<NNN>` and front matter carrying `id`, `title`, `status`,
`domain`, `owners`, `applies_to`, `related` and `source`.

The `related` field is currently derived rather than authored: the tooling
collects the identifiers a document's own body links to. That is cheap and
honest, and it is not the same thing as a curated relationship.

# Evidence

None yet beyond the draft's own argument. The corpus is small enough that the
cost of being wrong is a scripted rename.

# Consequences

Identifiers are cheap to introduce and expensive to abandon halfway, which the
draft says explicitly. Adopting them provisionally means accepting that cost if
the answer turns out to be option 1.

The domain prefix encodes the current domain split, so moving a document
between domains either breaks the prefix or leaves it lying. Whether an
identifier should encode location at all is part of what needs deciding.

Nothing enforces uniqueness, referential integrity or supersession today.
