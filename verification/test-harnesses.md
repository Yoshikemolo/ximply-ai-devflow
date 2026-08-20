---
id: AI-VER-005
title: Test Harnesses and Harness Independence
status: proposed
domain: verification
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 43
  - draft EN202608161000, section 44
---

# Test Harnesses and Harness Independence

The executable environment in which evidence is produced, and why the harness must not be authored by the same process it is meant to judge.

<!-- nav:start -->
`AI-VER-005` &middot; status **proposed** &middot; domain [`verification/`](./)

**Derived from** &mdash; [section 43. Test Harnesses](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#43-test-harnesses) &middot; [section 44. Harness Independence](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#44-harness-independence)
<!-- nav:end -->

---

## Test Harnesses

Repositories SHOULD contain deterministic harnesses capable of verifying system behavior independently of developer interpretation.

Recommended:

```text
/harness/
├── api/
├── integration/
├── contracts/
├── security/
├── performance/
├── migration/
└── regression/
```

Harnesses may validate:

* API behavior.
* Database migrations.
* Data ingestion.
* Serialization.
* Business rules.
* Authorization.
* Authentication.
* Tenant isolation.
* File processing.
* Event processing.
* External integrations.
* Performance thresholds.
* Regression behavior.

Harnesses SHOULD run automatically in CI where practical.

---

## Harness Independence

Harness expectations SHOULD preferably be defined from specifications, contracts or known invariants.

The implementation under test MUST NOT silently redefine its own acceptance oracle.

For critical workflows, the same AI session SHOULD NOT be considered sufficient authority for:

1. Requirement interpretation.
2. Implementation.
3. Test oracle.
4. Acceptance decision.

Human-defined requirements and independent executable checks create the necessary separation.
