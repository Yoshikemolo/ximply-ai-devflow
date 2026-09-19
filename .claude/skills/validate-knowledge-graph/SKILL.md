---
name: validate-knowledge-graph
description: Audit the corpus for structural and semantic coherence - identifiers, relationships, links, reachability, status consistency and normative contradictions between documents. Use before opening a Pull Request, when the corpus gate fails, after restructuring, or when asked whether the documentation still hangs together.
---

# Validate knowledge graph

Audit the corpus. Two passes, in this order: what a machine can check, then
what only reading can.

Running the second without the first wastes effort on a corpus that is already
broken in ways the gate would have named in a second.

## Pass 1 - mechanical

```bash
python tools/check_corpus.py
python tools/render_headers.py --check
python tools/render_summary.py --check
python tools/split_framework.py --check
```

What these already verify:

```text
front matter present and parseable, with the fields its document type requires
identifiers unique, well-formed, and matching the domain directory
status drawn from the vocabulary for that document type
related, affects and supersedes all resolving to real documents
every relative link resolving to a real file
every link fragment resolving to a real heading in its target
every document reachable by following links from README.md
navigation headers agreeing with the front matter they came from
the summary map agreeing with the documents it was derived from
links and anchors in README, CONTRIBUTING and the summary map
every section of the trunk document still having a home
```

A failure here is a defect, not a matter of opinion. Fix the cause. Never
edit a generated file to make the gate pass, and never weaken a check to
accommodate a document.

### What the gate does not check yet

Do these by reading, and report them as findings:

```text
circular supersession        A supersedes B supersedes A
stale supersession           a superseded document still cited as current
retired identifiers          references to an id no longer in the corpus
status coherence             an accepted document resting on an open question
orphan reachability quality  reachable, but only from a directory listing
owner presence               owners naming a person or team that still exists
```

If any of these turns out to be mechanically checkable, that is a better
outcome than finding it by hand. Say so in the report.

## Pass 2 - semantic

Read for contradictions between documents that each look correct alone. This
is the pass a script cannot do, and the reason the skill exists.

Look for:

- **Normative conflict.** Two documents stating incompatible requirements.
- **Silent drift.** A document describing a practice another document replaced.
- **Scope collision.** Two documents claiming authority over the same subject,
  which usually means the split was wrong.
- **Duplicated statement.** The same fact asserted in two places. It is not yet
  a contradiction; it is where the next one will come from.
- **Unanchored claim.** A document asserting something the corpus never
  established, and no `source` or `related` supporting it.
- **A derived view asserting something.** `summary/README.md` and `compiled/`
  must state nothing of their own. If the map carries a requirement, a caveat or
  an explanation that no linked document states, that is a defect in
  `tools/render_summary.py` and it is the most serious finding in this list: a
  second source of truth is exactly what the map exists to prevent.

The map is regenerated, so never fix it by editing it. Fix the document it was
derived from, or the generator, and regenerate.

Report a conflict like this:

```text
POTENTIAL NORMATIVE CONFLICT

  AI-SEC-004  states that external models MAY receive proprietary code under
              condition X.
  AI-SEC-001  appears to prohibit proprietary code reaching external models.

  Both are status: accepted. Neither supersedes the other.

  Do not resolve automatically. Human decision required.
  Closest open question: OQ-0008.
```

## The rule that governs the whole skill

> **Detect, do not resolve.**

A normative conflict between two authoritative documents is a human decision.
Choosing the one that reads better, or quietly editing one to agree with the
other, destroys the evidence that the corpus needed a decision - and produces
a corpus that looks coherent while nobody has agreed to what it now says. See
`principles/human-accountability.md`.

Structural defects are different: a dangling link or a malformed identifier
has one correct answer and may be fixed directly, with
`maintain-engineering-documentation`.

## Output

```text
Corpus validation

Mechanical:  passed - 66 documents, 66 identifiers
             (or: 3 failures, listed with the command that found them)

Derived views:  the map states nothing the corpus does not

Structural findings:  2
  - AI-GOV-004 lists an owner that no longer exists.
  - OQ-0007 is reachable only through the index directory listing.

Semantic findings:  1
  - Potential normative conflict between AI-SEC-001 and AI-SEC-004.

Nothing was changed. 1 finding requires a human decision.
```

Say plainly when a pass finds nothing. A clean corpus is a result.

## Rules

1. **Mechanical first.** Do not begin reading until the gate passes or its
   failures are understood.
2. **Detect, do not resolve** - for anything normative.
3. **Name both sides.** A conflict report with one identifier is not a
   conflict report.
4. **Do not weaken a check.** If the gate is wrong, that is a defect in the
   gate; fix it, and say what changed.
5. **Distinguish confidence.** "Contradicts" and "appears to contradict" are
   different claims. Use the one you can defend.
6. **A finding you cannot substantiate is noise.** Drop it.

## Do not

- Edit documents to make the audit come out clean.
- Resolve a normative conflict, however obvious the answer seems.
- Report every keyword coincidence as a semantic finding.
- Change `status` on anything. Status moves through decision records.
