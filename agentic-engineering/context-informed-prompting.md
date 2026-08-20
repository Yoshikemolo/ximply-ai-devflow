---
id: AI-AGT-002
title: Context-Informed Prompting Protocol
status: proposed
domain: agentic-engineering
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  - AI-SEC-002
source:
  - draft EN202608161000, section 20
---

# Context-Informed Prompting Protocol

How a task is framed before an agent starts: the context injected, the constraints stated, and the checkpoints defined. This is where minimum necessary context stops being a policy and becomes a practice.

---

Prompting is an engineering activity that benefits from method. Open-ended prompts tend to produce generic code that ignores the architecture of the system; constrained prompts tend to produce work that fits it and can be reviewed.

### Constraint injection

Every structural prompt SHOULD state, explicitly:

1. The role and stack (framework, language version, runtime).
2. The applicable architectural constraints, referenced by ADR identifier where one exists.
3. The layer and the boundaries the code must respect.
4. The mechanisms that MUST be used (existing abstractions, interfaces, conventions).
5. The mechanisms that MUST NOT be used.
6. The expected error handling, logging and validation behaviour.
7. The expected tests.

**Compliant example**

```text
Act as a senior .NET engineer working under ADR-2026-04 (event-driven isolation).
Write a command handler that processes an invoice.
Constraints:
- Do not instantiate or inject a DbContext in this handler.
- Publish all state changes through the existing IEventBus abstraction.
- Use the project's Result<T> error type; do not throw for expected validation failures.
- Log through the existing ILogger abstraction; no new telemetry conventions.
- Provide xUnit tests covering the invalid-invoice and duplicate-event cases.
```

**Non-compliant example**

```text
Write me an invoice processing service.
```

### Decomposition, and feature-scale work

The behaviour worth ruling out is the unconstrained one:

> Complete features MUST NOT be implemented as a single unconstrained generation step whose output is accepted wholesale.

That is different from saying an assistant may not work at feature scale. A capable agent can carry a complete feature when the work is decomposed, a plan exists, checkpoints are verified as it proceeds, and a human controls the result. What makes it acceptable is the structure around it, not the size of the task:

1. The engineer establishes the requirement, the acceptance criteria and the architectural constraints.
2. The work is broken into units that can be verified independently.
3. The assistant implements a unit; tests and checks run at that checkpoint.
4. The engineer inspects the result before the next unit builds on it.
5. Integration into the architecture, and responsibility for the whole, stay with the engineer.

The purpose is to keep the diff reviewable and to localize the blast radius of an incorrect assumption — the same intent as the small-batch section elsewhere in Part I.

> **Discussion point.** Where the line falls between "planned and checkpointed feature-scale work" and "one unconstrained generation step" deserves a concrete definition, ideally expressed as what a checkpoint has to produce.

### Comprehension of what is submitted

The proposed expectation is that an engineer who submits AI-generated code can explain, during review, every **material authored change** it contains, including:

* Why each dependency and abstraction is used.
* The failure modes and error paths.
* The concurrency, transaction and lifetime assumptions.
* The security implications.
* Why the chosen approach is appropriate for this system.

If a material part of the change cannot be explained by its human owner, the reasonable default is that it does not merge until it can.

**Generated artifacts are a separate case.** Migration scaffolding, generated API clients, schemas, lockfiles, snapshots and bulk fixtures are not read line by line by anyone, and a rule that pretends otherwise is one people quietly ignore. The suggestion is to hold a different expectation for them: the engineer chose the generator and its inputs, can explain what it produces and why, and the output is validated by contract, schema or test rather than by reading. Anything hand-edited afterwards returns to being a material authored change.

> **Discussion point.** Which categories count as generated artifacts differs per stack, and the boundary is worth writing down per repository rather than in the abstract.

### Session hygiene

* Context provided to an assistant MUST respect the AI context boundary described in Part I.
* Long sessions SHOULD be restarted when the assistant begins contradicting known constraints, as accumulated context increases drift. Accumulated context also raises a confidentiality question, addressed as context aggregation risk in [Agentic Security Boundary](../security/agentic-security-boundary.md).
* Statements produced by an assistant about the state of the repository, the behaviour of a dependency or the result of a command MUST be verified against the repository or the command output before being acted upon.
