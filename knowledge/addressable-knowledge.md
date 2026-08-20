---
id: AI-KNOW-005
title: Addressable Knowledge
status: proposed
domain: knowledge
owners:
  - engineering
applies_to:
  - software-repositories
  - this-repository
related:
  - AI-GOV-006
source:
  - draft EN202608161000, section 4 (Addressability, briefly)
---

# Addressable Knowledge

Versioning tells you which text you have; an identifier tells you which decision you are talking about. This is what turns a documentation tree into a queryable corpus, and it is the precondition for selective retrieval by an agent. This repository is the first place the idea is being tried.

<!-- nav:start -->
`AI-KNOW-005` &middot; status **proposed** &middot; domain [`knowledge/`](./)

**Related** &mdash; [Open Questions `AI-GOV-006`](../governance/open-questions.md)

**Derived from** &mdash; [Addressability, briefly](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#addressability-briefly)
<!-- nav:end -->

---

The chain works better if every piece of documentation can be named. Versioning alone is not enough: a version tells you which text you have, an identifier tells you *which decision you are talking about*.

A sketch, offered here as direction rather than as a finished proposal:

```text
ADR-0042             an architectural decision
SEC-0017             a security constraint or threat-model entry
AI-CTX-0006          a rule about what may enter an AI context
TEST-STRATEGY-0003   a testing strategy decision
```

With stable identifiers, pieces can declare their relationships — `supersedes`, `depends-on`, `applies-to`, `conflicts-with` — and the effects are concrete: an agent retrieves one decision instead of a whole document, a Pull Request cites the exact constraint it satisfies, a superseded decision stops being quoted years later, and a contradiction becomes detectable rather than a matter of who read what.

The result is a versioned knowledge graph, even though physically it remains Markdown in Git.

This deserves its own treatment before it becomes a convention — identifier scheme, ownership, tooling, migration of existing documents — and it is listed among [the open questions](../governance/open-questions.md) rather than settled here.

> **Discussion point.** Two questions on this section. First, whether the chain as drawn is the right one, or whether it is missing a link the teams would consider obvious. Second, whether addressable documentation is worth the discipline it costs: identifiers are cheap to introduce and expensive to abandon halfway.
