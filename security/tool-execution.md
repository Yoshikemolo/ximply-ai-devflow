---
id: AI-SEC-003
title: Shell and Tool Execution
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - agentic-tooling
related:
  - AI-AGT-003
source:
  - draft EN202608161000, section 22
---

# Shell and Tool Execution

What an agent is allowed to do. Where the context boundary governs information, this governs action: which commands and tools may execute, under whose identity, and with what approval.

<!-- nav:start -->
`AI-SEC-003` &middot; status **proposed** &middot; domain [`security/`](./)

**Related** &mdash; [Local Models and Organization-Owned Agentic Tooling `AI-AGT-003`](../agentic-engineering/local-and-corporate-agents.md)

**Derived from** &mdash; [section 22. Shell and Tool Execution](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#22-shell-and-tool-execution)
<!-- nav:end -->

---

AI agents capable of executing commands SHOULD run inside a constrained environment.

High-risk actions require explicit human control.

Examples include:

```text
rm
git reset --hard
git push --force
database destructive commands
infrastructure changes
credential operations
package publication
container registry publication
deployment commands
```

Automatic approval of command execution MUST NOT be enabled for work on organizational repositories or systems. [Local Models and Organization-Owned Agentic Tooling](../agentic-engineering/local-and-corporate-agents.md) covers auto-approval modes and the curated allow-list that replaces them.

Command output MUST be treated as evidence, not as truth beyond what the command actually verifies.
