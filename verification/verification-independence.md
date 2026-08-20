---
id: AI-VER-001
title: Verification Independence
status: proposed
domain: verification
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  - AI-FND-002
source:
  - draft EN202608161000, section 27
---

# Verification Independence

The AI-specific rule: what checks the work must not be what produced it. This is the operational consequence of agentic bias.

---

An important AI-specific rule is:

> **The implementation and the evidence proving the implementation should not rely exclusively on the same reasoning path.**

AI MAY generate both production code and tests.

However, critical behavior SHOULD also be anchored by at least one independent oracle such as:

* Human-defined acceptance criteria.
* Existing specification.
* API contract.
* Schema.
* Mathematical invariant.
* Domain invariant.
* Golden dataset.
* Regression fixture.
* Independent implementation.
* Property-based test.
* Previously validated behavior.

A test generated from an incorrect AI assumption can reproduce the same incorrect assumption and therefore falsely validate the implementation. The same applies to asking an assistant to check its own work, for the reasons given in [Agentic Bias](../ai-foundations/agentic-bias.md).

Passing self-generated tests alone is not sufficient evidence for critical behavior.
