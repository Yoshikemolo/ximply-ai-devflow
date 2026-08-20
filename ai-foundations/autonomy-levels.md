---
id: AI-FND-004
title: AI Autonomy Levels
status: proposed
domain: ai-foundations
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 11
---

# AI Autonomy Levels

Shared vocabulary for how much an agent is permitted to do without a human step. The levels are defined here because several domains refer to them; where they are granted and enforced belongs to the agentic engineering domain.

<!-- nav:start -->
`AI-FND-004` &middot; status **proposed** &middot; domain [`ai-foundations/`](./)

**Derived from** &mdash; [section 11. AI Autonomy Levels](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#11-ai-autonomy-levels)
<!-- nav:end -->

---

The idea here is that each project states, explicitly, how much autonomy it grants AI development tools, instead of leaving it implicit and discovering it during an incident.

> **Discussion point.** The levels below are a proposed vocabulary. Which level fits which repository class — and whether these four levels map cleanly onto the agent tooling in use — is exactly the kind of thing to settle in review.

### Level 0 — Advisory

AI can:

* Explain code.
* Analyze architecture.
* Suggest changes.
* Propose tests.
* Draft documentation.

AI cannot modify repository files.

---

### Level 1 — Workspace Modification

AI can:

* Modify files in a developer-controlled workspace.
* Generate tests.
* Execute approved local tools.

A developer reviews all modifications before committing them.

---

### Level 2 — Isolated Branch Agent

AI may operate on an isolated working branch where organizational tooling supports it.

The branch:

* MUST NOT be a shared development branch.
* MUST NOT be a release branch.
* MUST NOT be production-related.
* MUST remain associated with a human owner.

Any Pull Request produced by an agent MUST remain subject to human review and approval.

---

### Level 3 — Controlled Engineering Agent

AI may:

* Execute builds.
* Execute tests.
* Execute approved harnesses.
* Perform static analysis.
* Propose fixes.
* Update documentation.
* Prepare a Pull Request.

It MUST NOT cross the human integration boundary.
