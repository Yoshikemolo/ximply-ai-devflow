---
name: commit
description: Create git commits in this repository following the versioned commit convention in docs/ai/commits.md - English, no emoji, no attribution trailers, one logical change per commit. Use whenever committing, staging changes, splitting work into commits, or writing a commit message here.
---

# Commit

Implements the repository commit convention. The authoritative rule lives in
`docs/ai/commits.md`; this skill is the procedure that applies it. Read that
document when a case is not covered here — it wins over anything below.

## Procedure

### 1. Inspect before staging

```bash
git status --short
git diff
git diff --staged
git log --oneline -10
```

Read the actual diff. Never commit a change you have not inspected, and never
use `git add -A` without having looked at what it would pick up.

### 2. Check the branch boundary

```bash
git branch --show-current
```

If the current branch is protected (`main`, `dev`, `release/*`), stop and tell
the user. Work belongs on `feature/*`, `fix/*`, `refactor/*` or `technical/*`.
Do not push to a protected branch, merge into one, or force-push anywhere.

Exception: bootstrapping a repository that has no remote and no protected
branch yet. Say so explicitly when taking it.

### 3. Split into logical changes

One commit carries one logical change. If the working tree holds several,
stage them separately with explicit paths and commit one at a time. Never
bundle a mechanical reformat with a behavioral change.

### 4. Screen for secrets

Before staging, confirm the diff contains no credentials, tokens, private
keys, certificates, production endpoints, customer data or personal
information. This applies to the commit message as well. If something looks
like a secret, stop and ask.

### 5. Write the message

```text
<type>(<scope>): <summary>

<body>

<trailers>
```

Types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`,
`security`, `chore`.

The subject is imperative, 72 characters or fewer, no trailing period, and
completes "This commit will ...". The body says **why** — the constraint, the
defect or the decision. The diff already shows what.

Hard rules:

- English only.
- No emoji anywhere.
- No `Co-Authored-By`, no `Generated with`, no tool signature, no AI marker.
- No placeholder subjects (`wip`, `update`, `fixes`, `misc`).

Pass the message with a heredoc so quoting and line breaks survive:

```bash
git commit -F - <<'MSG'
docs(ai): add the repository commit convention

Body explaining why the change was made, wrapped at 72 columns.
MSG
```

On Windows, prefix with `git -c core.safecrlf=false` when the tree mixes line
endings and `.gitattributes` normalization would otherwise abort the commit.

### 6. Verify

```bash
git log --oneline -3
git status --short
```

Confirm the commit landed and that nothing unintended was left staged.

## Refuse to

- Amend or rewrite a commit already published to a shared branch.
- Use `--no-verify` or otherwise skip hooks and quality gates.
- Commit a state known to break the build or the tests.
- Push, merge or open a Pull Request unless the user asked for it.
