---
id: AI-PRIN-000
title: Purpose, Scope and Normative Language
status: proposed
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

---

## Purpose

This document proposes the engineering practices that would govern software development assisted by Artificial Intelligence. It is a draft for engineering review: the practices below are put forward for discussion, not issued as rules.

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

The proposal treats AI systems as **engineering assistants operating within explicitly defined boundaries**.

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

> **How to read this in a draft.** Requirement levels here express *the level being proposed* for each item, so that the intent is unambiguous when it is discussed. They are not obligations in force. Reading a MUST as "this is the strength I think this item needs — do you agree?" is the intended reading throughout Part I.
