---
id: AI-VER-002
title: Testing Strategy
status: accepted
domain: verification
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 28
  - draft EN202608161000, section 29
  - draft EN202608161000, section 30
  - draft EN202608161000, section 31
  - draft EN202608161000, section 32
  - draft EN202608161000, section 33
  - draft EN202608161000, section 34
---

# Testing Strategy

How test effort is allocated against risk, what each test level is evidence of, and what changes when the tests are themselves AI-generated. One document because these choices are made together, not one level at a time.

<!-- nav:start -->
`AI-VER-002` &middot; status **accepted** &middot; domain [`verification/`](./)

**Derived from** &mdash; [section 28. Risk-Based Test Portfolio](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#28-risk-based-test-portfolio) &middot; [section 29. Unit Tests](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#29-unit-tests) &middot; [section 30. Integration Tests and Real Dependencies](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#30-integration-tests-and-real-dependencies) &middot; [section 31. Contract Testing](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#31-contract-testing) &middot; [section 32. End-to-End Tests](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#32-end-to-end-tests) &middot; [section 33. Test Maintenance](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#33-test-maintenance) &middot; [section 34. AI-Assisted Test Generation](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#34-ai-assisted-test-generation)
<!-- nav:end -->

---

## Risk-Based Test Portfolio

Projects SHOULD maintain a test portfolio appropriate to their architecture rather than blindly optimizing for a fixed test pyramid.

The portfolio may include:

```text
Unit tests
Component tests
Integration tests
Contract tests
Property-based tests
Regression tests
End-to-End tests
Security tests
Performance tests
Resilience tests
Migration tests
Compatibility tests
```

The appropriate combination depends on:

* Business risk.
* Architectural boundaries.
* Cost of failure.
* Integration complexity.
* Change frequency.
* Security relevance.

---

## Unit Tests

Unit tests SHOULD:

* Remain fast.
* Remain deterministic.
* Test behavior rather than implementation detail.
* Focus on business rules.
* Include boundary conditions.
* Avoid unnecessary mocking.
* Produce useful failure messages.

Tests SHOULD NOT be changed simply to make an incorrect implementation pass.

When existing behavior changes intentionally, the requirement must justify the corresponding test change.

---

## Integration Tests and Real Dependencies

Where practical, integration tests SHOULD use real implementations of important infrastructure dependencies rather than behavioral imitations.

Examples:

* PostgreSQL.
* Redis.
* RabbitMQ.
* Kafka.
* Keycloak-compatible identity services.
* Object storage.
* Real serialization mechanisms.

Ephemeral containerized dependencies are preferred when they improve reproducibility and isolation.

Each test environment SHOULD start from a known state.

Shared mutable integration environments SHOULD be avoided because they introduce configuration drift and non-determinism.

---

## Contract Testing

Distributed architectures SHOULD consider automated contract testing.

Contract tests are particularly appropriate for:

* REST APIs.
* Event contracts.
* Microservices.
* Frontend/backend integration.
* Independently deployable services.

Where applicable, consumer/provider contracts SHOULD be validated during CI.

Contract compatibility can detect integration breakage earlier and more efficiently than relying exclusively on broad End-to-End suites.

---

## End-to-End Tests

E2E tests SHOULD validate high-value business workflows.

They SHOULD NOT become the primary mechanism for validating every possible behavior.

Good E2E candidates include:

* Authentication.
* Authorization.
* Critical workflows.
* Cross-service flows.
* Persistence.
* Main user journeys.
* Regression scenarios affecting several components.

E2E test failures MUST produce enough information to diagnose the affected step.

---

## Test Maintenance

Tests are production engineering assets.

They MUST be maintained with the same discipline as implementation code.

The team SHOULD regularly identify:

* Flaky tests.
* Duplicate tests.
* Obsolete tests.
* Slow tests.
* Tests without meaningful assertions.
* Excessive mocks.
* Tests coupled to implementation details.
* Uncovered business invariants.

A test SHOULD NOT be removed merely because an AI-generated implementation causes it to fail.

The engineer must first determine whether:

1. The test is incorrect or obsolete.
2. The requirement changed.
3. The implementation contains a regression.

---

## AI-Assisted Test Generation

AI is particularly useful for expanding test coverage.

AI MAY propose:

* Boundary conditions.
* Invalid inputs.
* Failure cases.
* Property-based tests.
* Security cases.
* Concurrency scenarios.
* State transitions.
* Regression cases.
* Contract tests.
* Mutation candidates.

However:

> **Generated test quantity is not a quality metric.**

Test quality depends on the behaviors and risks detected, not the number of test cases produced.
