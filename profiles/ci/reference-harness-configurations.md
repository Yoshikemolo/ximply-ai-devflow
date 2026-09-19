---
id: AI-PROF-001
title: Reference CI Harness Configurations
status: accepted
domain: profiles
owners:
  - engineering
applies_to:
  - implementation-profile
related:
  []
source:
  - draft EN202608161000, Annex A
---

# Reference CI Harness Configurations

Non-normative worked examples per stack. Expected to age faster than anything in the domain documents, and versioned separately from them.

<!-- nav:start -->
`AI-PROF-001` &middot; status **accepted** &middot; domain [`profiles/`](../)

**Derived from** &mdash; [Annex A — Reference CI Harness Configurations](../../compiled/AI-Assisted%20Software%20Engineering%20Framework%20-%20draft%20EN202608161000.md#annex-a-%E2%80%94-reference-ci-harness-configurations)
<!-- nav:end -->

---

Non-normative. The workflows below are worked examples of what the quality gate could look like for each stack, offered so that the discussion in Part I has something concrete attached to it. They are starting points to adapt, not configurations to copy unchanged, and they are expected to age faster than anything in Part I.

Where a repository drops one of these steps, the useful discipline is to note why — that note is more valuable than the step itself.

> **Version pinning.** Runtime, SDK and action versions shown here are illustrative and need aligning with what each repository actually targets and with the organization's supported release train. Keeping them current is part of maintaining this annex.

> **SonarQube project configuration.** Each repository would need a `sonar-project.properties` file (or the equivalent scanner parameters) declaring the project key, sources, tests, exclusions and coverage report paths. Excluding generated code, vendored code and build output matters more than it sounds: without it the metrics describe machinery rather than authored work.

### A. Frontend: Angular

AI assistants frequently regress to superseded frontend patterns: direct DOM manipulation instead of the framework's reactivity model, subscriptions that are never released, change-detection misuse, and unnecessary or unverified NPM dependencies.

**Harness objective:** enforce framework-idiomatic reactivity, catch asynchronous and subscription leaks, verify the production AOT build, and prevent unvetted dependencies from entering the tree.

`.github/workflows/angular-harness.yml`

```yaml
name: Angular Quality Harness

on:
  pull_request:
    branches: [ main, develop ]

permissions:
  contents: read

concurrency:
  group: angular-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate-frontend:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0   # full history is required for Sonar new-code detection

      - name: Setup Node.js runtime
        uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'

      - name: Install dependencies from lockfile
        run: npm ci

      - name: Audit dependencies
        run: npm audit --audit-level=high

      - name: Verify formatting
        run: npm run format:check

      - name: Lint
        run: npm run lint

      - name: Validate production AOT build
        run: npm run build -- --configuration=production

      - name: Unit and regression tests with coverage
        run: npm run test -- --watch=false --browsers=ChromeHeadless --code-coverage

      - name: SonarQube analysis
        uses: SonarSource/sonarqube-scan-action@v5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@v1
        timeout-minutes: 10
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

Coverage reaches SonarQube through `sonar.javascript.lcov.reportPaths` in `sonar-project.properties`. The test command MUST match the test runner actually configured in the project.

### B. Backend: .NET

AI-generated C# commonly introduces subtle erosion rather than obvious breakage: incorrect `async`/`await` usage, blocking calls on asynchronous paths, incorrect dependency-injection lifetimes, unsafe shared state, and Entity Framework queries that behave acceptably on developer data and degrade badly under production volume.

**Harness objective:** compile with analyzers enforced and warnings treated as errors, verify the data-access layer, and route Roslyn findings into SonarQube.

`.github/workflows/dotnet-harness.yml`

```yaml
name: .NET Quality Harness

on:
  pull_request:
    branches: [ main, develop ]

permissions:
  contents: read

concurrency:
  group: dotnet-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate-backend:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup .NET SDK
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'

      - name: Setup Java runtime required by the Sonar scanner
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Install SonarScanner for .NET
        run: dotnet tool install --global dotnet-sonarscanner

      - name: Restore NuGet packages
        run: dotnet restore

      - name: Verify formatting
        run: dotnet format --verify-no-changes

      - name: Begin SonarQube analysis
        run: >
          dotnet sonarscanner begin
          /k:"${{ vars.SONAR_PROJECT_KEY }}"
          /d:sonar.host.url="${{ secrets.SONAR_HOST_URL }}"
          /d:sonar.token="${{ secrets.SONAR_TOKEN }}"
          /d:sonar.cs.opencover.reportsPaths="**/coverage.opencover.xml"

      - name: Build with Roslyn analyzers enforced
        run: dotnet build --no-restore --configuration Release /p:TreatWarningsAsErrors=true

      - name: Test with coverage
        run: >
          dotnet test --no-build --configuration Release --verbosity normal
          /p:CollectCoverage=true
          /p:CoverletOutputFormat=opencover

      - name: End SonarQube analysis
        run: dotnet sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN }}"

      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@v1
        timeout-minutes: 10
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

