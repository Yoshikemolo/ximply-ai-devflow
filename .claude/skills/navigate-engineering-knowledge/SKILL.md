---
name: navigate-engineering-knowledge
description: Retrieve the smallest authoritative set of documents needed to answer a question or perform a task in this framework corpus. Use whenever you need to know what the framework says - about AI context, autonomy, verification, review, security, testing, governance - before answering, planning or changing anything. Also use when asked to cite a rule, resolve what applies to a change, or find the document behind an identifier.
---

# Navigate engineering knowledge

Retrieve the **smallest authoritative set** of documents required for the task
at hand, and cite what you used.

This is not "read the documentation". Reading everything is the failure mode
the corpus was built to prevent: attention is finite and degrades with volume,
so a large corpus helps only when it is consumed in small, high-signal pieces.
See `ai-foundations/context-economy.md`.

## Where to start

Never start with a broad search. Start with an index:

| You need | Start at |
|---|---|
| Anything, first time | `README.md` - domain table and question-to-document index |
| A rule about working in this repository | `CONTRIBUTING.md`, `docs/ai/` |
| What is undecided | `governance/open-questions.md` |
| Why something is the way it is | `decisions/` |
| A document whose identifier you have | Search the identifier, see below |

Resolve an identifier directly rather than guessing a path:

```bash
grep -rl "^id: AI-SEC-001" --include="*.md" .
```

## Identifier scheme

```text
AI-<DOMAIN>-NNN   a domain document      AI-SEC-001, AI-KNOW-005
OQ-NNNN           an open question       OQ-0011
AI-DEC-NNN        a decision record      AI-DEC-003
```

Domain prefixes: `PRIN`, `FND`, `KNOW`, `SEC`, `AGT`, `VER`, `INT`, `CHG`,
`GOV`, `PROF`, `DEC`.

Cite documents by identifier, not by path. Paths move; identifiers do not.

## Following relationships

Every document opens with a navigation header linking what it relates to. The
relationships that exist in this corpus today are:

```text
related     documents this one links to or depends on for meaning
affects     (questions only) documents that change if the question is answered
supersedes  (decision records) the record this one replaces
applies_to  a scope tag, not a link - do not traverse it
```

Follow a relationship only when the task needs it. Two hops from an index is
usually enough; if you are four documents deep, you are probably reading rather
than retrieving.

`depends-on` and `conflicts-with` do not exist yet. Do not invent them, and do
not report them as if the corpus declared them - that scheme is still open in
`OQ-0011`.

## Rules

1. **Minimum necessary context.** Retrieve what the task requires, then stop.
   A large context window is not permission to load more.
2. **Stop when the evidence is sufficient**, not when the corpus is exhausted.
3. **Prefer the authoritative document over a summary of it.** Never answer a
   question about what the framework requires from `compiled/`, from a commit
   message, or from memory of an earlier session.
4. **Check `status` before quoting.** Everything in this corpus is currently
   `proposed` and nothing is in force. Say so when it matters: "the framework
   proposes X" is accurate, "the framework requires X" is not.
5. **A question is not an answer.** An `open` question under
   `governance/open-questions/` records what has not been decided. Its
   "Provisional position" is a reading aid, never a rule to apply.
6. **Follow supersession.** If a decision record is superseded, read the record
   that replaced it and cite that one.
7. **Report conflicts, never resolve them.** If two authoritative documents
   disagree, say so, name both identifiers, and stop. Resolving a normative
   conflict is a human decision - see `principles/human-accountability.md`.
8. **Cite your evidence.** End with the identifiers you actually used.

## Output

When the retrieval is the answer, close with the evidence:

```text
Evidence: AI-SEC-001, AI-SEC-002, OQ-0008
```

List only documents you read. An identifier you did not open is not evidence.

## Do not

- Load the whole corpus, or `compiled/`, to answer a scoped question.
- Read a domain directory exhaustively when the index names the document.
- Quote `compiled/` as authoritative. It is a frozen snapshot that will drift;
  the domain documents are the source. See `AI-DEC-003`.
- Present a provisional position, a discussion point, or your own inference as
  what the framework says.
