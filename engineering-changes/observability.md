---
id: AI-CHG-003
title: Observability
status: proposed
domain: engineering-changes
owners:
  - engineering
applies_to:
  - all-services
related:
  []
source:
  - draft EN202608161000, section 52
---

# Observability

What a change must emit to be operable, and the conventions that keep it consistent across services.

<!-- nav:start -->
`AI-CHG-003` &middot; status **proposed** &middot; domain [`engineering-changes/`](./)

**Derived from** &mdash; [section 52. Observability](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#52-observability)
<!-- nav:end -->

---

Relevant functionality SHOULD expose appropriate:

* Logs.
* Metrics.
* Traces.
* Audit events.

Existing OpenTelemetry conventions SHOULD be followed where defined.

AI MUST NOT create alternative telemetry conventions when the project already has one.

Logging MUST NOT expose:

* Credentials.
* Authentication tokens.
* Private keys.
* Sensitive personal data.
* Confidential payloads.