C# analysis requires the dedicated .NET scanner wrapped around the build; the generic scan action alone does not produce a valid C# analysis. Repositories with a database layer MUST additionally run migration and integration tests against an ephemeral real database, as required by the integration-testing sections of Part I.

### C. Mission-critical: Embedded C / C++

Memory safety is the weakest area of AI-generated native code. Buffer overflows, off-by-one indexing, dangling and uninitialized pointers, unchecked return values, missing `volatile` qualifiers and uninitialized hardware state are all common.

**Harness objective:** enforce deep static application security testing before any firmware artifact can be certified, and treat findings as build failures rather than advisory output.

`.github/workflows/embedded-harness.yml`

```yaml
name: Embedded C/C++ Quality Harness

on:
  pull_request:
    branches: [ main, develop ]

permissions:
  contents: read

concurrency:
  group: embedded-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate-embedded:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install static analysis tooling
        run: |
          sudo apt-get update
          sudo apt-get install -y clang-tidy cppcheck build-essential cmake ninja-build

      - name: Configure build and export the compilation database
        run: cmake -S . -B build -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

      - name: Install the Sonar build wrapper
        uses: SonarSource/sonarqube-scan-action/install-build-wrapper@v5

      - name: Build under the build wrapper
        run: build-wrapper-linux-x86-64 --out-dir bw-output cmake --build build --clean-first

      - name: Cppcheck - memory and vulnerability scan
        run: >
          cppcheck --project=build/compile_commands.json
          --enable=warning,style,performance,portability
          --inline-suppr
          --suppress=missingIncludeSystem
          --error-exitcode=1

      - name: Clang-Tidy - standards and modernization check
        run: run-clang-tidy -p build -quiet -warnings-as-errors=*

      - name: Host-side unit tests
        run: ctest --test-dir build --output-on-failure

      - name: SonarQube native analysis
        uses: SonarSource/sonarqube-scan-action@v5
        with:
          args: --define sonar.cfamily.compile-commands=bw-output/compile_commands.json
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@v1
        timeout-minutes: 10
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

C/C++ analysis in SonarQube requires the build wrapper or a compilation database; running the scanner without one yields no meaningful native analysis. Where the project follows a safety coding standard (for example MISRA or AUTOSAR C++), conformance checking MUST be added to this workflow, and hardware-in-the-loop verification MUST occur before release.

### D. Automation and data engineering: Python

Python's dynamism lets incorrect AI output run far before failing: mismatched parameter types, attributes that do not exist, silently swallowed exceptions, unsafe deserialization, shell and SQL injection through string construction, and obsolete or unmaintained libraries.

**Harness objective:** enforce type consistency, formatting standardization and explicit security scanning of common injection vectors.

`.github/workflows/python-harness.yml`

```yaml
name: Python Quality Harness

on:
  pull_request:
    branches: [ main, develop ]

permissions:
  contents: read

concurrency:
  group: python-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate-python:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install project and verification tooling
        run: |
          pip install -r requirements.txt
          pip install ruff mypy bandit pip-audit pytest pytest-cov

      - name: Lint (Ruff)
        run: ruff check .

      - name: Verify formatting (Ruff)
        run: ruff format --check .

      - name: Strict static typing (Mypy)
        run: mypy --strict src

      - name: Security audit of source (Bandit)
        run: bandit -r src -ll

      - name: Dependency vulnerability audit
        run: pip-audit -r requirements.txt

      - name: Tests with coverage
        run: pytest --cov=src --cov-report=xml --cov-report=term

      - name: SonarQube analysis
        uses: SonarSource/sonarqube-scan-action@v5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@v1
        timeout-minutes: 10
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

Coverage reaches SonarQube through `sonar.python.coverage.reportPaths=coverage.xml` in `sonar-project.properties`.

### Controls common to every stack

Independently of stack, these are worth running at Pull Request time or on a schedule:

* Secret scanning with push protection enabled.
* Dependency vulnerability scanning and licence compliance.
* Software Composition Analysis and SBOM generation where required by the supply-chain sections of Part I.
* Infrastructure-as-Code and container image scanning where applicable.
* The repository's own harnesses as defined in the test-harness sections.
