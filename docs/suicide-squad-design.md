# Suicide Squad

## Java Cosmos DB SDK: invariant-driven testing and agentic PR mergeability

[Documentation index](README.md) |
[Research inputs and provenance](research/java-sdk/README.md) |
[Incomplete report status](research/java-sdk/reports/README.md)

| Field | Value |
|---|---|
| Document version | 0.2.2 |
| Created / last revised | 2026-10-31 / 2026-10-31 |
| Status | DESIGN DRAFT - NOT APPROVED FOR IMPLEMENTATION |
| Initial product | Full Azure Cosmos DB Java SDK for NoSQL feature surface: `azure-cosmos`, test/fault support, and the companion encryption-library contracts |
| Canonical project repository | [kushagraThapar/SuicideSquad](https://github.com/kushagraThapar/SuicideSquad) |
| SDK repository under study | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) |
| Immediate objective | Finalize this design, inventory existing evidence, and identify gaps before changing SDK code, tests, CI, or agent permissions |
| Long-term objective | Agents reproduce bugs, implement changes, review independently, iterate, and merge eligible PRs without routine human PR review |
| Explicit exclusion | Release execution, release automation, and production rollout are a separate project |

> This is the project's reference document and progress ledger. A checklist item is
> complete only when its linked acceptance evidence exists. Writing a requirement
> here does not mean the SDK already satisfies it.
> This repository copy supersedes the session draft as the reference for this
> revision. Publication on a review branch is not default-branch integration,
> design approval, implementation authorization, or merge-policy approval.

## Contents

