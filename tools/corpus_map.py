"""Conceptual map from the monolithic draft to the addressable corpus.

Each entry declares one target document: where it lives, its stable
identifier, the framing paragraph that opens it, and the sections of the
draft it is derived from.

The map is the interesting part of the split. It encodes a judgement about
which sections answer the same engineering question, and it is expected to be
argued with. Two rules keep it honest:

1. No section appears in more than one target document. Relationships are
   expressed as links, never as copies, because a copied paragraph is a
   future contradiction.
2. Every target document records the sections it came from, so the derivation
   can be checked against the draft.

A source entry is (section key, mode, subsection names), where mode is:

    "all"     the whole section
    "only"    just the named subsections, promoted one heading level
    "except"  the section without the named subsections
"""

ALL = "all"


def S(key, mode=ALL, names=()):
    return (key, mode, tuple(names))


MAP = [
    # ---------------------------------------------------------------- principles
    dict(
        path="principles/purpose-and-scope.md",
        id="AI-PRIN-000",
        title="Purpose, Scope and Normative Language",
        applies_to=["all-documents"],
        intro=(
            "What the framework is for, which engineering activities it covers, and how to "
            "read the requirement levels used throughout the corpus. Every other document "
            "assumes the reading of MUST, SHOULD and MAY defined here."
        ),
        sources=[S("1"), S("2"), S("3")],
    ),
    dict(
        path="principles/engineering-principles.md",
        id="AI-PRIN-001",
        title="Engineering Principles",
        applies_to=["all-documents"],
        intro=(
            "The seven ideas the rest of the corpus implements, and the conceptual chain that "
            "connects them. If consensus fails here, nothing further down is worth arguing "
            "about yet."
        ),
        sources=[
            S("70"),
            S("4", "except", ["Addressability, briefly"]),
            S("8", "only", ["8.3 Least privilege for AI"]),
        ],
    ),
    dict(
        path="principles/human-accountability.md",
        id="AI-PRIN-002",
        title="Human Accountability",
        applies_to=["all-changes"],
        intro=(
            "Who answers for a change, and which decisions are not delegable. This document "
            "draws the line between what an AI system may contribute and what only an "
            "accountable engineer may decide."
        ),
        sources=[
            S("8", "only", ["8.1 Human ownership", "8.2 Human-controlled integration"]),
            S("9"),
        ],
    ),
    dict(
        path="principles/evidence-and-verification.md",
        id="AI-PRIN-003",
        title="Evidence and Verification",
        applies_to=["all-changes"],
        intro=(
            "AI output is a proposal until something independent says otherwise. This document "
            "states the principle; the verification domain develops what independence means in "
            "practice."
        ),
        sources=[S("8", "only", ["8.4 Verification over generation"])],
    ),
    # ------------------------------------------------------------ ai-foundations
    dict(
        path="ai-foundations/capability-model.md",
        id="AI-FND-001",
        title="AI Capability Model",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "What these systems can and cannot be relied on to do, and the failure modes that "
            "the controls elsewhere in the corpus exist to catch. Agreeing on this precedes "
            "arguing about thresholds."
        ),
        sources=[S("5")],
    ),
    dict(
        path="ai-foundations/agentic-bias.md",
        id="AI-FND-002",
        title="Agentic Bias",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "Designed agreeableness and miscalibrated confidence, and why a session tends to "
            "confirm its own output. This is the reason verification has to come from outside "
            "the conversation that produced the work."
        ),
        sources=[S("6")],
    ),
    dict(
        path="ai-foundations/context-economy.md",
        id="AI-FND-003",
        title="Context Economy",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "Attention is finite and degrades with volume. A large corpus helps only if it can "
            "be consumed in small, high-signal pieces, which is what makes the rest of the "
            "conceptual chain necessary rather than merely tidy."
        ),
        sources=[S("7")],
    ),
    dict(
        path="ai-foundations/autonomy-levels.md",
        id="AI-FND-004",
        title="AI Autonomy Levels",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "Shared vocabulary for how much an agent is permitted to do without a human step. "
            "The levels are defined here because several domains refer to them; where they are "
            "granted and enforced belongs to the agentic engineering domain."
        ),
        sources=[S("11")],
    ),
    # ----------------------------------------------------------------- knowledge
    dict(
        path="knowledge/repository-source-of-truth.md",
        id="AI-KNOW-001",
        title="Repository as Engineering Source of Truth",
        applies_to=["software-repositories"],
        intro=(
            "The authoritative account of a system lives in its repository, not in "
            "conversations, tickets or memory. This is the first link of the conceptual chain: "
            "without it there is nothing authoritative to retrieve."
        ),
        sources=[S("12"), S("14")],
    ),
    dict(
        path="knowledge/living-documentation.md",
        id="AI-KNOW-002",
        title="Living Documentation",
        applies_to=["software-repositories"],
        intro=(
            "The repository is only authoritative if it is kept true. Documentation that "
            "contradicts the implementation is a defect, and the second link of the chain "
            "depends on treating it as one."
        ),
        sources=[S("13")],
    ),
    dict(
        path="knowledge/architecture-decisions.md",
        id="AI-KNOW-003",
        title="Architecture Decisions and Guardrails",
        applies_to=["software-repositories"],
        intro=(
            "How architectural decisions are recorded so they can be cited, superseded and "
            "checked against, and what an assistant must inspect before changing a system. "
            "AI may draft a decision; it may not accept one."
        ),
        sources=[S("15"), S("16")],
    ),
    dict(
        path="knowledge/ai-engineering-instructions.md",
        id="AI-KNOW-004",
        title="Versioned AI Engineering Instructions",
        applies_to=["software-repositories"],
        intro=(
            "Reusable engineering rules belong in the repository, versioned with the code they "
            "govern. The complementary half of the same decision is keeping private local "
            "agent configuration out of version control."
        ),
        sources=[S("17"), S("18")],
    ),
    dict(
        path="knowledge/addressable-knowledge.md",
        id="AI-KNOW-005",
        title="Addressable Knowledge",
        applies_to=["software-repositories", "this-repository"],
        intro=(
            "Versioning tells you which text you have; an identifier tells you which decision "
            "you are talking about. This is what turns a documentation tree into a queryable "
            "corpus, and it is the precondition for selective retrieval by an agent. This "
            "repository is the first place the idea is being tried."
        ),
        sources=[S("4", "only", ["Addressability, briefly"])],
    ),
    # ------------------------------------------------------------------ security
    dict(
        path="security/ai-context-boundary.md",
        id="AI-SEC-001",
        title="AI Context Boundary",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "What an agent is allowed to know. Minimum required context is both an accuracy "
            "control and the principal preventive control against cumulative exposure. Keep it "
            "separate from what an agent is allowed to do, which is a different boundary."
        ),
        sources=[S("19")],
    ),
    dict(
        path="security/agentic-security-boundary.md",
        id="AI-SEC-002",
        title="Agentic Security Boundary",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "Context aggregation risk, progressive disclosure, and the protection of "
            "intellectual property that no individual file would identify as confidential. "
            "Sensitivity is a property of the accumulated context, not of the item."
        ),
        sources=[S("21")],
    ),
    dict(
        path="security/tool-execution.md",
        id="AI-SEC-003",
        title="Shell and Tool Execution",
        applies_to=["agentic-tooling"],
        intro=(
            "What an agent is allowed to do. Where the context boundary governs information, "
            "this governs action: which commands and tools may execute, under whose identity, "
            "and with what approval."
        ),
        sources=[S("22")],
    ),
    dict(
        path="security/security-verification.md",
        id="AI-SEC-004",
        title="Security Verification and Threat Modeling",
        applies_to=["all-changes"],
        intro=(
            "The security checks a change passes before integration, and when a change is "
            "significant enough to require revisiting the threat model."
        ),
        sources=[S("48"), S("49")],
    ),
    dict(
        path="security/dependency-governance.md",
        id="AI-SEC-005",
        title="Dependency Governance",
        applies_to=["all-changes"],
        intro=(
            "An assistant proposing a dependency is proposing a long-term maintenance and "
            "security commitment. This document states who accepts that commitment and on what "
            "evidence."
        ),
        sources=[S("24")],
    ),
    dict(
        path="security/supply-chain.md",
        id="AI-SEC-006",
        title="Software Supply Chain",
        applies_to=["all-repositories"],
        intro=(
            "Integrity of what enters the build and what leaves it. Assisted development raises "
            "the rate at which third-party code is proposed, which increases rather than "
            "reduces the value of these controls."
        ),
        sources=[S("50")],
    ),
    dict(
        path="security/artifact-provenance.md",
        id="AI-SEC-007",
        title="Artifact Provenance and Signing",
        applies_to=["all-repositories"],
        intro=(
            "Being able to say what an artifact is, where it came from, and which source it was "
            "built from."
        ),
        sources=[S("51")],
    ),
    # ------------------------------------------------------- agentic-engineering
    dict(
        path="agentic-engineering/human-in-the-loop.md",
        id="AI-AGT-001",
        title="Human-in-the-Loop: The Engineer's Role",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "Where engineering attention moves when implementation gets cheaper. The role "
            "expands rather than shrinks: design and definition before, integration and "
            "validation after."
        ),
        sources=[S("10")],
    ),
    dict(
        path="agentic-engineering/context-informed-prompting.md",
        id="AI-AGT-002",
        title="Context-Informed Prompting Protocol",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "How a task is framed before an agent starts: the context injected, the constraints "
            "stated, and the checkpoints defined. This is where minimum necessary context stops "
            "being a policy and becomes a practice."
        ),
        sources=[S("20")],
    ),
    dict(
        path="agentic-engineering/local-and-corporate-agents.md",
        id="AI-AGT-003",
        title="Local Models and Organization-Owned Agentic Tooling",
        applies_to=["agentic-tooling"],
        intro=(
            "The deployment where the whole conceptual chain can be enforced at once: an "
            "ordinary model authorized to query a well-structured corpus under the identity and "
            "permissions of the person asking. A corporate agent implements this framework; it "
            "does not define it."
        ),
        sources=[S("23")],
    ),
    dict(
        path="agentic-engineering/implementation-planning.md",
        id="AI-AGT-004",
        title="Implementation Planning",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "The plan that makes feature-scale assisted work reviewable: decomposition, "
            "checkpoints, and an agreed target before generation begins."
        ),
        sources=[S("25")],
    ),
    dict(
        path="agentic-engineering/small-batch-development.md",
        id="AI-AGT-005",
        title="Small-Batch AI Development",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "A change is accepted at the speed it can be understood. Reviewability, not model "
            "capability, is the constraint that sets batch size."
        ),
        sources=[S("26")],
    ),
    dict(
        path="agentic-engineering/ai-assisted-refactoring.md",
        id="AI-AGT-006",
        title="AI-Assisted Refactoring",
        applies_to=["all-changes"],
        intro=(
            "Behaviour-preserving transformation is among the strongest uses of assistance, and "
            "it depends entirely on the regression tests that protect it."
        ),
        sources=[S("55")],
    ),
    # -------------------------------------------------------------- verification
    dict(
        path="verification/verification-independence.md",
        id="AI-VER-001",
        title="Verification Independence",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "The AI-specific rule: what checks the work must not be what produced it. This is "
            "the operational consequence of agentic bias."
        ),
        sources=[S("27")],
    ),
    dict(
        path="verification/testing-strategy.md",
        id="AI-VER-002",
        title="Testing Strategy",
        applies_to=["all-repositories"],
        intro=(
            "How test effort is allocated against risk, what each test level is evidence of, "
            "and what changes when the tests are themselves AI-generated. One document because "
            "these choices are made together, not one level at a time."
        ),
        sources=[S("28"), S("29"), S("30"), S("31"), S("32"), S("33"), S("34")],
    ),
    dict(
        path="verification/synthetic-test-data.md",
        id="AI-VER-003",
        title="Synthetic and Generated Test Data",
        applies_to=["all-repositories"],
        intro=(
            "Generated fixtures and mock data are engineering assets with a provenance, a "
            "safety boundary and a validation requirement. They are not disposable output."
        ),
        sources=[S("35"), S("36"), S("37"), S("38"), S("39"), S("40")],
    ),
    dict(
        path="verification/advanced-testing.md",
        id="AI-VER-004",
        title="Property-Based and Mutation Testing",
        applies_to=["all-repositories"],
        intro=(
            "Techniques that check the test suite rather than the implementation, and that "
            "become more valuable as the volume of generated code grows."
        ),
        sources=[S("41"), S("42")],
    ),
    dict(
        path="verification/test-harnesses.md",
        id="AI-VER-005",
        title="Test Harnesses and Harness Independence",
        applies_to=["all-repositories"],
        intro=(
            "The executable environment in which evidence is produced, and why the harness must "
            "not be authored by the same process it is meant to judge."
        ),
        sources=[S("43"), S("44")],
    ),
    dict(
        path="verification/static-analysis.md",
        id="AI-VER-006",
        title="Static Analysis and Code Quality",
        applies_to=["all-repositories"],
        intro=(
            "The properties a machine can check without running the code, and the clean-code "
            "expectations that generated output is held to."
        ),
        sources=[S("45"), S("47")],
    ),
    # --------------------------------------------------------------- integration
    dict(
        path="integration/ai-assisted-development-cycle.md",
        id="AI-INT-001",
        title="AI-Assisted Development Cycle",
        applies_to=["all-ai-assisted-work"],
        intro=(
            "The end-to-end sequence from requirement to merge, showing how far an agent can "
            "work and exactly where it stops."
        ),
        sources=[S("63")],
    ),
    dict(
        path="integration/branch-management.md",
        id="AI-INT-002",
        title="Branch Management",
        applies_to=["all-repositories"],
        intro=(
            "Assisted work happens outside protected branches, whatever those branches are "
            "called. The branching model is a team decision; the boundary is not."
        ),
        sources=[S("62")],
    ),
    dict(
        path="integration/pull-request-boundary.md",
        id="AI-INT-003",
        title="Pull Request Boundary",
        applies_to=["all-repositories"],
        intro=(
            "The Pull Request is the principal integration quality boundary: what a change must "
            "satisfy to be considered for acceptance, and what its author declares."
        ),
        sources=[S("58"), S("59"), S("60")],
    ),
    dict(
        path="integration/human-review.md",
        id="AI-INT-004",
        title="Human Review",
        applies_to=["all-changes"],
        intro=(
            "What a human reviewer is responsible for that no automated check covers, and the "
            "place AI review occupies alongside it rather than instead of it."
        ),
        sources=[S("61"), S("57")],
    ),
    dict(
        path="integration/quality-gates.md",
        id="AI-INT-005",
        title="Automated Quality Gates and CI Pipeline",
        applies_to=["all-repositories"],
        intro=(
            "The checks that run without asking anyone, and the branch protection that makes "
            "them a boundary rather than a suggestion. Concrete thresholds live in the "
            "implementation profiles so that changing a number does not reopen the framework."
        ),
        sources=[S("46"), S("64")],
    ),
    dict(
        path="integration/definition-of-done.md",
        id="AI-INT-006",
        title="Definition of Done",
        applies_to=["all-changes"],
        intro="Code generation is not completion. Verified behaviour is the deliverable.",
        sources=[S("65")],
    ),
    # -------------------------------------------------------- engineering-changes
    dict(
        path="engineering-changes/api-changes.md",
        id="AI-CHG-001",
        title="API Changes",
        applies_to=["public-contracts"],
        intro="Playbook for changing a published contract without breaking its consumers.",
        sources=[S("53")],
    ),
    dict(
        path="engineering-changes/database-changes.md",
        id="AI-CHG-002",
        title="Database Changes",
        applies_to=["persistence"],
        intro=(
            "Playbook for schema and data migration, where assisted work carries irreversible "
            "risk."
        ),
        sources=[S("54")],
    ),
    dict(
        path="engineering-changes/observability.md",
        id="AI-CHG-003",
        title="Observability",
        applies_to=["all-services"],
        intro=(
            "What a change must emit to be operable, and the conventions that keep it "
            "consistent across services."
        ),
        sources=[S("52")],
    ),
    # ---------------------------------------------------------------- governance
    dict(
        path="governance/governance-model.md",
        id="AI-GOV-001",
        title="Engineering Governance Model",
        applies_to=["this-corpus"],
        intro="Who owns the framework, who may change it, and how authority is distributed.",
        sources=[S("69")],
    ),
    dict(
        path="governance/compliance-and-exceptions.md",
        id="AI-GOV-002",
        title="Compliance and Exceptions",
        applies_to=["this-corpus"],
        intro=(
            "How the framework is enforced, and how an exception is granted so that it stays "
            "explicit, owned and time-bounded rather than becoming silent erosion."
        ),
        sources=[S("68")],
    ),
    dict(
        path="governance/ai-traceability.md",
        id="AI-GOV-003",
        title="AI Contribution Traceability",
        applies_to=["all-changes"],
        intro=(
            "What is worth recording about how a change came to be. The purpose is auditability "
            "rather than attribution, and the categories below are an open proposal rather than "
            "a decision."
        ),
        sources=[S("56")],
    ),
    dict(
        path="governance/metrics.md",
        id="AI-GOV-004",
        title="Metrics",
        applies_to=["this-corpus"],
        intro=(
            "What is measured to know whether the framework is working, and what measuring it "
            "distorts."
        ),
        sources=[S("66")],
    ),
    dict(
        path="governance/periodic-review.md",
        id="AI-GOV-005",
        title="Periodic AI Governance Review",
        applies_to=["this-corpus"],
        intro=(
            "The rhythm at which the framework is revisited, because the capability it governs "
            "moves faster than the framework does."
        ),
        sources=[S("67")],
    ),
    dict(
        path="governance/open-questions.md",
        id="AI-GOV-006",
        title="Open Questions",
        applies_to=["this-corpus"],
        intro=(
            "What the framework deliberately leaves undecided. This is the agenda for review, "
            "not a list of gaps to be quietly filled in. Each question that closes should close "
            "as a decision record."
        ),
        sources=[S("71")],
    ),
    # ------------------------------------------------------------------ profiles
    dict(
        path="profiles/ci/reference-harness-configurations.md",
        id="AI-PROF-001",
        title="Reference CI Harness Configurations",
        applies_to=["implementation-profile"],
        intro=(
            "Non-normative worked examples per stack. Expected to age faster than anything in "
            "the domain documents, and versioned separately from them."
        ),
        sources=[S("Annex A")],
    ),
    dict(
        path="profiles/quality-gates/baselines.md",
        id="AI-PROF-002",
        title="Proposed Quality Gate Baselines",
        applies_to=["implementation-profile"],
        intro=(
            "The concrete numbers, kept out of the domain documents on purpose so that "
            "discussing a coverage percentage does not mean reopening the framework."
        ),
        sources=[S("Annex B")],
    ),
    dict(
        path="profiles/pull-request/declaration.md",
        id="AI-PROF-003",
        title="Draft Pull Request Declaration",
        applies_to=["implementation-profile"],
        intro=(
            "A template sketch for the author declaration, offered as material for the "
            "traceability discussion rather than as an adopted form."
        ),
        sources=[S("Annex C")],
    ),
]
