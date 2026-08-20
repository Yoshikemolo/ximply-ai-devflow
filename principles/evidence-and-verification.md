---
id: AI-PRIN-003
title: Evidence and Verification
status: proposed
domain: principles
owners:
  - engineering
applies_to:
  - all-changes
related:
  - AI-FND-002
source:
  - draft EN202608161000, section 8 (8.4 Verification over generation)
---

# Evidence and Verification

AI output is a proposal until something independent says otherwise. This document states the principle; the verification domain develops what independence means in practice.

---

AI output is a proposal until independently verified.

Confidence expressed by an AI model MUST NOT be treated as evidence of correctness. [Agentic Bias](../ai-foundations/agentic-bias.md) describes why that confidence is systematically miscalibrated and what to do about it in practice.

Compilation is evidence that code is syntactically compatible.

Tests are evidence of tested behavior.

Static analysis is evidence of particular analyzed properties.

Review is evidence of human inspection.

None individually demonstrates complete correctness.
