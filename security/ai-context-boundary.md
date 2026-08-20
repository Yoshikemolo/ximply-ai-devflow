---
id: AI-SEC-001
title: AI Context Boundary
status: proposed
domain: security
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  - AI-SEC-002
source:
  - draft EN202608161000, section 19
---

# AI Context Boundary

What an agent is allowed to know. Minimum required context is both an accuracy control and the principal preventive control against cumulative exposure. Keep it separate from what an agent is allowed to do, which is a different boundary.

---

Context provided to an AI system MUST follow the principle:

> **Minimum required context.**

Normally acceptable:

```text
README.md
CONTRIBUTING.md
/docs
/ADR
relevant source files
relevant tests
public API contracts
engineering guidelines
sanitized test data
```

Normally prohibited unless specifically authorized:

```text
production credentials
private keys
production certificates
production database dumps
customer PII
secrets
confidential contracts
unrelated repositories
unnecessary infrastructure configuration
```

A large context window MUST NOT be interpreted as permission to provide unnecessary information.

Minimum required context is also the principal preventive control against cumulative exposure: the lists above classify information item by item, but sensitivity is a property of the accumulated context, not only of the individual item. [Agentic Security Boundary](agentic-security-boundary.md) develops this as context aggregation risk, and applies it to intellectual property that no single item in the lists above would identify as confidential.
