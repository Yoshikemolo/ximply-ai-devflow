# AI-Assisted Software Engineering Framework

A proposed engineering standard for software development assisted by AI
systems: where AI fits, what stays human, and what a change must prove before
it is allowed to become accepted software.

**Nothing here is in force.** Every document is a proposal open to challenge.
Requirement levels — MUST, SHOULD, MAY — express *the strength being proposed
for that item*, not an obligation. See
[Purpose, Scope and Normative Language](principles/purpose-and-scope.md).

## Start here

**[The Framework Map](summary/README.md)** — two pages: what the framework is
for, the chain it hangs on, the seven principles, and eight blocks that link
straight into the authoritative documents. Read it to understand the model,
follow the links to apply it, read the decision records to understand why.

It is a derived navigation layer. It states nothing of its own and is
regenerated from the documents below, which remain authoritative.

## What this repository is

The framework itself, as an addressable corpus: fifty-one documents grouped by
the engineering question they answer, each with a stable identifier, a status
and a record of where it came from.

## What it is not

Not a tool manual, not a product, and not a description of any particular
agent. An implementation applies this framework; it does not define it.

Not a finished standard either. The corpus is complete in the sense that the
whole draft has been placed, not in the sense that it has been agreed.

## The idea it rests on

Most of the framework is one argument followed through its consequences:

```text
repository as source of truth
    → living documentation
        → context economy
            → selective retrieval
                → minimum necessary context
                    → intellectual property protection
                        → internal agent layer, querying it all back
```

Weaken any link and the ones after it stop working. Read backwards, the same
chain describes the useful end state — not a model trained on everything the
organization has, but an ordinary model authorized to query a well-structured
corpus under the identity and permissions of the person asking.

This repository is the first attempt to build such a corpus.
[Engineering Principles](principles/engineering-principles.md) develops the
chain in full.

## Domains

| Domain | Question it answers | Documents |
|--------|--------------------|-----------|
| [`principles/`](principles/) | What do we believe, and who is accountable? | 4 |
| [`ai-foundations/`](ai-foundations/) | What are we actually governing? | 4 |
| [`knowledge/`](knowledge/) | How does engineering knowledge stay true and findable? | 5 |
| [`security/`](security/) | What may an agent know, and what may it do? | 7 |
| [`agentic-engineering/`](agentic-engineering/) | How do we work with agents in practice? | 6 |
| [`verification/`](verification/) | What counts as proof that generated code is correct? | 6 |
| [`integration/`](integration/) | What has to happen before a change is accepted? | 6 |
| [`engineering-changes/`](engineering-changes/) | How do we make specific kinds of risky change? | 3 |
| [`governance/`](governance/) | How does the framework itself stay alive? | 7 |
| [`profiles/`](profiles/) | What does this look like on a concrete stack? | 3 |
| [`decisions/`](decisions/) | How did we get here, and what did we reject? | 3 |

## Where to find things

| If you want to know | Read |
|---------------------|------|
| What we can put into an AI context | [AI Context Boundary](security/ai-context-boundary.md) |
| Why that limit is not just about secrets | [Agentic Security Boundary](security/agentic-security-boundary.md) |
| How much an agent is allowed to do alone | [AI Autonomy Levels](ai-foundations/autonomy-levels.md) |
| What an agent may execute | [Shell and Tool Execution](security/tool-execution.md) |
| Where AI must not decide | [Human Accountability](principles/human-accountability.md) |
| Why AI confidence is not evidence | [Agentic Bias](ai-foundations/agentic-bias.md) |
| Why bigger context is not better context | [Context Economy](ai-foundations/context-economy.md) |
| What has to be true before merging | [Definition of Done](integration/definition-of-done.md) |
| How a change reaches `main` | [AI-Assisted Development Cycle](integration/ai-assisted-development-cycle.md) |
| How we test AI-generated code | [Testing Strategy](verification/testing-strategy.md) |
| Why the tests cannot be trusted to the generator | [Verification Independence](verification/verification-independence.md) |
| What is still undecided | [Open Questions](governance/open-questions.md) |
| How something gets decided | [Decision Process](governance/decision-process.md) |
| What a CI harness could look like | [Reference CI Harness Configurations](profiles/ci/reference-harness-configurations.md) |
| Which numbers are being proposed | [Quality Gate Baselines](profiles/quality-gates/baselines.md) |
| What a Pull Request would declare | [Draft PR Declaration](profiles/pull-request/declaration.md) |

