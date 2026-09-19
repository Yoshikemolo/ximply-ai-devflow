---
id: AI-VER-004
title: Property-Based and Mutation Testing
status: accepted
domain: verification
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 41
  - draft EN202608161000, section 42
---

# Property-Based and Mutation Testing

Techniques that check the test suite rather than the implementation, and that become more valuable as the volume of generated code grows.

<!-- nav:start -->
`AI-VER-004` &middot; status **accepted** &middot; domain [`verification/`](./)

**Derived from** &mdash; [section 41. Property-Based and Invariant Testing](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#41-property-based-and-invariant-testing) &middot; [section 42. Mutation Testing](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#42-mutation-testing)
<!-- nav:end -->

---

## Property-Based and Invariant Testing

Where applicable, important business properties SHOULD be expressed independently from concrete examples.

Examples:

```text
authorization never crosses tenant boundaries
serialization round-trip preserves the domain value
sorting never changes the item set
retry does not duplicate a committed operation
migration preserves all valid entities
```

Property-based testing is particularly useful for AI-assisted development because it checks a broader input space than examples generated during the same reasoning session.

---

## Mutation Testing

For high-risk logic, teams SHOULD consider mutation testing or equivalent techniques to evaluate whether tests can actually detect incorrect implementations.

Coverage indicates that code executed.

It does not prove that assertions would detect a defect.

Mutation analysis can reveal apparently well-covered code whose tests do not meaningfully validate behavior.
