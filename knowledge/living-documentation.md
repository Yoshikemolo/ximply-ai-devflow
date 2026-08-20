---
id: AI-KNOW-002
title: Living Documentation
status: proposed
domain: knowledge
owners:
  - engineering
applies_to:
  - software-repositories
related:
  - AI-FND-003
source:
  - draft EN202608161000, section 13
---

# Living Documentation

The repository is only authoritative if it is kept true. Documentation that contradicts the implementation is a defect, and the second link of the chain depends on treating it as one.

---

`/docs` is considered part of the product.

Documentation MUST evolve with the implementation.

Documentation that materially contradicts current implementation is a defect — with the qualification made in [the context-economy section](../ai-foundations/context-economy.md): a descriptive document that disagrees with the code is out of date, while an approved specification that disagrees with the code usually means the code has drifted. Both are defects; they are not fixed in the same place.

A code change is therefore incomplete when it changes documented behavior without updating the corresponding documentation.

Recommended structure:

```text
/docs/
├── architecture/
├── implementation/
├── testing/
├── security/
├── operations/
├── integration/
└── ai/
```

Examples:

```text
/docs/architecture/system-overview.md
/docs/architecture/event-flow.md

/docs/implementation/report-generation.md
/docs/implementation/video-processing.md

/docs/testing/e2e-strategy.md
/docs/testing/test-data-strategy.md

/docs/security/authorization-model.md
/docs/security/threat-model.md

/docs/integration/mission-control.md
```
