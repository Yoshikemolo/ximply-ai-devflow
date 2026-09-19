---
id: AI-FND-003
title: Context Economy
status: accepted
domain: ai-foundations
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 7
---

# Context Economy

Attention is finite and degrades with volume. A large corpus helps only if it can be consumed in small, high-signal pieces, which is what makes the rest of the conceptual chain necessary rather than merely tidy.

<!-- nav:start -->
`AI-FND-003` &middot; status **accepted** &middot; domain [`ai-foundations/`](./)

**Derived from** &mdash; [section 7. Context Economy: Coherence, Degradation and Model Fit](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#7-context-economy-coherence-degradation-and-model-fit)
<!-- nav:end -->

---

The previous section deals with how an assistant's answers can mislead. This one deals with the material it is answering from, and with a resource that engineering teams tend to treat as free: the context itself.

Context is finite, and it degrades. Not only in a single session, but across the corpus the organization keeps feeding its agents — documentation, ADRs, comments, tickets, prior conversations. A codebase whose narrative contradicts itself will make every agent working on it worse, and will do so silently.

### Context is a budget, not a container

Published evaluations converge on a result that matters for daily work: model accuracy declines as input length grows, well before the documented context limit, across every frontier model tested. The effect is not uniform — information placed in the middle of a long context is retrieved markedly worse than information at the beginning or the end. Attention behaves like a budget that every token draws on, with diminishing returns.

The practical consequence is the opposite of the intuition a large context window invites:

* The objective SHOULD be the **smallest set of high-signal tokens** that makes the task solvable, not the largest set that fits. This is the same principle as the minimum-necessary-context rule stated for confidentiality reasons in the context-boundary section, arriving from the direction of quality rather than security.
* Filling a context window because it is available MUST NOT be treated as thoroughness. It is a measurable reduction in the assistant's reliability, paid for in tokens.
* Where a task genuinely needs a large corpus, retrieval SHOULD be selective rather than exhaustive: pull the relevant pieces at the moment they are needed, using stable identifiers — file paths, symbol names, ADR identifiers, ticket references — rather than loading everything in advance.

### Session length and agent proliferation

Long sessions accumulate more than information. They accumulate superseded decisions, abandoned approaches, corrected mistakes and contradictory instructions, all of which remain in context competing with what is currently true. Multi-agent setups add a second axis: every additional agent carries coordination context, and their combined output can exceed what any of them can usefully hold.

* Sessions SHOULD be brought to a close at natural boundaries — a completed unit of work, a merged change, a shift in subject — rather than run indefinitely. This complements the session-hygiene guidance already given for prompting.
* When a session must continue past the point where its history is mostly noise, it SHOULD be compacted deliberately: a summary of what was decided, what is done, what is in progress and what is blocked, carried into a fresh context, with the working state captured in the repository rather than in the conversation.
* Where sub-agents are used, they work best when each returns a **condensed result** rather than its full working context. A sub-agent that hands back everything it read has moved the problem, not solved it.
* More agents is not more capability. Each one added SHOULD earn its place by isolating work that would otherwise pollute the main context.

### Corpus coherence: descriptive documents and normative ones

The context an agent reads is not only what the engineer types. It is the repository: comments, documentation, ADRs, README files, ticket descriptions. When that narrative drifts away from the code, the agent inherits the drift — and, unlike a developer who knows a comment is old, it has no way to date the claim.

Stale comments are not a cosmetic problem. Code–comment inconsistency is associated with misunderstanding, longer debugging and bug introduction, which is why it is an active research area in its own right. An assistant will read a confident but obsolete comment as a statement of fact about code it contradicts.

Which side wins a contradiction depends on what kind of document is contradicting the code, and the distinction is worth drawing sharply:

* **Descriptive documents** claim what the system *does*: comments, README sections, architecture overviews, runbooks, generated references. Against these, the code, the tests and the observed output are authoritative. A descriptive document that disagrees with the implementation is out of date, and the correction belongs in the document.
* **Normative documents** state what the system *must* do: approved specifications, accepted ADRs, contracts and schemas, acceptance criteria, security and regulatory requirements. These are authoritative about intent. When the implementation disagrees with one of them, the defect is more likely in the code — and the resolution is a decision rather than a correction: either the implementation is brought back into line, or the specification is changed deliberately and recorded as such.

> **Observed behaviour is authoritative about what the system does. An approved specification is authoritative about what it should do.** Where the two diverge, one of them contains a defect, and deciding which is a human judgement — it MUST NOT be silently resolved by an agent in either direction.

* Documents SHOULD make their kind evident — description, intent, or requirement. The damaging case is not the stale document but the one whose kind is ambiguous: a plan is a legitimate document, a plan mistaken for a description is a trap, and a description mistaken for a requirement is worse.
* Contradictions between the corpus and the implementation SHOULD be treated as defects to be resolved rather than ambiguities to be worked around — in whichever of the two the defect turns out to be.
* Reusable AI instructions SHOULD state this priority explicitly, so that the outcome does not fall to whichever text happens to appear later in the context. An instruction that quietly resolves the contradiction in favour of the prose is worse than no instruction; so is one that quietly assumes the code must be right.

### What comments are for

Code is largely self-explanatory to a competent reader, and modern assistants read it well. A comment that restates what the code already says adds nothing, and takes on a maintenance obligation it will eventually fail.

Comments earn their place when they carry what the code **cannot** express:

* Intent and the reason a non-obvious approach was chosen.
* Invariants and preconditions the type system does not capture.
* Constraints imposed from outside — hardware behaviour, protocol quirks, regulatory requirements, a third-party bug being worked around.
* Trade-offs accepted deliberately, and what would have to change to revisit them.
* Pointers to the authoritative source: the ADR, the ticket, the specification section.
* Warnings about consequences that are not visible locally.

Excess commentary carries three costs at once: it makes the code harder to read, it drifts into contradiction as the code evolves, and it consumes context that would be better spent on the problem being solved. The clean-code expectations elsewhere in Part I already exclude commented-out code and dead explanation; this section adds the reason that has become sharper with AI-assisted work — every redundant line of prose in a file is paid for again on every retrieval.

### Fitting the model to the task

Not every task deserves the strongest available model, and using one indiscriminately is not a neutral choice.

* Mechanical and well-specified work — translation, formatting, renaming, mechanical refactors, boilerplate, simple extraction — SHOULD be given to a small, fast model. It is cheaper, it is quicker, and on this class of task it is not measurably worse.
* Work that requires judgement — architecture and design analysis, security reasoning, reviewing an unfamiliar diff, debugging with ambiguous symptoms, evaluating a document — SHOULD be given to the strongest model available, because the failure mode of an undersized model here is confident shallowness that still has to be reviewed.
* Routing work to the smallest sufficient model is a well-documented cost reduction, but cost is not the main argument. A right-sized model produces a tighter answer with less elaboration to wade through, which keeps both the context and the engineer's attention available for the parts that need them.
* Teams SHOULD make this an explicit habit rather than a default setting, and MAY document per-task guidance in `/docs/ai` alongside the other engineering instructions.

### Making the corpus navigable

The most effective way to spend less context is to stop reading everything. An agent that can *find* does not need to be *given*.

* Repositories SHOULD expose structure that an agent can traverse: a symbol and call graph, an import graph, or a ranked repository map built from the syntax tree. Published implementations of this pattern — structural indexes exposed to agents as query tools — report order-of-magnitude reductions in tokens consumed and roughly half the tool calls, because each retrieval returns a meaningful unit rather than an arbitrary chunk of text.
* Full-text and symbol search, including n-gram or trigram indexes, SHOULD be available to agents as a first move, before file reading.
* Documentation SHOULD be structured so that a single relevant section can be retrieved without its containing document: stable headings, one subject per file, explicit identifiers.
* The repository SHOULD offer an entry map — what exists, where, and what to read for a given kind of task — so that the first minutes of a session are not spent rediscovering the layout. The README and `/docs` structure described earlier in Part I serve exactly this purpose, and are worth maintaining for agents as much as for people.
* Where an internal MCP layer exists, exposing these structural queries as tools is one of its highest-value uses, and fits inside the boundaries set for organization-owned tooling.

### Working recommendations

**In the prompt**

* State the task, the constraints and the definition of done; leave the approach open unless the approach is the constraint.
* Point at evidence rather than pasting it: file paths, symbol names, ADR and ticket identifiers.
* Ask for the assessment before the implementation on anything non-trivial, so that a wrong premise is caught before code is written on top of it.
* Avoid embedding the expected conclusion, for the reasons given in the preceding section.
* Ask explicitly for uncertainty and for what was not checked; an assistant will rarely volunteer either.

**In the context**

* Provide the minimum that makes the task solvable, and prefer interfaces, contracts and representative examples over complete implementations.
* Keep instructions short and current. Long instruction files compete for the same attention budget as the problem, and contradict each other as they grow.
* Remove superseded material rather than appending corrections to it.
* Keep documentation, comments and ADRs consistent with the code, and fix contradictions when they are found rather than routing around them.
* Preserve context for the problem. Reiteration, redundant prose and unnecessary file dumps are paid for in the quality of the answer, not only in tokens.

> **Discussion point.** Two of these are cheap to adopt immediately — evidence over narrative, and fitting the model to the task. Two need a decision: whether we invest in a structural index or repository map for the main codebases, and whether cross-model confrontation becomes an expected step for security-relevant or architectural work or stays at each engineer's discretion.

### References

Consulted while drafting this section; listed so that the claims above can be checked rather than taken on trust.

* Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL 2024 — position-dependent retrieval degradation.
* Chroma Research, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*, 2025 — degradation measured across 18 frontier models: <https://research.trychroma.com/context-rot>
* Anthropic, *Effective context engineering for AI agents*, 2025 — attention budget, just-in-time retrieval, compaction, sub-agent condensation: <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
* Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR 2024: <https://arxiv.org/abs/2310.01798>
* Du et al., *Improving Factuality and Reasoning in Language Models through Multiagent Debate*, 2023: <https://composable-models.github.io/llm_debate/>
* *Investigating the Impact of Code Comment Inconsistency on Bug Introducing*, 2024: <https://arxiv.org/pdf/2409.10781>
* *Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP*, 2026 — reported token and tool-call reductions from structural indexing: <https://arxiv.org/abs/2603.27277>
* RouteLLM and FrugalGPT — cost/quality results for routing to smaller models: <https://arxiv.org/abs/2406.18665>, <https://arxiv.org/abs/2305.05176>
