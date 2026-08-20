---
id: AI-KNOW-004
title: Versioned AI Engineering Instructions
status: proposed
domain: knowledge
owners:
  - engineering
applies_to:
  - software-repositories
related:
  - AI-SEC-002
source:
  - draft EN202608161000, section 17
  - draft EN202608161000, section 18
---

# Versioned AI Engineering Instructions

Reusable engineering rules belong in the repository, versioned with the code they govern. The complementary half of the same decision is keeping private local agent configuration out of version control.

<!-- nav:start -->
`AI-KNOW-004` &middot; status **proposed** &middot; domain [`knowledge/`](./)

**Related** &mdash; [Agentic Security Boundary `AI-SEC-002`](../security/agentic-security-boundary.md)

**Derived from** &mdash; [section 17. Versioned AI Engineering Instructions](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#17-versioned-ai-engineering-instructions) &middot; [section 18. Private AI Configuration](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#18-private-ai-configuration)
<!-- nav:end -->

---

## Versioned AI Engineering Instructions

Reusable engineering rules SHOULD live in the repository, versioned with the code they govern. The complementary half — keeping private, local AI configuration out of it — is the subject of the next section.

Recommended:

```text
/docs/ai/
├── general-engineering.md
├── backend-development.md
├── frontend-development.md
├── testing.md
├── security-review.md
├── refactoring.md
├── database-development.md
├── observability.md
└── documentation.md
```

These instructions represent **engineering knowledge**, not tool-specific prompts.

They SHOULD define:

* Architectural boundaries.
* Framework conventions.
* Dependency rules.
* Error-handling strategy.
* Logging conventions.
* Validation.
* API design.
* Persistence patterns.
* Testing expectations.
* Naming.
* Security requirements.
* Observability.
* Code-quality rules.

---

## Private AI Configuration

Private AI configuration MUST be separated from versioned engineering knowledge.

Examples requiring exclusion or explicit review include:

```text
.claude/
.cursor/
.settings/
.local-ai/
.ai-private/
```

Such locations may accidentally contain:

* API keys.
* Tokens.
* Internal URLs.
* Customer information.
* Local paths.
* Infrastructure details.
* Private prompts.
* Credentials.
* Certificates.
* Security information.

These directories SHOULD normally be excluded through `.gitignore`.

Safe, reviewed, reusable engineering instructions belong under `/docs/ai`, not private local-agent configuration.

Stored prompts, session history and local agent state deserve the same treatment for a second reason: they accumulate organizational context over time, which is the exposure discussed in [Agentic Security Boundary](../security/agentic-security-boundary.md). Excluding these locations from version control keeps that accumulation out of the repository; it does not by itself limit what was placed in the context to begin with.
