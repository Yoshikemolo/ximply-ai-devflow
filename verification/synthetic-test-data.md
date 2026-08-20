---
id: AI-VER-003
title: Synthetic and Generated Test Data
status: proposed
domain: verification
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 35
  - draft EN202608161000, section 36
  - draft EN202608161000, section 37
  - draft EN202608161000, section 38
  - draft EN202608161000, section 39
  - draft EN202608161000, section 40
---

# Synthetic and Generated Test Data

Generated fixtures and mock data are engineering assets with a provenance, a safety boundary and a validation requirement. They are not disposable output.

<!-- nav:start -->
`AI-VER-003` &middot; status **proposed** &middot; domain [`verification/`](./)

**Derived from** &mdash; [section 35. AI-Generated Mock and Synthetic Test Data](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#35-ai-generated-mock-and-synthetic-test-data) &middot; [section 36. Synthetic Data Safety Rules](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#36-synthetic-data-safety-rules) &middot; [section 37. Synthetic Data Provenance](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#37-synthetic-data-provenance) &middot; [section 38. Scenario-Based Test Data](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#38-scenario-based-test-data) &middot; [section 39. Synthetic Data Validation](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#39-synthetic-data-validation) &middot; [section 40. Golden and Regression Datasets](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#40-golden-and-regression-datasets)
<!-- nav:end -->

---

## AI-Generated Mock and Synthetic Test Data

AI MAY generate synthetic or mock data when real data is unnecessary, unavailable, sensitive, expensive or operationally difficult to obtain.

Examples include:

* API responses.
* Database fixtures.
* Domain entities.
* Events.
* Files.
* Telemetry.
* Images.
* Inspection measurements.
* Error cases.
* Edge cases.

Generated data MUST respect the actual domain constraints.

---

## Synthetic Data Safety Rules

Synthetic data used for testing SHOULD be:

* Artificial.
* Reproducible.
* Clearly identified.
* Schema-valid.
* Domain-valid where required.
* Free from production credentials.
* Free from real customer PII.
* Free from confidential information.

Production datasets MUST NOT simply be provided to an external AI model for transformation into "mock data".

Where production-derived data is required, an approved sanitization or anonymization process MUST precede AI processing.

---

## Synthetic Data Provenance

Important generated datasets SHOULD record how they were produced.

Recommended metadata includes:

```text
generator
generator version
generation date
schema version
seed
scenario
constraints
source classification
validation status
```

For deterministic generators, a seed SHOULD be stored.

Example:

```json
{
  "generator": "inspection-fixture-generator",
  "version": "1.4.0",
  "seed": 381902,
  "schema": "scan-zone-v3",
  "scenario": "corrosion-boundary-cases",
  "containsRealCustomerData": false
}
```

This allows failures to be reproduced.

---

## Scenario-Based Test Data

Synthetic data SHOULD not be generated randomly without engineering purpose.

Datasets SHOULD represent scenarios such as:

```text
nominal
minimum
maximum
empty
invalid
duplicate
out-of-order
partial
corrupted
expired
unauthorized
high-volume
concurrent
legacy-version
future-compatible
```

Domain-specific scenarios SHOULD also be documented.

---

## Synthetic Data Validation

AI-generated test data MUST be validated before it becomes authoritative test input.

Validation may include:

* JSON Schema.
* OpenAPI validation.
* Database constraints.
* Domain invariants.
* Statistical constraints.
* File-format validation.
* Referential integrity.
* Range checking.

AI-generated data that violates the underlying domain can produce meaningless test confidence.

---

## Golden and Regression Datasets

Complex transformations SHOULD maintain curated golden datasets where appropriate.

Typical cases include:

* Image processing.
* Data ingestion.
* Report generation.
* Serialization.
* Geometry.
* Numerical algorithms.
* Protocol conversion.
* Migration.

Golden datasets SHOULD be deliberately reviewed.

AI MAY expand them.

AI MUST NOT silently rewrite the expected result solely to make a regression disappear.