1. [Intent and requirements](#1-intent-and-requirements)
2. [Scope and boundaries](#2-scope-and-boundaries)
3. [Observed starting point](#3-observed-starting-point)
4. [Architecture and evidence model](#4-architecture-and-evidence-model)
5. [Feature and behavior inventory](#5-feature-and-behavior-inventory)
6. [SDK invariant catalog](#6-sdk-invariant-catalog)
7. [Status-code and substatus behavior catalog](#7-status-code-and-substatus-behavior-catalog)
8. [Scenario model and interaction coverage](#8-scenario-model-and-interaction-coverage)
9. [Coverage dimensions and improvement policy](#9-coverage-dimensions-and-improvement-policy)
10. [Test architecture and execution](#10-test-architecture-and-execution)
11. [Historical bug benchmark](#11-historical-bug-benchmark)
12. [Agentic review, iteration, and merging](#12-agentic-review-iteration-and-merging)
13. [Security and trust boundaries](#13-security-and-trust-boundaries)
14. [Failure handling and operational controls](#14-failure-handling-and-operational-controls)
15. [Evaluation and autonomy graduation](#15-evaluation-and-autonomy-graduation)
16. [Design decisions and unresolved questions](#16-design-decisions-and-unresolved-questions)
17. [Milestones and progress](#17-milestones-and-progress)
18. [Risks and alternatives](#18-risks-and-alternatives)
19. [Working agreement and continuation](#19-working-agreement-and-continuation)
20. [References](#20-references)

## 1. Intent and requirements

### 1.1 Problem

Human review currently supplies judgment that a green test run alone cannot:
understanding intended behavior, recognizing missing scenarios, checking
compatibility, and challenging unsafe assumptions. Removing routine human review
requires making substantially more of that judgment explicit and executable.

The project is not "generate enough tests to reach a percentage." It is a
versioned system of contracts, tests, independent review, and auditable merge
decisions. Near-100% executable line coverage remains an important goal.

No finite suite, coverage percentage, or number of agent approvals proves the
absence of bugs. The design must measure residual risk and block changes outside
its demonstrated competence rather than imply universal correctness.

### 1.2 Confirmed direction

| ID | Requirement |
|---|---|
| R-01 | Start with the Java SDK and extend the tests and fault-injection infrastructure already present. |
| R-02 | Inventory SDK features, status/substatus behaviors, Cosmos-specific scenarios, and general database/client scenarios; derive executable invariants from them. |
| R-03 | Use multiple coverage dimensions. PRs must improve confidence rather than reduce scores when features or fixes are introduced. The exact numerical interpretation requires D-02. |
| R-04 | Target near-100% production executable line coverage, with additional branch, assertion-strength, behavioral, and interaction evidence. |
| R-05 | Build a historical bug benchmark using public GitHub issues, linked fixes, and reproducible scenarios. |
| R-06 | Use independent PR Review Router-led agent reviews and evidence-backed iterations before granting mergeability. The implementation agent must not approve its own work. |
| R-07 | Finish and approve the design before implementation. This draft authorizes no SDK, pipeline, permission, or merge-policy changes. |
| R-08 | Do not act on releases or design release automation in this project. |
| R-09 | Keep this document useful for a long-running project: stable IDs, explicit decisions, acceptance criteria, dependencies, and progress evidence. |
| R-10 | The initial pilot covers the entire Java SDK feature/behavior surface, not only retry decisions or deadlines. Reconcile the full changelog and current APIs/implementation with the invariant catalog before declaring inventory completeness. Initial PR experiments may involve any SDK domain. |
| R-11 | Use `kushagraThapar/SuicideSquad` as the canonical repository for this project's design documents, inventories, evidence and future project files. Do not leave authoritative project work only in a chat/session directory. |

### 1.3 Success

An eligible PR has reproducible evidence that it preserves existing contracts,
adds complete evidence for new behavior, meets multidimensional gates, and
survives independent Router-led review on the actual merge candidate.

An ineligible PR is blocked with an actionable explanation. Routine human review
is eventually unnecessary for proven scopes; policy-setting, intentional
contract changes, and unresolved ambiguity remain explicit governance decisions.
The eventual breadth of autonomy is earned, not assumed.

## 2. Scope and boundaries

### 2.1 Initial scope

- Production code and public NoSQL client behavior in `sdk/cosmos/azure-cosmos`.
- Existing tests in `azure-cosmos-tests`, relevant tests elsewhere in the Cosmos
  subtree, and supporting fault-injection facilities in `azure-cosmos-test`.
- Build, test discovery, coverage collection, compatibility checks, and
  PR-validation wiring necessary to substantiate mergeability.
- Sync and async APIs, public configuration, internal algorithms, transport,
  routing, consistency, diagnostics, and supported preview paths present at the
  chosen baseline.
- Consumer-facing compatibility at relevant boundaries, including packaged-JAR
  checks. Validating a candidate artifact is not permission to publish it.
- Companion `azure-cosmos-encryption` feature contracts, constraints and
  core-client integration. Its implementation and test denominators remain a
  separately identified package lane, not silently folded into `azure-cosmos`.

### 2.2 Outside the first autonomy boundary

Spark, Kafka and Spring integrations are separate connector/framework products,
not part of the Java NoSQL client feature denominator. Their relevant contracts
can supply consumer tests and benchmark candidates. This boundary does not
exclude the companion Java encryption library from feature discovery.

Whole-SDK pilot scope is not blanket autonomous merge permission: every package
and change class, including encryption, must meet its required evidence and
qualification rules. Security-sensitive changes stay under the current approval
policy until separately qualified.

Other SDKs are reference implementations and parity evidence, not implementation
targets. Shared Azure build infrastructure requires its own ownership and
approval; this project cannot unilaterally change repository-wide policy.

No work in this design executes deployments, modifies service topology, performs
live fault injection, changes branch protections, enables auto-merge, or publishes
packages. All such implementation actions require later authorization.

### 2.3 Whole-SDK initial pilot

The user-directed scope is **all Java SDK features and behaviors from the first
pilot**, including retries/status/substatus responses, consistency/session
semantics, transport, data operations, background workflows, observability and
compatibility. Retry/deadline accounting is one lane, not the admission boundary
for experiments.

The initial catalog and experiment model must cover every F-/INV-/ST-/SC- family
in this document plus capabilities found during source/changelog reconciliation.
Use parallel domain lanes to manage depth without declaring the rest of the SDK
out of scope:

| Pilot lane | Included behavior |
|---|---|
| Client and credentials | Construction/defaults, lifecycle, authentication, permissions, extension hooks and shared resources |
| Failure and consistency | Status/substatus decisions, retries/deadlines, session/consistency, metadata caches and regional routing |
| Network and availability | Direct/Gateway transport, supported protocols, pooling, TLS, hedging, circuit breaking and recovery |
| Data and query | CRUD/read-many, serialization, partition/feed ranges, SQL/vector/full-text/hybrid queries, paging and continuations |
| Writes and background work | Batch/bulk/patch, change-feed pull/processor, leases/checkpoints, throughput control and resource/policy APIs |
| Cross-cutting and companion | Diagnostics/tracing/metrics, runtime/API/artifact compatibility, encryption and core integration |

Experiments can select an existing or proposed PR in any lane, including
multi-domain changes. Map the change to its full impacted-contract set and
required evidence. If a necessary contract or fixture is missing, the experiment
exposes and tracks that gap; it is not rejected merely because it is not a retry
change, and it is not granted autonomous mergeability.

Inventory completeness, test-execution completeness and autonomous-merge
qualification are three different milestones. All-domain design coverage does
not imply all paths already have adequate tests or authorize all-domain merges.

## 3. Observed starting point

### 3.1 Evidence snapshot and limits

Sources were inspected read-only on 2026-10-31. No Java builds, tests, coverage
runs, or historical reproductions were executed for this draft.

- The local Java checkout reported branch `main`, commit
  `d062a952ddd3e7498f2359e5ccc541701879d42e`, dated 2026-07-15.
  Its local/remote tracking histories were substantially divergent. This is
  **not a verified current upstream baseline**; local files were not updated.
- For version 0.2, GitHub's main-commit API pinned upstream inventory to
  [`42702a3a1421498ee457ff9cbe56713d0877d39f`](https://github.com/Azure/azure-sdk-for-java/commit/42702a3a1421498ee457ff9cbe56713d0877d39f),
  committed 2026-10-31T22:50:37Z. GitHub semantic search reported the same indexed
  revision. This resolves the source-snapshot part of D-01, not the supported
  runtime/branch/service-capability decisions.
- The complete pinned core changelog was retrieved: 1,478 lines, from
  `4.84.0-beta.1 (Unreleased)` through `4.0.1-beta.1 (2020-03-10)`.
  Unreleased and historical entries are inventory evidence, not GA promises.
- Non-truncated Git tree manifests were retrieved for `azure-cosmos`,
  `azure-cosmos-tests` and `azure-cosmos-test`. A full file manifest proves
  structural enumeration, not that every method/branch/contract was inspected.
- The canonical concept repository was fast-forward synced on `main` and
  inspected at `bcfbc786fa5296deebcccd11369efb583e63e48c`.
- Six closed, Cosmos-and-bug-labeled public issue summaries/bodies were sampled.
  This was neither a complete issue export nor proof of root cause or fix.
- The local PR Review Router, PR Test Model Reviewer, Review Quality Gate, and
  peer-map definitions were inspected. They are local configuration, not yet
  pinned repository-owned production policy.
- No `ado` server tools were exposed in the available tool inventory. Live Azure
  DevOps pipeline history and required-check settings were not inspected.
  RCAKit's earlier lookup required authentication; no operational incident
  corpus is claimed here.
- Recovery note for version 0.2.1: the four initial background inventory agents
  became unavailable before completed reports were persisted. Their downloaded
  public-source research inputs remain, but there are no completed domain
  reports or changelog semantic ledger from those runs. Do not describe the
  reports as pending arrival or the research as completed. Resume from the saved
  inputs and keep the affected checklist items open.
- Repository import for version 0.2.2 preserves the fixed initial `source/`
  intake, not a whole session or a complete SDK checkout. The
  [import manifest](research/java-sdk/import-manifest.json) records every
  original path, deduplication, verification and exclusion. The
  [report status](research/java-sdk/reports/status.json) remains incomplete.
  Two cached copies of `RxGatewayStoreModel.java` did not match the pinned public
  blob; their bytes are excluded and their digests recorded, with a verified
  public replacement retained. One public emulator-default key literal is also
  redacted from the archival CI copy, with original and imported hashes kept
  distinct. New parent-authored recovery outputs are deferred
  to a separate completed handoff, not represented as recovered agent reports.

All version 0.2 feature research uses the pinned upstream source, not the
divergent local Java checkout. Continue reconciling local-versus-upstream
configuration and the supported SDK/runtime/service matrix. The configuration
observations in Section 3.2 remain explicitly version-0.1 local observations
until individually revalidated against upstream.

### 3.2 Verified configuration observations

Paths in this table are relative to the Java repository, except the Router files.

| Observation | Evidence | Consequence for the design |
|---|---|---|
| Production POM sets `jacoco.skip=true`, with a comment that tests run from `azure-cosmos-tests`. | `sdk/cosmos/azure-cosmos/pom.xml:35-49` | Aggregate executions against production classes across modules; do not measure only the test module. |
| Test-module POM also sets `jacoco.skip=true`. | `sdk/cosmos/azure-cosmos-tests/pom.xml:25-34` | Current coverage percentages cannot be inferred from the configured minimum values. |
| Surefire has `skipTests=true`, while the `unit` profile configures Failsafe with a TestNG suite. | `azure-cosmos-tests/pom.xml:229-337` | Trace effective Maven lifecycle, inherited bindings, and test discovery before selecting a canonical command. `mvn test` is not assumed sufficient. |
| Unit suite selects the `unit` group under `com.azure.cosmos.*`. | `azure-cosmos-tests/src/test/resources/unit-testng.xml:26-42` | Verify each intended test is discovered, not merely present on disk. |
| Unit and emulator jobs are configured in the Cosmos-specific CI template. | `eng/pipelines/templates/stages/cosmos-sdk-client.yml:55-108` | Reuse existing jobs and validate their effective PR requirements. |
| Live testing config includes HTTP/2 and network-fault variants; the YAML says `trigger: none`. | `sdk/cosmos/tests.yml:1-110` | Presence is not proof of per-PR execution or absence of scheduling elsewhere. Discover schedules and status-check mapping. |
| Some POM paths are excluded from CI/PR path filters. | `sdk/cosmos/ci.yml:30-108` | Configuration-only changes need an explicit validation path; do not infer that every important change triggers this pipeline. |
| Fault-injection validation explicitly limits supported combinations, including gateway connection-error rules. | `azure-cosmos-tests/src/test/java/com/azure/cosmos/faultinjection/FaultInjectionUnitTest.java:60-140` | Do not assume one harness can inject every protocol or metadata failure. |
| Connection-fault tests include real-account, Direct-mode cases. | `azure-cosmos-tests/src/test/java/com/azure/cosmos/faultinjection/FaultInjectionConnectionErrorRuleTests.java:50-123` | Fault-injection tests are not necessarily offline or deterministic. |
| The current Router dispatches test-model and skeptical review in Standard/Deep tiers, normalizes findings, and retains a human approval gate. | Locally installed PR Review Router agent definition, Stages 5-7 and Hard rules; unversioned integration input, see Section 20.3 | Autonomous judgment needs a separately approved integration contract; the existing Router is not already an autonomous merge service. |

Pinned upstream CI reinspection for version 0.2 confirms unit/emulator job
configuration and POM path-filter exclusions. It also shows live-test jobs
resolving fixed, shared accounts rather than creating a fresh account per run,
with post-run cleanup templates
([`tests.yml:11-27`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/tests.yml#L11-L27)).
Consequently, fixture isolation, concurrent-run ownership and precise cleanup
are first-class test-system obligations. This is source configuration evidence,
not proof that those jobs ran, were required, or cleaned up successfully.

### 3.3 Baseline deliverables

The assessment must produce:

1. Production source/class inventory, public API inventory, dependency/runtime
   matrix, and supported-versus-preview feature list.
2. Test inventory with source location, runner, groups, data-provider cases,
   effective command, environment, result count, skips, duration, and owner.
3. Test-to-production and test-to-invariant mappings, including uncovered and
   unmapped entries.
4. Coverage by package and risk domain, split by suite and aggregated safely.
5. CI trigger, schedule, artifact, credential, and required-status-check map.
6. Flakiness, retry, quarantine, runtime, and resource-cost baseline.
7. Historical bug candidate inventory and reproducibility triage.
8. An explicit gap list ranked by impact, historical failures, change frequency,
   complexity, and lack of a reliable oracle.
9. A changelog-to-feature/invariant ledger covering all releases and semantic
   entries, plus a current-public-API/configuration reconciliation. Include
   preview, deprecated, removed, dependency, compatibility and docs-only entries
   with explicit classification; do not make old entries disappear.
10. A whole-SDK domain completeness matrix separating source discovery,
    contract verification, test mapping, execution and autonomy qualification.

All numerical scores in this draft are **unmeasured** unless labeled as a
proposed policy. Do not invent a baseline.

## 4. Architecture and evidence model

### 4.1 Logical components

```text
Public issues / SDK specifications / Java API and implementation inventory
                              |
                              v
           Versioned feature, behavior, invariant, and scenario registry
                              |
                              v
               Existing tests + targeted test extensions
                              |
                    Trusted execution pipeline
                              |
             Immutable evidence bundle + score vector
                              |
              Independent PR Review Router review runs
                              |
                 Findings -> agent repair -> new SHA
                              |
              Router merge-eligibility decisions
                              |
           Restricted merge executor + repository policy
                              |
                     Validated merge to main

                       STOP: no release action
```

These are responsibilities, not a demand to build a new service for each box.
Prefer repository metadata, current Maven/TestNG tooling, existing CI, and small
policy adapters before introducing infrastructure.

### 4.2 Traceability graph

```text
feature -> behavior -> invariant -> applicable scenario cells -> test cases
issue -> affected revision -> regression case -> invariant
test execution -> result + coverage + assertion-strength evidence
PR -> impacted contracts -> required checks -> evidence -> review disposition
merge candidate -> exact evidence/reviews -> merge receipt
```

Every link must be explainable in both directions. An invariant without tests is
a gap; a test without meaningful assertions is weak evidence; an uncovered
implementation branch cannot be hidden because it has no registered feature.

Runtime coverage establishes execution relationships, not semantic correctness.
Source search and static relationships support impact analysis, but do not alone
prove that a behavior has been tested.

### 4.3 Registry records

Proposed record types and fields:

| Record | Required information |
|---|---|
| Feature | Stable ID, APIs/options, lifecycle, Java versions, supported configurations, implementation boundaries, owners, evidence status |
| Behavior | Feature ID, operation/resource, status/substatus and origin if relevant, preconditions, state transitions, allowed outcome, forbidden outcome, contract source |
| Invariant | Stable ID/revision, precise predicate, applicability, oracle, positive/negative/boundary cases, risk, references, test IDs, verification state |
| Scenario | Stable ID, dimensions, ordered events, valid constraints, initial state, seed/schedule, completion bounds, expected observations |
| Test | Stable logical ID, parameter-case IDs, runner/profile, source, invariant/scenario links, environment, expected discovery, runtime class |
| Benchmark case | Issue/fix provenance, affected revision, reproducer, regression assertion, historical environment, corpus partition, execution state |
| Exception | Exact scope, reason, evidence, approver, expiry, impact on autonomy, replacement/repair task |
| Review receipt | Candidate/base/policy digests, run identity, required roles, verdict, findings/dispositions, context gaps, evidence references |

Prefer repository-versioned YAML or JSON with schema validation, but choose the
format in D-04. This draft does not create implementation files or schemas.

### 4.4 Verification states

Use explicit states:

`proposed -> contract-verified -> test-mapped -> execution-verified -> autonomy-qualified`

Also support `unsupported`, `blocked`, and `retired-with-history`.

The catalogs below are **seed catalogs**, not claims of exhaustive discovery or
passing coverage. Promotion requires Java-specific contract evidence and actual
execution. Keep disputed semantics as blocked questions, not green invariants.

### 4.5 Contract authority and conflicts

Use canonical concept docs for domain grounding and Java's approved public
contracts/specifications for Java behavior. Implementation shows what the SDK
currently does, which may itself be defective. Peer SDKs provide comparison, not
automatic authority.

If documents, Java code, issue descriptions, and service observations disagree:
record the conflict, preserve provenance, obtain an explicit contract decision,
and block autonomous changes to the disputed behavior.

In particular, the retry concept chapter includes .NET examples and defaults;
do not mechanically convert them into Java retry rules. Canonical chapters also
contain qualified or unverified statements. Those are research tasks, not test
oracles. No blanket "Direct retries are always a superset of Gateway" rule is
adopted without Java-specific verification.

## 5. Feature and behavior inventory

### 5.1 Seed inventory

For each row, enumerate public entry points and internal support paths, then map
documented variants to behaviors, invariants, scenarios, and tests.

| ID | Domain | Inventory and edge cases to capture |
|---|---|---|
| F-01 | Client construction and lifecycle | Sync/async builders; lazy initialization; warmup/proactive initialization; concurrent use; shared resources; failed construction; repeated close; close during requests; use after close |
| F-02 | Configuration and precedence | Public/internal defaults; null versus unset; explicit false/zero; invalid bounds; environment/system properties; request overrides; incompatible options; feature detection and fallback |
| F-03 | Authentication and authorization | Keys; key rotation; resource tokens; token credentials and refresh; authorization resolver; permissions; restricted resource access; authentication versus authorization failures |
| F-04 | Resource lifecycle | Databases/containers; create-if-not-exists races; delete/recreate with same name and different RID; account/container metadata; stale handles |
| F-05 | Item operations | Create/read/upsert/replace/delete; missing items; response-content options; partition-key extraction; read-many; exceptions and response metadata |
| F-06 | Serialization and models | Custom serializers; parameters versus item payloads; projections; null/missing/undefined; number/date/Unicode boundaries; unknown fields; malformed JSON; response-body ownership |
| F-07 | Partition keys and feed ranges | Hash versions; single/hierarchical keys; prefixes; null/none; escaped paths; range endpoints; opaque FeedRange round-trip and applicability |
| F-08 | Caches and metadata | Account, name/RID, partition map, address, query-plan caches; cold/warm states; refresh coalescing; invalidation; concurrency; deletion/recreation |
| F-09 | Consistency and session tokens | All supported levels and overrides; automatic/explicit tokens; merge and cache scope; region-scoped behavior; splits/merges; invalid tokens; recreate isolation |
| F-10 | Retry and deadlines | Status/substatus decisions; retry budgets; backoff/jitter; metadata retries; nested retry composition; ambiguous writes; cancellation; end-to-end versus per-attempt timeout |
| F-11 | Regional routing | Preferred/excluded regions; endpoint discovery; single/multi-writer accounts; regional outage/recovery; topology change; no eligible region; metadata reachability |
| F-12 | Availability mechanisms | Threshold-based availability/hedging; per-partition circuit breaker and failover where supported; winning/losing requests; cooldown; probes; state isolation |
| F-13 | Direct transport | RNTBD handshake/framing; TLS; channels/pools; multiplexing; connection acquisition; read/write timeouts; partial I/O; leak-free shutdown |
| F-14 | Gateway and HTTP transport | HTTP/1.1 and HTTP/2 where supported; proxy; connection pooling; stream limits; GOAWAY/reset/PING; redirects; malformed headers; local versus regional failure |
| F-15 | Thin-client and capability negotiation | Supported account types; explicit versus implicit enablement; endpoint probe; regional endpoints; fallback; disabled paths; service capability mismatch |
| F-16 | SQL query execution | Point/single/cross-partition; query plans; parameterization; parallelism; prefetch; ORDER BY; aggregates; DISTINCT; GROUP BY; TOP/OFFSET/LIMIT; supported continuation combinations |
| F-17 | Vector/full-text/hybrid queries | Embedding/index configuration; score scope; RRF/ranks; empty/unequal result sets; ties; custom serialization; multiple subscriptions; service capability limits |
| F-18 | Paging and iterables | Async/sync pages; continuation/resume; empty intermediate pages; page size hints; resubscription/reiteration; cancellation; topology changes; token compatibility |
| F-19 | Transactional batch | Same-logical-partition scope; mixed operations; atomicity; per-operation results; failure dependencies; limits; conditionals; response-content configuration |
| F-20 | Bulk execution | Adaptive concurrency/batching; per-item outcomes; mixed success; retry/split behavior; streaming input; completion; correlation; null response versus exception; throughput controls |
| F-21 | Patch and optimistic concurrency | Set/add/remove/replace/increment/move where supported; filters; ETags; non-idempotent operations; retry ambiguity; path escaping; invalid operation combinations |
| F-22 | Change-feed pull model | Start modes; continuation; empty/304 handling; full-fidelity/all-versions modes where supported; feed ranges; split/merge; resume; retention limits |
| F-23 | Change Feed Processor | Lease acquisition/renewal/rebalance; callbacks; checkpoint modes; restart; at-least-once delivery; failed callbacks; split/merge; graceful shutdown; estimator |
| F-24 | Throughput and throttling | Manual/autoscale metadata APIs; shared/dedicated offers; priority; local/global throughput control; hot partitions; 429 attribution and retry budgets |
| F-25 | Container policies | Indexing/spatial/composite/vector/full-text policies; unique keys; TTL; computed properties; conflict policies; validation and wire compatibility |
| F-26 | Scripts and child resources | Stored procedures/triggers/UDFs; users/permissions; conflicts; parameter serialization; pagination; supported operation constraints |
| F-27 | Dedicated gateway and caching | Relevant request options; staleness/consistency configuration; bypass; cache hit/miss metadata; unsupported combinations |
| F-28 | Diagnostics and observability | Exception/status preservation; request charge; activity IDs; retry/subrequest attribution; tracing; metrics; callbacks; privacy; bounded overhead |
| F-29 | Reactive and concurrency contracts | Cold/lazy execution; repeated subscriptions; request-state isolation; backpressure; cancellation races; scheduler/context propagation; no event-loop blocking |
| F-30 | Compatibility and runtime | Source/binary APIs; token compatibility; supported JDK/OS/TLS/dependency ranges; JPMS; packaged artifacts; consumer classpath conflicts |
| F-31 | New/preview metadata features | Global secondary index and encryption-policy/key metadata visible in the selected baseline; feature flags; unsupported-account errors; lifecycle and compatibility |

Presence of a model in the local tree is an inventory lead, not proof that its
service feature is generally available. D-01/D-05 must classify each feature and
its supported combinations.

### 5.2 How inventory completeness is established

Do not declare completeness from a hand-authored list alone:

1. Enumerate exported public types, methods, constructors, options, enums, and
   configuration keys at the pinned baseline.
2. Enumerate implementation domains, status/substatus constants and decision
   sites, supported protocol paths, feature flags, and background workflows.
3. Reconcile documentation, changelogs, test groups, issue themes, and consumer
   integrations against that enumeration.
4. Assign every entry a feature/behavior ID or an explicit exclusion with reason.
5. Review unmapped entries and orphaned tests. A new API, status constant,
   configuration switch, or behavior-changing branch must create an inventory
   delta in its PR.
6. Record coverage of the inventory itself: mapped / discovered entries, plus
   unresolved and intentionally unsupported counts.

Inventory completeness is relative to an immutable SDK version and declared
scope. Service evolution requires new catalog revisions.

### 5.3 Changelog reconciliation is a required closure gate

Review the entire core changelog, including old beta/hotfix releases, Features
Added/New Features, Bugs Fixed, Breaking Changes and Other Changes. Also account
for companion encryption release history. A latest-release summary or a search
for feature keywords is not sufficient.

Every semantic entry needs a ledger record:

```text
entry ID and pinned source line span
release/version and heading
normalized behavior/change summary
classification: feature / behavior-fix / breaking / dependency / docs / other
feature and invariant mappings, or an explicit unresolved item
lifecycle: current / preview / deprecated / removed / historical / unknown
mapping strength: explicit behavior / family-level lead / unresolved
source/API/implementation verification and candidate regression evidence
```

Changelog entries are discovery evidence, not complete specifications. A fix can
expose a missing invariant even when it introduces no public API. A dependency
upgrade can imply runtime, TLS, wire-encoding, scheduling or allocation
obligations. Removed APIs remain in lifecycle/compatibility history without
being reintroduced as current features.

Reconcile in both directions:

1. Changelog entry -> feature/behavior -> atomic invariant -> scenarios/tests.
2. Current exported API/option/feature flag and internal workflow -> feature/
   behavior -> changelog entry, approved specification, or documented-history gap.

Track total entries, classified entries, explicit semantic mappings,
family-level mappings, unresolved entries and current source elements still
unmapped. "100% of rows classified" is not "100% of behaviors verified."

### 5.4 Whole-SDK completeness and experiment admission

For every domain, record independent columns for:

- Current API/configuration and internal-path enumeration.
- Full-history reconciliation and lifecycle classification.
- Java-specific atomic contract/oracle verification.
- Status/substatus and interaction-scenario mapping.
- Existing test/assertion discovery and required fixture capability.
- Actual execution, multidimensional scores and remaining gaps.
- Change-class autonomy qualification.

No experiment is excluded because its domain was not the first implementation
workstream. Unmapped or incompletely modeled behavior instead becomes a
blocking contract/evidence task in that experiment. Required sentinel invariants
span the whole SDK, while impacted domain/dependency tests supply deeper checks.

An SDK-wide inventory can be approved only after every discovered entry has an
explicit mapping or a justified lifecycle/out-of-product classification.
Family-level leads do not satisfy atomic contract verification. Domain breadth
is mandatory from the start; execution and qualification can progress at
different rates without concealing incomplete domains.

## 6. SDK invariant catalog

### 6.1 What qualifies as an invariant

An invariant is a precise statement of behavior under stated preconditions, not
a slogan such as "retries work."

Each record must specify:

- Applicable APIs/configurations and initial state.
- Triggering event or event sequence.
- Observable allowed and forbidden outcomes.
- Timing/resource bounds where meaningful.
- An oracle independent of the implementation under test.
- Contract citation and Java-specific verification.
- Tests covering success, failure, boundaries, and applicable concurrency.

Separate safety ("must never") from liveness ("must eventually within a bound").
Liveness bounds must account for supported deadlines and cleanup behavior, not
assume instantaneous network cancellation or forced reversal of a committed write.

### 6.2 Seed invariant families

All rows below begin as proposed contracts pending the verification states in
Section 4.4. Each family will expand into atomic, machine-checkable records.

| ID | Candidate invariant / proof obligation |
|---|---|
| INV-CFG-01 | Public and internal layers resolve null/unset/explicit values consistently with the documented default and precedence rules. |
| INV-CFG-02 | Invalid or incompatible configuration is rejected as documented; a requested feature does not silently degenerate into weaker behavior unless that fallback is an explicit contract. |
| INV-LIFE-01 | Supported concurrent client operations do not share mutable per-request state or close resources still owned by another live client. |
| INV-LIFE-02 | Closing a client has bounded cleanup; repeated close follows its contract; post-close calls fail explicitly rather than hang or masquerade as success. |
| INV-AUTH-01 | Requests use credentials appropriate to the target resource; rotation/refresh is concurrency-safe and never exposes credential material in logs or diagnostics. |
| INV-AUTH-02 | Authorization failures are distinguished from endpoint/routing failures; refresh and retries are bounded and specific to the documented credential behavior. |
| INV-CRUD-01 | Item identity, partition key, conditional headers, request options, and body are preserved through the documented request pipeline. |
| INV-CRUD-02 | A failure preserves the relevant status/substatus and cause; bodyless successes and disabled response-content options remain valid outcomes. |
| INV-SER-01 | Item, query-parameter, projection, patch, and supported child-resource serialization use the documented serializer path; custom serializers are neither bypassed nor applied to unrelated metadata. |
| INV-SER-02 | Malformed payloads and serializer failures are explicit, bounded, and do not leak buffers or silently truncate values. |
| INV-PK-01 | Partition-key encoding/hash selection and range membership match approved vectors, including hierarchical and boundary cases. |
| INV-PK-02 | A stable feed-range request is resolved against current topology; persisted physical range IDs are not mistaken for stable logical identities. |
| INV-CACHE-01 | Metadata refresh cannot regress a newer routing/account state or resurrect a deleted container's identity. |
| INV-CACHE-02 | Concurrent refreshes and partial failures do not cause cache stampedes, deadlocks, or cross-container contamination beyond explicit bounds. |
| INV-SESSION-01 | Valid compatible token merges preserve monotonic progress; merge algebra is checked against the supported token format, not a different SDK's representation. |
| INV-SESSION-02 | Session state is scoped to the correct account/container/partition/region context; delete/recreate does not inherit stale identity-bound state. |
| INV-SESSION-03 | Session reads either satisfy the applicable documented token requirement or fail explicitly; retries/failover do not silently weaken consistency. |
| INV-CONS-01 | Account/request consistency combinations are validated or propagated as documented; the SDK does not claim stronger consistency than the configured service can provide. |
| INV-RETRY-01 | Retry decisions depend on operation, status/substatus, failure origin, transmission state, connectivity mode, and options; a single status-only rule is insufficient. |
| INV-RETRY-02 | Retry counts, delays, and nested policy execution respect their configured budgets and end-to-end deadline semantics. No hidden unbounded retry loop exists. |
| INV-RETRY-03 | Ambiguous non-idempotent writes are not replayed outside the documented opt-in contract; a timeout/cancellation does not imply the server did not commit. |
| INV-RETRY-04 | Exhaustion returns the documented final exception, including any intentional status transformation and diagnostic cause chain. |
| INV-RETRY-05 | Server retry-after handling has explicit boundary behavior for missing, zero, negative, malformed, huge, and over-budget values. |
| INV-ROUTE-01 | Requests use an eligible endpoint under preferred/excluded-region, write-location, discovery, and failover rules. No eligible endpoint produces a bounded explicit failure. |
| INV-ROUTE-02 | Local channel/stream failures do not automatically poison region-wide health unless the Java policy explicitly calls for it. |
| INV-AVAIL-01 | Hedged attempts produce one logical terminal result; losing attempts are cleaned up and cannot corrupt the winning result or its consistency/diagnostics. |
| INV-AVAIL-02 | Circuit-breaker/failover state transitions and recovery probes are scoped correctly and cannot starve healthy partitions indefinitely. |
| INV-TRANS-01 | Each request/stream correlation ID resolves to the correct response or failure even with multiplexing, reordering, partial reads, and channel shutdown. |
| INV-TRANS-02 | Connection acquisition, timeout races, protocol errors, TLS failures, and pool saturation terminate as documented without unbounded queued work. |
| INV-TRANS-03 | Buffers, streams, timers, channels, threads, and subscriptions are released according to ownership after success, failure, cancellation, and close. |
| INV-HTTP-01 | Capability negotiation and explicit protocol options select only supported paths; fallback neither downgrades security nor silently changes semantic guarantees. |
| INV-QUERY-01 | Query result values/order/aggregates match the approved oracle for the supported query shape and dataset, independent of partition arrival order. |
| INV-QUERY-02 | Query concurrency/prefetch controls preserve semantics and bound resources; repeated subscriptions do not mix independently fetched intermediate results. |
| INV-QUERY-03 | Full-text/vector/hybrid scoring handles empty, unequal, tied, and partially failed component results according to its verified Java/service contract. |
| INV-PAGE-01 | Under a fixed dataset and a supported resumable query shape, page/resume yields the expected result multiset and required ordering without gaps or extra duplication. |
| INV-PAGE-02 | Empty nonterminal pages, opaque continuations, unsupported token/query combinations, topology changes, and repeated iteration follow explicit contracts. |
| INV-BATCH-01 | A valid transactional batch preserves documented atomicity within its supported logical-partition scope and faithfully reports per-operation failures. |
| INV-BULK-01 | Every accepted bulk input receives its documented correlated outcome or explicit stream failure; mixed outcomes never become false all-success. |
| INV-BULK-02 | A failed bulk operation can have an exception without a normal response; diagnostics/result handling must not dereference absent success state. |
| INV-PATCH-01 | Conditional/ETag failures do not mutate data; non-idempotent patch operations obey ambiguous-write retry restrictions. |
| INV-CF-01 | Change-feed ordering and visibility are asserted only within the documented partition/mode scope; no global ordering or exactly-once promise is invented. |
| INV-CF-02 | Restart/checkpoint/split/merge preserves the documented delivery guarantee; permitted replay is distinguished from unintended data loss or extra replay. |
| INV-CFP-01 | Lease/checkpoint transitions and callback failures preserve ownership rules and at-least-once processing semantics under the supported checkpoint mode. |
| INV-RU-01 | Request charge, throttling source, throughput-control decisions, and retries remain correctly attributed; client-side control is not mistaken for a service response. |
| INV-POLICY-01 | Container/index/TTL/conflict policies and script parameters preserve their documented wire representation and validation constraints. |
| INV-DIAG-01 | Diagnostics/tracing preserve operation and attempt boundaries across retries, pages, failures, and repeated subscriptions without duplicate lifecycle transitions. |
| INV-DIAG-02 | Telemetry and user hooks obey documented error handling, privacy, cardinality, and overhead limits; observer failures do not silently change database outcomes. |
| INV-RX-01 | Async APIs obey applicable Reactor signal, laziness, cancellation, backpressure, and context rules; unsupported multiple-subscription assumptions are not introduced. |
| INV-RX-02 | Independent subscriptions and request objects isolate mutable state; timeout/cancel/response races do not produce duplicate terminal signals. |
| INV-COMPAT-01 | Changes preserve approved source/binary/wire/token contracts and supported runtime/dependency combinations, or are explicitly routed outside autonomous scope. |
| INV-COMPAT-02 | Newly introduced third-party implementation types are not exposed through customer-facing APIs. Existing intentional public dependencies are baseline contracts, not implicitly removed. |
| INV-PERF-01 | Applicable throughput, latency, allocation, resource, and cancellation-cleanup budgets remain within calibrated limits on comparable workloads. |

### 6.3 Avoid overstrong or false contracts

- Query pagination is not automatically a snapshot across concurrent writes.
  Use a fixed dataset for exact enumeration tests; model allowed concurrent
  outcomes separately.
- Change Feed Processor delivery is not exactly once. Callback success and
  checkpoint persistence are different events.
- Bulk operations are not a cross-partition transaction.
- A timed-out write may have committed; retry safety depends on operation and
  the documented options.
- Session guarantees are not account-global guarantees across arbitrary clients.
- Service consistency, indexing, TTL, and topology behavior are not fully
  implemented or provable by the SDK. Test the client contract and validate
  service assumptions using appropriate live fixtures.
- Page-size and concurrency options may be hints, not exact result-size promises.
- Resource bounds must distinguish supported workload envelopes from impossible
  demands under an unbounded caller input stream.

### 6.4 Example atomic invariant

`INV-RETRY-02` must expand into concrete records such as:

```yaml
id: INV-RETRY-02A
revision: 1
state: proposed
feature: F-10
contract: "Throttling retries respect both attempt and cumulative-delay limits."
preconditions:
  - "A verified Java API/configuration defines both limits."
  - "The operation reaches the throttling policy with a scripted response sequence."
oracle:
  - "Compute allowed attempts and delays from the approved specification."
  - "Observe attempted requests and scheduled delays independently of policy state."
cases:
  - "No retry allowed."
  - "Delay exactly at, just below, and just above the remaining budget."
  - "429 followed by success; persistent 429; cancellation during backoff."
  - "Retry budget interacts with a shorter end-to-end deadline."
forbidden:
  - "Extra attempt outside the verified contract."
  - "Fresh full deadline allocated by a nested retry."
evidence:
  contract_source: pending
  java_symbols: pending
  tests: []
```

Numbers, defaults, and inclusive/exclusive timing decisions are intentionally
not invented. Their resolution is part of contract verification.

## 7. Status-code and substatus behavior catalog

### 7.1 Model the full decision key

Use at least:

```text
(operation/resource type, status, substatus, origin,
 connectivity/protocol, request transmission/commit ambiguity,
 consistency/session state, retry options, region/topology state,
 remaining budgets, feature capability)
    -> retry/refresh/route/delay/surface decisions + diagnostics + cleanup
```

`1002` without its HTTP status is ambiguous. `403/1008` and `410/1008` are
different behaviors. Server failures, SDK-generated exceptions, and locally
injected faults must remain distinct.

Every row needs success-after-recovery, persistent-failure, exhausted-budget,
cancel/deadline, read/write safety, and diagnostics cases where applicable.

### 7.2 Seed status matrix

This table states **questions and obligations to verify**, not blanket current
Java retry behavior.

| ID | Status / family | Required contract and cases |
|---|---|---|
| ST-01 | 200 / 201 / 204 and other applicable 2xx | Body/no-body success; headers; charge; session capture; content-response options; unknown successful response handling |
| ST-02 | 304 | Conditional-read versus change-feed semantics; no new content; continuation/ETag progression; no busy-spin; correct public representation |
| ST-03 | 400 | Invalid requests and query plans; 1001 partition-key mismatch; 1004 cross-partition query not servable; distinguish genuine invalid input from verified refresh/recovery paths |
| ST-04 | Client-generated 400 / 10101, 10102 | Custom-serializer failure and invalid ID; preserve cause; no unintended network operation |
| ST-05 | 401 | Invalid/expired credentials, refresh interactions, clock skew and resolver failures; never infinite credential retries |
| ST-06 | 403, generic | Access denial versus special failover/capability conditions; no blanket "all 403 retry" or "all 403 terminal" rule |
| ST-07 | 403 / 3 | WriteForbidden; current writable topology, refresh and reroute, excluded regions, exhausted/no alternate endpoints |
| ST-08 | 403 / 1008 | Database-account-not-found condition; endpoint/account refresh contract; distinguish wrong/deleted account from transient topology |
| ST-09 | 404, generic | Missing item/resource; normal surfacing; create/delete/recreate races; do not disguise missing data as success |
| ST-10 | 404 / 1002 | ReadSessionNotAvailable; token-aware replica/region policy; explicit token; budget exhaustion |
| ST-11 | 404 / 1003, 1013 | Owner-resource-not-exists / collection-not-available-for-read in applicable metadata paths; stale cache versus true absence |
| ST-12 | 405 | Unsupported operation or method; preserve the service contract rather than invent a recovery strategy |
| ST-13 | 408 and local timeout exceptions | Server timeout versus acquisition/connect/read/write/transit/client deadline; sent versus unsent versus ambiguous request |
| ST-14 | 409 | Duplicate identity / applicable conflict; conditional retry safety; no automatic overwrite |
| ST-15 | 410, generic | Distinguish stale address/name/range, transport-generated events, and topology state; bound nested recovery |
| ST-16 | 410 / 1000 | Name-cache stale; invalidate correct name/RID scope; exhausted retry transformation |
| ST-17 | 410 / 1002 | PartitionKeyRangeGone; refresh ranges; remap query/point/feed/bulk operations correctly |
| ST-18 | 410 / 1007 | CompletingSplitOrMerge; both split and merge, repeated stale responses, partial metadata availability |
| ST-19 | 410 / 1008 | CompletingPartitionMigration; refresh and recovery differ from 403/1008 |
| ST-20 | 410 / 1022 | Lease-not-found path; verified Java retry/translation/failover behavior and final substatus |
| ST-21 | Substatus 1024 | Incorrect-container-RID constant in the inspected Java source; establish valid status pairings from producers/handlers rather than assign a global meaning |
| ST-22 | 412 | ETag or patch predicate failure; no mutation; bulk/batch correlation; no accidental conversion into success |
| ST-23 | 413 | Item/batch/request size limits at boundary; client versus server validation; streaming cleanup; split batching only where supported |
| ST-24 | 423 | Locked resource; operation-specific surface/retry contract; deadlines |
| ST-25 | 429, service-origin | Retry-after; budgets; hot partition; response headers; concurrent callers; fairness; priority where supported |
| ST-26 | 429 / 3200 where applicable | User request rate limit; source attribution; preserve known and unknown throttling substatuses |
| ST-27 | Client throughput-control failures | 10003 / 10005 rate-too-large and 10004 offer-not-configured families; establish actual paired status and policy from Java producers |
| ST-28 | 449 | RetryWith; verify Java behavior separately by mode, operation, budgets, and write-safety options; do not import .NET defaults |
| ST-29 | 500 | Service/internal versus SDK-generated errors; preserve cause, cleanup, and documented policy; no blanket retry rule |
| ST-30 | 503 | Endpoint/replica availability; alternate regions; eligible writes; health-state transitions; exhausted recovery |
| ST-31 | Gateway-generated local failures | 10001 unavailable; 10002 read timeout; correct origin, request state, health and failover effects |
| ST-32 | HTTP/2 local PING closure / 10006 | Present in inspected local source; verify availability at chosen baseline and distinguish local channel failure from regional outage |
| ST-33 | 20001 / 20002 | Transport-generated / timeout-generated 410 families; recovery, budget composition, and final cause |
| ST-34 | 20008 / 20911 | Client-operation timeout / transit timeout families; exact status pairing, deadlines, request state, diagnostic attribution |
| ST-35 | 20901-20914, defined entries | Enumerate negative timeout, context/token/auth/response/state failures, closed client and circuit-breaker/session state; gaps in numeric range are not invented codes |
| ST-36 | 21001-21012, defined entries | Exhausted retry, server-generated failures, quorum/barrier/parse conditions; validate status transformations and preserved causes |
| ST-37 | Connection/DNS/TLS/proxy/protocol exceptions | No valid HTTP response; handshake/connection/stream state, retry safety, cleanup; no bypass of certificate validation |
| ST-38 | Batch dependency failures | Per-operation failure and dependent-operation representation, including 424 where applicable; discover all codes emitted by batch handling |
| ST-39 | Unknown, missing, malformed status/substatus | Forward-compatible explicit handling; safe classification; no accidental infinite retry or dropped error |

Sources for numeric names above: inspected Java
`HttpConstants.java:381-519`. This file is a seed, not a complete list of all
numeric literals, enums, mappings, or service substatuses used anywhere in Java.

### 7.3 Exhaustiveness procedure

- Inventory constants, exception producers, retry handlers, response mappers,
  switch/default cases, batch decoders, and relevant wire/service contracts.
- Map known service substatuses beyond Java constants where the SDK has explicit
  behavior or observable preservation requirements.
- Confirm each code's valid HTTP pairing, origin, operation, and mode.
- Assign each decision branch a behavior ID, oracle, and tests.
- Include unknown/default paths and newly introduced values.
- Generate a catalog diff on every relevant PR. A new constant or handler with
  no behavior record blocks autonomous merging.

Java's existing test harness may not support injecting some rows. Mark those as
gaps and choose transport-level or live fixtures, rather than relabeling them
covered by a mock of the retry method itself.

## 8. Scenario model and interaction coverage

### 8.1 Axes

| Axis | Representative values / constraints |
|---|---|
| API | Sync, async, paging, bulk stream, batch, change-feed pull, processor callbacks |
| Operation | Read, read-many, query, metadata read/write, create/upsert/replace/delete/patch, script, feed |
| Connectivity | Direct RNTBD, Gateway HTTPS, supported HTTP versions, thin-client paths; valid combinations only |
| Account | Single region, multi-region single writer, multi-writer; supported service capabilities |
| Consistency | Supported account levels and request overrides; automatic/explicit session state |
| Partitioning | Single/multiple physical ranges, single/hierarchical logical keys, boundary values, split/merge/migration |
| Cache state | Cold, warm, stale, partially refreshed, concurrent refresh, delete/recreate |
| Failure | Status/substatus families, malformed/partial response, lost response, DNS/TLS/connectivity, unavailable metadata |
| Request phase | Before connection, before send, after partial/full send, possible commit, response parsing, user callback |
| Timing | Just before/at/after deadline, delayed response, cancellation during backoff, simultaneous completion/close |
| Load | Idle, steady, burst, hot partition, saturated pool, slow consumer, large input; bounded supported envelope |
| Data | Empty/single/many items, null/missing fields, Unicode, numbers, payload limits, skew, ties, projections |
| Lifecycle | Initialization, steady state, reconfiguration, recovery, shutdown, restart, lease transfer |
| Runtime | Supported JDK/OS/architecture/TLS provider/dependency combinations selected from the actual support policy |
| Feature state | Enabled, disabled, unset/default, capability detected/not detected, unsupported account/version |

### 8.2 Interaction strategy

Full Cartesian coverage is usually infeasible and includes invalid combinations.
Use:

1. Exhaustive small decision tables for critical algorithms and status branches.
2. Constraint-aware pairwise coverage for broad configuration combinations.
3. Explicit higher-order combinations for critical behavior; pairwise is not
   sufficient for failures involving three or more interacting states.
4. Stateful/property-based sequence generation and targeted concurrency
   schedules, with minimized failing traces retained as regressions.
5. Live validation of the simulation's service assumptions.

A covered pair does not imply that every sequence involving that pair is safe.
Report pairwise and higher-order sequence coverage separately.

Source/API/changelog reconciliation must preserve configuration combinations
that change behavior, not collapse them into one feature checkbox. For example,
"query supported" is not closure for query shape x partition scope x serializer
x continuation x consistency x failure mode. Enumerate constrained obligations
at a useful atomic granularity and retain higher-order interactions explicitly.

### 8.3 Mandatory seed scenarios

| ID | Scenario and principal proof obligation |
|---|---|
| SC-01 | 429 -> backoff -> success near a deadline; correct attempts, delay, final result and diagnostics |
| SC-02 | 429 -> 410 -> metadata refresh -> 503 -> alternate region; nested retries share the appropriate budgets |
| SC-03 | Write sent, server commits, response lost; default and opt-in replay contracts remain distinct |
| SC-04 | Cancel during backoff, connection acquisition, partial response, and concurrent completion; bounded cleanup |
| SC-05 | Cold client plus unavailable account/container/address metadata; no deadlock or unbounded warmup |
| SC-06 | Split during query/page resume with stale range map; complete fixed-dataset results for supported query shapes |
| SC-07 | Merge during change-feed resume from timestamp/continuation; allowed replay, range mapping and RU overhead visible |
| SC-08 | Container deleted/recreated under same name during requests; no stale RID/session state contamination |
| SC-09 | Region becomes read-only or unavailable mid-write; eligible rerouting, write-safety contract, explicit failure if none |
| SC-10 | All configured/preferred regions excluded or unavailable; bounded failure and recoverable health state |
| SC-11 | Concurrent cache refresh with out-of-order responses; stale metadata cannot overwrite newer accepted state |
| SC-12 | HTTP/2 PING closure, stream reset, or GOAWAY under load; local versus region health attribution and cleanup |
| SC-13 | Hedged read plus slow losing response, cancellation and session token; one logical outcome without state corruption |
| SC-14 | Circuit opens for one partition while others stay healthy; isolation, probes, cooldown and recovery |
| SC-15 | Bulk mixed success, timeout and missing response; per-input correlation, no diagnostics NPE or false success |
| SC-16 | Patch increment with lost response; no undocumented replay; 412 predicate failure remains distinct |
| SC-17 | Batch mixed operations with an ETag failure; atomicity and complete per-operation error representation |
| SC-18 | Query with empty intermediate pages, throttling, continuation, and resubscription; no accidental truncation |
| SC-19 | Hybrid query components arrive in different orders on repeated subscriptions; scores and result alignment remain valid |
| SC-20 | Custom serializer with query parameters, projections, read-many and patch; correct serializer boundaries |
| SC-21 | Change-feed callback fails before checkpoint, worker restarts or lease moves; allowed replay without data loss |
| SC-22 | Credential refresh/key rotation during concurrency and region failover; bounded refresh and no credential leakage |
| SC-23 | Client closes during active bulk/query/feed operations; explicit outcomes and resource ownership respected |
| SC-24 | Diagnostics callback throws, telemetry saturates or repeats subscription; database outcome and trace lifecycle remain correct |
| SC-25 | Hot logical partition while others are idle; correct 429 handling and no assumption of uniform workload capacity |
| SC-26 | Corrupt/truncated/oversized wire response or continuation; explicit error and bounded parsing/resource use |
| SC-27 | Supported dependency/JDK transition; binary compatibility, module access, TLS and consumer behavior preserved |
| SC-28 | New service substatus or capability mismatch; safe unknown handling without fictitious successful fallback |

Each scenario needs precise prerequisites and an oracle before execution.
Topology and feature combinations unsupported by the service are `unsupported`,
not skipped successes.

### 8.4 General database semantics to make explicit

These are not all promises of Cosmos DB; they are questions whose applicable
guarantees and non-guarantees must be encoded correctly:

| ID | Scenario family | Required distinctions |
|---|---|---|
| DB-01 | Concurrent writers and lost updates | ETag-protected writes versus unconditional last-writer behavior; retries must not remove concurrency conditions |
| DB-02 | Isolation and transaction boundaries | Single logical-partition transaction versus independent bulk/cross-partition operations; no invented cross-partition atomicity |
| DB-03 | Identity and uniqueness | Item ID plus logical partition scope, configured unique keys, duplicate create, delete/recreate and concurrent create-if-not-exists |
| DB-04 | Data representation | Null versus missing, number precision/ranges, Unicode/escaping, dates and custom serializers; no silent value corruption |
| DB-05 | Query determinism | Required ordering and ties, result multisets, projections, aggregate edge cases and empty sets; unordered results are not tested as a fixed order |
| DB-06 | Concurrent mutation during enumeration | Allowed visibility and continuation behavior; absence of snapshot isolation is not mistaken for an SDK enumeration bug |
| DB-07 | Expiration and retention | TTL visibility/cleanup and change-feed retention are service-defined; no exact client-clock deletion deadline is invented |
| DB-08 | Index and schema evolution | Changed policies, unknown model fields, capability availability and service transformation progress; no undocumented immediate-readiness promise |
| DB-09 | Failure after possible commit | Returned failure versus actual persisted state; distinguish confirmed rejection, unknown outcome and safe caller reconciliation |
| DB-10 | Durability and consistency claims | Verify the SDK preserves selected contracts and returns correct evidence; service durability is not proven by a unit test |
| DB-11 | Authorization changes mid-workflow | Revoked/rotated credentials, lease-resource permissions and partial pagination; preserve access boundaries and explicit failure |
| DB-12 | Multi-tenant isolation | Concurrent clients/accounts/containers with similar names or IDs; no credential, cache, token, diagnostics or request-state crossover |

## 9. Coverage dimensions and improvement policy

### 9.1 Score vector, not one blended score

Track a vector per SDK, package/domain, and relevant changed scope. Never allow
improved getter coverage to compensate for a retry or consistency regression.

| Dimension | Definition | Required interpretation |
|---|---|---|
| Executable lines | Executed production lines / all reportable production executable lines | Include never-loaded classes; show per-suite and aggregate results |
| Branch outcomes | Executed instrumented branch outcomes / reportable outcomes | Compiler/tool limitations and exclusions are visible; not equivalent to MC/DC or path coverage |
| Mutation detection | Killed eligible mutants / all eligible mutants in the comparable cohort | Show survived, no-coverage, timeout, invalid and unresolved separately |
| Invariant evidence | Applicable invariant obligations with passing required evidence / all applicable obligations | A linked test name alone is not coverage; show critical obligations separately |
| Status decision coverage | Verified, passing decision cells / required valid cells | Cells include operation/mode/origin and other applicability, not just status labels |
| Scenario/interaction coverage | Passing required scenario cells and valid interactions / declared required cells/interactions | Report individual axes, pairs and critical sequences separately |
| Historical regression detection | Reproduced eligible benchmark faults detected by the candidate suite / eligible faults in the frozen cohort | Separate reproducibility/admission coverage from detection; unported cases cannot disappear |
| Compatibility | Applicable API/binary/wire/token/runtime checks with valid passing evidence | A hard constraint, not an average that tolerates a broken API |
| Operational quality | Reliability, flake rate, resource/leak outcomes and calibrated performance budgets | Lower-is-better metrics use explicit budgets, not the "all scores increase" wording |

Optional presentation scores must not become merge authority. Keep numerators,
denominators, applicability, cohort revisions, and raw evidence visible.

### 9.2 Proposed no-regression and improvement rule

R-03 needs an explicit resolution because strict increases in every dimension
are mathematically impossible once a dimension reaches 100%, and some PRs do
not touch executable behavior.

**Recommendation for D-02, not yet an approved relaxation of R-03:**

1. No applicable dimension regresses on comparable existing obligations at
   repository, affected-domain and critical-invariant scopes.
2. New/changed behavior supplies complete required evidence; proposed default:
   100% of changed executable lines and all feasible critical changed branch
   outcomes, with narrowly reviewed exceptions.
3. Behavior-changing PRs improve at least one unsaturated coverage dimension or
   add independently verified new obligations/evidence while preserving all
   existing gates.
4. Saturated, not-applicable, documentation-only and behavior-neutral cases have
   explicit classifications. Equality is never silently treated as improvement.
5. No weighted aggregate, numeric rounding, test count, or agent confidence can
   override an individual critical gate.

If the intended rule is stricter, settle it before enforcement. Keep the
confirmed aspiration and the chosen operational policy separately recorded.

### 9.3 Comparable cohorts and denominator changes

For each comparison record base SHA, merge-candidate SHA, policy/catalog
revision, tool versions, class/source digests, configuration and environment.

Maintain both:

- A frozen prior-obligation comparison, so existing guarantees cannot disappear.
- The honest full candidate score, including newly discovered/newly introduced
  obligations and all current production code.

Split changes into retained, added, modified, retired and newly discovered
obligations. A catalog expansion may lower the honest full score even without
a code regression. Report the drop and classify it as newly exposed debt; do
not hide it by freezing the public dashboard denominator.

The decision to allow such a discovery-only PR without immediate remediation is
D-02. It must not grant autonomy to the newly unproven behavior. New product
behavior with incomplete obligations remains blocked.

Legitimate code deletion/refactoring also changes denominators. Compare retained
contracts and stable cohorts, require evidence that removed branches/obligations
are truly obsolete, and show both absolute gaps and ratios. No automatic
exemption permits deletion of an inconvenient test.

### 9.4 Mutation accounting

Use a pinned mutator/operator set and deterministic cohort selection. Evaluate
PIT against representative domains across the whole-SDK pilot, including
multi-module classpaths and the current Java/TestNG stack, before committing
to repository-wide tooling. A feasibility spike in one domain does not define
the feature scope of the pilot.

Record:

- `K`: valid mutants killed by the expected behavioral assertion.
- `S`: survived mutants.
- `U`: mutants with no relevant test execution.
- `T`: timeout or otherwise inconclusive executions.
- `X`: invalid/nonviable mutants with independently auditable reason.
- `E`: approved equivalent mutants, with evidence and expiry/revisit policy.

For a complete comparable cohort, the custom scored denominator is
`K + S + U + T`, after explicitly approved `X` and `E` exclusions. An unresolved
timeout is not counted as killed. Also publish raw counts before exclusions.
Unexecuted planned cohort entries make the result incomplete, not implicitly
removed from the denominator.

The score is `K / (K + S + U + T)` for a nonempty completed cohort; empty is
`not_applicable`, not 100%. CI infrastructure errors invalidate the run.
This project metric must not be confused with a tool's narrower "test strength"
metric that omits uncovered mutants.

Do not let the implementing agent classify its own surviving mutants as
equivalent without independent review. Samples must state sample size,
selection, cohort digest, uncertainty and coverage limits. A sampled result is
not a full-SDK mutation score.

### 9.5 Target setting and exclusions

Long-term target: near-100% reportable executable line coverage, high branch and
mutation coverage, and complete critical invariant/status/scenario obligations.
Exact per-domain thresholds, timing envelopes and staged ratchets are D-03.

Do not jump from an unmeasured baseline to an invented universal 99% or 95%
threshold. Set attainable milestones after baseline measurement; once a
threshold is adopted, agents cannot lower it in an ordinary SDK PR.

Exclusions require exact classes/lines/obligations, reason, evidence, owner and
expiry. Show raw production and adjusted eligible views. Generated, compiler
synthetic, vendored, deprecated, or difficult-to-reach code is not blanket
permission to exclude it. Never exclude an error path merely because the
current harness cannot reach it.

### 9.6 Evidence integrity

Passing assertions, not execution alone, establish semantic evidence.
Hardcoded expected results that merely restate the implementation are weak
oracles. Use independent mathematical/reference models, golden vectors,
metamorphic properties, verified service fixtures, and regression assertions.

Safety properties also need negative controls: deliberately disable the
protection or inject a representative fault and demonstrate detection.

## 10. Test architecture and execution

### 10.1 Layers

| Layer | Reuse / extension | What it proves | Limits |
|---|---|---|---|
| Deterministic unit/property | Current TestNG/Mockito/Reactor tests; approved property runner if needed | Decision tables, bounds, state transitions, token/range algebra | Mocked collaborators can encode the same wrong assumption |
| Stateful client/transport harness | Current fault injection and TCP/HTTP test infrastructure where suitable | Real SDK composition across scripted faults, caches, time and scheduling | Must validate service/protocol fidelity and unsupported injections |
| Emulator integration | Existing emulator jobs/suites | Real wire serialization, request pipeline and supported database behavior | Not a substitute for multi-region and all preview capabilities |
| Live service | Existing account/matrix infrastructure | Real topology/capability/consistency assumptions | Expensive, nondeterministic, credentialed and service-version dependent |
| Concurrency/stress/soak | Existing leak detection/benchmarks plus targeted tools | Race schedules, bounded resource behavior, long-lived recovery | A finite stress run is not proof of all interleavings |
| Compatibility/performance | Current API/build checks and consumer/benchmark fixtures | Artifact/API/runtime compatibility and resource budgets | Requires controlled comparable environments |

### 10.2 Deterministic harness design

Prefer narrow seams in existing internal abstractions over a rewrite or a new
public API. Candidate controllable inputs are clock, scheduler, random source,
transport outcome, account/range/address snapshots, and completion ordering.

The harness should:

- Execute production retry/routing/session code rather than mock the very
  algorithm being tested.
- Script request-phase-specific outcomes, including "committed but response
  lost" and stale/partial metadata.
- Capture independent request observations: endpoint, operation, headers,
  attempt times, routing refreshes, completion and released resources.
- Replay a seed and controlled schedule and minimize failing sequences.
- Use virtual time only where the actual code is wired to that clock/scheduler.
  Advancing a Reactor scheduler does not automatically advance Netty, native
  timers, or system time.
- Include real scheduler/event-loop and transport tests to catch behavior that
  virtual time cannot model.
- Declare which protocol and metadata faults it cannot represent.
- Periodically compare scripted expectations against service/emulator traces
  and approved contracts.

Fault injection must distinguish the injection taking effect from the expected
recovery outcome. A green test whose injection never fired is invalid evidence.

### 10.3 Coverage collection across modules and jobs

The first implementation spike must establish a canonical effective Maven
lifecycle for each suite, including inherited Failsafe executions, forks,
profiles, JaCoCo agent attachment and existing JVM arguments.

Requirements:

1. Instrument/test the intended candidate production classes, not an older
   installed `azure-cosmos` JAR pulled from a local cache or repository.
2. Collect execution data from all relevant forked JVMs and shard processes.
3. Preserve existing JVM module/leak-detection settings when adding agent args.
4. Produce reports using the exact matching class files/source revision.
5. Include every in-scope production class, including classes never loaded.
6. Union compatible executions within a candidate revision; never average
   per-job percentages and never merge incompatible bytecode.
7. Distinguish per-configuration evidence from the union. One mode executing a
   line does not prove the same behavior in another mode.
8. Publish missing/empty/truncated execution files, discovery discrepancies and
   source/class mismatch as failed evidence.
9. Separately report instrumented coverage runs and uninstrumented performance
   runs; instrumentation overhead is not a product performance regression.
10. Verify the normal packaged artifact is the same intended candidate apart
    from declared instrumentation; coverage must not accidentally validate only
    a test-only source variant.

### 10.4 Test discovery and assertions

Every required logical test and parameter row needs a stable ID and expected
discovery result. Validate zero-tests-passed, empty data providers, wrong groups,
disabled tests, skipped setup, suite XML drift, swallowed async failures and
test-worker crashes.

Use meaningful observable assertions. Interaction verification is useful for
requests/attempts, but cannot replace result, consistency, safety and resource
assertions. Add contract-level tests even for trivial code where the public
mapping matters; avoid thousands of redundant getter tests just to raise a
score.

Order-dependent tests must be repaired or explicitly isolated with explained
ordering. Random order/seeded schedule runs supplement, not replace, stable
reproduction.

### 10.5 PR scheduling and cost

Proposed execution tiers:

| Tier | Runs | Purpose |
|---|---|---|
| A | Every relevant PR/candidate | Inventory/policy validation, build/API checks, mandatory sentinel invariants, impacted deterministic tests, changed coverage |
| B | Every behavior-changing candidate in qualified scope | Relevant emulator/integration suites, fixed mutation cohort, affected status/scenario and historical regressions |
| C | Required when impacted by the change | Live multi-region/topology/network/capability, stress and performance suites |
| D | Scheduled full assessment | Broad matrices, expanded mutations/fuzzing, historical corpus growth, simulator validation, flakiness/coverage discovery |

Tier D cannot substitute for a required candidate-specific Tier C result.
Test-selection changes are protected policy. Unmapped changes, uncertain
dependencies, shared infrastructure changes, or failed impact analysis trigger
broader testing or block autonomy; never silently select fewer tests.

Use runtime coverage and verified static dependencies as aids, with a permanent
sentinel suite independent of selection. Periodically run the full relevant
suite to detect selection misses.

Allocate budgets for wall time, parallelism, live RU/resource use, mutation
count and agent iterations. Budget exhaustion yields `blocked`, not a smaller
undeclared evidence requirement. Numeric budgets are D-03/D-10.

For fixed/shared live accounts, namespace every run's resources and track exact
ownership. Fault rules, generated data, leases and cleanup must not interfere
with another run or delete pre-existing resources. Resolve cleanup on failure
and cancellation as well as success; a missing cleanup receipt is operational
debt, not permission for broad deletion. Shared-account tests require capacity
coordination and bounded fault scope before they can be used unattended.

### 10.6 Flakiness and performance

Record the first outcome and all retries. Passing after retry is not equivalent
to a clean pass. Separate demonstrated infrastructure failure from product
failure using explicit diagnostics and a bounded retry policy.

Quarantine creates visible test debt and removes autonomy for obligations that
lose their only reliable evidence. Quarantine is not deletion from the score.

Measure latency distributions, throughput, allocations, heap/off-heap growth,
open channels, pending tasks, thread counts, and cleanup time where relevant.
Compare uninstrumented base/candidate artifacts under the same environment,
warmup, workload and repeated-sample protocol. Record service-side variability
and uncertainty; no noisy single run or self-reported agent estimate is a gate.

## 11. Historical bug benchmark

### 11.1 Source and coverage

Use public GitHub issues as the primary starting corpus:

[Java SDK issues](https://github.com/Azure/azure-sdk-for-java/issues).

Issues are not guaranteed to contain all bugs, complete reproducers, or correct
root causes. Include linked PR regression tests and relevant changelog entries.
Later, authorized sanitized incident/support findings can augment the corpus,
but private customer material must not be copied into a public benchmark.

Because this is a monorepo, label selection alone is insufficient. Scope by
package, stack traces, affected versions, linked fixes and issue content, then
classify connector/feature/support/service-only reports separately.

### 11.2 Benchmark record and admission

Each case needs:

- Canonical issue URL and any duplicate/related issue relationships.
- Observed symptom, affected SDK/service/configuration and source provenance.
- Confirmed fix PR/commit and an affected revision; closed is not synonymous
  with fixed.
- Minimal sanitized reproducer and an assertion tied to an invariant.
- Red evidence on the affected baseline and green evidence on the corrected
  candidate under a compatible fixture.
- Explanation of how historical tests were ported and whether porting changed
  the scenario.
- Cases such as "known-bad behavior returns a wrong value" rather than a failure
  caused by missing dependencies, compilation or unavailable service features.
- Neighboring boundary/mode/operation cases and mutation/negative controls.
- Corpus status, cost/runtime, requirements, license/provenance notes and
  detection versus reproduction classification.

Use states:

`candidate -> triaged -> reproduction-ready -> red-confirmed -> fix-confirmed -> benchmark-admitted`

Additional states include duplicate, not-a-core-bug, unsupported historical
environment, nonreproducible, needs-service-fixture and needs-contract-decision.
Keep all counts. A difficult case is not silently removed from inventory.

### 11.3 Representative seed candidates, not verified benchmarks

| Issue | Why it is a useful candidate | Current state |
|---|---|---|
| [Azure/azure-sdk-for-java#50148](https://github.com/Azure/azure-sdk-for-java/issues/50148) | Reported null bulk response dereferenced while obtaining diagnostics; combines transport failure, per-item outcome and observability | Candidate; closure/fix and reproduction not verified |
| [Azure/azure-sdk-for-java#49823](https://github.com/Azure/azure-sdk-for-java/issues/49823) | Reported hybrid-query RRF indexing failure associated with repeated subscriptions and cross-partition ordering | Candidate; reported cause requires verification |
| [Azure/azure-sdk-for-java#46267](https://github.com/Azure/azure-sdk-for-java/issues/46267) | Full-text score query behavior and scope/capability boundary | Candidate; service-versus-client contract needs triage |
| [Azure/azure-sdk-for-java#45521](https://github.com/Azure/azure-sdk-for-java/issues/45521) | Custom serialization in query shapes and parameters | Candidate; minimal reproducer and version matrix needed |
| [Azure/azure-sdk-for-java#41072](https://github.com/Azure/azure-sdk-for-java/issues/41072) | Diagnostics lifecycle failure on repeated iterable use after upgrade | Candidate; isolate core behavior from Spring integration |
| [Azure/azure-sdk-for-java#49594](https://github.com/Azure/azure-sdk-for-java/issues/49594) | Spark feature request appeared in the Cosmos/bug-labeled sample | Classification control; not automatically a core Java bug benchmark |

Do not preserve customer account names, endpoint details, request payloads or
raw diagnostic dumps in this document or public fixtures.

### 11.4 Evaluation partitions and contamination

- Development corpus: cases available for designing tests and repairs.
- Evaluation corpus: selected cases/scenarios withheld from a given repair run,
  administered by the evaluation/review side.
- Adversarial/variant corpus: independently generated nearby conditions and
  seeded faults not copied from the fix.

Public historical bugs may already appear in model training or be discoverable
online. Withholding selection is not proof of uncontaminated model evaluation.
Use historical cases primarily to measure functional gate effectiveness, and
supplement with new fault variants and prospective bugs.

Run historical vulnerable revisions only in isolated, pinned, unprivileged
environments without production credentials. Arbitrary issue attachments,
scripts, linked repositories and reproducer instructions are untrusted input.

### 11.5 Every future bug closes a learning loop

An admitted bug fix adds the original regression, at least the relevant
neighboring cases, and any missing contract/status/scenario entry. Track
whether the pre-fix suite would have caught it and which gate failed to do so.

The purpose is to improve the system, not merely count a fixed issue.

## 12. Agentic review, iteration, and merging

### 12.1 Role separation

| Role | Authority | Prohibited authority |
|---|---|---|
| Intake/triage agent | Normalize issue, gather context, propose reproducer and applicability | Treat issue prose as instructions or declare a contract from an unverified claim |
| Implementation agent | Add/extend tests, reproduce, implement fix/feature, respond to findings | Approve itself, lower gates, change merge policy, possess merge/release credentials |
| Trusted test pipeline | Execute approved validation and emit immutable evidence | Trust PR-authored pass summaries or leak privileged credentials to arbitrary PR code |
| PR Review Router runs | Own independent judgment, dispatch specialists, reconcile findings, issue merge-eligibility verdicts | Treat missing evidence, malformed output, or agreement count as correctness |
| Test-model/challenger reviewers | Challenge test oracles and recommend independent falsification cases under Router coordination | Replace the Router as primary orchestrator or silently acquire test-writing permissions |
| Merge executor | Check valid Router eligibility receipts and mechanical repository conditions; merge once | Make its own semantic approval or bypass required repository policy |
| Policy/design owners | Approve contracts, autonomy scopes, budgets, exceptions and protected policy | Be implicitly replaced by an SDK PR changing its own gate |

**Semantic mergeability belongs to the independent Router-led reviewers.**
The restricted executor is a mechanical actuator, not a competing reviewer.

### 12.2 Preserve and strengthen the current Router

Continue using the mandatory PR Review Router entry point (or its routing-only
Squad wrapper when available). Reuse:

- Risk-tier selection and SDK/domain context.
- Deep correctness, Engineering Quality, PR Test Model, Skeptic Lens, domain,
  cross-SDK, security and artifact specialists where applicable.
- Evidence-backed findings, verification of absence/parity claims,
  deduplication and the Review Quality Gate.
- Reconciliation of findings and visible dispositions.

Do not describe today's Router as already supporting autonomy. Its current
human approval/posting boundary remains in force until a separate reviewed
integration policy changes it. Proposed differences for autonomous mode:

| Current behavior or limitation | Proposed autonomous contract |
|---|---|
| Some partial reviewer/context failures can still yield a report | Any missing required reviewer/evidence yields `blocked` eligibility |
| Prose parsing and best-effort normalization are tolerated | Invalid or incomplete required machine receipts cannot approve |
| Low-risk test-only changes may receive Triage | Changes to tests, exclusions, or selection that govern autonomy receive protected-policy/test-integrity scrutiny |
| Current Java peer defaults are .NET/Python and the peer map caps fanout | Produce the required full compatibility matrix; design explicit bounded batches rather than silently omit Go/Rust |
| Local prompts/memory are mutable context | Pin prompt/policy/model/tool/catalog provenance for each decision; memory cannot override protected contracts |
| Human approval governs posting | Specify independently approved boundaries for unattended comments, repair, verdicts and merge execution |

No agent definitions or review settings are changed by this draft.

The existing PR Test Model Reviewer remains read-only. If executable independent
challenge tests are required, use a separately authorized, isolated test-authoring
step under Router coordination and trusted execution. Do not silently turn a
read-only reviewer into a code-writing agent.

### 12.3 Independence and sufficient review

Proposed minimum for an autonomously mergeable behavior change:

1. A Router-led review covering correctness, domain invariants, test quality and
   affected compatibility/operational risks.
2. A separate fresh Router-led final-candidate review run, with its own initial
   judgment before reading the other run's conclusions.
3. Independent verification/challenge of the important new tests or reproducers,
   rather than trusting only the implementation agent's test plan.
4. Reconciliation of all required findings, followed by final eligibility
   receipts bound to the same candidate and evidence.

Specialists remain Router-dispatched. Separate runs/contexts reduce anchoring;
different models may be useful but do not make errors independent or produce
mathematically meaningful approval probabilities. Model selection is a later
policy decision, not prescribed here.

The exact number of mandatory runs and risk-tier requirements are D-07.
Do not require performative back-and-forth when a PR is already sound. When
findings exist, iteration continues until the evidence and required
dispositions are complete or the run blocks.

### 12.4 Candidate state machine

```text
intake
  -> contract-and-impact-mapped
  -> reproduction-or-feature-acceptance-ready
  -> implementation-ready
  -> candidate-tested
  -> independent-review
       -> changes-required -> repair -> new-candidate-tested -> independent-review
       -> blocked / needs-contract-decision / rejected
       -> eligibility-approved
  -> merge-candidate-revalidated
  -> mechanically-authorized
  -> merged
```

For a bug, require an assertion failure on the affected revision and pass on
the candidate. For a feature, require approved behavior/acceptance obligations
and evidence that negative controls detect a missing/broken implementation.
For a behavior-neutral refactor, preserve contracts and compare both versions.

### 12.5 Findings and iteration protocol

Each finding has stable ID, category/severity, candidate SHA, evidence,
invariant/scenario links, requested action and disposition.

Allowed dispositions:

- Fixed, with commit and regression/evidence links.
- Refuted, with evidence and independent reviewer acceptance.
- Intentional contract change, requiring the protected design/policy path.
- Deferred only if policy declares it nonblocking and no required evidence is
  lost; blocking safety findings cannot be deferred into autonomous approval.

The implementing agent cannot close its own blocker. Majority vote does not
erase a supported blocker; disagreement triggers a targeted experiment or
explicit contract decision. No reviewer can silently downgrade a substantive
correctness finding just because another reviewer disagrees.

Retries/repair rounds are bounded by elapsed time, cost and iteration limits.
Oscillating fixes, repeated inability to reproduce, contradictory contracts,
or unresolved blockers end in a clear blocked state.

### 12.6 Cross-SDK compatibility matrix

For changed behavior, include Java, .NET, Python, Go and Rust at minimum, with
JavaScript/TypeScript and connector consumers when relevant to the contract.
Do not infer parity from similar class names.

Each cell records:

- Supported equivalent behavior, intentional difference, unsupported feature,
  verified gap, or unverified.
- Source file/symbol and commit/version.
- Configuration/default/retry differences.
- Relevant tests or contract evidence.
- Whether a difference affects this PR's eligibility.

Unknown is not unsupported. Intentional language/runtime or feature differences
are not automatically bugs. Required unresolved parity questions block autonomy
for affected semantics. Expansion beyond the current Router peer cap must be an
explicit integration change.

### 12.7 Evidence bundle and verdict

An evidence bundle needs:

```text
identity:
  repository, PR, base SHA, head SHA, merge-candidate SHA/tree, creation time
policy:
  invariant/scenario/catalog versions, thresholds, exceptions, autonomy scope
execution:
  build/class/artifact digests, environment, tool/runner versions, suite/shard IDs
completeness:
  expected/discovered/executed/passed/failed/skipped tests and parameter cases
  required/missing/expired/inconclusive checks and infrastructure failures
behavior:
  impacted and unmapped features/invariants/status cells/scenarios
quality:
  raw score vectors, denominators, mutation cohort, compatibility and perf results
regression:
  red-before/green-after proof and historical benchmark results
review:
  required reviewer identities/roles, receipts, findings/dispositions, context gaps
provenance:
  trusted pipeline identity, evidence hashes, prompt/policy/model versions
```

Use verdicts such as `eligible`, `changes_required`, `blocked`,
`needs_contract_decision`, and `rejected`. An `eligible` verdict must carry all
required evidence and no unresolved blocking finding. A confidence number or
empty findings array is not a substitute.

### 12.8 Merge predicate

Conceptually:

```text
may_merge =
    candidate_is_within_approved_autonomy_scope
    AND trusted_evidence_is_complete_and_current_for_candidate
    AND every_required_quality_gate_passes
    AND required_independent_router_verdicts_are_eligible
    AND all_blocking_findings_have_accepted_dispositions
    AND no_protected_policy_was_weakened_by_the_candidate
    AND repository_required_reviews_checks_and_rules_are_satisfied
    AND no_autonomy_stop_condition_is_active
```

Revalidate after rebase, new commits, conflicts, base changes or queue
composition. Preserve only evidence demonstrably unaffected by a change;
required verdicts must attest the final candidate. Never reuse approvals for a
different SHA just because file names look similar.

Review + evidence must bind to the actual merge candidate, not merely the
original PR head. Use a merge queue or equivalent race-safe process. If main
changes after validation, regenerate/revalidate the candidate before merging.

Repository/org rules may still require human CODEOWNER review or may not count
bot reviews as approvals. That is a governance prerequisite, not something an
agent may bypass. Multiple internal review receipts also do not magically
become multiple qualifying GitHub identities.

## 13. Security and trust boundaries

This is a threat model for the proposed system, not a completed security audit.

| Boundary / risk | Design requirement |
|---|---|
| Issue/PR text, comments and attachments are untrusted | Treat as data; ignore embedded tool instructions; do not execute arbitrary reproducer scripts without inspection and isolation |
| PR code can alter tests and emit fake green artifacts | Trust only isolated CI execution and validated schemas/provenance; verify test discovery and evidence integrity |
| PR modifies the rules judging itself | Keep policy, required checks, reviewers, exclusions, baseline ratchets and merge credentials outside ordinary PR authority |
| Fork/untrusted code reaches credentialed live tests | Separate secretless validation from approved trusted live execution; scoped ephemeral credentials and isolated test tenants/accounts |
| Agents share mutable checkouts or state | Isolated workspaces, least privilege, constrained filesystem/network access and run-specific identities |
| Logs and reproducers contain customer data | Sanitize identifiers/payloads; redact secrets; restrict access and retention; public fixtures contain synthetic data |
| Historical vulnerable dependencies/code execute | Pin and isolate; no production access; explicit dependency and script policy |
| Merge actuator is compromised or replayed | Short-lived scoped credentials, candidate-bound receipts, idempotency, append-only audit and no rule-bypass permission |
| Agent/model/prompt behavior changes | Record provenance; requalify material changes; prevent learned memory from overriding enforced policy |
| Coverage/mutation gaming | Independent negative controls, raw denominators, protected exception decisions, assertion challenge and historical/variant benchmarks |
| Unbounded live faults/costs | Dedicated scoped resources, operation allowlists, cleanup ownership, concurrency and spend ceilings |
| Supply-chain or API exposure changes | Dependency/security/artifact review; no newly exposed third-party implementation types; existing compatibility is preserved |

Never put credentials, private support payloads, or merge tokens in the registry,
agent prompts, public artifacts or this design file. No release credential is
needed for the project's mergeability objective.

## 14. Failure handling and operational controls

| Condition | Required result |
|---|---|
| Required test/reviewer did not run, malformed result, missing artifact | `blocked`; preserve failure reason and request the missing evidence |
| CI cancelled, timed out, or lost a shard | Incomplete, not passed; bounded rerun policy |
| Live fixture unavailable or service behavior cannot be established | Required live obligation remains unproven; do not substitute a mock automatically |
| Test passes after retry | Record original failure; classify/triage under explicit flake policy |
| Simulation disagrees with live contract | Block affected invariants and autonomy; preserve traces and resolve oracle |
| Base/candidate/policy/catalog changes | Invalidate affected evidence and receipts; recompute required checks |
| Evidence collector/score computation fails | Fail closed; do not fall back to agent prose |
| Repair loop exceeds budget or oscillates | Stop with reproducible blocker and remaining questions |
| Merge request response is ambiguous | Reconcile actual repository state before retrying; no duplicate/conflicting merge actions |
| Post-merge CI finds a product regression | Pause the affected autonomy scope, open regression work, restore branch health through governed PR/revert policy |
| Evidence of gate manipulation or credential leak | Stop autonomy; contain access; preserve audit; incident handling |
| Broad CI/service outage | Pause admission/merges rather than repeatedly consuming budgets |

### 14.1 Observability

Track:

- Time to reproduce, fix, review, reconcile and merge.
- Coverage vectors, absolute uncovered obligations, inventory drift and
  exception/quarantine age.
- Required-check completeness, false-green test discovery, selection misses.
- First-run failure and retry/flake rates.
- Reviewer disagreements, unsupported findings, repair oscillation and
  precision of findings.
- Historical and seeded fault detection, prospective escaped regressions.
- CI/agent/live-resource cost and cleanup failures.
- Autonomous decisions by scope/policy revision and reasons for blocking.

An audit record must reconstruct why a PR was or was not merged. Evidence
retention, artifact access and storage cost are D-10.

### 14.2 Stops and recovery

Provide a global kill switch and per-domain/autonomy-scope stops. Neither is
controlled by the implementation agent.

Recovery requires repair of the escaped invariant/test/gate defect, renewed
evidence, and explicit requalification. A source revert alone does not establish
that the autonomous system is trustworthy again.

Automated revert behavior itself is a later policy decision: a revert may break
dependent changes and must not be performed blindly. Release rollback is outside
this design.

## 15. Evaluation and autonomy graduation

### 15.1 Distinct questions to measure

1. Did tests execute the intended implementation?
2. Would the assertions detect the relevant wrong behavior?
3. Did the catalog include the behavior and interactions at all?
4. Would the review/merge system block the faulty candidate?
5. Does this generalize to prospective changes rather than memorized bugs?

Use deliberately seeded faults in retry conditions, budget accounting, token
merging, endpoint selection, serialization, bulk null handling and cleanup.
Include a "pipeline lies" test: skipped suites, stale evidence, malformed
review receipts, policy weakening and mismatched SHAs must all block merging.

### 15.2 Graduation stages

| Stage | Mode | Exit evidence |
|---|---|---|
| G-0 | Design only | All blocking design decisions settled; catalogs and interfaces specified; implementation authorized separately |
| G-1 | Whole-SDK baseline and pilot, no autonomous merges | All-domain inventory and measured baseline; reproducible domain contracts, reliable gates and independent negative controls; gaps visible per domain |
| G-2 | Whole-SDK shadow decisions | Experiments may involve any domain or cross-domain PR; humans keep current approval; measure findings, misses, evidence gaps, cost and reliability by domain |
| G-3 | Narrow autonomous scope | Approved risk class/path scope, demonstrated fault detection, enforced repository policy, stops and recovery exercised |
| G-4 | Broader autonomous scope | Each new domain/change class separately qualified; no automatic inheritance from unrelated modules |

Initial excluded autonomy classes should include public contract changes,
auth/security-sensitive changes, dependency upgrades, protected CI/policy
changes and poorly modeled distributed features until qualified. These are
staging decisions, not a permanent ban.

### 15.3 Qualification criteria

Set numeric minimums after the baseline and before graduation, not retrospectively
to make a run pass. Criteria include:

- Complete critical obligations and no unresolved critical contract ambiguity.
- Required historical and independent seeded-fault detection.
- Defined sample sizes, risk mix, observation duration and uncertainty.
- Acceptable flakiness, cost, end-to-end duration and no false-green evidence.
- No unexplained blocking reviewer disagreement or autonomy bypass.
- Successful exercises of stale-evidence rejection, kill switch and recovery.
- Acceptable prospective escape rate relative to an explicitly chosen baseline.

Zero observed escapes in a small sample is not a zero failure rate. Report the
denominator and uncertainty. Human decisions in shadow mode are comparison
evidence, not infallible ground truth; investigate disagreements.

### 15.4 Whole-SDK experiment portfolio

The pilot portfolio must be stratified across all feature domains, not filled
with whichever retry bugs are easiest to reproduce. Record a domain/change-type
matrix containing:

| Experiment class | Required learning |
|---|---|
| Historical bug fix | Would existing gates detect the old failure, and do new tests cover neighboring cases? |
| New feature / option | Does the catalog discover new obligations, defaults, unsupported combinations and required service capabilities? |
| Behavior-neutral refactor | Do contracts and comparable evidence remain stable despite moved/deleted implementation lines? |
| Cross-domain change | Are the transitive contracts selected, such as serialization + query or routing + session + transport? |
| Runtime/dependency change | Are scheduling, TLS, encoding, API/artifact and performance consequences modeled beyond source-line coverage? |
| Test-only / gate change | Can weakened assertions, exclusions, missing discovery or selection changes be detected and routed to protected governance? |
| New/unknown status or capability | Does the system expose missing contracts and block unsupported approval rather than invent a successful fallback? |

Use the full-domain completeness matrix to expose empty cells. A lane with no
experiments or only shallow happy-path evidence is visibly unqualified even if
the SDK-wide aggregate looks healthy. Exact sample sizes remain D-11; selecting
experiments across every domain is already a scope requirement.

Shadow experimentation can begin after design approval and a trustworthy
baseline/receipt path exist; it does not wait for near-100% coverage or every
fixture to be implemented. An early experiment can validly conclude
`blocked: missing invariant/fixture/evidence`. Feed that gap into the appropriate
domain backlog and repeat the experiment after remediation. Such a result is
useful learning, not an eligible merge and not permission to weaken the gate.

Separate two evaluation tracks:

- **Discovery/shadow:** whole-SDK PR selection from the start, recording catalog,
  fixture, score and review failures.
- **Merge qualification:** positive eligibility requires all required impacted
  evidence plus global safeguards and explicitly qualified authority.

This prevents test-implementation sequencing from recreating a retry-only
pilot or postponing experimentation until the entire project is complete.

## 16. Design decisions and unresolved questions

### 16.1 Confirmed decisions

| ID | Decision | Status |
|---|---|---|
| DEC-01 | Project name: Suicide Squad | Confirmed |
| DEC-02 | Start with Java; build on existing tests; inventory gaps first | Confirmed |
| DEC-03 | Multiple coverage dimensions and invariant-based testing | Confirmed |
| DEC-04 | Historical public-issue benchmark | Confirmed |
| DEC-05 | Independent Router-led review/iteration owns semantic mergeability | Confirmed direction; exact protocol pending |
| DEC-06 | Design completion precedes implementation | Confirmed |
| DEC-07 | Releases are separate; no release work now | Confirmed |
| DEC-08 | Initial pilot/experiments cover the full Java SDK, not a retry/deadline-only slice; full changelog and current-source reconciliation are required | Confirmed by user on 2026-10-31 |
| DEC-09 | `https://github.com/kushagraThapar/SuicideSquad` is the canonical home for all SuicideSquad project documents and files | Confirmed by user on 2026-10-31; repository configured in the app |

### 16.2 Decisions required before implementation

| ID | Question | Recommended starting position | Blocks |
|---|---|---|---|
| D-01 | Which source revision, supported branches/JDKs, and service capabilities define the baseline? | Inventory source pinned to `42702a3a...`; supported runtime/branch/capability matrix remains open | Reliable contracts and measurements |
| D-02 | What exactly does "all PRs increase scores" mean at saturation and under denominator/catalog changes? | Component-wise non-regression, complete new obligations and positive improvement where meaningful, with explicit saturated/N/A/discovery-only rules | Gate semantics |
| D-03 | What threshold-setting procedure, ratchets, performance tolerances and CI/agent budgets apply? | Approve the procedure and assessment budgets during design; derive numeric coverage/performance floors from M-1 and approve them before enforcement | Enforceable acceptance |
| D-04 | Which in-repository layout and schema format hold design/registry/evidence definitions? | Repository and documentation layout resolved in Section 19.1: `docs/suicide-squad-design.md` and `docs/research/java-sdk/`; keep shared Cosmos concepts in canonical concept docs and eventual SDK-side execution bindings close to SDK tests | Runtime registry/evidence schema and SDK integration remain open; the import manifest is not their implementation |
| D-05 | What completes the whole-SDK feature/status/scenario inventory and verifies disputed contracts? | Close full-changelog/current-API/internal-path mappings and lifecycle gaps at the pinned baseline; family-level hints and disputed semantics are not approved atomic contracts | Catalog approval |
| D-06 | How can org/repo rules permit agentic merging, and who owns protected policy? | Preserve current human gates until governance explicitly approves an unattended mode | Any autonomous merge |
| D-07 | How many independent Router runs and which roles are mandatory by risk? | Two independent Router-led judgments for behavior changes, independent test challenge, required-role completeness | Review contract |
| D-08 | How is cross-SDK matrix coverage reconciled with current Router peer limits? | Explicit bounded batches covering Java/.NET/Python/Go/Rust; verified sources and visible unknowns | Review integration |
| D-09 | Which mutation/property/concurrency tools fit current Java/TestNG/multi-module constraints? | Spike PIT and existing Reactor/test tooling; add only justified dependencies | Tool selection |
| D-10 | What are evidence retention, access, cost, cleanup and outage policies? | Immutable candidate-bound evidence with scoped access and bounded execution | Operational readiness |
| D-11 | What benchmark corpus and shadow qualification sample are sufficient? | Stratify by risk and domain; use historical plus fresh seeded/prospective cases | Autonomy graduation |
| D-12 | Who resolves intentional invariant changes, compatibility exceptions and historical behavior that is itself a bug? | Protected contract/design decision, not the implementation agent or a majority vote | Safe evolution |

These are a decision queue, not a claim that the design is finalized. Resolve
them through focused design discussions and update the decision log.
Distinguish design-policy choices from measurements: approving a measurement-only
assessment does not require inventing baseline-dependent thresholds in advance,
and does not authorize autonomous merges. Threshold values and qualification
sample sizes must be approved before their corresponding gates or graduation
steps are enabled.

## 17. Milestones and progress

### 17.1 Design-phase checklist

Status legend: `done` means the artifact exists and was inspected; `draft` means
written but not approved; `pending` means no completion evidence yet.

| ID | Deliverable | State | Acceptance evidence / next requirement |
|---|---|---|---|
| DS-00 | Named project and written design reference | done | This document, version 0.2.2; implementation still not approved |
| DS-01 | Initial source/configuration reconnaissance | done, limited | Version 0.2 pins upstream source/changelog/manifests; original local CI observations and live-check limitations remain labeled |
| DS-02 | Whole-SDK feature/behavior inventory | draft | Sections 5.3-5.4 require full changelog/API/internal-path reconciliation and explicit unmapped-entry review |
| DS-03 | Atomic invariant specifications | draft | Section 6 families; Java-specific contract verification and per-record oracles required |
| DS-04 | Status/substatus decision catalog | draft | Section 7 seed; producer/handler/mode mapping required |
| DS-05 | Scenario matrix and constraints | draft | Section 8 seed; valid-cell generation and critical sequences required |
| DS-06 | Coverage and monotonicity policy | draft | Section 9; D-02/D-03 must be settled |
| DS-07 | Test architecture and collection specification | draft | Section 10; effective lifecycle and tool compatibility remain open |
| DS-08 | Historical benchmark admission/evaluation design | draft | Section 11; corpus and qualification criteria pending |
| DS-09 | Router, repair, evidence and merge integration | draft | Section 12; current human-gate and peer-limit differences explicitly identified |
| DS-10 | Threat model, operational failure and stop policies | draft | Sections 13-14; ownership/access/budget decisions pending |
| DS-11 | Graduation/evaluation plan | draft | Section 15; numeric sample/exit criteria not selected |
| DS-12 | Design review and adversarial walkthrough | pending | Required perspectives, evidence-backed findings, accepted dispositions and residual risks |
| DS-13 | Design approval and implementation authorization | pending | D-01 through D-12 resolved or explicitly deferred without blocking scope; approval recorded |
| DS-14 | Changelog/API evidence ledger and whole-SDK domain matrix | incomplete - recovery required | Four original background agents are unavailable; no completed reports/semantic ledger were saved. See [report status](research/java-sdk/reports/README.md) and [resume checklist](research/java-sdk/recovery/README.md). |
| DS-15 | Canonical repository promotion | imported - review/integration pending | Design and safe fixed-intake inputs are repository artifacts with [provenance](research/java-sdk/import-manifest.json). Publication uses a feature-branch PR; default-branch integration and later recovery packages are not claimed. |

Required design-review perspectives: Java SDK/domain, test engineering,
distributed-system failure semantics, API/compatibility, CI/EngSys,
security/permissions, agent-review governance and operability. These are
review obligations, not a request to spawn agents now.

### 17.2 Future implementation roadmap - not started or authorized

| Milestone | Work | Prerequisites | Exit criteria |
|---|---|---|---|
| M-0 | Approve whole-SDK design and pilot protocol | DS-13 | Approved all-domain scope, owners, measurement budgets and threshold-setting procedure; no retry-only experiment boundary |
| M-1 | Measure whole-SDK baseline and make execution observable | M-0 | Per-domain discovery/lifecycle and production coverage, gap/risk dashboard, honest denominators; proposed numeric gates approved before enforcement |
| M-2 | Formalize domain contracts and deterministic/service fixtures | M-1 | Every feature domain represented; atomic invariants and stateful scenarios verified or explicitly blocked, with independent oracles |
| M-3 | Extend tests and assertion-strength checks across SDK domains | M-2 | Per-domain line/branch/mutation/invariant gates; whole-SDK sentinels and targeted negative controls detect their intended failures |
| M-4 | Admit a domain-stratified historical benchmark | M-2 | Versioned cases across feature/status/consistency/query/client domains, red/green evidence, variants and visible nonreproducible counts |
| M-5 | Wire evidence and Router whole-SDK shadow protocol | M-1 plus an approved contract/impact map and receipt schema for each experiment | Any-domain/cross-domain experiments can surface missing evidence before M-3/M-4 are complete; no positive eligibility without all required evidence; bounded repair and fail-closed exercises |
| M-6 | Evaluate shadow outcomes and qualify narrow merge scope | M-5 plus completed M-2/M-3/M-4 obligations for the proposed authority scope and required global safeguards | Approved G-3 criteria met; repository governance, stops and recovery validated; incomplete other domains remain visible, not autonomously eligible |
| M-7 | Enable approved narrow autonomous merging | M-6 | Correct race-safe merges with auditable receipts; no release action |
| M-8 | Expand merge authority by qualified change class | M-7 plus domain-specific qualification | Whole-SDK pilot scope stays unchanged; additional domains/change classes earn merge authority only when their evidence and review gates pass |

Some work inside a milestone can proceed independently; prerequisite columns
state actual dependencies, not merely list order. Whole-SDK shadow experiments
run alongside domain-by-domain test and benchmark expansion; they do not depend
on all-domain test completion.

### 17.3 Progress scorecard

| Measure | Current value |
|---|---|
| Design approval | Not approved |
| Complete baseline feature/behavior enumeration | Not measured |
| Execution-verified atomic invariants | Not measured |
| Line / branch / mutation coverage | Not measured |
| Status decision / scenario coverage | Not measured |
| Historical benchmark admitted cases | None admitted in this design exercise; existing regression inventory not yet assessed |
| Independent autonomous eligibility evaluations | Not run |
| Autonomous merges authorized by this project | None |
| Release actions | Out of scope |

Replace "not measured" only with a linked, reproducible measurement. Do not use
zero as a substitute for unknown existing coverage.

## 18. Risks and alternatives

| Risk / alternative | Assessment and response |
|---|---|
| Line-coverage-only program | Easy to report but blind to weak assertions and omitted behavior; rejected as the sole gate |
| Agents write tests matching their own broken implementation | Independent contracts/oracles, mutation/negative controls and Router-led test challenge |
| Full live-service Cartesian matrix on every PR | Too slow/costly and still incomplete; use constrained layers plus required targeted live evidence |
| All mocks, no real protocol/service validation | Fast but risks a fictitious service; retain emulator/live contract validation |
| Exhaustive global path coverage | Generally infeasible due to loops/state/interleavings; target branch/decision/contract evidence plus bounded model/scenario exploration |
| Strict numeric increase in every dimension forever | Saturation and changing denominators make it impossible; explicit D-02 decision required |
| New framework replaces existing SDK test system | High migration risk; prefer current TestNG/Failsafe/fault infrastructure and narrow seams |
| More reviewers used as a correctness probability | Correlated mistakes and anchoring; require independent evidence, falsification and explicit disagreement handling |
| Existing Router reused unchanged for unattended merges | Current human gates and degraded-mode fallbacks are not an autonomous contract; approved integration needed |
| Historical benchmark overfit or training contamination | Separate evaluation selection, fresh variants, prospective cases and transparent limitations |
| Coverage percentage hides severe uncovered domain | Per-domain/critical gates, absolute gaps, raw denominators and no cross-domain compensation |
| Broad autonomy enabled before catalog maturity | Qualify narrow scopes first and fail closed on unmapped behavior |
| Permanent manual review for all changes | Useful comparison during shadow mode, but not the target state for qualified scopes |
| Completely autonomous policy changes | Self-amending gates undermine assurance; protected governance remains separate |

## 19. Working agreement and continuation

### 19.1 Single reference and persistence

The canonical project home is
[kushagraThapar/SuicideSquad](https://github.com/kushagraThapar/SuicideSquad).
Keep the design, inventory reports, source-provenance records, decisions and
progress there going forward. This file, `docs/suicide-squad-design.md`, is the
reference for this imported revision. The prior session file is a read-only
import source, not a competing long-term authority. A session canvas should
point to this document rather than maintain another editable design copy.
Feature-branch publication does not imply default-branch integration.

The documentation layout is:

| Path | Responsibility |
|---|---|
| [Documentation index](README.md) | Entry point for the project design and research |
| `docs/suicide-squad-design.md` | Design decisions, scope and progress ledger |
| [Research index](research/java-sdk/README.md) | Input provenance, licensing, import counts and limitations |
| `docs/research/java-sdk/snapshot/` | Selected verified public upstream files, retaining upstream-relative paths |
| `docs/research/java-sdk/metadata/` | Original module/tree manifests and historical download receipt |
| [Import manifest](research/java-sdk/import-manifest.json) | Payload hashes, upstream commit/path/blob IDs, original paths, deduplication and exclusions |
| [Report status](research/java-sdk/reports/README.md) | Missing domain reports, semantic ledger and domain matrix; not completion evidence |
| [Recovery checklist](research/java-sdk/recovery/README.md) | Resume steps and the preserved, portable historical fetch helper |

This fixes the documentation-import layout, not the runtime registry/evidence
schema or SDK-side execution bindings in D-04. Root instructions and autonomous
development guidance are maintained by a separate contribution; this import
does not overwrite or duplicate them.

Use an isolated repository session for repository writes; do not write into the
primary checkout. Coordinate with the separate repository-guidelines work so
root instructions and the project design do not overwrite or duplicate each
other. Preserve existing project artifacts and any user changes.

Promote reusable Cosmos concepts into the appropriate numbered canonical
concept doc through a normal reviewed PR; keep Java-specific execution policy
and project progress in the chosen project/SDK location. Do not move
confidential investigation material into a public repository.

Versions 0.1 and 0.2 were session-only drafts. The user authorized repository
promotion on 2026-10-31. Promotion imports design/research only; it does not
authorize SDK implementation, autonomous merging or release work.

Preserve provenance and licensing for downloaded public SDK research inputs.
Classify cached source snapshots as research, not a forked SDK implementation.
Do not upload credentials, private support payloads, chat transcripts or unrelated
session files. Record any intentionally excluded temporary/generated cache and
how the underlying evidence can be recovered.

The first import is limited to the captured design and the original research
`source/` subtree. A new parent-authored `recovery/` subtree was created after
intake and is deliberately deferred until a separate completed handoff. Neither
the old unavailable agent runs nor that unfinished package count as reports.
Record later research additions in their own provenance-bearing contribution.

### 19.2 Updating progress

For each completed task record:

```text
ID:
Status:
Design revision / SDK baseline:
Evidence links (file, issue, PR, CI run, report or decision):
Acceptance criteria met:
Remaining gaps / exceptions:
Date:
```

When semantics change, revise the invariant/catalog, show affected tests and
consumers, and retain the prior contract history. A bug fix may intentionally
correct historical behavior, but it may not silently redefine the oracle.

### 19.3 Resume procedure

1. Read the header, decisions and design checklist before acting.
2. Read the canonical project repository and confirm whether the project remains
   in design-only mode.
3. Read the [input manifest](research/java-sdk/import-manifest.json),
   [incomplete report status](research/java-sdk/reports/status.json), and
   [recovery checklist](research/java-sdk/recovery/README.md). Do not wait for
   unavailable agents or relabel cached files as completed reports.
4. Reconcile the current upstream baseline before trusting old code observations;
   preserve this pinned capture rather than silently updating its snapshots.
5. Pick the next unresolved design obligation and update its evidence. Import a
   later completed recovery package separately and label its actual authorship.
6. Resolve blocking design decisions and review findings.
7. Start implementation only after DS-13 explicitly records authorization.

Recommended next design session: finish the whole-SDK changelog/API/behavior
reconciliation, resolve D-02 and the remaining support/capability part of D-01,
then verify atomic invariants across all domain lanes. Retry/deadline/status
records are one lane, not the gate for selecting initial PR experiments.

### 19.4 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-31 | Initial design-only reference; seed catalogs, quality vector, benchmark protocol, Router/merge architecture, decision queue and progress ledger |
| 0.2 | 2026-10-31 | User-directed whole-SDK pilot; pinned upstream source and full changelog; parallel feature/behavior inventories; companion encryption discovery and explicit inventory/qualification separation |
| 0.2.1 | 2026-10-31 | Canonical project repository confirmed; design/research promotion authorized; unavailable background runs and incomplete inventory explicitly recorded |
| 0.2.2 | 2026-10-31 | Portable repository import; documentation layout and relative input/report/recovery links; verified deduplicated provenance, licensing, two excluded cache mismatches and one redacted public fixture-key literal; DS-14 remains incomplete and default-branch integration remains pending |

## 20. References

### 20.1 Canonical Cosmos DB concepts

Concept snapshot for this draft:
`tvaron3/cosmosdb-design-docs@bcfbc786fa5296deebcccd11369efb583e63e48c`.
The links below are pinned to that inspected revision; refresh intentionally
and record the new revision when updating contracts.

- [Partitioning: SDK-Side Terminology and Split Semantics](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/04-partitioning.md#sdk-side-terminology)
- [Replication and Consistency: Consistency Levels](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/05-replication-consistency.md#consistency-levels--detailed-breakdown)
- [Transport: Two Connectivity Modes](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/06-transport-layer-rntbd.md#two-connectivity-modes)
- [Query Engine: ExecuteQuery](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/07-query-engine.md#executequery---the-core-entry-point)
- [RUs and Throttling: Hot Logical Partition](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/11-request-units-throttling.md#per-physical-ru-ceiling-and-the-hot-logical-partition)
- [Change Feed: Merge and StartFrom Scenarios](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/12-change-feed.md#partition-merge--startfrom-timestamp--scenarios-and-performance-concerns)
- [Session Tokens: Scope and Non-Goals; Lifecycle; Topology Changes](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/16-session-tokens.md)
- [Status Codes and SDK Retries: Overview and Status Reference](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview)

Read these as domain grounding with the qualifications in Section 4.5. Do not
adopt another SDK's numeric defaults or an explicitly unverified discussion as
a Java contract.

### 20.2 Pinned Java source/configuration references

Version 0.2 upstream inventory revision:
`Azure/azure-sdk-for-java@42702a3a1421498ee457ff9cbe56713d0877d39f`.
These links are pinned, but they do not retroactively convert version 0.1 local
observations into upstream observations. Section 3 preserves that distinction.

- [`azure-cosmos/CHANGELOG.md`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/CHANGELOG.md)
- [`azure-cosmos/pom.xml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/pom.xml)
- [`azure-cosmos-tests/pom.xml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos-tests/pom.xml)
- [`azure-cosmos-tests/README.md`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos-tests/README.md)
- [`unit-testng.xml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos-tests/src/test/resources/unit-testng.xml)
- [`HttpConstants.java`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/HttpConstants.java)
- [`FaultInjectionUnitTest.java`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos-tests/src/test/java/com/azure/cosmos/faultinjection/FaultInjectionUnitTest.java)
- [`FaultInjectionConnectionErrorRuleTests.java`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos-tests/src/test/java/com/azure/cosmos/faultinjection/FaultInjectionConnectionErrorRuleTests.java)
- [`sdk/cosmos/ci.yml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/ci.yml)
- [`cosmos-sdk-client.yml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/eng/pipelines/templates/stages/cosmos-sdk-client.yml)
- [`sdk/cosmos/tests.yml`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/tests.yml)
- [`live-platform-matrix.json`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/live-platform-matrix.json)

### 20.3 Existing review-system integration references

These are previously inspected, locally installed integration inputs, not
portable final policy. Their names are retained without machine-local paths;
their prompt files and configuration were not part of this import:

- PR Review Router agent definition: Stages 3-7, structured
  findings, partial-failure handling and human approval boundary.
- PR Test Model Reviewer agent definition: practical coverage,
  conceptual test gaps and evidence-backed recommendations.
- Review Quality Gate agent definition: evidence, severity,
  deduplication and required-versus-optional findings.
- Cross-SDK peer-map configuration: peer defaults,
  fanout cap and degraded-mode behavior.

Repository-owned, versioned interfaces for unattended use are a design
deliverable; a local prompt file is not sufficient merge authority.

### 20.4 Imported project research

- [Import scope, attribution and provenance](research/java-sdk/README.md).
- [Complete core changelog input](research/java-sdk/snapshot/sdk/cosmos/azure-cosmos/CHANGELOG.md);
  this is not the missing semantic ledger.
- [Payload/origin/hash manifest](research/java-sdk/import-manifest.json).
- [Report and ledger recovery status](research/java-sdk/reports/README.md).
- [Recovery and later-handoff checklist](research/java-sdk/recovery/README.md).
