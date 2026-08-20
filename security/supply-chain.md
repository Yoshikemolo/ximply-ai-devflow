---
id: AI-SEC-006
title: Software Supply Chain
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - all-repositories
related:
  []
source:
  - draft EN202608161000, section 50
---

# Software Supply Chain

Integrity of what enters the build and what leaves it. Assisted development raises the rate at which third-party code is proposed, which increases rather than reduces the value of these controls.

---

The engineering pipeline SHOULD provide visibility into software composition and artifact provenance.

Where organizational maturity permits, builds SHOULD generate an SBOM using a recognized format such as:

* CycloneDX.
* SPDX.

Release artifacts SHOULD be traceable to:

* Source revision.
* Build workflow.
* Dependencies.
* Build environment.
* Produced artifact.
