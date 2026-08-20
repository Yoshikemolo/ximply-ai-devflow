---
id: AI-DEC-001
title: Spread the draft into an addressable domain corpus
status: accepted
created: 2026-08-20
owners:
  - jorge-rodriguez
supersedes: []
related:
  - AI-KNOW-001
  - AI-KNOW-005
  - AI-FND-003
---

<!-- nav:start -->
`AI-DEC-001` &middot; status **accepted** &middot; domain [`decisions/`](./)

**Related** &mdash; [Repository as Engineering Source of Truth `AI-KNOW-001`](../knowledge/repository-source-of-truth.md) &middot; [Addressable Knowledge `AI-KNOW-005`](../knowledge/addressable-knowledge.md) &middot; [Context Economy `AI-FND-003`](../ai-foundations/context-economy.md)
<!-- nav:end -->
# Context

The framework existed as one document of roughly three thousand lines, in
Markdown, DOCX and PDF. That form was right for starting the discussion: a
complete text is easier to argue with than a set of headings.

It is the wrong form for maintaining consensus. A reader cannot cite a
paragraph, an objection cannot be scoped, a change touches the whole document,
and an agent asked a narrow question has to be handed the entire corpus - which
is exactly what the framework's own context economy argues degrades the answer.

# Options considered

1. **Keep the single document.** Lowest cost, and it preserves the reading
   flow the draft was written for. It leaves every problem above unsolved.
2. **Split mechanically, one file per numbered section.** Seventy-one files.
   Cheap and reversible, but it distributes the problem rather than solving it:
   the eighteen testing sections are not eighteen independent decisions, and
   splitting them apart makes the allocation of test effort against risk harder
   to see, not easier.
3. **Spread by conceptual domain, then extract decisions when they earn their
   own identity.** Roughly fifty documents in ten domains. More judgement
   required, and the judgement is contestable.

# Decision

Option 3.

Fifty documents across ten domains, derived by `tools/split_framework.py` from
a map that is itself part of the repository and part of what is under review.
Two invariants: no source section appears in two target documents, and every
target document records where it came from.

# Evidence

The draft names its own conceptual chain - repository as source of truth,
living documentation, context economy, selective retrieval, minimum necessary
context, IP protection, internal agent layer - and states that most of Part I
is one idea followed through its consequences. Grouping by that structure
preserves relationships the section numbering obscured.

The eighteen testing sections collapsing to six documents is the clearest case,
and the one where a mechanical split would have done real damage.

# Consequences

The reading flow of the original document is lost. Someone who wants to read
the framework end to end now needs a compiled view, which does not yet exist
and is the subject of AI-DEC-003.

The domain boundaries are a judgement and some are arguable - security
verification placed under security rather than verification, the prompting
protocol under agentic engineering rather than security. Those are the
placements to challenge first.

Cross-references are now links between files and can rot. Nothing checks them
yet beyond a manual pass.