## Reading a document

Every document opens with front matter:

```yaml
id: AI-SEC-001          # stable identifier, cite this rather than a path
status: proposed        # proposed | accepted | deprecated | superseded | rejected
applies_to: [...]       # where it is meant to bite
related: [...]          # identifiers this document links to
source: [...]           # where in the draft it came from
```

`status` is the field that matters. Everything is currently `proposed`.

Passages marked `> **Discussion point.**` are places where the wording is a
provisional position rather than a conclusion. They are the best places to
start arguing.

## How to propose a change

Small changes — a correction, a clarification, a better example — go straight
to a Pull Request against the document.

Anything that changes what the framework asks for opens a decision record
under [`decisions/`](decisions/) first. The record carries the argument; the
domain document is updated when the record is accepted.

Participation is open throughout. Not having been in an earlier discussion
does not remove anyone's voice, and it does not create a retrospective veto
either. See [Decision Process](governance/decision-process.md), and
[CONTRIBUTING.md](CONTRIBUTING.md) for the mechanics.

## Order of discussion

The corpus is complete; the consensus is not. Opening every domain at once
would produce noise rather than agreement, so discussion proceeds in waves.

| Wave | Domains | Question |
|------|---------|----------|
| 1 | `principles/`, `ai-foundations/` | What is AI in our process, and who stays accountable? |
| 2 | `knowledge/`, `security/` | What may an agent know, and how do we build a corpus worth querying? |
| 3 | `agentic-engineering/` | How much autonomy do we actually want to allow? |
| 4 | `verification/` | What does it mean to demonstrate that generated code is correct? |
| 5 | `integration/` | What has to happen before we accept a change? |
| 6 | `governance/` | How do we keep this alive without turning it into bureaucracy? |

Implementation profiles follow, per stack.

## The original document

[`compiled/`](compiled/) holds the draft the corpus was derived from, frozen at
revision EN202608161000, in Markdown, DOCX and PDF.

It is a snapshot, not an output, and it will drift. The domain documents are
authoritative — see [AI-DEC-003](decisions/AI-DEC-003-invert-the-source-of-truth.md).
A build that compiles the corpus back into a single readable document does not
exist yet and is the reverse of `tools/split_framework.py`, which performed the
original split and is kept as provenance for it.

## Working on this repository

Rules for contributors and assistants working *on* this repository — as
distinct from the framework it contains — live under [`docs/ai/`](docs/ai/).
The framework asks for exactly that separation: reviewed, reusable engineering
instructions versioned alongside the work they govern, and private agent
configuration kept out.

- [Commit Convention](docs/ai/commits.md) — English, no emoji, no attribution
  trailers, one logical change per commit.

Agent skills under [`.claude/skills/`](.claude/skills/) turn the corpus into
behaviour. The documents describe the knowledge; the skills describe how to act
using it. Everything else under `.claude/` is private and untracked.

| Skill | Use it to |
|-------|-----------|
| [`navigate-engineering-knowledge`](.claude/skills/navigate-engineering-knowledge/SKILL.md) | Find the smallest authoritative set of documents a task needs |
| [`documentation-impact-analysis`](.claude/skills/documentation-impact-analysis/SKILL.md) | Decide whether a change affects documented behaviour, without editing |
| [`maintain-engineering-documentation`](.claude/skills/maintain-engineering-documentation/SKILL.md) | Update the corpus so it stays true, and keep the gate green |
| [`validate-knowledge-graph`](.claude/skills/validate-knowledge-graph/SKILL.md) | Audit identifiers, relationships and normative contradictions |
| [`commit`](.claude/skills/commit/SKILL.md) | Apply the commit convention |

Decision management and framework compilation are deliberately absent until the
first four have been used enough to know what they got wrong.

## Status

Draft. Under discussion. Not ratified, not adopted, not enforced.
