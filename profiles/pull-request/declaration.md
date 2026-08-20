---
id: AI-PROF-003
title: Draft Pull Request Declaration
status: proposed
domain: profiles
owners:
  - engineering
applies_to:
  - implementation-profile
related:
  - AI-GOV-006
source:
  - draft EN202608161000, Annex C
---

# Draft Pull Request Declaration

A template sketch for the author declaration, offered as material for the traceability discussion rather than as an adopted form.

<!-- nav:start -->
`AI-PROF-003` &middot; status **proposed** &middot; domain [`profiles/`](../)

**Related** &mdash; [Open Questions `AI-GOV-006`](../../governance/open-questions.md)

**Derived from** &mdash; [Annex C — Draft Pull Request Declaration](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#annex-c-%E2%80%94-draft-pull-request-declaration)
<!-- nav:end -->

---

Non-normative. This annex sketches how the traceability discussed in Part I could look in practice, so that the discussion has something concrete to react to. The categories below are a starting point for the conversation described in [the open questions](../../governance/open-questions.md), not an agreed list.

### Design intent

The declaration tries to capture the *kind and degree* of AI intervention that changes how a reviewer should read the change, rather than whether an assistant was involved at all. A field that everyone always ticks the same way carries no information and costs attention.

Two ideas are worth testing during review:

* Only categories that change reviewer behaviour are worth declaring.
* Where the information can be derived automatically — for example from commit trailers, agent tooling or branch metadata — it should be, rather than asked of the author again.

### Sketch: `.github/pull_request_template.md`

```markdown
## Summary

<what changes and why; link the ticket>

## AI involvement

Tick anything that applies. Leave everything unticked if assistance was
limited to routine completion or explanation.

- [ ] Substantial agent-generated change (an agent produced a significant
      part of the diff rather than isolated fragments)
- [ ] AI-generated tests
- [ ] AI-generated synthetic or fixture data
- [ ] AI-assisted data or schema migration
- [ ] AI-assisted change to security-sensitive code
      (authentication, authorization, cryptography, tenant isolation,
      secrets handling, input validation at a trust boundary)
- [ ] AI-assisted change to CI, infrastructure or deployment configuration

Human owner: <name>

## Verification

- [ ] Material authored changes reviewed and explainable by the author
- [ ] Generated artifacts identified, and validated through their generator,
      contract or tests rather than line by line
- [ ] Tests added or updated; suite passes locally
- [ ] Static analysis and quality gate pass
- [ ] Documentation and ADRs updated where behaviour or architecture changed
- [ ] New dependencies reviewed (existence, identity, licence, advisories)
- [ ] No credentials, secrets or real personal data introduced

Independent evidence relied on: <acceptance criteria, contract, schema,
golden dataset, existing specification, ...>

## Risk notes for the reviewer

<anything the reviewer should look at first: assumptions made, areas the
author is least sure about, behaviour intentionally changed>
```

### Points to settle before this is adopted

* Whether the categories above are the right ones, and whether any of them can be derived automatically instead of declared.
* Whether the security-sensitive category should route the Pull Request to a specific reviewer group.
* Whether the "risk notes" field is genuinely useful or will decay into boilerplate.
* How this interacts with existing templates and with the checklist in Part I, so that the same thing is not asked twice.
