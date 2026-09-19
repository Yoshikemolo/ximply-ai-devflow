---
id: AI-INT-001
title: AI-Assisted Development Cycle
status: accepted
domain: integration
owners:
  - engineering
applies_to:
  - all-ai-assisted-work
related:
  []
source:
  - draft EN202608161000, section 63
---

# AI-Assisted Development Cycle

The end-to-end sequence from requirement to merge, showing how far an agent can work and exactly where it stops.

<!-- nav:start -->
`AI-INT-001` &middot; status **accepted** &middot; domain [`integration/`](./)

**Derived from** &mdash; [section 63. Recommended AI-Assisted Development Cycle](../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#63-recommended-ai-assisted-development-cycle)
<!-- nav:end -->

---

```mermaid
flowchart TD
    subgraph FRAME["Frame the work"]
        direction LR
        S1["1. Understand requirement"] --> S2["2. Establish acceptance criteria"] --> S3["3. Read README / docs / ADRs"] --> S4["4. Identify architecture and security constraints"] --> S5["5. Define test strategy and behavioral oracles"] --> S6["6. Create/update implementation plan"]
    end

    subgraph BUILD["Build in isolation"]
        direction LR
        S7["7. Work in isolated branch/workspace"] --> S8["8. Implement small incremental change"] --> S9["9. Add/update tests"] --> S10["10. Generate/validate synthetic test data if required"]
    end

    subgraph VERIFY["Verify"]
        direction LR
        S11["11. Run local tests"] --> S12["12. Run integration/contract tests"] --> S13["13. Run harnesses"] --> S14["14. Run static/security analysis"] --> S15["15. Inspect diff"] --> S16["16. Refactor if necessary"] --> S17["17. Update documentation"]
    end

    subgraph PUBLISH["Publish"]
        direction LR
        S18["18. Human developer review"] --> S19["19. Commit / publish change"] --> S20["20. Open Pull Request"]
    end

    subgraph INTEGRATE["Cross the integration boundary"]
        direction LR
        S21["21. CI validation"] --> S22["22. Quality Gate"] --> S23["23. Human PR review"] --> S24["24. Approval"] --> S25["25. Merge into dev"]
    end

    FRAME --> BUILD --> VERIFY --> PUBLISH --> INTEGRATE
```

AI can participate extensively in engineering steps.

It cannot independently cross the integration boundary.
