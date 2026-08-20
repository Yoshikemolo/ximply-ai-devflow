---
id: AI-SEC-004
title: Security Verification and Threat Modeling
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - all-changes
related:
  []
source:
  - draft EN202608161000, section 48
  - draft EN202608161000, section 49
---

# Security Verification and Threat Modeling

The security checks a change passes before integration, and when a change is significant enough to require revisiting the threat model.

---

## Security Verification

AI-assisted changes MUST preserve secure development practices.

Depending on system risk, CI SHOULD include:

* Secret scanning.
* SAST.
* Dependency scanning.
* Software Composition Analysis.
* Container scanning.
* IaC scanning.
* Authentication tests.
* Authorization tests.
* Tenant-isolation tests.
* Input validation tests.

Security-sensitive changes require explicit human security review.

---

## Threat Modeling

Relevant features SHOULD include threat analysis.

Threat modeling SHOULD consider:

* Assets.
* Trust boundaries.
* Identities.
* Permissions.
* External inputs.
* Network boundaries.
* Data classification.
* Abuse cases.
* Failure modes.

For AI-enabled functionality, also consider:

* Prompt injection.
* Data poisoning.
* Sensitive-information disclosure.
* Excessive agency.
* Tool abuse.
* Unauthorized action chaining.
