# Suicide Squad: .NET design handoff

[Project scope](../../README.md) |
[Contribution workflow](../../CONTRIBUTING.md) |
[Autonomous-development guidelines](../autonomous-development-guidelines.md)

| Field | Value |
|---|---|
| Document version | 0.1.0 |
| Recorded | 2026-10-31 |
| Status | DESIGN-ONLY CONTEXT TRANSFER; FINAL JAVA CHECKPOINT AND .NET ACTIVATION PENDING |
| Canonical project home | [kushagraThapar/SuicideSquad](https://github.com/kushagraThapar/SuicideSquad) |
| Future SDK research target | [Azure/azure-cosmos-dotnet-v3](https://github.com/Azure/azure-cosmos-dotnet-v3) |
| .NET source baseline | Not selected or inspected in this handoff |
| Initial canonical Java import | [Design v0.2.2 at a10d3042a61540b907edbe17b710c6294b997a7f](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/suicide-squad-design.md) |
| Implementation / SDK execution authorization | None |
| Release execution, automation and production rollout | Deferred to a separate project |

This document transfers context, not Java implementation facts or approval.
The user chose a **versioned Java design/research checkpoint with explicit
remaining gaps**, not a fully source-verified Java feature/invariant catalog,
as the handoff point before prioritizing .NET. The initial Java import is
persistent; the coordinator has **not** confirmed the final checkpoint or
activated .NET-specific investigation. A corrected final checkpoint is pending
the Java workstream's repository-layout cleanup.

The eventual goal remains agents discovering and reproducing SDK bugs,
implementing fixes, running comprehensive validation, receiving independent
PR Review Router-led review, iterating, and merging eligible candidates without
routine human intervention. That goal grants no current execution, unattended
merge, deployment or release authority.

## 1. Scope, acceptance and boundaries

The accepted slice is a standalone .NET starting document that:

- Preserves applicable requirements, unresolved decisions and recovery limits.
- Separates reusable framework from .NET-specific contract revalidation.
- Provides immutable existing references and explicit pending checkpoint fields.
- Leaves the Java design/research and root guidance untouched.
- Gives ordered, design-only continuation steps behind the coordinator's gate.

Only this .NET-scoped document is introduced. There is no .NET source,
changelog, test, CI, package or public-issue investigation in this contribution.
The existing .NET checkout is a future read-only research input, not an output
destination. No SDK code, test infrastructure, agent definitions, permissions,
live resources or Agent merge settings are changed; no agents are launched.

**Repository layout:** SuicideSquad retains project-authored design, discovery,
catalog/provenance records and pinned upstream references, not vendored SDK
source snapshots. Future researchers need access to the target SDK repository
at the recorded immutable revision. Do not copy SDK source into this .NET
documentation area. The coordinator's layout correction supersedes the
historical initial Java import's snapshot layout; Java cleanup belongs to that
separate workstream.

The whole .NET SDK feature/behavior surface is the intended design scope from
the beginning, not a retries/deadlines-only pilot. Exact package boundaries,
supported versions and service combinations require .NET revalidation. Later
activation permits design investigation only; implementing fixtures, executing
SDK assessments, changing CI or enabling merges requires separate authorization.

**Status discipline:** confirmed direction, proposed controls, inherited Java
observations and .NET-verified facts are different categories. This handoff
contains no .NET-verified source/test facts. Written requirements are not
implemented controls, and publication is not independent design approval.

## 2. Provenance and the pending Java checkpoint

### 2.1 Inputs and authority

The supplied Java session design v0.2.1 was read, including scope, architecture,
catalogs, metrics, tests, benchmarks, review, operations and continuation.
After the coordinator supplied the canonical v0.2.2 import, its complete diff
against that intake was inspected. The immutable repository version below
supersedes the local design as the reference for that revision. The old v0.1
attachment is stale and was not used.

| Input | Reference and limit |
|---|---|
| Canonical Java design | [v0.2.2, sections 2 and 4-19](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/suicide-squad-design.md); initial import, not final stabilization |
| Historical Java import provenance | [Research index](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/README.md) and [import manifest](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/import-manifest.json); the old snapshot layout is superseded, not approved for .NET reuse |
| Incomplete Java research | [Report status](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/reports/README.md) and [import recovery checklist](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/recovery/README.md); the checklist is not the later parent-authored recovery package |
| Parent-authored recovery narrative | Supplied `recovery/README.md`, with the intake digest below; read as new discovery output, not a recovered agent report. Canonical final-checkpoint reference pending |
| Recovery exports | `changelog-discovery-ledger.json` and `source-discovery-inventory.json`, summarized by that narrative; not copied, independently recomputed or admitted as .NET evidence here |
| Cosmos concepts | `tvaron3/cosmosdb-design-docs@bcfbc786fa5296deebcccd11369efb583e63e48c`; applicable sections consulted, with qualifications in section 12 |

Intake SHA-256 receipts identify exactly which revisions informed this transfer:

| Input | SHA-256 |
|---|---|
| Original supplied Java design v0.2.1 | `53f53195f6da2c04b3511824056d0042d9e8111e90d9459a47254c54c60263f8` |
| Canonical Java design v0.2.2 | `6dab296f3db25bf448bded9ed0079eaf4f76404c94521e700bccc7677716437f` |
| Supplied parent recovery narrative | `01778dd74cf96b5857804a553a61011841a5a9c840de5013d658565097e06266` |

These are document receipts, not source/test verification. Machine-local
session paths are not long-term authority. When the coordinator supplies the
final checkpoint, record its immutable design, recovery and handoff references
here, retaining these intake receipts rather than silently rewriting history.

### 2.2 Checkpoint receipt still required

| Required coordinator record | Current state |
|---|---|
| Corrected final Java checkpoint commit and design version | Pending; `a10d3042...` is the historical initial import only |
| Canonical parent-recovery location and provenance | Pending; not included in that initial import |
| Java pause / .NET-first priority recorded in the Java handoff | Follow-up pending |
| Explicit remaining Java gaps and accepted checkpoint boundary | Supplied as context below; final checkpoint confirmation pending |
| Explicit .NET design-investigation activation | Not received |

The initial import is [#2](https://github.com/kushagraThapar/SuicideSquad/pull/2).
Feature-branch publication does not establish default-branch integration,
design approval, inventory closure or .NET activation. The imported Java design
still describes Java-first work; the user-directed transition changes the next
research priority, not the truth of its historical observations. The parent
owns recording that transition and the final Java checkpoint in the Java lane.
The Java workstream is removing source snapshots from its current net diff
while retaining `a10d3042...` in history. Recovery receipts remain historical
discovery evidence, not justification to retain or re-vendor SDK source here.

## 3. Reuse versus revalidate

| Area | Carry forward | Must be established for .NET after activation |
|---|---|---|
| Product scope | Whole-SDK feature/behavior scope; separate discovery, execution and autonomy milestones | Actual APIs, internal workflows, packages, lifecycle and supported combinations |
| Evidence model | Atomic contracts, independent oracles, bidirectional traceability and distinct verification states | .NET symbols, assertions, runners, candidate artifacts and exact execution receipts |
| Quality policy | Multidimensional evidence; critical gaps cannot be averaged away | Baselines, measurable denominators, tool limits and D-02/D-03 decisions |
| Status and consistency | Full decision key, write ambiguity, session/topology distinctions | Actual producers/handlers, defaults, overrides, safe replay and final error mapping |
| Scenarios | Constrained interactions, critical sequences and database non-guarantees | Applicable .NET runtime, transport, account and service-capability cells |
| Test architecture | Reuse existing facilities; negative controls; deterministic plus real-service evidence | Actual build/test discovery, instrumentation, controllable clocks, fault fidelity and fixtures |
| Historical bugs | Public provenance, behavioral red/green proof, neighboring cases, contamination limits | A .NET-specific candidate corpus and admitted reproductions |
| Review and merging | Router-led independent semantic judgment; separate restricted actuator; fail closed | Repository governance, bounded peer fanout, required roles, candidate-bound protocol and approval |
| Safety and operations | Protected policy/oracles, least privilege, bounded cost, privacy, ownership and recovery | Concrete owners, enforcement, retention, access, capacity, cleanup and outage procedures |

Java's Maven/TestNG/Reactor/Netty/JaCoCo/PIT observations or recommendations are
not .NET tool selections. Java public names, numeric defaults, retry matrices,
wire tokens, package counts and fixture capabilities are not .NET contracts.
Even .NET examples in the concept repository need current candidate/service
verification. Similar class names and apparently shared features do not prove
equivalence.

## 4. Whole-SDK discovery and contract obligations

### 4.1 Feature breadth

The Java F-IDs below are navigation back to the seed catalog, not approved .NET
IDs or evidence of .NET availability. All rows require source-backed discovery,
applicability and contract decisions. Preserve unsupported, preview, deprecated,
removed, historical and unresolved entries explicitly; unknown is not
unsupported.

| Java seed | .NET discovery/revalidation scope |
|---|---|
| F-01 | Client construction, initialization, concurrent use, shared-resource ownership, failed construction, close/dispose and calls during/after shutdown |
| F-02 | Public/internal defaults and precedence; null/unset/explicit false or zero; invalid bounds; client/request/environment settings; feature detection and fallback |
| F-03 | Credentials, authorization, refresh/rotation, restricted resources, resolver failures and sensitive-data boundaries |
| F-04 | Database/container/resource lifecycle, create races, stale handles and delete/recreate with changed identity |
| F-05 | Item CRUD, read-many variants, identity/key extraction, conditional headers, bodyless results and response metadata |
| F-06 | Serialization paths for items, query parameters, projections, patch and child resources; null/missing/undefined, numeric/Unicode boundaries and stream ownership |
| F-07 | Logical/hierarchical keys, prefixes and boundaries; hash/range encoding; feed-range identity, round-trip and topology applicability |
| F-08 | Account/name/RID/range/address/query-plan caches, refresh coalescing, invalidation, races and identity isolation |
| F-09 | Account/client/request consistency, automatic/explicit session state, token formats/merges/scopes and split/merge/recreate behavior |
| F-10 | Status/substatus decisions, nested budgets, retry-after/backoff, metadata recovery, cancellation, deadlines and ambiguous writes |
| F-11 | Regional selection/exclusion/discovery, single/multi-writer topology, outage/recovery and no eligible endpoint |
| F-12 | Availability/hedging/circuit-breaker mechanisms actually supported; winner/loser cleanup, probes, cooldown and state isolation |
| F-13 | Direct transport framing/negotiation, TLS, multiplexing, pooling, acquisition/timeout/partial-I/O behavior and shutdown |
| F-14 | Gateway/HTTP protocols actually supported, proxies, pooling/stream limits, local failures versus regional health and malformed responses |
| F-15 | Thin-client/capability mechanisms if present; explicit/default enablement, probes, fallback and unsupported-account behavior |
| F-16 | SQL/query plans, partition scope, parameters, ordering/ties, aggregates, distinct/grouping, limits, concurrency and continuation support |
| F-17 | Vector/full-text/hybrid capabilities if present; configuration, score scope, component alignment, empty/tied results and service limits |
| F-18 | Paging/iterator/stream surfaces actually present, empty intermediate pages, page-size hints, resume, repeated use, cancellation and token compatibility |
| F-19 | Transactional batch scope, limits, conditionals, per-operation results, atomicity and dependent failures |
| F-20 | Bulk scheduling/batching, bounded input/concurrency, per-item correlation, mixed outcomes, retry/topology interactions and absent normal responses |
| F-21 | Patch operations, paths, filters/ETags, invalid combinations, non-idempotent updates and replay restrictions |
| F-22 | Change-feed pull modes, start/resume/retention, 304 progression, ranges and topology/capability interactions |
| F-23 | Processor leases, ownership/renewal/rebalance, callback failure, checkpoint modes, restart, estimator and bounded shutdown |
| F-24 | Throughput metadata, manual/autoscale/shared/dedicated arrangements, priority/control features if present, hot partitions and throttling attribution |
| F-25 | Container/indexing/spatial/composite/vector/full-text/unique-key/TTL/conflict/computed-property policies actually present and wire validation |
| F-26 | Scripts, triggers, UDFs, users/permissions, conflicts and other child-resource contracts, including parameters and paging |
| F-27 | Dedicated-gateway/cache features if present; staleness/consistency, bypass, metadata and unsupported combinations |
| F-28 | Diagnostics/errors, charge/activity/retry attribution, tracing/metrics/hooks, privacy/cardinality and bounded overhead |
| F-29 | Actual .NET async/concurrency/cancellation/context and repeat-use contracts; request-state isolation and terminal races, not transposed Reactor semantics |
| F-30 | Source/binary/package/wire/token compatibility; supported .NET target frameworks, OS/architecture/TLS/dependencies and consumer integration |
| F-31 | New/preview metadata and service features, including GSI/encryption metadata if present; capability/lifecycle and compatibility boundaries |

Companion-package contracts genuinely in .NET scope need separately identified
lanes and denominators, not silent inclusion or exclusion. Encryption discovery
must go beyond policy/key metadata to key resolution, rotation/rewrap/caching,
serialization/query/operation combinations, errors and privacy. Actual .NET
package membership and contracts remain unverified. Connectors/frameworks are
consumers or separately scoped products, not automatically part of the client
denominator.

### 4.2 Closure is more than a feature list

At an immutable .NET baseline, reconcile the entire changelog history, including
beta/hotfix and Other Changes, with current public APIs/options/configuration,
internal workflows, capabilities, protocol paths and companion history.
Preserve nested changes and repeated entries with their source spans. One
changelog bullet can create several semantic obligations.

Each semantic obligation needs a stable record, source/version/span, lifecycle,
classification, affected behavior and atomic invariant, or an explicit
unresolved/lifecycle-exclusion disposition. Reconcile both directions:
history to current contracts and current source to history/specification or
an explicit history gap. Dependency and documentation changes can expose
compatibility or behavioral obligations. Neither file enumeration nor lexical
family classification proves semantic closure.

Each atomic invariant must identify preconditions/configuration, event sequence,
allowed and forbidden observable outcomes, safety versus bounded liveness,
an independent oracle, contract authority, scenarios, actual assertions and
exact execution evidence. Cover positive, negative, boundary and applicable
concurrency cases. An implementation observation can itself be a bug; resolve
conflicting source, specification, issue and service claims explicitly rather
than training the oracle to agree with the candidate.

Use approved reference/mathematical models, golden vectors, metamorphic
properties or verified service fixtures where suitable. Hardcoded expectations
that merely restate the implementation are not independent correctness evidence.
Cross-cutting obligations include request/option propagation, mutable-state
isolation, version-scoped token algebra, one logical terminal result and
diagnostic lifecycle, explicit failures and bounded resource ownership.

Required traceability is:

```text
feature -> behavior -> atomic invariant -> applicable scenario -> test/assertion
        -> exact execution/evidence -> independent Router review
        -> restricted merge receipt
issue -> affected revision -> behavioral regression -> invariant
```

Keep `proposed`, `contract-verified`, `test-mapped`, `execution-verified` and
`autonomy-qualified` distinct, with explicit blocked, unsupported and
retired-with-history dispositions. All .NET obligations here remain proposed
or unresolved. A test name is not assertion evidence; line execution is not
proof that the relevant contract was asserted.

### 4.3 Status/substatus decision cells

Required decision inputs include:

```text
operation/resource, HTTP+substatus pair, origin,
mode/protocol, transmission/possible-commit state,
consistency/session, options/capabilities, topology/cache state,
remaining attempt/delay/deadline/resource budgets
    -> retry/refresh/route/delay/surface + diagnostics + cleanup
```

Inventory constants, producers, handlers, transformations, batch decoders and
unknown/default paths. Include success/bodyless/304 behavior, validation and
serialization, authentication/authorization, resource/session/metadata absence,
conflicts and preconditions, topology/Gone, local/server timeouts, service and
client throttling, RetryWith, availability, non-HTTP transport failures,
dependent batch errors and missing/malformed/new codes. Java's 39 status
families are discovery questions, not a .NET decision table.

Substatus alone and HTTP status alone are insufficient. Distinguish SDK,
service, transport and injected origins. Each applicable cell needs recovery,
persistent failure, budget exhaustion, cancellation/deadline, read/write safety,
diagnostics and cleanup cases. Unknown required cells block eligibility;
they are not permission to guess a retry or copy a Java default.

### 4.4 Scenarios and non-guarantees

Model API/operation, connectivity, account topology/capability, consistency,
partitioning, caches, request phase, failures, timing, load, data, lifecycle,
runtime and feature state. Use valid constraints, exhaustive small critical
decision tables, pairwise combinations, explicit higher-order interactions and
stateful/concurrency sequences. Record seeds/schedules and minimized failures.
Pairwise coverage does not prove a critical sequence safe.

Carry the following Java scenario seeds as questions to specialize:

| Java seeds | Preserved scenario obligations |
|---|---|
| SC-01 through SC-04 | Throttle near deadline; nested throttle/topology/availability recovery; committed write with lost response; cancellation during backoff/acquisition/partial response/completion |
| SC-05 through SC-08 | Cold/unavailable metadata; query resume through split; change-feed timestamp/continuation through merge; delete/recreate identity and session isolation |
| SC-09 through SC-14 | Mid-write regional change; no eligible region; out-of-order cache refresh; local protocol failure; hedged result/session/cleanup; partition-scoped circuit recovery |
| SC-15 through SC-17 | Bulk mixed results and absent responses; non-idempotent patch with lost response and failed conditions; batch atomicity and dependent errors |
| SC-18 through SC-20 | Empty-page/throttle/resume/repeat-use interactions; hybrid component ordering/alignment; serializer boundaries across query/read-many/patch |
| SC-21 through SC-23 | Callback failure/checkpoint/lease transfer/restart; concurrent credential rotation/failover; close during active bulk/query/feed work |
| SC-24 through SC-26 | Failing/saturated/repeated telemetry hooks; hot logical partition despite idle peers; malformed/partial/oversized wire data and tokens |
| SC-27 through SC-28 | Supported runtime/dependency transitions and consumer compatibility; new status/capability mismatch with explicit safe failure |

The 12 general database scenario families also remain required: concurrent
writers/lost updates; isolation/transaction boundaries; identity/uniqueness;
representation/serialization; query determinism; concurrent mutation during
enumeration; expiration/retention; index/schema evolution; possible-commit
failure; durability/consistency claims; authorization changes mid-workflow;
and multi-client/account/container isolation.

Do not invent snapshot isolation for pagination, cross-partition transactions
for bulk, global ordering or exactly-once processing for change feed, or
non-commit from timeout/cancellation. Keep fixed-dataset enumeration oracles
separate from allowed concurrent outcomes. Session guarantees are not
account-global across arbitrary clients. Page-size/concurrency options may
be hints. TTL/service progress is not an exact client-clock deadline. Unit
tests do not prove service durability or all distributed behavior.

## 5. Quality vector and unresolved improvement policy

Near-100% reportable executable line coverage remains a goal, not a correctness
proof or measured .NET result. Track separately:

| Dimension | Evidence/denominator required |
|---|---|
| Executable lines | Exact candidate production code, including never-loaded code; per-suite/configuration and compatible aggregate |
| Branch outcomes | Reportable outcomes, instrumentation limits and explicit exclusions; not a claim of exhaustive paths or MC/DC |
| Mutation detection | Pinned operators/cohorts; killed, survived, uncovered, inconclusive, invalid and independently approved equivalent cases |
| Atomic invariants | Applicable obligations with required passing assertions and independent oracles; critical gaps visible |
| Status decisions | Required valid decision cells, not merely enumerated status numbers |
| Scenarios/interactions | Declared valid axes/pairs and critical sequences, reported separately |
| Historical regressions | Frozen eligible fault cohort; admission/reproduction separated from detection |
| Compatibility | Applicable source/API, binary, package, wire, token and runtime contracts; hard constraints, not averages |
| Reliability/performance/resources | First-run flakiness, leaks, cleanup, throughput/latency/allocation and calibrated budgets |

Report raw counts, numerators, denominators, cohort/catalog/policy versions,
absolute gaps, applicability and evidence validity at SDK/domain/critical scope.
Improvement in one domain must not compensate for another domain's critical
gap. No weighted score, rounding, test count or agent confidence overrides a
failed required obligation.

The user wants PRs to improve these dimensions and never degrade them.
**D-02 remains open:** strict increase at saturation, docs-only or
behavior-neutral PRs, newly discovered debt, added/retired obligations and
growing denominators need an explicit policy decision. Comparable-cohort
component-wise nonregression plus complete new obligations is a recommendation,
not an approved relaxation or implemented gate.

Preserve both frozen old obligations and the honest full candidate denominator.
Classify retained, added, modified, retired and newly discovered obligations.
Expose discovery-only score drops; do not hide them or call equality
improvement. N/A, empty cohorts and discovery-only treatment need explicit
dispositions, not a fabricated 100%. Discovery cannot qualify newly unproven
behavior for merging. Legitimate deletions require obsolete-contract evidence,
not removal of inconvenient tests.

For mutation accounting, preserve the proposed Java design distinction:
`K` killed by the expected assertion, `S` survived, `U` uncovered, `T`
inconclusive/timeout, `X` invalid and `E` independently approved equivalent.
The proposed completed-cohort score is `K / (K + S + U + T)` after auditable
`X`/`E` exclusions, with raw counts retained. Unexecuted planned cases mean
incomplete; infrastructure errors invalidate a run; timeout is not a kill.
Sampling is not a full-SDK score, and the repair agent cannot approve its own
equivalence exclusions. .NET tooling and metric policy are not selected here.

Numerical thresholds, ratchets, performance tolerances and resource/iteration
budgets remain D-03/D-10. No universal 99%/95% threshold or Java retry/time
default is adopted. Approved exclusions need exact scope, evidence, owner and
expiry; an unreachable fault path is a fixture gap, not an automatic exclusion.

## 6. Test, execution and evidence requirements to specialize

Reuse .NET facilities only after establishing what actually exists and runs.
The proposed layers remain deterministic unit/property checks, stateful
client/transport faults, emulator integration, required live service validation,
concurrency/stress/soak, and compatibility/performance. No particular .NET
runner, mutation engine, concurrency tool, emulator capability or CI command
has been verified or selected.

The later design must specify:

- Exact setup/build/test discovery, logical and parameter-case identities,
  configuration/platform matrix, dependencies and expected result counts.
  Zero discovered tests, empty parameter sources, skips, swallowed async
  failures and lost/crashed workers cannot look like success.
- Candidate production assembly/source/symbol/package identity and digests.
  Collect all required workers/shards; union only compatible candidate data,
  never average percentages or combine incompatible binaries. Preserve
  per-configuration evidence and include unexecuted production code.
- Independently observable outcomes, request/attempt details, meaningful
  assertions and negative controls. Confirm an injected fault fired before
  accepting its recovery result. Do not mock away the algorithm under test.
- Narrow controllable seams for clocks, timers, scheduling, randomness,
  transport, metadata and completion order. Virtual time proves only paths
  actually wired to those controls; real scheduler/transport checks and
  service/emulator fidelity remain necessary.
- Serialization/stream/buffer/timer/connection/task ownership through success,
  failure, cancellation and shutdown. Timing/resource bounds must reflect
  supported workloads, not unbounded caller input.
- Permanent sentinels plus impact-selected checks, with verified dependency
  mapping. Unmapped changes, uncertain selection or shared infrastructure
  changes require broader checks or blocked eligibility, not fewer tests.
- Candidate-specific required evidence versus scheduled full assessments.
  Scheduled coverage cannot replace an impacted live/performance obligation.
  Instrumented coverage and uninstrumented performance runs stay separate.
- First outcomes and every bounded retry, product versus infrastructure
  classification, visible quarantine debt and independently governed policy.
  A retry pass is not a clean pass; losing sole reliable evidence removes the
  affected autonomy, not the obligation.
- Comparable uninstrumented performance artifacts, controlled warmup/workload,
  repeated samples, uncertainty and service variability. No noisy single run
  or agent estimate is a performance gate.

Live-account ownership is a design obligation, not a request for resources.
Revalidate whether .NET uses shared accounts. Before any future authorized live
execution, define exact run namespaces/ownership, fault scope, capacity/RU
coordination, credentials and cleanup after success/failure/cancellation.
Never delete pre-existing resources or interfere with other runs. Cleanup
failure remains visible debt; outages or exhausted budgets block/pause rather
than silently dropping required evidence.

## 7. Historical bug benchmark

Use public .NET issues/PRs/changelog provenance only after activation and
scope/version triage. No Java seed issue is an admitted benchmark or
automatically a .NET bug. No .NET case was investigated or admitted here.
Closed does not mean fixed, and issue prose does not establish root cause.

Preserve the admission protocol:

```text
candidate -> triaged -> reproduction-ready -> red-confirmed
          -> fix-confirmed -> benchmark-admitted
```

Retain duplicate, non-client-bug, unsupported historical environment,
nonreproducible, needs-fixture and needs-contract-decision states and counts.
Each admitted case needs sanitized synthetic reproduction, affected and fixed
revisions, a real behavioral assertion failing before and passing after,
configuration/fixture and porting provenance, linked atomic invariants, and
neighboring mode/boundary/operation variants or negative controls. Build or
dependency failure is not red behavioral evidence.

Keep development, held-out evaluation and independently generated variant
partitions distinguishable. Public historical bugs can be in training data;
hidden selection does not prove uncontaminated evaluation. Supplement historical
gate detection with seeded and prospective faults. Treat issue attachments and
scripts as untrusted; historical vulnerable code requires pinned, isolated,
unprivileged execution without production access and separate authorization.

Every later admitted fix closes a learning loop: retain the original regression
and relevant variants, add missing contract/status/scenario obligations, and
record whether the pre-fix suite would detect it and which gate missed it.

## 8. Independent review, merge governance and safety

### 8.1 Responsibilities, not an existing autonomous system

The reusable responsibility flow is inventory/contracts -> tests -> trusted
execution -> immutable evidence -> independent Router judgment -> repair/new
candidate -> final eligibility -> restricted merge executor -> receipt.
Prefer mature existing primitives and minimal adapters, not a new service for
every responsibility.

PR reviews/re-reviews must enter through PR Review Router, optionally via the
routing-only Squad wrapper. Specialists are Router-coordinated, never
replacement primary reviewers. Semantic mergeability belongs to independent
Router-led judgment. The actuator checks valid receipts and repository rules;
it cannot approve semantics, weaken policy or bypass human gates.

The existing local Router is not already an autonomous merge system. Its
human approval/posting boundary remains intact. Repository-owned protocol,
policy/prompt/model/tool provenance, required reviewers and fail-closed behavior
need explicit design. Two independent Router-led judgments plus independent
test challenge are the Java draft recommendation, not an approved .NET quorum;
exact risk-tier requirements remain D-07. Model diversity does not establish
statistical independence. No reviews or agents are run by this handoff.

Cross-SDK review covers Java, .NET, Python, Go and Rust, with JS/TS and consumers
when relevant. Each compatibility cell needs pinned source/contract/test
evidence, configuration/default differences, applicability and eligibility
impact, using equivalent / intentional difference / unsupported / verified gap /
unverified distinctly. Resolve bounded fanout and current Router integration
under D-08; do not silently omit peers. New customer-facing exposure of
third-party implementation types is a blocker; legitimate existing public
dependencies are baseline contracts, not implicitly removed.

### 8.2 Candidate-bound evidence and failure behavior

Evidence must bind repository/PR, base/head/actual merge-candidate identity,
production artifacts, environment, runner/tools, configuration, policy/catalog
and cohort digests, expected/discovered/executed test cases, raw vector/results,
missing or inconclusive checks, red/green proof, reviewer identities/roles,
findings/dispositions and trusted provenance.

Required outcomes include `eligible`, `changes_required`, `blocked`,
`needs_contract_decision` and `rejected`. Missing reviewer/results/context,
malformed or stale receipts, wrong SHA/artifact, lost shard, weak test discovery,
unresolved oracle or supported blocker, policy weakening and exhausted budgets
cannot yield eligibility. The implementation agent cannot close its own
blocker. Majority vote and an empty findings array are not approval evidence.
Findings are fixed with evidence, independently refuted, or routed through
protected contract change; blocking safety work cannot be deferred into approval.

Rebase, new commits, conflicts, base/queue composition and policy/catalog
changes invalidate affected evidence. Final judgment must bind the actual merge
candidate through a race-safe process. Reconcile an ambiguous external response
before retrying a merge or other side effect. Repository/org review rules,
CODEOWNERS and qualifying identities remain prerequisites; internal receipts
do not manufacture GitHub approval identities.

### 8.3 Protected evaluation and operations

Separate implementation authority from policy, oracle/evaluator, exclusions,
test-selection rules, reviewer settings and merge credentials. Treat issue/PR
text, downloaded artifacts and candidate-emitted pass summaries as untrusted.
Use scoped access, reproducible isolation, trusted evidence, independent
negative controls, and redaction/retention boundaries; a worktree is not a
security sandbox. Do not copy private support data, credentials or sensitive
telemetry into public benchmarks or prompts.

Keep untrusted PR execution secretless and separate from approved credentialed
live tests. Implementation agents must not hold merge/release credentials.
Observer/telemetry failures must follow the verified hook contract rather than
silently changing database outcomes.

Specify finite time/cost/repair/retry limits, auditability, independent global
and per-scope stops, stale-evidence rejection, outage admission behavior and
cleanup ownership. Gate manipulation, credential exposure or escaped regression
requires stopping the affected scope and governed recovery/requalification;
a source revert alone does not restore trust. No automatic revert, merge,
permission change or release is authorized here.

## 9. Java prior art and explicit remaining gaps

These are **inherited Java observations**, not independently rerun audits or
.NET measurements. Java source baseline:
[`Azure/azure-sdk-for-java@42702a3a1421498ee457ff9cbe56713d0877d39f`](https://github.com/Azure/azure-sdk-for-java/tree/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos).
Its source revision is not a support-policy or GA-capability guarantee.

| Prior-art fact | Limit to preserve |
|---|---|
| Design seeds: 31 feature, 52 invariant, 39 status, 28 critical scenario and 12 general database families | Families/questions, not complete verified atomic contracts |
| Four original research agents became unavailable without completed reports | Saved inputs survived; do not describe reports as completed or still pending arrival. Recovery outputs were newly authored by the parent |
| Recovery accounts for all 145 core release headings and 721 top-level bullets, preserving nested text | Full structural changelog accounting, not semantic closure; companion encryption changelog absent from supplied recovery |
| 705 bullets have lexical family hints; 16 have no hint | All 721 lack verified atomic semantic mapping in that export. This is not a 97.8% contract score, and the 16 are not the whole backlog |
| Saved manifests: 1,287 core production, 515 test-module and 31 fault-injection production Java files; encryption 54 production / 19 test files | Includes descriptors/helpers; not API, executable-line, assertion or test-case counts |
| 183 files under unqualified exported core packages have matching cached bytes | Not 183 APIs; visibility, overloads, inheritance, qualified exports and companion surfaces still need reconciliation |
| Original cache audit: 903/905 copies matched, representing 679 distinct matching upstream paths | Two identical original `RxGatewayStoreModel.java` copies were unverified. Historical v0.2.2 excluded those bytes and retained a verified pinned public replacement; original-intake/imported receipts stay distinct, but do not endorse source vendoring |
| Selected CI/configuration observations and shared live accounts exist in Java inputs | Not proof of current required checks, successful execution/cleanup or equivalent .NET fixtures |
| No SDK coverage/mutation scores measured, benchmarks admitted or SDK execution performed in the Java design exercise | Not evidence that existing SDK coverage or regression tests are zero. No SDK implementation, live operations or releases occurred |

The final Java checkpoint must retain these gaps without completing every
Java contract first. Pausing Java preserves its backlog; it does not mark
DS-14 or design approval complete.

### Consequential leads to carry as discovery prompts

| Java lead | Future .NET question, not a .NET finding |
|---|---|
| Account consistency versus `ReadConsistencyStrategy` | Enumerate actual account/client/request/strategy precedence and supported transport/topology combinations; do not invent an equivalent API |
| Gateway 449 changed in Java history while chapter 17 gives generic/older guidance | Verify current .NET orchestration and safe replay by mode/version; no blanket Direct retry-superset rule |
| 408/21013 write-barrier changelog/source discrepancy | Resolve applicable service/producer/outer-policy paths and oracle; do not label a .NET defect from the Java partial trace |
| HTTP/2 local PING failure versus region poisoning | Discover actual .NET protocols, failure origins, health scope and cancellation/ownership behavior |
| Metadata-only 404/0/1003/1013 recovery | Distinguish resource/operation-specific recovery from missing item behavior; no universal 404 rule |
| Multiple read-many contracts, continuation identity and hierarchical `/id` completion | Discover actual API variants, key extraction, token binding, limits and unsupported combinations |
| Lost options on resume, clone or hedging rebuilds | Enumerate propagation of authorization, serializer, consistency/session, routing, deadline and throughput state at each real .NET boundary |
| Shared metadata caches, workload-ID tokens and N-region commit | Establish presence, sharing/identity/lifecycle, wire encoding and commit/barrier capability from .NET/service evidence |
| GSI, throughput buckets, hybrid/vector/full-text queries and custom serializers | Establish actual availability, feature flags, query/serialization semantics and account limitations |
| Change-feed mode, retention, start-time/merge, 304, leases and checkpoint interactions | Verify actual contracts and allowed replay, lease ownership, resume and shutdown; no unverified cost multiplier or exactly-once claim |

No Java cache, seed issue, test count or discovery export becomes .NET evidence
by relabeling it. A counterpart may be absent or intentionally different.

## 10. Decision queue carried forward

The D-IDs intentionally retain correspondence to Java design section 16.2.
Recommendations remain recommendations. The repository destination, whole-SDK
breadth and .NET-first-after-checkpoint direction are settled; the following
technical/governance decisions are not.

| ID | .NET-scoped unresolved decision |
|---|---|
| D-01 | Immutable SDK baseline and supported branches, target frameworks/runtimes, OS/architecture, transports, account/service-capability and package matrix |
| D-02 | Exact improvement/nonregression policy at saturation, docs-only/neutral changes, discovery-only debt, N/A and changing denominators |
| D-03 | Threshold-setting procedure, staged ratchets, numerical performance tolerances and authorized assessment/CI/agent budgets |
| D-04 | Runtime catalog/evidence layout, schemas and eventual SDK-side bindings; project records and pinned upstream references belong here, SDK source does not. This handoff path is chosen, not the catalog implementation |
| D-05 | Source/changelog/API/internal-workflow closure, atomic oracle authority, disputed contracts and explicit lifecycle exclusions |
| D-06 | Org/repository unattended-merge governance, protected-policy owners and compatibility with current human approval rules |
| D-07 | Reviewer independence, required roles/quorum by risk, independent test challenge and final-candidate reconciliation |
| D-08 | Full cross-SDK matrix depth and bounded Router peer fanout/integration without silent missing peers |
| D-09 | Mutation/property/concurrency and coverage tooling fit to actual .NET runtime/build/test/package constraints |
| D-10 | Evidence retention/access/provenance, cost/concurrency, live ownership/capacity/fault isolation, cleanup and outage/stop/recovery procedures |
| D-11 | Historical corpus admission mix, shadow/qualification sample sizes, risk strata, duration, uncertainty and prospective escape criteria |
| D-12 | Protected intentional contract changes, exceptions, obsolete obligations and historical behavior that is itself incorrect |

Policy design and baseline-dependent measurements must remain separate.
Designing an assessment does not invent its results; authorizing a bounded
measurement does not authorize implementation or unattended merges. Thresholds
and graduation samples require approval before their corresponding gates run.

## 11. Ordered design-only continuation

1. **Wait for the coordinator.** Receive the corrected final Java checkpoint commit,
   version, recovery/handoff paths, accepted remaining gaps and explicit .NET
   activation. Update section 2 and the version log with immutable references.
   The initial import, a merged PR or elapsed time alone is not activation.
2. **After activation, reconcile scope and select a research baseline.** Read
   current project guidance and the checkpoint, then inspect the .NET target
   read-only to pin a source revision and propose the D-01 support/capability
   matrix. Access source in the target SDK repository, not a SuicideSquad
   snapshot. Baseline selection is not permission to execute SDK tests.
3. **Establish .NET discovery provenance and gaps.** Reconcile full history,
   APIs/options/internal workflows, companion boundaries and status decision
   sites. Separate structural inventory, atomic contracts, test mapping,
   execution and qualification; do not copy Java denominators.
4. **Specify atomic contracts and interaction oracles.** Resolve conflicts
   against .NET public/service evidence, qualify conceptual guidance, and map
   all domains, status cells and critical/general database scenarios.
5. **Resolve measurement and review design.** Settle D-02/D-03 policy, catalog
   and receipt schemas, actual tool/fixture feasibility, benchmark admission,
   bounded cross-SDK review, protected governance and operations. Source
   discovery and independent policy discussions may progress concurrently;
   this ordered list does not make them artificial implementation dependencies.
6. **Obtain design review and explicit authorization for any next phase.**
   Preserve findings/dispositions, unverified gaps and residual risk. No
   implementation, measurement campaign, shadow execution or merge authority
   follows merely from completing the document.

The later graduation model remains design -> whole-SDK measured baseline ->
whole-SDK shadow decisions -> qualified narrow merge scopes -> separately
qualified expansion. Any-domain shadow experiments can expose useful
`BLOCKED: missing contract/fixture/evidence` results before every fixture exists,
after design approval and authorized trustworthy baseline/receipt paths.
Experiment breadth never grants all-domain autonomy, and positive eligibility
requires every impacted obligation and global safeguard.

### Current progress and stop condition

| Item | State |
|---|---|
| Context transfer | This versioned .NET document; independent review/default-branch integration not claimed |
| Final Java checkpoint | Pending coordinator confirmation |
| .NET-specific investigation | Not started; activation pending |
| .NET source-backed contracts, test/CI facts and supported matrix | Unverified; not zero, unsupported or complete |
| .NET coverage, mutation, benchmark and performance results | Unmeasured / not run by this contribution |
| .NET design approval / implementation authorization | Not granted |
| Autonomous merging / releases | Not authorized; releases remain separate |

**Stop here after publication and report the path, version and immutable
reference to the coordinator. Do not start step 2 until the explicit signal.**
On resumption, re-read this gate and current repository state; do not blindly
replay external side effects or treat remembered progress as durable evidence.

## 12. Canonical concept references and qualifications

The canonical concept clone was fast-forward synced on `main` and consulted
at `bcfbc786fa5296deebcccd11369efb583e63e48c`, the same revision used by Java.
These sources ground design questions, not current .NET implementation proof.

| Document and consulted section | Use and qualification |
|---|---|
| [04-partitioning.md: SDK-Side Terminology; Split semantics](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/04-partitioning.md#sdk-side-terminology) | Distinguish logical key, EPK, range, physical identity and opaque API contract; independently verify .NET token/range compatibility |
| [05-replication-consistency.md: Consistency Levels - Detailed Breakdown](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/05-replication-consistency.md#consistency-levels--detailed-breakdown) | Keep service guarantees separate from account/client/request options and actual SDK enforcement |
| [06-transport-layer-rntbd.md: Two Connectivity Modes](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/06-transport-layer-rntbd.md#two-connectivity-modes) | Frame transport discovery; examples do not establish current .NET versions, protocol support or defaults |
| [07-query-engine.md: ExecuteQuery - The Core Entry Point](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/07-query-engine.md#executequery---the-core-entry-point) | Separate client query/continuation obligations from backend execution; no inferred snapshot guarantee |
| [11-request-units-throttling.md: Per-Physical RU Ceiling and the Hot Logical Partition](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/11-request-units-throttling.md#per-physical-ru-ceiling-and-the-hot-logical-partition) | Include skewed load and attribution; illustrative capacity math is not a measured .NET budget or universal account model |
| [12-change-feed.md: Partition Merge + StartFrom Timestamp - Scenarios and Performance Concerns](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/12-change-feed.md#partition-merge--startfrom-timestamp--scenarios-and-performance-concerns) | Contains hypotheses and qualified capability-dependent claims; do not adopt asserted replay/cost multipliers or example APIs as universal oracles |
| [16-session-tokens.md: Scope and Non-Goals; Session Token Lifecycle; Partition Topology Changes](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/16-session-tokens.md#scope-and-non-goals) | Scope, version and identity matter; generic merge examples and Java-specific region behavior do not establish current .NET algebra or propagation |
| [17-status-codes-and-sdk-retries.md: sections 1-2 and 6](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview) | Distinguish SDK and service retry surfaces; reconcile version/SDK divergences, defaults and blanket mode comparisons against actual .NET paths |

Concept material may contain .NET examples, implementation-specific statements
or explicit hypotheses. None bypasses candidate-specific verification,
independent oracle decisions or privacy policy. No canonical concept documents
were modified by this handoff.

## 13. Publication evidence and version history

The project worktree began clean at
`117aeefc095e1fa08136bc1da66c6dfa50c64a90`. Applicable root instructions,
contribution requirements and autonomous-development guidance were inspected.
Only `docs/dotnet/design-handoff.md` belongs to this contribution; no root
pointer or Java import is edited. Documentation verification and the publication
commit/PR receipt belong in this contribution's PR, not an invented SDK test
report. The available tool catalog did not expose an `ado` server; no live
Azure DevOps pipeline or approval state was queried.

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-31 | Transfer the Java design framework, full-domain seeds, unresolved decisions and separately attributed recovery limits into a .NET-specific starting document; pin the historical initial Java import; record the non-vendoring correction; keep corrected final checkpoint and activation pending |
