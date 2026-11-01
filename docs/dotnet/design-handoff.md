# Suicide Squad: .NET design handoff

[Project scope](../../README.md) |
[Contribution workflow](../../CONTRIBUTING.md) |
[Autonomous-development guidelines](../autonomous-development-guidelines.md)

| Field | Value |
|---|---|
| Document version | 0.2.1 |
| Recorded | 2026-11-01 UTC; original transfer 2026-10-31 |
| Status | .NET DESIGN-ONLY DISCOVERY ACTIVE; JAVA PAUSED AT ACCEPTED DESIGN/RESEARCH CHECKPOINT |
| Canonical project home | [kushagraThapar/SuicideSquad](https://github.com/kushagraThapar/SuicideSquad) |
| SDK research target | [Azure/azure-cosmos-dotnet-v3](https://github.com/Azure/azure-cosmos-dotnet-v3) |
| D-01 source and verification policy | User-selected: default `main`, all SDK source across the repository, existing SDK CI-derived baselines, Gateway and Direct; [decision receipt](#101-user-selected-d-01-baseline-policy) |
| Historical .NET intake pin | [`52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8`](https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8); initial main-based discovery, not a forever-fixed project baseline or semantic closure |
| Accepted Java checkpoint | [Design v0.2.3 at 5d92106027629ec6c5022a7cd5ef2085014d6973](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/suicide-squad-design.md) |
| Current .NET records | [Design/baseline v0.1.1](design-baseline.md) and [whole-SDK domain-gap matrix v0.1.1](domain-gap-matrix.md) |
| Implementation / SDK execution authorization | None |
| Release execution, automation and production rollout | Deferred to a separate project |

This document transfers context, not Java implementation facts or approval.
The user chose a **versioned Java design/research checkpoint with explicit
remaining gaps**, not a fully source-verified Java feature/invariant catalog,
as the handoff point before prioritizing .NET. The coordinator has now confirmed
the corrected Java v0.2.3 checkpoint and explicitly activated bounded,
**design-only .NET discovery**. Java is paused with its unresolved backlog.
This is a stable handoff record, not a claim that Java SDK behavior or the .NET
design is complete. The original pending gate remains visible in v0.1.0 history.

The eventual goal remains agents discovering and reproducing SDK bugs,
implementing fixes, running comprehensive validation, receiving independent
PR Review Router-led review, iterating, and merging eligible candidates without
routine human intervention. That goal grants no current execution, unattended
merge, deployment or release authority.

## 1. Scope, acceptance and boundaries

The initial context transfer is persistent at commit
`d9d02138e7fa72b32bfcc72dd63028d208004297`, and the first source-pinned
baseline/inventory/gap draft at
`2c67e23092a1f1cbcd719a71c6db51114926a31c`. This bounded follow-up records
the user's D-01 policy selection, not another SDK investigation campaign.
Observable acceptance is consistent policy/progress wording in these three
documents, unchanged historical evidence, explicit remaining CI/artifact/
assertion gaps, and no implication that D-02 through D-12 were approved.

Only the .NET documentation lane is changed: this handoff and its linked
baseline and matrix. The existing .NET checkout remains a read-only input,
not an output destination. This update performs no new SDK source/test/pipeline
inspection or execution and no exhaustive CI audit. No SDK/reproducer/exporter
code, build, test, coverage, mutation or benchmark is executed. No SDK code,
tests, pipelines, agent definitions, permissions, live resources or Agent merge
settings are changed; no SDK CI is triggered, no agents/reviews are launched
and no merge, deployment or release is authorized.

**Repository layout:** SuicideSquad retains project-authored design, discovery,
catalog/provenance records and pinned upstream references, not vendored SDK
source snapshots. Future researchers need access to the target SDK repository
at the recorded immutable revision. Do not copy SDK source into this .NET
documentation area. The coordinator's layout correction supersedes the
historical initial Java import's snapshot layout; Java cleanup belongs to that
separate workstream.

The whole .NET SDK feature/behavior surface is the design scope from
the beginning, not a retries/deadlines-only pilot. D-01 now selects all SDK
source across `Azure/azure-cosmos-dotnet-v3`, both Gateway and Direct, and
the existing SDK CI as the source of build/runtime/platform/account/
service-capability baselines. Policy selection is complete; evaluating that
effective matrix and mapping assertions/scenarios remain factual work for a
later bounded slice. Missing CI coverage is a gap to improve, not an exclusion
from scope. Implementing fixtures, changing SDK tests/pipelines, executing
assessments or enabling merges still requires separate authorization.

**Status discipline:** confirmed direction, proposed controls, inherited Java
observations and pinned .NET source observations are different categories.
The baseline records actual source/configuration and selected assertion text,
not executed tests or approved atomic contracts. All invariant candidates
remain proposed or unresolved. Written requirements are not implemented
controls, and publication or activation is not independent design approval.

## 2. Provenance and the accepted Java checkpoint

### 2.1 Inputs and authority

The supplied Java session design v0.2.1 was read, including scope, architecture,
catalogs, metrics, tests, benchmarks, review, operations and continuation.
The historical v0.2.2 import was compared with that intake. The corrected
v0.2.3 checkpoint and its recovery/source-access records now supersede both
as current authority. The old v0.1 attachment is stale and was not used.

| Input | Reference and limit |
|---|---|
| Current canonical Java design | [v0.2.3, especially sections 16-17 and 19.4](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/suicide-squad-design.md); accepted design/research checkpoint with incomplete Java contract/test closure |
| Current checkpoint provenance | [Research index](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/README.md), [checkpoint validation](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/checkpoint-validation.json) and [source-access boundary](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/source-access.json); project records and pinned source references, not vendored SDK payloads |
| Historical Java import provenance | [Research index](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/README.md) and [import manifest](https://github.com/kushagraThapar/SuicideSquad/blob/a10d3042a61540b907edbe17b710c6294b997a7f/docs/research/java-sdk/import-manifest.json); the old snapshot layout is superseded, not approved for .NET reuse |
| Incomplete Java research | [Report status](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/reports/README.md) and [current recovery wrapper](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/recovery/README.md); unavailable agents did not produce completed reports |
| Parent-authored recovery narrative | [Original receipt under discovery-checkpoint/](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/recovery/discovery-checkpoint/README.md); its bytes match the supplied narrative's digest below. New parent discovery, not a recovered agent report |
| Recovery exports | The [historical package manifest](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/research/java-sdk/recovery/discovery-checkpoint/package-manifest.json) and wrapper preserve the original receipts and their interpretation; no Java cache/export is copied or admitted as .NET evidence |
| Cosmos concepts | `tvaron3/cosmosdb-design-docs@bcfbc786fa5296deebcccd11369efb583e63e48c`; applicable sections consulted, with qualifications in section 12 |

Intake SHA-256 receipts identify exactly which revisions informed this transfer:

| Input | SHA-256 |
|---|---|
| Original supplied Java design v0.2.1 | `53f53195f6da2c04b3511824056d0042d9e8111e90d9459a47254c54c60263f8` |
| Canonical Java design v0.2.2 | `6dab296f3db25bf448bded9ed0079eaf4f76404c94521e700bccc7677716437f` |
| Current canonical Java design v0.2.3 | `6fafb38eec4c84164157f8fdfe441717d4a8e216738699b1d44a359f40f7597f` |
| Supplied parent recovery narrative | `01778dd74cf96b5857804a553a61011841a5a9c840de5013d658565097e06266` |

These are document receipts, not source/test verification. Machine-local
session paths are not long-term authority. The original intake receipts remain
historical; current immutable references do not silently rewrite that intake.

### 2.2 Confirmed checkpoint and activation receipt

| Required coordinator record | Current state |
|---|---|
| Corrected final Java checkpoint commit and design version | Coordinator confirmed v0.2.3 at `5d92106027629ec6c5022a7cd5ef2085014d6973` and the exact remote head |
| Canonical parent-recovery location and provenance | Four unchanged historical discovery receipts under `recovery/discovery-checkpoint/`, interpreted through the current wrapper |
| Java pause / .NET-first priority recorded in the Java handoff | Recorded in Java section 19.4 and requirements R-12/R-13; Java implementation/contract backlog remains paused |
| Explicit remaining Java gaps and accepted checkpoint boundary | Versioned design/research checkpoint accepted; DS-14 contract/test closure and DS-13 design/implementation approval are not complete |
| Explicit .NET design-investigation activation | Received, limited to this read-only source-pinned baseline/inventory/gap draft |

The corrected checkpoint is published in
[#4](https://github.com/kushagraThapar/SuicideSquad/pull/4), open/unmerged at
activation. Its corrected net change is 23 project-authored documentation,
research and provenance files, with no vendored SDK source/build/CI payloads.
The historical [#2](https://github.com/kushagraThapar/SuicideSquad/pull/2) is
superseded and closed/unmerged; `a10d3042...` is historical only. Recovery
receipts are discovery evidence, not instructions to restore source snapshots.

The checkpoint satisfies the handoff gate, not independent design review,
default-branch integration, Java semantic closure or SDK release readiness.
Activation approves neither design nor either PR and grants no merge authority.

## 3. Reuse versus revalidate

| Area | Carry forward | Must be independently established for .NET |
|---|---|---|
| Product scope | Whole-SDK feature/behavior scope; D-01 includes all SDK source across the repository, not just core | Actual APIs, internal workflows, CI wiring, lifecycle and applicable build/artifact combinations without silently excluding source |
| Evidence model | Atomic contracts, independent oracles, bidirectional traceability and distinct verification states | .NET symbols, assertions, runners, candidate artifacts and exact execution receipts |
| Quality policy | Multidimensional evidence; critical gaps cannot be averaged away | Baselines, measurable denominators, tool limits and D-02/D-03 decisions |
| Status and consistency | Full decision key, write ambiguity, session/topology distinctions | Actual producers/handlers, defaults, overrides, safe replay and final error mapping |
| Scenarios | Constrained interactions, critical sequences and database non-guarantees | Effective runtime/platform/account/service-capability cells derived from the existing SDK CI, with both Gateway and Direct |
| Test architecture | User-selected CI-native reuse and strengthening of SDK pipelines/tests, not a parallel verification platform; independent oracles/review retained | Effective build/test discovery and assertion mapping, instrumentation, controllable clocks, fault fidelity and fixture gaps in that CI |
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

All SDK source across the repository is in D-01 scope, including companion
packages and staged/preview projects. Their contracts need separately identified
lanes and candidate-bound denominators, not silent exclusion. Encryption discovery
must go beyond policy/key metadata to key resolution, rotation/rewrap/caching,
serialization/query/operation combinations, errors and privacy. Actual .NET
package declarations are observed at the historical intake pin; effective CI/
artifact applicability, atomic contracts and denominators remain incomplete.
The matrix adds distinct .NET lanes for LINQ, preview distributed
transactions/inference, the two encryption
packages and FaultInjection rather than forcing everything into Java seeds.
Connectors/frameworks are consumers or separately scoped products, not
automatically part of the client denominator.

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

The architecture is **CI-native**: reuse and strengthen the .NET SDK's existing
pipelines and their tests so future agent-authored PRs can obtain correctness
evidence through those pipelines, not a parallel verification platform.
The assurance goals still span deterministic unit/property checks, stateful
client/transport faults, emulator integration, required live service validation,
concurrency/stress/soak, and compatibility/performance. D-01 selects the existing
CI baseline, not a new runner/tool stack or approval of its current sufficiency.
The linked baseline records historical declarations and selected assertion text,
not evaluated discovery or execution. Later authorized work must map all
features/scenarios/behaviors and the nine-dimensional vector to actual CI
assertions and improve gaps there. Green current CI alone does not establish
complete correctness or replace independent PR Review Router judgment.

The later design must specify:

- Exact setup/build/test discovery, logical and parameter-case identities,
  effective configuration/platform/account/service-capability cells from the
  existing SDK CI, both connectivity modes, dependencies and expected results.
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

The accepted Java checkpoint retains these gaps without completing every
Java contract first. Pausing Java preserves its backlog; it does not mark
DS-14 or design approval complete.

### Consequential leads to carry as discovery prompts

| Java lead | .NET revalidation question, not an inherited .NET finding |
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
breadth and .NET-first-after-checkpoint direction are settled. **D-01's initial
baseline policy is now user-selected; D-02 through D-12 remain open.**
Factual CI/artifact/assertion reconciliation is not an unanswered policy choice.

| ID | .NET-scoped decision and remaining work |
|---|---|
| D-01 | SELECTED: default `main`; all SDK source across the repository; existing SDK CI-derived build/runtime/platform/account/service-capability baselines; Gateway and Direct; strengthen established pipelines/tests. Effective matrix, artifacts and assertion/scenario mapping remain unverified; see the receipt below |
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

### 10.1 User-selected D-01 baseline policy

The user selected this initial policy, relayed by the coordinator on
2026-11-01 UTC. It supersedes the earlier open D-01 wording, not historical
source observations or the remaining eleven decisions.

| Axis | Selected initial policy |
|---|---|
| Source | Use the default `main` branch of `Azure/azure-cosmos-dotnet-v3` to check code, features and bugs |
| Repository/package scope | Include all .NET SDK source files across that repository, not only the core package; retain companion, staged and preview lanes |
| Build, runtime and platform | Derive the baseline variants and runtime/platform matrix from the SDK's existing CI pipelines, not an independently invented matrix |
| Account and service capabilities | Derive baseline account/service-capability cells from those same SDK CI pipelines; evaluate actual configuration and fixtures later |
| Connectivity and dependencies | Include both Gateway and Direct configurations; follow the actual dependency/source and CI wiring at each assessed revision |
| Verification architecture | Reuse and strengthen the established SDK pipelines and tests to cover every feature, scenario, area and behavior; do not build a parallel verification platform |

`52ff1383...` and E-01 through E-28 remain historical intake evidence from
`main`, not a forever-fixed project baseline. For each future assessment,
resolve and record the exact `main`, base, candidate/actual merge-candidate,
CI/configuration and artifact identities before evaluation. Keep those
identities fixed within the run; do not follow a moving ref mid-run or
silently rewrite the old evidence when `main` advances.

Per the user's context, Direct source migration is separate ongoing work
intended to replace the external Direct DLL dependency with in-repository
source. It is not a completed replacement or a SuicideSquad implementation
task. Preserve the observed dependency at each recorded revision and follow
actual CI/artifact wiring as the migration lands; do not copy source here.

Policy selection does not enumerate or evaluate the effective CI matrix.
A later bounded slice must reconcile variants, runtimes/platforms, accounts/
capabilities, Gateway/Direct paths, artifact identities and assertions/scenarios.
Missing or skipped CI coverage is a gap to improve in the existing pipelines/
tests, not an exclusion or proof that green current CI is sufficient.
The nine-dimensional assurance goals, independent oracles and Router-led
review remain unchanged. No SDK test/pipeline edits, execution, CI triggers,
live resources or governance changes are authorized by this decision.

Policy design and baseline-dependent measurements must remain separate.
Designing an assessment does not invent its results; authorizing a bounded
measurement does not authorize implementation or unattended merges. Thresholds
and graduation samples require approval before their corresponding gates run.

## 11. Ordered design-only continuation

1. **Checkpoint and activation receipt: recorded.** Section 2 identifies the
   corrected Java checkpoint, preserved gaps and explicit design-only signal.
   Java remains paused; publication is not design approval.
2. **Historical intake and D-01 policy: recorded.** The
   [baseline](design-baseline.md) preserves the initial main-derived pin and
   distinguishes source declarations, package/preprocessor surfaces, structural counts,
   selected assertions and CI configuration from unmeasured behavior.
   D-01 now selects default main and CI-native baselines. A later bounded slice
   must evaluate the effective existing CI matrix and artifact identities,
   including Gateway/Direct and all repository SDK source; no audit or SDK
   execution is authorized by this update.
3. **First gap draft: recorded; closure remains open.** The
   [whole-SDK matrix](domain-gap-matrix.md) retains all 31 shared navigation
   lanes, adds .NET-specific lanes and marks every atomic candidate proposed.
   Continue history/API/internal-workflow and assertion/scenario reconciliation
   against existing CI only within a subsequent bounded design slice; record
   pipeline/test improvement gaps, not Java denominators or a parallel platform.
4. **Specify and independently validate atomic contracts and oracles.** Resolve conflicts
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
| Context transfer | v0.1.0 persistent; v0.2.0 records the checkpoint/activation; v0.2.1 records the user-selected D-01 policy |
| Final Java checkpoint | v0.2.3 accepted at `5d921060...`; Java paused with explicit incomplete closure |
| .NET-specific investigation | Activated design-only; initial source-pinned baseline/inventory/gap draft recorded |
| D-01 baseline policy | Selected: default main, all repository SDK source, both connectivity modes, existing CI-derived matrices and pipeline/test improvements |
| .NET source/API/configuration/test/CI reconnaissance | E-01 through E-28 remain historical intake evidence; effective current CI/artifact reconciliation incomplete; no new SDK audit or execution |
| .NET atomic contracts and CI assertion/scenario mapping | Proposed/incomplete; selected baseline policy is not contract verification, CI sufficiency or capability qualification |
| D-02 through D-12 | Open; D-01 selects none of their measurement, tooling, governance or qualification policies |
| .NET coverage, mutation, benchmark and performance results | Unmeasured / not run by this contribution |
| .NET design approval / implementation authorization | Not granted |
| Autonomous merging / releases | Not authorized; releases remain separate |

**Stop after publishing this bounded D-01 update and report its paths, versions
and immutable reference to the coordinator.** Do not expand it into exhaustive
closure, SDK execution or implementation without the appropriate next scope
and authorization. On resumption, re-read this gate and current repository
state; do not blindly replay external side effects or treat remembered
progress as durable evidence.

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
The initial one-document contribution is at `d9d02138...`, and the initial
three-document discovery at `2c67e23...`. This D-01 revision changes
only `docs/dotnet/design-handoff.md`, `docs/dotnet/design-baseline.md` and
`docs/dotnet/domain-gap-matrix.md`; no root pointer or Java import is edited.
Documentation verification and the publication commit/PR receipt belong in
[#3](https://github.com/kushagraThapar/SuicideSquad/pull/3), not an invented SDK
test report. The available tool catalog did not expose an `ado` server; no live
Azure DevOps pipeline or approval state was queried. The original source
inspection read pinned Git objects, not vendored payloads or the SDK's different
detached working revision. This follow-up preserves that evidence without new
SDK investigation, execution or an exhaustive CI audit.

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-31 | Transfer the Java design framework, full-domain seeds, unresolved decisions and separately attributed recovery limits into a .NET-specific starting document; pin the historical initial Java import; record the non-vendoring correction; keep corrected final checkpoint and activation pending |
| 0.2.0 | 2026-11-01 | Record the accepted corrected Java v0.2.3 checkpoint, preserved recovery receipts and .NET design-only activation; select the independent .NET source pin; link the initial baseline and whole-SDK gap draft without closing the twelve decisions or authorizing execution/merges |
| 0.2.1 | 2026-11-01 | Record the user-selected D-01 default-main, all-repository SDK source and CI-native baseline policy with Gateway/Direct; preserve historical intake evidence and incomplete factual reconciliation; D-02 through D-12 remain open; no SDK audit, execution or changes |
