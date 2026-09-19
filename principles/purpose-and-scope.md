---
id: AI-PRIN-000
title: Purpose, Scope and Normative Language
status: accepted
domain: principles
owners:
  - engineering
applies_to:
  - all-documents
related:
  []
source:
  - draft EN202608161000, section 1
  - draft EN202608161000, section 2
  - draft EN202608161000, section 3
---

# Purpose, Scope and Normative Language

What the framework is for, which engineering activities it covers, and how to read the requirement levels used throughout the corpus. Every other document assumes the reading of MUST, SHOULD and MAY defined here.

<!-- nav:start -->
`AI-PRIN-000` &middot; status **accepted** &middot; domain [`principles/`](./)

**Derived from** &mdash; [section 1. Purpose](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#1-purpose) &middot; [section 2. Scope](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#2-scope) &middot; [section 3. Normative Language](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#3-normative-language)
<!-- nav:end -->

---

## Purpose

This document sets out the engineering practices that govern software development assisted by Artificial Intelligence. They are applied in practice by [Ximplicity Software Solutions](https://ximplicity.es) in its own products, such as [EVIDENT App](https://evidentapp.ai), and in client projects. The methodology is living: the practices below remain open to review and change through the [decision process](../governance/decision-process.md).

Its objective is to increase engineering productivity and quality through AI-assisted development while preserving:

* Software correctness.
* Security and confidentiality.
* Architectural consistency.
* Maintainability.
* Testability.
* Reproducibility.
* Traceability.
* Supply-chain integrity.
* Operational reliability.
* Human accountability.
* Controlled software promotion.

The framework treats AI systems as **engineering assistants operating within explicitly defined boundaries**.

Under that view they are not software owners, architectural decision authorities, security authorities, release authorities or autonomous approvers — not because the output is untrustworthy in itself, but because accountability cannot be delegated to a system that cannot carry it.

The core suggestion is that AI-generated or AI-modified software remain subject to the same engineering expectations, verification, security controls, review processes and acceptance criteria as software produced manually.

> **AI may accelerate engineering work. It must never lower the engineering standard required to accept that work.**

---

## Scope

The proposed scope covers the use of AI for engineering activities such as:

* Source-code generation.
* Code modification.
* Refactoring.
* Debugging.
* Test generation.
* Test-data generation.
* Documentation.
* Architecture analysis.
* ADR drafting.
* Database migrations.
* Infrastructure as Code.
* API definition.
* Security analysis.
* Dependency selection.
* Code review.
* Performance optimization.
* CI/CD configuration.
* Operational scripts.
* Repository maintenance.

It is intended to apply equally to:

* IDE assistants.
* LLM coding assistants.
* Autonomous or semi-autonomous coding agents.
* Local models.
* Cloud-hosted models.
* Multi-agent development systems.
* CLI-based agents.
* CI-integrated AI services.

---

## Normative Language

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express requirement levels.

* **MUST / MUST NOT** — mandatory.
* **SHOULD / SHOULD NOT** — recommended unless a documented reason justifies otherwise.
* **MAY** — optional.

Exceptions to a MUST requirement would require explicit human approval and, where architecturally significant, an ADR.

> **How to read this in a living methodology.** Requirement levels here express the level applied today in the projects that follow the framework. They are not frozen: a requirement that proves too strict or too weak is changed through the [decision process](../governance/decision-process.md), and a justified departure from a MUST is handled as described in [Compliance and Exceptions](../governance/compliance-and-exceptions.md).
