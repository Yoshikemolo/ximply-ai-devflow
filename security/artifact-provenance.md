---
id: AI-SEC-007
title: Artifact Provenance and Signing
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 51
---

# Artifact Provenance and Signing

Being able to say what an artifact is, where it came from, and which source it was built from.

---

Higher-assurance systems SHOULD generate verifiable build provenance and SHOULD consider signing release artifacts.

The organization SHOULD progressively adopt software-supply-chain controls consistent with frameworks such as SLSA.

Where signing is implemented, artifacts may include:

* Container images.
* Binaries.
* Packages.
* SBOMs.
* Build attestations.

The objective is to establish:

```mermaid
flowchart LR
    S["source"] --> B["controlled build"] --> A["traceable artifact"] --> P["verifiable provenance"] --> D["authorized deployment"]
```
