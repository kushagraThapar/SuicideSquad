# Suicide Squad: .NET design handoff

[Project scope](../../README.md) |
[Contribution workflow](../../CONTRIBUTING.md) |
[Autonomous-development guidelines](../autonomous-development-guidelines.md)

| Field | Value |
|---|---|
| Document version | 0.2.9 |
| Recorded | 2026-11-01 UTC; original transfer 2026-10-31 |
| Status | SHARED .NET DOCUMENTATION UPDATE ONLY; SDK TESTING WORK SEPARATELY AUTHORIZED; JAVA PAUSED AT ACCEPTED DESIGN/RESEARCH CHECKPOINT |
| Shared standards/process home | [kushagraThapar/SuicideSquad](https://github.com/kushagraThapar/SuicideSquad); SDK-specific authoritative records follow D-04's SDK-docs ownership |
| SDK research target | [Azure/azure-cosmos-dotnet-v3](https://github.com/Azure/azure-cosmos-dotnet-v3) |
| D-01 source and verification policy | User-selected: default `main`, all SDK source across the repository, existing SDK CI-derived baselines, Gateway and Direct; [decision receipt](#101-user-selected-d-01-baseline-policy) |
| D-02 behavioral assurance and spec-first policy | User-approved: preserve comparable existing obligations, prove new/changed behavior, applicable testing evidence for every PR and design/spec before feature/bug implementation; [decision receipt](#102-user-approved-d-02-and-spec-first-requirement) |
| D-03 CI-gate and limit approach | User-approved approach: start with existing SDK CI gates/configured limits, strengthen demonstrated behavioral gaps and require comparable evidence/rationale for new numerical tolerances; values remain unreconciled; [decision receipt](#103-user-approved-d-03-approach) |
| D-04 ownership/layout approach | User-selected: shared rules/spec workflow/templates and cross-SDK process in SuicideSquad; SDK-specific specs, mappings, results and audits in each SDK's docs; exact paths/formats/wiring and migration pending; [decision receipt](#104-user-selected-d-04-ownership-and-layout-approach) |
| D-05 inventory/contract/oracle approach | User-approved approach: whole-SDK reconciliation and explicit dispositions, atomic behavior contracts, versioned authority with independent oracles, preserved disputes and lifecycle states; factual closure pending, exact owners/schema/tools unselected; [decision receipt](#105-user-approved-d-05-approach) |
| D-06 unattended-merge approach | User-approved DESIGN ONLY: eventually qualified ordinary SDK PRs, independent Router approval, exact-candidate unit plus emulator/live evidence and a separate restricted merge identity; no bypass, activation or permission change; [decision receipt](#106-user-approved-d-06-approach) |
| D-07 review approach and Router scope | User-selected: two independent judgments plus independent test challenge, risk expertise and final-candidate reconciliation; add the personal Router's written scope with explicit adaptations, not runtime proof or activation; [receipt](#107-user-selected-d-07-approach-and-router-scope-addition) and [scope/provenance](#84-personal-router-scope-adapted-for-the-shared-design) |
| D-08 cross-SDK approach | User-approved DESIGN ONLY: always-visible six-core-SDK matrix (.NET primary, Java, Python, Go, Rust, JS/TS), behavior/risk-dependent evidence depth and bounded Router integration; no completed comparisons, configuration change or execution; [receipt](#108-user-approved-d-08-approach) and [current scope](#87-six-sdk-behavior-comparison-and-bounded-router-integration) |
| D-09 verification-technique approach | User-approved DESIGN ONLY: extend native MSTest/test/coverage/CI, behavior/risk-selected techniques and evidence-based tool admission; named candidates are not adopted versions/adapters or verified fit; no installation, spike, execution or activation; [receipt](#109-user-approved-d-09-approach) and [scope](#61-d-09-verification-techniques-and-admission) |
| Historical .NET intake pin | [`52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8`](https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8); initial main-based discovery, not a forever-fixed project baseline or semantic closure |
| Accepted Java checkpoint | [Design v0.2.3 at 5d92106027629ec6c5022a7cd5ef2085014d6973](https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/suicide-squad-design.md) |
| Current .NET bootstrap records | [Design/baseline v0.1.9](design-baseline.md) and [whole-SDK domain-gap matrix v0.1.9](domain-gap-matrix.md); preserve historical inputs pending controlled SDK-docs migration/indexing |
| Implementation / SDK execution authorization | None for this documentation workstream; separately authorized spec-first SDK testing increment reported by coordinator in [section 11.1](#111-separate-sdk-testing-authorization-context) |
| Release execution, automation and production rollout | Deferred to a separate project |

This document transfers context, not Java implementation facts or approval.
The user chose a **versioned Java design/research checkpoint with explicit
remaining gaps**, not a fully source-verified Java feature/invariant catalog,
as the handoff point before prioritizing .NET. The coordinator confirmed
the corrected Java v0.2.3 checkpoint and initially activated bounded,
**design-only .NET discovery**. A separate SDK testing increment has since
been authorized; this workstream remains documentation-only (section 11.1).
Java is paused with its unresolved backlog.
This is a stable handoff record, not a claim that Java SDK behavior or the .NET
design is complete. The original pending gate remains visible in v0.1.0 history.

The eventual goal remains agents discovering and reproducing SDK bugs,
implementing fixes, running comprehensive validation, receiving independent
PR Review Router-led review, iterating, and merging eligible candidates without
routine human intervention. That goal or policy approval alone grants no
execution, unattended merge, deployment or release authority. The separate
SDK task's authorization is not general autonomy or authority for this workstream.

## 1. Scope, acceptance and boundaries

The initial context transfer is persistent at commit
`d9d02138e7fa72b32bfcc72dd63028d208004297`, and the first source-pinned
baseline/inventory/gap draft at
`2c67e23092a1f1cbcd719a71c6db51114926a31c`; D-01 was recorded at
`fecb6db64817175ef5752ce28b6f8c675196b348`, D-02/spec-first at
`a4af4bcee8b4f931b1e127599ca6fdc719aa2dee`, the D-03 approach at
`ccb094cb3292c5b3135dd57d49eb5b12017d633e`, D-04 ownership at
`3b141f8c82a18d660069627c399ccfc9efc837c0`, D-05 at
`532e2401be02da06becbbc459dd58b78ae9b35d4`, D-06 at
`72e9f57918ed81a38bd750f4a6aca58173877d7b`, D-07 at
`1fef335ecb72e15e75518cffc2d39814c2e6bd13`, and D-08 at
`12c7cc3af87208d46a81b3f066262bcfdd3ceab2`. This bounded follow-up records
the approved D-09 DESIGN-ONLY approach, not a tool spike or execution campaign.
PR7 was open/unmerged at D-08 publication; it is now verified merged. The
fresh D-09 feature branch starts from current SuicideSquad main
`c1c929b5ab437aa3be8c67449a147b81c6ce604e`, not a merged feature branch.
Sections 13.1/13.3/13.4/13.5 preserve publication/source-head/merge distinctions.

Observable acceptance is the exact D-09 user request, approval question,
selected label and design-only conditions, all seven technique/admission
areas in section 6.1, and three open decisions D-10 through D-12. Named tool
candidates are not adopted versions/adapters, supported-matrix proof or
qualification. Preserve exact D-01 through D-08 receipts, the complete
D-07 personal-Router intake/source digests/adaptations, D-08 six-SDK policy
and historical four-open snapshot, frozen evidence and Java freeze. Pending
D-04 details and factual/value/tool-fit gaps remain intact. No SDK/peer
research/review, personal audit, tool installation/spike/execution, A-01/result
import or governance implementation is included; earlier receipts keep their
original counts and authorization limits.

Only the .NET documentation lane is changed: this handoff and its linked
baseline and matrix. This workstream does not modify or execute the .NET
checkout, nor duplicate the separate SDK task. This update performs no new SDK
source/test/pipeline inspection or execution and no exhaustive CI audit. No SDK/reproducer/exporter
code, build, test, coverage, mutation or benchmark is executed. No SDK code,
tests, pipelines, agent definitions, permissions, live resources or Agent merge
settings are changed; no SDK CI is triggered, no agents/reviews are launched
and no merge, deployment or release is authorized.

**Repository layout:** D-04 assigns shared agentic coding standards/rules,
spec-driven workflow/templates and cross-SDK process guidance to SuicideSquad.
SDK-specific specs, invariant/scenario/test mappings, benchmark result records,
historical bug/reproduction/fix/regression evidence and audits belong under
each SDK repository's docs area, using suitable existing conventions.
Executable SDK tests and established pipelines stay in their normal SDK
locations, not copied into docs or SuicideSquad. SDK source remains in the
target repository at the recorded immutable revision, never vendored here.

The existing .NET baseline/gap inputs are bootstrap receipts, not an expanding
SDK catalog in SuicideSquad. Their eventual authoritative SDK-specific home
follows D-04; controlled migration/indexing is follow-up, with exact paths,
formats and integration pending. Preserve published inputs and references:
do not delete, move or rewrite historical evidence in this update. The Java
freeze, recovery receipts and non-vendoring correction remain unchanged.

The whole .NET SDK feature/behavior surface is the design scope from
the beginning, not a retries/deadlines-only pilot. D-01 now selects all SDK
source across `Azure/azure-cosmos-dotnet-v3`, both Gateway and Direct, and
the existing SDK CI as the source of build/runtime/platform/account/
service-capability baselines. Policy selection is complete; evaluating that
effective matrix and mapping assertions/scenarios remain factual work for a
later bounded slice. Missing CI coverage is a gap to improve, not an exclusion
from scope. SDK work requires its own scoped authorization, such as the separate
testing increment recorded in section 11.1; it is not authorized by D-01
or this documentation update. Merge authority remains separate and ungranted.

D-02 makes behavior preservation and prevention of unintended cross-feature
changes the goal, not maximizing percentages or test counts. Every PR needs
applicable testing coverage/evidence. AI coding agents must produce a
change-proportionate design document/specification before implementing any
feature or bug fix; it is not a retrospective PR summary. The selected policies
do not establish implemented gates or approve the three remaining decisions.

D-03 selects existing SDK CI gates and configured limits as the initial
baseline, to be strengthened where the audit demonstrates missing behavioral
protection. It approves an approach, not the effective gates, configured
values, benchmark/resource tolerances or run evidence. Those facts still need
reconciliation; no arbitrary coverage-percentage target is selected.

D-04 selects ownership, not a catalog engine, concrete schema, SDK-side wiring,
approval quorum or enforcement mechanism. Durable SDK-docs result records
must preserve reproducibility, result/configuration identities and appropriately
retained references to large/raw artifacts in the existing CI artifact system,
not an empty list of moving links. Shared rules and SDK records/results need
versioned references; concrete retention/access details remain D-10 work.

D-05 approves the reconciliation/contract/oracle approach in section 10.5,
not a completed inventory, authoritative outcome for any disputed contract,
assertion sufficiency or executed proof. Unknown lifecycle states remain
unresolved, not exclusions. Unresolved affected behavior is ineligible for
autonomous qualification; unrelated well-grounded inventory/test improvements
may proceed within their separately authorized scope. D-05 adds no routine human
sign-off and selects no exact oracle owners/schema/tools or D-07 quorum.

D-06 selects a future qualified ordinary-PR merge model, not permission to
operate it. Independent Router approval, applicable unit plus emulator/live
evidence for the exact actual merge candidate and a separate restricted merge
identity are prerequisites. Current repo/org checks, reviews and CODEOWNERS
remain binding; qualification initially stays non-merging. D-06 itself selected
no exact identities, owners, permission schema, operational implementation or
D-11 graduation scope/criteria. Effective SDK/org policy access is still unresolved
(section 10.6), not inferred from SuicideSquad's documentation merges.

D-07 now selects the independent review approach and adds the personal Router's
written scope through the shared mapping/provenance/adaptations in sections
8.4-8.6. Two independent Router-led judgments plus a separate test challenger
must explicitly pass for ordinary SDK implementation/test/CI changes, with
applicable higher-risk expertise and final-candidate reconciliation. This is
not runtime implementation, automatic adoption of personal routing values or
selection of exact identities/tools/budgets. No routine human sign-off is added
to the future target; existing review/posting/protection requirements remain.

D-08 extends the current always-visible matrix to six core SDKs: .NET
(primary), Java, Python, Go, Rust and JavaScript/TypeScript. JS/TS was
previously conditional; this is a deliberate new scope decision, not a claim
that personal routing already registers it. Depth follows changed atomic
behavior, preservation neighbors and risk, not line-for-line comparison or
automatic all-peer builds. Section 8.7 records evidence, dispositions and
bounded integration; exact mappings, actual comparisons and qualification
remain unverified. D-09 tooling/runtime fit and D-10 execution/resource/live
scope remain unselected; .NET paired testing and D-05 authority are unchanged.

D-09 now selects the native-CI verification-technique and admission approach
in section 6.1, not exact tool versions, adapters or compatibility closure.
Retain the existing coverage path initially; evaluate Stryker.NET first for
mutation, FsCheck for suitable properties/models, selective Coyote only after
fit proof, and qualify/extend the existing SharpFuzz path. No candidate mention
is adoption, exclusion or qualification. Historical D-07/D-08 references to
then-unselected tooling and earlier open counts remain intact; actual runtime/
tool fit is still unclosed. No installation, spike or execution is authorized.

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
| Quality policy | Approved D-02 behavioral nonregression for comparable obligations plus complete applicable evidence for new/changed behavior; metrics support that goal; D-03 starts with existing CI gates/configured limits, strengthened for demonstrated gaps | Honest full-candidate comparisons/debt, assertion sufficiency, tool limits, effective gate/value reconciliation and comparable evidence/rationale for new numerical tolerances |
| Change workflow | Agent-authored design/spec and test plan before any feature/bug implementation; every PR needs applicable testing evidence | Actual feature/bug specs in SDK docs, guided by versioned shared rules/templates; concrete affected/interacting obligations and meaningful CI assertions; exact paths/formats/wiring pending |
| Documentation ownership | D-04: shared agentic standards/spec workflow/process in SuicideSquad; SDK-specific records/results in each SDK's docs, normal tests/pipelines stay in place | Suitable SDK conventions, native CI formats plus minimal missing traceability, versioned cross-references, durable result identities and controlled bootstrap migration/indexing; no duplicate test database or pipeline definition |
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

Under the [approved D-05 approach](#105-user-approved-d-05-approach), at an
immutable .NET baseline reconcile the entire changelog history, including
beta/hotfix and Other Changes, with current public APIs/options/configuration,
internal workflows, capabilities, protocol paths, companion history, historical
bugs, existing tests and CI. The 37 lanes are navigation, not a completeness claim.
Preserve nested changes and repeated entries with their source spans. One
changelog bullet can create several semantic obligations.

Each semantic obligation needs a stable record, source/version/span, lifecycle,
classification, affected behavior and atomic invariant, or an explicit
disposition. Preserve supported, preview, deprecated, removed,
unsupported and unresolved lifecycle states with versioned rationale; unknown
never silently becomes unsupported or an exclusion. Reconcile both directions:
history to current contracts and current source to history/specification or
an explicit history gap. Dependency and documentation changes can expose
compatibility or behavioral obligations. Neither file enumeration nor lexical
family classification proves semantic closure.

Each atomic invariant must identify preconditions/configuration, event sequence,
allowed and forbidden observable outcomes, interacting features, safety versus
bounded liveness, an independent oracle, contract authority, scenarios, actual
assertions and exact execution evidence. Cover positive, negative, boundary and applicable
concurrency cases. An implementation observation can itself be a bug; resolve
conflicting code, tests, documentation/specification, issue and service claims
explicitly. Preserve each claim's version/provenance and the resolution rationale,
rather than changing expectations merely to obtain green CI.

Ground expected results in attributable versioned contracts/specifications,
supported by appropriate independent reference/mathematical models, golden
vectors, properties or verified service fixtures. The current implementation
and existing tests are evidence, not automatically correctness authority.
Hardcoded expectations that merely restate the implementation are not independent
correctness evidence. Unresolved affected behavior remains ineligible for
autonomous qualification, without blocking unrelated well-grounded inventory/
test improvements in authorized scopes. Exact oracle owners/schema/tools remain
unselected; factual closure is not established by this approach.
Cross-cutting obligations include request/option propagation, mutable-state
isolation, version-scoped token algebra, one logical terminal result and
diagnostic lifecycle, explicit failures and bounded resource ownership.

Required traceability is:

```text
change intent -> pre-implementation design/spec and test plan -> implementation
feature -> behavior -> atomic invariant -> applicable scenario -> test/assertion
        -> exact execution/evidence -> independent Router review
        -> restricted merge receipt
issue -> affected revision -> behavioral regression -> invariant
```

The design/spec links intended behavior, affected/interacting invariants,
preservation requirements, edge scenarios and the test plan before
implementation; the second chain traces their eventual proof. Preserve that
ordering and linkage, not just a retrospective PR description. Existing
sufficient assertions can supply proof; a spec alone cannot.

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

## 5. Quality vector and approved behavior-preservation policy

The goal is preserving existing behavior and avoiding unintended cross-feature
regressions when adding features or fixing bugs, not chasing percentages or
test counts. The earlier near-100% line-coverage aspiration is supporting
diagnostic evidence, not an acceptance target by itself or correctness proof.
Retain the full quality vector and track its dimensions separately:

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

**D-02 is user-approved:** preserve assurance for comparable existing
obligations and require complete applicable evidence for new or changed
behavior, including potentially interacting features. Unaffected or already
saturated dimensions may remain equal; equality is not a numerical increase.
No gain elsewhere can offset a critical regression. Unproven affected behavior
remains ineligible, regardless of a green aggregate percentage.

Every PR requires applicable testing coverage/evidence. Existing sufficient
tests can supply that proof; no artificial quota of new tests or
documentation-only/no-test waiver is authorized. The required design/spec and
test plan precede implementation, as recorded in section 10.2. This is approved
policy, not a claim that the SDK CI already enforces it.

Preserve both frozen old obligations and the honest full candidate denominator.
Classify retained, added, modified, retired and newly discovered obligations.
Report full candidate counts and newly discovered debt honestly, including
discovery-only score drops; discovery is neither hidden nor described as
numerical improvement. N/A and empty cohorts need explicit truthful
dispositions, not a fabricated 100% or testing waiver. Discovery cannot qualify
newly unproven affected behavior for merging. Legitimate retirement or
intentional contract changes still require the protected D-12 process, not
removal of inconvenient obligations/tests or self-approval in a spec.

For mutation accounting, preserve the proposed Java design distinction:
`K` killed by the expected assertion, `S` survived, `U` uncovered, `T`
inconclusive/timeout, `X` invalid and `E` independently approved equivalent.
The proposed completed-cohort score is `K / (K + S + U + T)` after auditable
`X`/`E` exclusions, with raw counts retained. Unexecuted planned cases mean
incomplete; infrastructure errors invalidate a run; timeout is not a kill.
Sampling is not a full-SDK score, and the repair agent cannot approve its own
equivalence exclusions. D-02 does not select this proposed mutation formula,
.NET tooling, numeric thresholds, tolerances or review quorum.

Under the approved [D-03 approach](#103-user-approved-d-03-approach), reuse
existing SDK CI gates and configured limits as the initial baseline, and
strengthen them where the audit demonstrates missing behavioral protection.
Any new numerical tolerance needs comparable evidence and an explicit
rationale; no arbitrary coverage-percentage target or Java retry/time default
is adopted. Effective gates, configured values, benchmark/resource tolerances
and run evidence still need reconciliation, not assumed approval.
Additional agent/cost budgets and operational details remain D-10 work.
Approved exclusions need exact scope, evidence, owner and expiry; an
unreachable fault path is a fixture gap, not an automatic exclusion.

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

For every feature or bug fix, AI coding agents must write the
[pre-implementation design/spec and test plan](#102-user-approved-d-02-and-spec-first-requirement)
before changing implementation. Map preservation, intended changes and
interacting-feature risks to meaningful existing/new assertions in the
established SDK CI. Every PR needs applicable testing evidence; merely adding
tests, citing a percentage or writing a spec does not prove correctness.

Applicable existing checks and spec-required test evidence must pass.
Missing, skipped or inconclusive required evidence cannot count as success.
Added regression checks become permanent behavioral protection, not checks
to weaken for green CI; legitimate changes still need protected D-12 handling.

Shared spec-driven rules/templates remain in SuicideSquad; actual SDK feature/
bug specs and assertion/scenario/result records belong in SDK docs under D-04.
The coordinator relays that A-01 reports Markdown/docs path filters, consistent
with the historical [E-19 witness](design-baseline.md#e-19).
Assurance specs, policy and test mappings under docs must not silently receive
a blanket docs-only bypass. Reconcile this in future existing-CI wiring work;
this is an integration concern, not a filter change, audit import or new run.

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
  affected autonomy, not the obligation. Runs, retries and agent repair must
  have finite bounds; first failures remain visible and exhaustion is
  blocked/inconclusive, never passing. D-03 does not invent their values;
  additional agent/cost budgets and operational details remain D-10.
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

### 6.1 D-09 verification techniques and admission

The [approved D-09 receipt](#109-user-approved-d-09-approach) selects a
**design-only approach** to strengthening native MSTest/test/coverage/CI,
not a parallel verification platform. Select techniques by applicable behavior
and preservation risk, then qualify actual tools against effective SDK build/
test/package/runtime constraints. Existing declarations are starting evidence,
not integration or supported-matrix proof. Exact versions/adapters/fit remain
pending; no installation, spike, retargeting or execution follows from this
decision.

| Area | Approved approach and admission boundary |
|---|---|
| 1. Native integration and risk selection | Extend existing MSTest/test/coverage/CI rather than create a separate platform. Select techniques by applicable behavior and preservation risk, then establish actual compatibility with effective SDK build/test/package/runtime constraints. A project/package declaration alone does not establish integration, test discovery or supported-matrix coverage |
| 2. Coverage and compiled-code scope | Retain the existing Coverlet/Cobertura/ReportGenerator path initially. Reconcile full applicable compiled-code denominators, including never-loaded code, exclusions and GA/preview/configuration distinctions; bind results to actual tested assemblies. Packaged Direct, staged Direct source, companion and native/artifact boundaries cannot silently disappear or become automatic exclusions. Instrumentation limits remain explicit gaps, not fabricated coverage |
| 3. Mutation candidate and distinct outcomes | Stryker.NET is the first candidate to evaluate, not a selected version or verified integration. Initially focus affected behavior and preservation neighbors. Preserve assertion-detected, survived, uncovered, timeout, invalid-mutant and tool-error outcomes separately; a native headline score is not qualification. Tool errors, timeouts and omitted proof are not relabeled behavioral detection. This selects neither the proposed section 5 mutation formula nor an equivalence exclusion or numerical gate |
| 4. Independently grounded properties and models | Generated inputs and operation sequences must use independently approved D-05 properties/reference models, not implementation-derived expected results. FsCheck is a candidate integrated with existing MSTest where suitable, with reproducible seeds, shrinking and permanent regression cases for discovered failures. Do not adopt an unexamined adapter or experimental state-model API; actual integration/compatibility requires evidence |
| 5. Concurrency and bounded schedules | Use explicit synchronization, controlled time and existing fault/test hooks first; use Coyote selectively only after compatibility proof. Preserve/replay schedules for cancellation, disposal, shared-state races and progress. Bounded systematic exploration is neither formal verification/race-freedom proof nor proof for uncontrolled transport/service execution; identify the actually controlled boundary |
| 6. Existing fuzz path and replay | Qualify/extend the existing SharpFuzz path, not a duplicate facility. Record actual entrypoints, meaningful failure oracles, corpus provenance and replay. A net10 fuzz project declaration is not executed/registered CI proof. Effective instrumented assemblies, runner/runtime/dependencies, corpus suitability and applicability remain to be established |
| 7. Tool admission, evidence and shipping isolation | Pin versions and prove a representative unmodified baseline, intentional relevant-defect detection and reproducible failure replay before admitting actual tooling. Verify effective runner/runtime/configuration/symbol/dependency/loaded-artifact identities, not merely installation. Reconcile expected/discovered/executed terminal cases; retain mutant details, counterexamples and schedules through existing SDK/CI records. Incomplete instrumentation, unsupported boundaries and exhausted runs remain explicit gaps. Keep dependencies/instrumentation test-only: no rewritten test assemblies or third-party testing types in shipped customer artifacts/APIs. No technique or tool score substitutes for required behavioral proof |

These techniques do not replace paired unit plus
emulator/authorized-isolated-live proof, existing API/package/performance checks,
D-07 independence or D-08's six-SDK comparisons. Injection evidence must name its layer: a policy/helper
test does not establish Gateway/backend effects. Controlled time/schedules or
client hooks prove only the boundaries actually exercised, not service fidelity.

D-03 existing/reconciled gates and finite attempts remain binding, with
separate failures and missing proof visible rather than converted to success.
D-04 exact formats/wiring/migration, D-05 independent authority, D-10 numerical
budgets/retention/resources, D-11 graduation and D-12 intentional changes remain
distinct and unclosed. Candidate mention supplies neither an exclusion nor
qualification. No numerical results, compatibility proof, implementation or
whole-design closure is asserted here.

### 6.2 D-09 grounding and unresolved tool fit

The coordinator reports consulting the existing D-08
[baseline topology](design-baseline.md#3-observed-project-package-and-framework-topology)
and [test/CI observations](design-baseline.md#7-test-coverage-and-ci-arrangements-observed-read-only),
plus bounded A-01 excerpts during the approval discussion. This workstream
reads only the existing shared records; it does not inspect/import A-01 or
evolving SDK results, refresh SDK source or duplicate that investigation.
The historical declarations remain frozen evidence, not proof of current
runner or artifact fit.

The following are **coordinator-reported public-document reads on
2026-11-01**, not new source/tool audits by this workstream. Public pages may
change; no exact tool version, adapter, maintenance state or licensing/fit
closure follows from these bounded observations.

| Official source reported read | Grounding and unresolved boundary |
|---|---|
| [Stryker.NET getting started](https://stryker-mutator.io/docs/stryker-net/getting-started/) | The current documented tool requires a .NET 10-or-newer tool runtime, explicitly not a .NET 10 application target. This does not establish compatibility with the SDK's effective runner/runtime; do not silently retarget SDK/test projects or treat the historical declarations as satisfied installation/runtime prerequisites |
| [FsCheck documentation](https://fscheck.github.io/FsCheck/) | Describes properties/shrinking, an experimental model-based API and community MSTest integrations. This is candidate technique/integration context, not approval of any adapter or experimental state-model API, an independent oracle or actual SDK integration |
| [Coyote documentation](https://microsoft.github.io/coyote/) | Describes systematic testing/binary rewriting and explicitly not formal verification. Selective use still needs compatibility proof, controlled-boundary identification and test-only shipping isolation; it does not prove uncontrolled transport/service behavior or race freedom |

The coordinator reports that a Coyote overview URL returned HTTP 404 and the
GitHub repository maintenance read was blocked by Microsoft-org SAML SSO.
Requested sign-in could not replace the session-provided credential; no
credential substitution or configuration change occurred. Those access limits
leave maintenance unverified, not absent or clean. The public docs do not close
maintenance, licensing or actual runtime integration. This task performs no
new maintenance lookup, authentication workaround or tool trial.

The canonical concept clone was synchronized and
[chapter 17 section 1](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview)
consulted at `bcfbc786fa5296deebcccd11369efb583e63e48c` for distinct SDK and
gateway/backend surfaces. It grounds layer attribution, not individual .NET/
peer contracts or a claim that policy/helper injection reaches the backend.
Section 12's qualifications remain unchanged.

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

The reusable responsibility flow is inventory/contracts -> pre-implementation
design/spec and test plan -> implementation/tests -> trusted execution ->
immutable evidence -> independent Router judgment -> repair/new candidate
(update the spec before revised implementation) -> final eligibility ->
restricted merge executor -> receipt.
Prefer mature existing primitives and minimal adapters, not a new service for
every responsibility.

PR reviews/re-reviews must enter through PR Review Router, optionally via the
routing-only Squad wrapper. Specialists are Router-coordinated, never
replacement primary reviewers. Semantic mergeability belongs to independent
Router-led judgment. Under the [approved D-06 design](#106-user-approved-d-06-approach),
qualified ordinary SDK PRs may eventually merge without routine human review
only with independent Router-led approval, applicable unit plus emulator or
authorized-live evidence bound to the exact actual merge candidate, and a
restricted merge identity separate from the implementation agent. That identity
cannot approve semantics, weaken its own eligibility rules or bypass repository
protections. Existing repo/org required checks/reviews/CODEOWNERS remain binding
until explicitly authorized compatible governance changes; internal receipts
do not manufacture qualifying approval identities.

The existing local Router is not already an autonomous merge system. Its
current human approval/posting boundary remains intact; D-06 design approval
does not activate auto-merge or remove existing requirements. Qualification
initially stays non-merging, with graduation scope/criteria still D-11.
The [selected D-07 approach](#107-user-selected-d-07-approach-and-router-scope-addition)
requires **two independent Router-led judgments plus a separate independent
test challenger** for ordinary SDK implementation/test/CI changes. One judgment
owns correctness/contracts, the other preservation/interactions; the challenger
independently challenges the test protection and its evidence. All required
roles must explicitly pass. Majority override, empty-findings approval and
reviewer-shopping cannot qualify a candidate.

Initial review contexts are separate from implementation and from each other
until first reports are recorded. Verified versioned contracts, source and raw
evidence may be shared; another agent's conclusion is not an independent
judgment. Model diversity alone is not independence. Many nested specialists,
two reports by one identity or a read-only test-plan artifact do not manufacture
independent quorum, executed challenge evidence or GitHub approvals.

Higher risk adds applicable security, concurrency/performance, domain and
CI/shipped-artifact expertise. The author cannot downgrade its own tier;
assurance specs/mappings/gates cannot hide behind docs-only handling.
The current personal Router's specialist strategies are scope inputs, not a
replacement for these minimum roles or a requirement to run every specialist
or duplicate CI for every change. Section 8.4 retains the D-07 written-scope
mapping; sections 8.5-8.6 preserve its provenance and adaptation limits.
Current D-08 peer scope and integration are in section 8.7.

D-07 adds no routine human sign-off to the future qualified ordinary-PR target
and selects no exact models/providers/apps/GitHub identities, budgets or tool
implementation. Repository-owned protocol and policy/prompt/model/tool
provenance still require protected integration and validation. No reviews or
agents are run by this handoff, and no existing posting/review rule is removed.

Under the [approved D-08 approach](#108-user-approved-d-08-approach), cross-SDK
review always shows .NET (primary), Java, Python, Go, Rust and
JavaScript/TypeScript; add Spark/Kafka/Spring/other consumers when affected.
Compare behavior and preservation neighbors at risk-dependent depth, not every
line or every SDK build. Each cell needs applicability, pinned evidence,
rationale and eligibility impact with distinct dispositions (section 8.7).
Bounded Router integration must not silently omit required peers. New
customer-facing exposure of third-party implementation types remains a blocker;
legitimate existing public dependencies are baseline contracts, not implicitly
removed.

Sections 8.4-8.6 remain byte-for-byte D-07 intake history. Their five-SDK minimum
and references to then-open D-08 reflect that publication, not the current
six-SDK policy. Section 8.7 deliberately extends project scope while retaining
those receipts. No personal peer-map edit or existing JS/TS registration is
claimed; the narrower personal defaults/cap cannot define qualification scope.

### 8.2 Candidate-bound evidence and failure behavior

Evidence must link the pre-implementation spec/test plan, its obligations and
the resulting implementation/assertions/execution, preserving their order
rather than substituting a later PR summary. It must bind repository/PR,
base/head/actual merge-candidate identity,
production artifacts, environment, runner/tools, configuration, policy/catalog
and cohort digests, expected/discovered/executed test cases, raw vector/results,
missing or inconclusive checks, red/green proof, reviewer identities/roles,
findings/dispositions and trusted provenance.

Required outcomes include `eligible`, `changes_required`, `blocked`,
`needs_contract_decision` and `rejected`. Missing reviewer/results/context,
malformed or stale receipts, wrong SHA/artifact, lost shard, weak test discovery,
unresolved oracle or supported blocker, policy weakening and exhausted budgets
cannot yield eligibility. The author cannot close its own supported blocker;
fixes and refutations require independent verification. Dissent and earlier
failures persist with their dispositions. Majority vote and an empty findings
array are not approval evidence; optional suggestions remain nonblocking.
Findings are fixed with evidence, independently refuted, or routed through
protected contract change; blocking safety work cannot be deferred into approval.

Fixes, rebase, new commits, conflicts, base/queue composition and policy/catalog
changes invalidate affected evidence. Final reconciliation must bind the actual
merge candidate and all required findings, roles and evidence through a race-safe
process. Missing required reviewers/proof, unresolved affected contracts or
stale/incompatible evidence block qualification, not just lower a report's
confidence. Reconcile an ambiguous external response
before retrying a merge or other side effect. Repository/org review rules,
CODEOWNERS and qualifying identities remain prerequisites; internal receipts
do not manufacture GitHub approval identities.

GitHub's ability to accept skipped or neutral checks is not sufficient behavioral
proof. Required evidence must actually cover the applicable discovered/executed
cases and cohorts with matching candidate/configuration/artifact identities;
missing, stale, skipped or inconclusive required evidence blocks merging.
D-06 preserves these fail-closed requirements, not a platform-status shortcut.

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
permission change or release is authorized here. In the D-06 design, authorized
policy owners can suspend the future capability; their exact identities remain
unselected, as do the D-10 stop/budget/recovery implementation details.

### 8.4 Personal Router scope adapted for the shared design

The user explicitly requested the personal Router's current scope in the .NET
review design. The coordinator supplied a direct-read intake of the written/
configured protocol; this workstream distills that intake rather than auditing
the personal setup again. The scope below is usable as shared process guidance
without a contributor's personal-home installation. It is **not** proof that
runtime dispatch, specialist installation, source access, CI or qualification
works. No PR was reviewed and no agents were dispatched.

The source protocol and the selected D-07 eligibility requirements are distinct.
The former supplies review coverage, context and evidence practices; the latter
requires independent roles and complete applicable proof even when a personal
advisory strategy would produce a smaller or degraded report. Read the scope
with the explicit discrepancies in section 8.6, not as wholesale adoption of
personal heuristics, caps, overrides or storage/tool choices.

| Area | Distilled written Router scope and .NET design application |
|---|---|
| 1. Thin orchestration and candidate intake | Router normalizes repository/PR, detects SDK/affected surfaces and explains risk; it routes, assembles context, merges and reconciles findings while specialists review code. The optional Squad wrapper is routing-only; Router remains the sole PR-review orchestrator. Build one coherent cached PR metadata/files/diff snapshot per candidate and refresh for a changed actual candidate, not a stale lifecycle-wide cache |
| 2. Strategies and SDK-aware risk | Retain Triage/Standard/Deep strategies and routing for API, retry, auth, serialization, query, diagnostics, transport, dependencies and security-adjacent build/release/package surfaces. Distinguish source/tests/docs/build/generated/noise without silently skipping shipping generated/public contracts, manifests, migrations, baselines or security. Preserve strategy/scope, not every personal heuristic score, numerical cap, tier override or docs/test force rule as a qualification value |
| 3. Specialist family and composition | The written family is Tier1 Fresh Eyes; Tier2 PR Deep, Engineering Quality, PR Test Model and Skeptic Lens, with conditional CI Artifact and Security; Tier3 adds cosmos-pr-reviewer when Cosmos-domain surfaces match, with Interactive Deep only when explicitly requested. Review Quality Gate follows merged findings. PR Deep may coordinate Past Review, Past PR Investigator, Review Context Builder, Fresh Eyes and Cross SDK; Cross SDK receives explicit peer scope and returns verified comparisons. All stay Router-coordinated. Domain ownership/scope filters avoid duplicate full-stack work; preserve specialist obligations without all specialists or duplicate CI on every change. This composition does not itself satisfy D-07 independence or create qualifying GitHub identities |
| 4. Correctness, API and published surfaces | Examine prior behavior/history, callers/callees, related tests/specs, null/default consistency, async/cancellation/default compatibility, diagnostics/error preservation and customer-facing API/shipped-surface compatibility. Newly introduced third-party type leakage is a BLOCKER across all customer-reachable published artifacts, including optional companions/adapters. Compare base/head; do not silently remove legitimate preexisting public contracts |
| 5. Engineering Quality | Retain rubric D1/D2/D3/D5 with cross-cutting D6 verification: observability/supportability/debuggability, API hygiene, complexity and allocation; actual changed-path, failure, boundary, concurrency, deterministic and red-before/green-after regression coverage; hot-path/lock/async/backpressure/payload/allocation costs and applicable comparable benchmark evidence. Agentic readiness has five explicit dimensions: streaming/async for LLM consumers; structured I/O contracts; documented idempotency/safe-retry contracts; machine-readable observability; tool-callable public APIs. Other selected assurances, such as deadlines, retain their own obligations; do not silently expand these five dimensions or select numeric scores/thresholds |
| 6. PR Test Model and independent challenge | Its dedicated READ-ONLY artifact inventories practical existing file:test/assertion evidence for changed behaviors/paths, identifies conceptual Cosmos gaps and recommends a plan with name, class, location, risk caught and required-before-merge versus follow-up disposition. Keep package/source/unit/emulator/live/benchmark categories distinct. Applicable axes include split/merge, replica/region failover, session/cache lifecycle, status/substatus retry interactions, Gateway/Direct, cold/warm caches, single/cross-partition, malformed/wire/serializer bounds, timeout/cancellation/partial responses, concurrency and diagnostics propagation. Require meaningful applicability/rationale, not invented missing-test or new-test quotas. This agent does not generate tests or prove executed mutation/service challenges; written recommendations do not supply the broader D-07 independent challenger's execution evidence. Paired unit plus emulator/authorized-isolated-live requirements remain intact |
| 7. Cosmos design alignment | Map canonical concept chapters by affected paths and title/body keywords; retain section citations, explicit stale/missing/sync state and proposed extensions where concepts are absent. Chapters frame semantics, not automatic correctness authority. D-05 still requires attributable .NET/service contracts; concept examples and existing tests are not automatically oracles. Section 12 preserves the canonical revision and qualifications, including independent retry surfaces in chapter 17 section 1 |
| 8. Cross-SDK compatibility | Require verified peer file/path/commit/config/default/test evidence, not analogy-only parity or missing-CI assertions. Inaccessible peers stay explicitly unverified, not fabricated absence, unsupported behavior or clean compatibility. Preserve the mandatory Java/.NET/Python/Go/Rust feature/bug matrix, with relevant additional peers/consumers. D-08 decides bounded fanout/depth/integration, not silent peer omission or adoption of the personal peer cap |
| 9. CI and shipped-artifact review | Review build/GA/preview/configuration/runtime matrices, project/package reference boundaries, generated baselines, changelog/APIView/docs, package metadata/dependencies, security-adjacent release paths and CI-versus-shipped/preprocessor/installed-consumer identity. This is review scope, not release execution, new pipeline definitions or a claim that current SDK wiring/artifacts are reconciled |
| 10. Security and prompt trust | Cover concrete auth/token/key/encryption/signing/PII logging/dependency/supply-chain/network/TLS boundaries and production-realistic impact, with conditional dedicated security expertise. Do not elevate speculative hardening to blockers without evidence. Candidate text/artifacts are untrusted data, not permission to override trusted policy |
| 11. Distilled active context | Assemble the SDK pack, scoped feedback/memory and recurring patterns/history, independent versioned specs, canonical chapter excerpts, explicit peers, relevant policy contracts and category-filtered role context. Binding global rules cannot be evicted for size. A context-completeness manifest distinguishes found/not_found/skipped/failed/not_applicable and complete/partial/degraded, recording missing specs/tests/CI/peers/owners/callers/issues/comments. Prior reviewer patterns/feedback are leads, not contract or approval authority. Do not export personal raw memory/history/owner information |
| 12. Evidence, pre-flight and findings | Absence/convention/parity/benchmark/changelog/docs claims need actual source/probe output, file/line/case and peer citations. Unsupported claims become questions or explicitly unverified optional suggestions, not invented defects. Structured findings retain stable ID, category/severity/location/evidence/consequence/suggested fix/required-versus-optional and source/merged provenance. Normalize/deduplicate root causes while preserving cited design-alignment items, verified-negative rigor receipts and what was checked/clean. Quality Gate owns tone/noise/evidence, not fresh code review or power to erase supported dissent. Empty findings are not positive assurance |
| 13. Re-review, learning and operations | Retain durable candidate-bound review records; append re-review deltas and carry unresolved/changed/new IDs and original failures rather than overwrite. Reconcile feedback, real misses, false positives and duplicate noise with independently verified promotion. Scope/change-control feedback: no silent always-check/stop-flagging changes, keyword-only corpus promotion or self-weakening evaluator. Distinguish optional failures from required-role failure; no primary fallback to Fresh Eyes. Preserve partial reports/errors and finite budget/stop/recovery boundaries. Values/mechanisms remain D-10, corpus/graduation D-11 and intentional changes D-12 |

This is shared standards/process material under D-04, not a new SDK catalog.
Actual candidate specs, review/test mappings and result records follow SDK-docs
ownership, with existing CI artifacts retained in their native system. No raw
prompts/config, reviewer history, memory JSON, scripts or SDK facts are imported.
Concrete global schemas, storage paths, runtime wiring and qualifying identities
remain unimplemented/unselected; descriptive source fields are not that decision.

### 8.5 Portable Router intake source receipts

These are **coordinator-supplied direct-read receipts**, not independently
byte-verified by this documentation workstream. The coordinator reports
`PR Review Router.agent.md` as 443 lines / 46,059 bytes, with the same digest
across its reads. `router-design.md` calls itself v3.2 and is not perfectly
consistent with the newer entrypoint. Portable filenames and the supplied
locators below identify the intake; no personal path, owner identity or
installation is a prerequisite for contributors.

| Portable filename | Supplied locator / scope use | SHA-256 |
|---|---|---|
| `PR Review Router.agent.md` | Stages 0-10 and hard rules; written orchestration/review protocol | `1e6d6edab0463622843be838e941ea8e777845f5ee5b1a92e14e6579a3e8e792` |
| `router-design.md` | v3.2 design/history; discrepancies retained in section 8.6 | `056ef7e75d3bd711e1e27b1aae10540108286324ce0dab7046013c176f47453c` |
| `engineering-quality-rubric.md` | D1-D6 rubric; scope uses D1/D2/D3/D5 and cross-cutting D6 verification | `e5ac978e5dae133e7d414adf4fce2afec37ebdd594b6c0a46b1f5b86df07dbb3` |
| `sdk-packs/dotnet.md` | SDK context/default/path hints, not verified .NET contract facts | `9905624ce811b1fa5b87d7eb8c7d760987c5582b34cdbc690beb61780f8a0185` |
| `cross-sdk-peers.md` | Personal peer configuration; not authority to narrow the required matrix | `1e5ca2fc101a0625a901401494c80b22c3677eaa98c8206104d93e6dd214c23a` |
| `PR Test Model Reviewer.agent.md` | Read-only test inventory/gap/recommended-plan artifact | `a7d1447ed1fcb3d5907ab643df4afed6cb1a133fc878184dc112f067a06053cd` |
| `prompt-trust-boundaries.md` | Candidate content versus trusted policy boundary | `02c0708d952c4acc78cb3c83291eaec9e75158795280ca2bc4996a189c0659b2` |
| `diff-filtering-policy.md` | Source/test/docs/build/generated/noise scope filtering | `e82abddf1ded7cca45e600fe8139594c0240cc7ac08d3a836140ecec0b1cfff6` |
| `comment-quality-gate.md` | Finding quality, tone, evidence and noise | `3c144b775f3144abce65895989902947d3378c2c831704083b0c0f9497cdbb71` |
| `reviewability-confidence-policy.md` | Reviewability/context/confidence and degraded-advisory limits | `69261183a95435b9e53f6f2a4b1d9db13edef13c31746722ef24ff47c6b630ba` |
| `agent-operations-policy.md` | Bounded operations, partial reports and failure handling | `1d2724d7857b3df583c3041fca372baee64566e2d228ac7173f3adf7a1a39699` |
| `security-routing-policy.md` | Conditional security scope/routing | `92d34d444fb2ff969dd1acdc27a7a174a05630712d7983513a1b2703598493e0` |
| `reconciliation-workflow.md` | Re-review/feedback reconciliation and promotion boundaries | `10de21687f0c542b57705cdc61c77829593c16a756495920d3ec762c5c43d6dd` |

Other resources named by those files, including industry guidance/map/schema,
raw memory and helper internals, were references, not independently audited or
imported inputs. Neither those references nor these digests prove runnable
completeness, specialist availability or an executed review/test outcome.
No fresh personal-source audit, SDK investigation or test run is performed here.

### 8.6 Explicit source discrepancies and adaptation boundaries

Preserve these differences rather than silently promoting personal advisory
configuration into protected .NET eligibility:

| Boundary | Supplied current/older source observation | Shared-design adaptation |
|---|---|---|
| A. Routing is not eligibility | Entrypoint labels, user `--tier` and all-doc/all-doc-plus-test force-Tier1 handling are personal advisory routing. The older v3.2 risk table even lists YAML as force-Tier1, while the newer entrypoint floors ordinary CI-only changes at Tier2 | Record the inconsistency; do not select weights/overrides or present the sources as consistent. Neither tier labels nor docs/test/CI classification can evade D-07 minimum independent roles/mandatory proof, especially assurance docs/test/CI/gates |
| B. Peer configuration is narrower | The personal .NET peer map defaults to Java/Python, caps peers at 3 and allows peer override replacement | This is sourced configuration, not permission to narrow the mandatory Java/.NET/Python/Go/Rust feature/bug matrix. D-08 fanout/depth/integration remains open; no new cap or omission is selected or disguised as complete |
| C. SDK-pack hints are not authority | The personal .NET pack says default branch `master`, focuses core paths and includes unverified generic test/performance/idempotency/diagnostic hints | Treat them as review leads needing current source/contract validation, not .NET facts/oracles. D-01 still selects default `main`, all repository source and companions, native CI and both transports; D-05 authority and paired-test requirements remain. Do not repeat individual API idempotency hints as universal guarantees |
| D. Advisory degradation is not passing proof | Best-effort stale design context, partial/sub-agent failures, prose parse fallback, unknown-severity-to-minor and absence-claim downgrade may support a labeled advisory report | None creates complete required reviewers/proof, clean compatibility, qualification or approval. Downgrading an unverified defect claim as noise does not resolve separate missing mandatory assurance; that remains blocked |
| E. Current human/file workflow is descriptive | The current human approval-to-POST gate, read-only model, human-verification feedback reconciliation and file sinks describe the personal workflow | This update neither removes nor activates/automates them. Do not impose permanent routine-human approval on the future qualified ordinary-PR target; posting approval is not semantic approval or merge permission. Runtime migration, qualifying identities and protected wiring are unimplemented; exact automated feedback/corpus ownership is unselected |
| F. Scope adoption is not wholesale configuration adoption | Current threshold/cap/count/CLI/path examples and findings schema are personal protocol details that may be described or reused where suitable | Do not select every numerical heuristic, a global SDK-docs schema, provider/tool/budget, D-08 fanout, D-09 tooling, D-10 operations, D-11 graduation or D-12 exception mechanism. Concrete integration needs separate design/authorization; this update changes no personal agent/config or permission |

### 8.7 Six-SDK behavior comparison and bounded Router integration

D-08 selects this **design approach**, not completed peer comparisons, approved
individual contracts or runtime qualification. It extends the historical
five-SDK minimum without rewriting the personal-Router intake or earlier
decisions. JavaScript/TypeScript is now always visible, rather than only an
additional relevant peer. The primary .NET scope still includes all repository
SDK source and companions under D-01, not a stale pack's core-path hints.

| Aspect | Approved approach and evidence boundary |
|---|---|
| 1. Complete visible scope, proportional depth | The required always-visible matrix contains six core SDKs: .NET (primary), Java, Python, Go, Rust and JavaScript/TypeScript. Add Spark/Kafka/Spring/other consumers when affected. Cover changed behaviors at risk-dependent depth, not every line or an automatic rebuild of every SDK for every PR. Explicit SDK/companion/consumer mapping and supported applicability still need verified inputs; do not claim existing personal routing already registers JS/TS. No max-three-peer/default-Java-Python setting or `--peers` override may silently shrink required qualification coverage |
| 2. Compare atomic semantics and preservation neighbors | Compare each changed atomic behavior plus preservation neighbors: applicable contracts, defaults/options, status/substatus/error handling, retry/cancellation, consistency/session, serialization/API and artifact/configuration differences. Match semantic preconditions/outcomes and scope, not identical language implementation shape, APIs or diagnostic output. Retain all-repository .NET/companion scope and the affected interactions, not only changed lines or core paths |
| 3. Pin and classify actual evidence | Pin .NET base/candidate and the actual merge candidate as required by section 8.2, plus each peer's actual repository/revision/configuration. Cite attributable contracts, source and actual test assertions. Distinguish inspected source, written/discovered tests and executed results. Keep branch code versus released package, GA/preview/runtime/transport/fixture and loaded-artifact identity distinct where applicable. A checked-in test or current-main source claim is not proof of released/runtime equivalence |
| 4. Per-cell applicability, disposition and ownership | Each behavior/peer cell records applicability, evidence, rationale and eligibility impact, using equivalent / intentional difference / unsupported / verified gap / unverified. Equivalence is bounded to the named behavior/configuration and evidence, not a universal SDK guarantee. Evidence-backed unsupported/non-applicable or intentional lifecycle/default differences are legitimate; unknown/inaccessible is never silently unsupported, N/A, clean or passing. Preserve actual product ownership of a discovered gap rather than blaming .NET for a peer issue. These are information requirements, not a selected universal SDK-docs schema; D-04 formats remain pending |
| 5. Deepen by behavior and risk | Begin with relevant contracts/source/assertions; deepen as behavior/risk requires. Use common vectors/differential execution where meaningful and needed, and turn useful peer edge cases into .NET regression-test obligations. Do not mandate automatic whole-SDK rebuilds/all-peer test runs, meaningless language diagnostics parity or redundant tests. D-09 tooling/runtime fit and D-10 execution/resource/live scope remain unselected. Peer comparison does not replace .NET's required paired unit plus emulator/authorized-isolated-live proof |
| 6. Bounded Router integration without manufactured independence | Supply the full explicit required peer manifest to Router-coordinated Cross SDK review. Use scoped searches, immutable evidence caches and bounded batches, not duplicated full review pipelines for every peer. Preserve D-07 initial independent judgments; shared verified facts/cache are not another reviewer's conclusion or extra quorum votes. Resource/budget exhaustion yields explicit incomplete cells and blocked required proof, never silent dropping. Numerical concurrency/time/cost/caps remain D-10; no personal cap is adopted as eligibility and no personal map/config changes are performed |
| 7. Contract authority and scoped qualification impact | Peer majority/current implementation is not correctness authority; D-05 approved contracts/oracles remain authoritative. Verified lack of a feature in other SDKs must not block a legitimate well-proven .NET-first feature. Conversely unresolved required comparisons or unjustified affected-contract deviations block autonomous qualification. Scope the impact: an unresolved unrelated peer is not a global prohibition on unrelated work. Missing access is not compatible/unsupported; claims or decisions missing service/oracle/evidence remain unclosed, not averaged away. A peer finding does not authorize changing, executing against, provisioning for or publishing that peer; follow-up needs its own scope |

This update creates no actual behavior/peer result cells or numerical results.
The always-visible manifest requirement does not assert complete repository/
companion/consumer registration or factual CI/artifact reconciliation. Evidence
selection and applicability must be justified rather than replaced by the
personal defaults or by treating an inaccessible peer as absent.

The approval discussion used [chapter 17 section 1](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview)
to distinguish SDK attempts from gateway/backend retry surfaces. The canonical
clone was synchronized and the section consulted at `bcfbc786...`; this is
concept grounding, not approval of individual .NET/peer behavior or new SDK
research. Existing section 12 qualifications remain binding.

No peer review/research, common-vector execution, build/test/CI/live action,
agent dispatch, personal config change or merge is performed by recording the
approach. D-06 qualification initially remains non-merging; D-07 independent
role requirements and final-candidate proof remain intact.

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
Recommendations remain recommendations. Whole-SDK breadth and the
.NET-first-after-checkpoint direction are settled. **D-01 through D-09
approaches are selected; D-10 through D-12 remain open (three
decisions).** D-04 selects ownership, not exact paths/formats/integration or
completed migration. Factual CI/gate/value/artifact/assertion reconciliation
and inventory/contract/oracle/execution closure are not unanswered approach
choices or completed work. D-06 approves a design model, not actual unattended
merging, effective SDK/org policy verification or permission changes. D-07
selects the review approach and Router scope, not runtime dispatch, qualifying
identities, numerical routing values, implementation or activation. D-08
selects six-SDK scope, behavior-focused depth and bounded integration, not
actual peer comparison results, contracts, registration or qualification.
D-09 selects techniques/candidate evaluation and tool admission, not exact
versions/adapters, effective runtime fit, integration or execution approval.

Sections 10.1 through 10.8 retain their published historical receipts, including
their historical open-count/cross-reference wording and authorization limits.
The current queue, D-09 receipt in section 10.9, current scope in section 6.1,
separate SDK context in section 11.1 and documentation merge receipts in
sections 13.1/13.3/13.4/13.5 supersede
current-status readings of those older references; they do not imply later
approvals already existed. D-07 intake sections 8.4-8.6 and D-08 policy/receipt
sections 8.7/10.8 remain byte-for-byte, including the historical four-open
snapshot; the six-SDK comparison requirement stays binding.

| ID | .NET-scoped decision and remaining work |
|---|---|
| D-01 | SELECTED: default `main`; all SDK source across the repository; existing SDK CI-derived build/runtime/platform/account/service-capability baselines; Gateway and Direct; strengthen established pipelines/tests. Effective matrix, artifacts and assertion/scenario mapping remain unverified; see the receipt below |
| D-02 | APPROVED: preserve assurance for comparable existing obligations; complete applicable evidence for new/changed behavior; equality for unaffected/saturated dimensions is allowed but not an increase; report full-candidate counts/debt; no critical-regression offsets or unproven affected behavior. Every PR needs applicable testing evidence; agent-authored design/spec precedes feature/bug implementation; receipt below |
| D-03 | APPROVED APPROACH: existing SDK CI gates/configured limits are the initial baseline; strengthen demonstrated behavioral gaps; new numerical tolerances require comparable evidence/rationale, not arbitrary coverage targets. Required evidence must pass, regression checks remain protection, runs/retries/repair are bounded with visible first failures and blocked/inconclusive exhaustion. Effective gates/values/benchmark/resource tolerances/run evidence still need reconciliation; additional agent/cost budgets and operations remain D-10; receipt below |
| D-04 | SELECTED OWNERSHIP/LAYOUT APPROACH: shared agentic rules, spec workflow/templates and cross-SDK process in SuicideSquad; SDK-specific specs/mappings/results/history/audits in each SDK's docs; normal tests/pipelines stay in place. Prefer existing conventions/CI formats and minimal missing traceability, durable result identities with retained CI artifact references, not duplicate test databases/pipelines. Exact paths/formats/schema/wiring and controlled bootstrap migration/indexing remain pending; receipt below |
| D-05 | APPROVED APPROACH: reconcile whole-SDK APIs/options/workflows/history/bugs/tests/CI with every obligation explicitly disposed; atomic behavior contracts and actual assertions; attributable versioned authority with appropriate independent oracles; preserve/resolve disputes without green-CI expectation changes; explicit versioned lifecycle states, unknown never excluded. Unresolved affected behavior is ineligible for autonomous qualification, not a bar to unrelated well-grounded improvements. Factual inventory/oracle/assertion/execution closure and exact owners/schema/tools remain pending; D-07 review approach now recorded, D-12 changes/retirement remain open; historical receipt below |
| D-06 | APPROVED DESIGN-ONLY APPROACH: eventually qualified ordinary SDK PRs may merge without routine human review only through independent Router approval, applicable unit plus emulator/live evidence bound to the exact actual merge candidate, and a separate restricted identity that cannot bypass protections or weaken its eligibility rules. Missing/stale evidence blocks merging; authorized policy owners can suspend; qualification starts non-merging, graduation D-11. Existing repo/org checks/reviews/CODEOWNERS remain binding pending explicitly authorized compatible changes; identities/apps/permission schemas/owners, D-10 implementation and D-11 scope/criteria unselected; D-07 approach now recorded, no activation, permission change or unattended merge authorized; historical receipt below |
| D-07 | SELECTED APPROACH PLUS USER-DIRECTED ROUTER SCOPE: two independent Router-led judgments for correctness/contracts and preservation/interactions plus a separate independent test challenger for ordinary SDK implementation/test/CI changes; all required roles explicitly pass, separate initial contexts, independent verification of fixes/refutations and retained dissent/failures. Higher-risk expertise and actual-merge-candidate reconciliation apply; no author tier downgrade, docs bypass, reviewer-shopping or missing-proof success. Adopt the supplied written personal-Router scope with provenance/discrepancies, not personal heuristic values, runtime proof, exact identities/tools/budgets or activation; receipt below |
| D-08 | APPROVED DESIGN-ONLY APPROACH: always-visible six-core-SDK matrix (.NET primary, Java, Python, Go, Rust, JS/TS), plus affected consumers; compare changed atomic behavior/preservation neighbors at risk-dependent semantic depth. Pin repositories/revisions/configurations and actual assertion evidence, distinguish written/inspected/executed and source/released/loaded artifacts, give each cell applicability/evidence/rationale/disposition/impact and preserve product ownership. Full explicit peer manifest, scoped searches/immutable caches/bounded batches preserve D-07 independence; exhaustion blocks required proof, never drops peers. D-05 authority, legitimate .NET-first features and scoped qualification impact remain; no personal cap/config adoption, completed matrix, execution or new numerical/tool/live scope; receipt below |
| D-09 | APPROVED DESIGN-ONLY APPROACH: extend native MSTest/test/coverage/CI with behavior/risk-selected techniques and evidence-based tool admission; initially retain Coverlet/Cobertura/ReportGenerator and reconcile full compiled denominators/artifact boundaries. Stryker.NET first mutation candidate, FsCheck properties/models candidate, controlled hooks/time/synchronization before selective compatible Coyote, qualify/extend existing SharpFuzz. Separate outcomes, independent D-05 oracles, reproducible baseline/defect/replay and effective runner/artifact/case identities; test-only dependencies/instrumentation, no shipped testing types/rewritten test assemblies. Paired/API/package/performance/D-07/D-08 proof and injection-layer boundaries remain; exact versions/adapters/compatibility unclosed, no installations/spike/execution/activation; receipt below |
| D-10 | Evidence retention/access/provenance, cost/concurrency, live ownership/capacity/fault isolation, cleanup and outage/stop/recovery procedures |
| D-11 | Historical corpus admission mix, shadow/qualification sample sizes, risk strata, duration, uncertainty and prospective escape criteria |
| D-12 | Protected intentional contract changes, exceptions, obsolete obligations and historical behavior that is itself incorrect |

### 10.1 User-selected D-01 baseline policy

The user selected this initial policy, relayed by the coordinator on
2026-11-01 UTC. It supersedes the earlier open D-01 wording, not historical
source observations. The subsequent D-02 selection and D-03/D-04 approaches
are recorded below; D-05 through D-12 remain open.

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

### 10.2 User-approved D-02 and spec-first requirement

The user accepted the comparable-obligation preservation policy and added
the behavioral and spec-first requirements, relayed by the coordinator on
2026-11-01 UTC: "our aim is to not go after numbers" and "No PR should go in
without testing coverage."

The approved policy preserves assurance for comparable existing obligations,
requires complete applicable evidence for new/changed behavior and permits
equality for unaffected/already-saturated dimensions without calling it an
increase. Report full candidate counts and newly discovered debt honestly;
discovery is not numerical improvement. Gains cannot offset a critical
regression, and unproven affected behavior stays ineligible. Retirements and
intentional contract changes still need the protected D-12 process.

**Before implementing any feature or bug fix, AI coding agents must produce a
design document/specification.** It is proportionate to the change, not a large
RFC for every small fix or a retrospective PR summary. Its minimum is:

| Spec element | Change-proportionate minimum |
|---|---|
| Intended behavior/contract | Observable intended behavior; for a bug, the reproduction and expected correction, without claiming unexecuted red/green proof |
| Impact and interactions | Affected and potentially interacting features/invariants, including cross-feature regression risks |
| Preservation and changes | Behaviors that must remain unchanged and explicit intended changes; disputed/intentional contract changes cannot bypass D-12 |
| Failure/edge scenarios | Relevant negative, boundary, failure and interaction cases needed to distinguish the correction/feature from regressions |
| Test plan | Map these obligations to meaningful existing/new assertions and the established SDK CI; identify missing proof rather than invent results |

Every PR must have applicable testing coverage/evidence. Existing sufficient
tests may provide it; no artificial new-test count or documentation-only/
no-test waiver is approved. A spec neither replaces test evidence nor
self-authorizes an otherwise unapproved contract change.

The full quality vector and honest comparisons remain diagnostic/supporting
evidence for the behavioral goal; no dimension is dropped for convenience.
This decision selects no storage/schema, numerical thresholds/tolerances,
tooling, independent-review quorum, approval identity or new human sign-off
requirement. The later D-03/D-04 approaches are recorded below; D-05 through
D-12 remain open and existing review/permission boundaries remain unchanged.
Approval of this policy is not approval of the overall design or either PR,
nor authorization for SDK implementation, execution or governance changes.

Policy design and baseline-dependent measurements must remain separate.
Designing an assessment does not invent its results; authorizing a bounded
measurement does not authorize implementation or unattended merges. New
numerical tolerances and graduation samples require the applicable evidence,
rationale and approval before their corresponding gates run.

### 10.3 User-approved D-03 approach

The user approved the immediately preceding approach, relayed by the
coordinator on 2026-11-01 UTC: "sounds good, yearh the approach looks good,
let's proceed to D4." This receipt selects the D-03 approach only.
The subsequent D-04 ownership/layout selection is recorded below;
D-05 through D-12 remain open (eight decisions).

| Aspect | Approved approach |
|---|---|
| Initial gates and limits | Reuse the SDK's existing CI gates and configured limits as the initial baseline, not a parallel gate system |
| Behavioral gaps | Strengthen existing CI/tests where the audit demonstrates missing behavioral protection; no arbitrary coverage-percentage targets |
| New numerical tolerances | Require comparable evidence and an explicit rationale; do not invent values or treat this approach approval as value approval |
| Required evidence | Applicable existing checks and spec-required test evidence must pass; missing, skipped or inconclusive required evidence cannot count as success |
| Regression protection | Added regression checks become permanent protection, not checks to weaken for green CI; legitimate changes remain subject to protected D-12 handling |
| Finite attempts and visible failure | Bound runs, retries and agent repair; preserve first failures and per-attempt evidence; exhaustion is blocked/inconclusive rather than passing |

Policy selection is separate from factual/value approval. Effective CI gates,
configured values, benchmark/resource tolerances and actual run evidence still
need reconciliation; none was evaluated or approved by this documentation
update. Historical observed settings remain evidence at their recorded pin.
Additional agent/cost budgets and operational details remain D-10 work.

D-01/D-02, the full quality vector, behavior-first/spec-first requirements and
independent review remain intact. This decision selects no tooling, schemas,
reviewers/quorum, new human sign-off or merge authority. It is not approval of
the overall design or either PR, implemented enforcement, SDK execution or
whole-SDK assurance. The separately reported audit is not imported here.

### 10.4 User-selected D-04 ownership and layout approach

The user selected this ownership approach, relayed by the coordinator on
2026-11-01 UTC: "Makes sense, we should keep the SDK specifics in the SDK
repositories in the docs folders, maybe in a separate folder which has all
the benchmark results, records, historical bug references, their fixes, etc.
And AI agnetic coding standards, rules, spec driven development things in the
suicide squad repository."

| Material | Selected ownership/layout approach |
|---|---|
| Shared agentic process | SuicideSquad owns shared coding standards/rules, spec-driven workflow/templates and cross-SDK process guidance |
| SDK-specific documentation and records | Each SDK repository's docs area owns actual feature/bug specs, invariant/scenario/test mappings, benchmark result records, historical bug references/sanitized reproductions/fix links/regression evidence, and SDK-specific audit/reconciliation records |
| Executable SDK tests and pipelines | Stay in their normal SDK locations; do not copy them into docs or SuicideSquad or duplicate pipeline definitions |
| Results versus large/raw artifacts | Durable SDK-docs records/summaries retain results, reproducibility/configuration identities and appropriately retained artifact references, not an empty moving-link index; large/raw artifacts remain in the existing CI artifact system |
| Formats and traceability | Prefer suitable existing SDK docs conventions and CI report/artifact formats, adding only minimal missing traceability metadata, not a second test database or new catalog engine |
| Shared-to-SDK references | Version shared rules/workflow/templates and SDK records/results; bind relevant revisions and candidate/configuration/result/artifact identities rather than following moving links |
| Current bootstrap material | Preserve published .NET baseline/gap inputs and handoff/research receipts; eventual SDK-specific authority belongs in SDK docs, with controlled migration/indexing as follow-up, not a growing SDK catalog here |

The approach is selected; exact subfolder names/paths, concrete formats/schema,
SDK-side integration/wiring and physical migration remain pending. A dedicated
SDK docs subfolder is possible, not a chosen name or newly created location.
Concrete artifact retention/access remains D-10. No new numerical results or
executed evidence are created by this update.

The coordinator reports A-01 complete and delivered to its Library, with
original SHA-256
`63e368bc66f5c876bb853de62116a9d54ce34f9e1066b5f0b89da8df95b4949c`.
This is a coordinator-supplied identity/status receipt, not a byte audit or
import. The report has not been imported into either repository; its eventual
authoritative home follows SDK-docs ownership. Do not read/import it, duplicate
the SDK investigation, move/delete historical inputs or physically edit the
SDK repository under this assignment. The Java freeze remains unchanged.

The coordinator-relayed Markdown/docs path-filter concern is recorded only
as future existing-CI wiring work, also grounded in historical E-19.
Assurance specs/policy/test mappings under docs must not silently gain a
blanket docs-only bypass. No filters are changed here; applicable D-02 testing
evidence and D-03 gate/failure requirements remain.

D-01/D-02/D-03 and their factual/value gaps are preserved. D-05 through D-12
remain open (eight decisions); choosing D-04 ownership settles neither all
its implementation details nor tooling, reviewers/quorum, new human sign-off,
policy enforcement or merge authority. No overall design approval, physical
migration, audit import, SDK execution or verified whole-SDK assurance follows.

### 10.5 User-approved D-05 approach

The user approved the coordinator's immediately preceding D-05 proposal,
relayed on 2026-11-01 UTC, verbatim:
"On the other hand, I like the D5 approach, let's make progress now with d6."
This selects D-05's approach; it does not select D-06.

| Aspect | Approved approach |
|---|---|
| Whole-SDK reconciliation | Reconcile APIs/options/configuration, internal workflows, full changelog history, historical bugs, existing tests and CI; give every discovered obligation an explicit disposition. The 37 navigation lanes are not a completeness claim or closed denominator |
| Atomic behavior contracts | Identify preconditions, applicable configurations, allowed/forbidden outcomes, interacting features, positive/negative/boundary scenarios and actual assertions; a feature label, executed line or test name is not behavioral proof |
| Expected results and authority | Ground expected results in attributable versioned contracts/specifications supported by appropriate independent reference models, golden vectors, properties or verified service fixtures. Current implementation and existing tests are evidence, not automatically correctness authority |
| Disagreements and eligibility | Preserve and explicitly resolve disagreements among code/tests/documentation/service claims with provenance and rationale; agents cannot obtain green CI simply by changing expectations. Unresolved affected behavior remains ineligible for autonomous qualification without blocking unrelated well-grounded inventory/test improvements within authorized scope |
| Lifecycle and applicability | Preserve supported/preview/deprecated/removed/unsupported/unresolved states and versioned rationale; unknown never silently becomes unsupported or an exclusion |

This is approach approval, not factual inventory, contract/oracle, assertion or
execution closure. E-01 through E-28, all 37 lanes and eight atomic candidates
retain their original evidence depth and proposed/unverified qualifications;
no candidate is promoted by this decision. Disputed expectations do not
self-resolve because code and a test agree.

The approach adds no routine human sign-off and selects no exact oracle
owners, schema or tools. Actual reviewer roles/quorum remain D-07; intentional
changes/retirement remain subject to protected D-12 handling. Existing independent
Router-led review and approval requirements remain; no governance, approval
identity, merge/release authority or implemented enforcement is selected.

D-01/D-02/D-03/D-04 and their factual/value gaps remain intact, including
D-04's pending paths/formats/integration and controlled migration. D-06 through
D-12 remain open (seven decisions). The separately authorized SDK testing
increment in section 11.1 is distinct from this policy approval and docs-only
assignment. This update imports neither its drafts/plan nor A-01 and claims no
completed SDK tests/fixes, executed assurance or overall design approval.

### 10.6 User-approved D-06 approach

The coordinator relayed the main-session `ask_user` decision on 2026-11-01 UTC.
Its prompt explicitly described the model below and stated that approval records
the **DESIGN ONLY**, not actual auto-merge or permission changes.
The user selected verbatim: "Approve this D-06 approach (Recommended)".

| Aspect | Approved design approach and boundary |
|---|---|
| Eventual eligible work | Qualified ordinary SDK PRs may eventually merge without routine human review, not all PRs or immediate autonomous authority |
| Independent judgment and proof | Independent Router-led approval plus applicable unit and emulator/live evidence bound to the exact actual merge candidate; preserve all required cohort/artifact/configuration and assertion/scenario evidence |
| Restricted actuator | A restricted merge identity separate from the implementation agent; it cannot bypass repository protections or weaken its own eligibility rules |
| Fail-closed evidence | Missing/stale evidence blocks merging; skipped/inconclusive required checks or incompatible/incomplete cohorts/artifacts remain ineligible. GitHub accepting skipped/neutral checks is not sufficient behavioral proof |
| Existing governance | Repo/org required checks/reviews/CODEOWNERS remain binding until explicitly authorized compatible governance changes; internal receipts do not manufacture qualifying approval identities |
| Qualification and suspension | Qualification initially stays non-merging; D-11 decides graduation scope/criteria. Authorized policy owners can suspend the future capability, without selecting their identities or implementing stops/recovery here |

This approval selects no exact identities/apps/permission schemas, policy owners,
review roles/quorum (D-07), operational budgets/stops/recovery implementation
(D-10) or graduation scope/criteria (D-11). It authorizes no governance enforcement,
protected-input integration, auto-merge/Agent merge activation, actual permission
change or unattended SDK merge. It promotes no SDK contract/candidate and claims
no SDK qualification. Existing review requirements are not waived by this receipt.

**Effective SDK/org policy access remains unverified.** The coordinator reports
that a read-only upstream policy read stopped at GitHub HTTP 403 under Azure-org
SAML SSO enforcement before branch/rules retrieval. This is a portable reported
access limitation, not a successful policy inspection or evidence of permissive
SDK rules. SuicideSquad's user-directed documentation merges and its rules do
not establish `Azure/azure-cosmos-dotnet-v3` governance or implement D-06.
No new policy read or access workaround is performed by this update.

D-01 through D-05, their qualified evidence and factual/value gaps remain intact.
D-04 paths/formats/integration and controlled migration remain pending.
D-07 through D-12 remain open (six decisions). The separate SDK testing
workstream and its evolving reports remain distinct from this docs-only
assignment; no files/report import, SDK execution or final delivery is claimed.
The documentation merge receipts below do not retroactively grant authority
to earlier decisions or authorize this new feature PR's merge.

### 10.7 User-selected D-07 approach and Router scope addition

The coordinator relayed the following freeform user response to the main-session
D-07 proposal on 2026-11-01 UTC:

> In addition to the above reviewers approach, let's also add how my personal PR reviewer router works currently. Let's copy the scope of our current PR reviewer router to this design of .NET SDK review

This records the presented independent-review approach plus the explicitly
requested Router-scope extension. The user answered freeform; there is no
selected approval-choice label to reproduce or invent.

The base approach requires two independent Router-led judgments
(correctness/contracts and preservation/interactions), plus a separate
independent test challenger for ordinary SDK implementation/test/CI changes.
All required roles explicitly pass, with separate initial contexts until first
reports, independent verification of fixes/refutations, preserved dissent and
earlier failures, applicable higher-risk expertise and final actual-candidate
reconciliation. Missing required roles/proof, unresolved affected contracts or
stale/incompatible evidence block qualification. Majority overrides, empty
findings, reviewer-shopping, author tier downgrades and assurance-docs bypass
cannot substitute for that proof; optional suggestions remain nonblocking.

Sections 8.1-8.2 specify those obligations. Sections 8.4-8.6 distill all thirteen
supplied personal-Router scope areas, thirteen portable source digests and
six observed adaptation boundaries. They describe the coordinator-read written/
configured protocol, not an independently audited runtime or proof that dispatch/
specialists work. This update does not repeat the audit, dispatch reviewers,
review a PR, modify personal agents/config or import raw prompts/memory/history.
The PR Test Model's read-only artifact is not executed independent challenge
evidence; the paired unit plus emulator/authorized-isolated-live requirement
remains intact.

No routine human sign-off is added to the future qualified ordinary-PR target.
No exact models/providers/apps/GitHub identities, budgets/tool implementations
or activation are selected. Personal scores/caps/tier overrides, peer defaults,
pack hints, advisory fallbacks and current human posting/feedback steps do not
silently become protected eligibility or override D-01 through D-06.
Existing repository/org review/protection requirements remain binding and
unverified SDK policy is not assumed permissive.

D-08 through D-12 remain open (five decisions); D-04 paths/formats/wiring/
migration and factual inventory/oracle/CI/assertion/value gaps remain pending.
Historical D-01 through D-06 receipts, E-01 through E-28, original pins/digests,
lanes/candidates/scenarios/vector and Java freeze retain their qualifications.
No SDK testing evidence, A-01 or evolving SDK result documentation is imported;
no SDK execution, physical migration, protected-rule/permission change, merge,
deployment or release is authorized. Initial qualification remains non-merging.

### 10.8 User-approved D-08 approach

The coordinator relayed the main-session `ask_user` decision on 2026-11-01 UTC.
Its prompt described the D-08 approach in section 8.7 and the **design-only /
no-execution boundary**. The user selected verbatim:
"Approve this D-08 approach (Recommended)".

This selects the approach, not blanket overall-design approval, individual
peer contracts, a completed comparison matrix or runtime qualification.
The current always-visible matrix now includes six core SDKs: .NET (primary),
Java, Python, Go, Rust and JavaScript/TypeScript. JS/TS is deliberately promoted
from the earlier conditional additional-peer treatment. Earlier five-SDK
requirements, the D-07 freeform quote/receipt and the thirteen-source Router
intake remain byte-for-byte history, not retroactively expanded or proof of
JS/TS registration in personal routing.

Section 8.7 records the approved behavior/preservation-neighbor depth, pinned
contract/source/actual-assertion evidence, distinct evidence/artifact classes,
per-cell applicability/dispositions/ownership, risk-dependent deepening,
bounded full-manifest Router integration and scoped fail-closed qualification.
Unverified access is not absence/compatibility; peer majority is not authority.
Verified peer feature absence does not veto a well-proven .NET-first feature,
and an unresolved unrelated peer does not prohibit unrelated work. Missing
required comparisons or unjustified affected-contract deviations still block
autonomous qualification. A peer finding grants no follow-up execution or
change authority for that product.

D-01 through D-07 remain intact, including D-05 authority, D-07 independence
and .NET paired unit plus emulator/authorized-isolated-live proof. No personal
peer cap/default/override can narrow required scope; no personal map/config is
changed. D-09 through D-12 remain open (four decisions), alongside D-04
paths/formats/wiring/migration and factual inventory/oracle/CI/gate/value/
artifact/assertion gaps. Numerical concurrency/time/cost/caps and execution/
tool/runtime/live details are not selected here.

This docs-only update performs no SDK/peer research, review, execution,
agent dispatch, CI/live operations, raw prompt/memory/history/A-01/result import,
source vendoring, physical migration, protected-rule/permission change, merge,
deployment or release. No numerical results, completed peer cells or SDK
qualification are claimed. Initial qualification remains non-merging.

### 10.9 User-approved D-09 approach

The coordinator relayed the user's request verbatim on 2026-11-01 UTC:
"cool, let's move on to d9 now."

After the proposal now recorded in sections 6.1-6.2, the exact main-session
`ask_user` question was:
"Approve this as the D-09 design-only approach, keeping exact tool versions, adapters and compatibility closure pending, with no installations, execution or activation authorized by this decision?"

The user selected exactly: "Approve this D-09 approach (Recommended)".

This approves the design-only technique/admission approach, not exact tools/
versions/adapters, verified integration/supported matrices, exclusions, runtime
qualification, a tool spike or overall-design closure. Extend native MSTest/
test/coverage/CI with applicable behavior/preservation-risk selection; retain
the existing coverage path initially and qualify actual tools against effective
SDK constraints. Stryker.NET is the first mutation candidate to evaluate;
FsCheck and selective Coyote remain compatibility-dependent candidates;
qualify/extend the existing SharpFuzz path, not a parallel platform.

Section 6.1 retains full compiled-code/artifact denominators, separate mutation
outcomes, independently approved D-05 properties/models, seeds/shrinking/
regression cases, controlled/replayable schedules, meaningful fuzz oracles/
corpus/replay, and baseline/defect/replay/identity/case evidence for admission.
Keep dependencies/instrumentation test-only, with no rewritten test assemblies
or third-party testing types in shipped customer artifacts/APIs. Public tool
documentation does not close maintenance, licensing or runtime integration;
no SDK/test project is silently retargeted to a tool's runtime prerequisite.
Injection evidence names its layer and does not infer Gateway/backend effects
from policy/helper tests.

D-01 through D-08 remain intact, including D-03 existing/reconciled gates and
finite attempts, D-05 independent authority, paired unit plus emulator/
authorized-isolated-live proof, existing API/package/performance checks,
D-07 independence and D-08 six-SDK comparisons. D-10 through D-12 remain open
(three decisions), alongside D-04 paths/formats/wiring/migration and factual
inventory/oracle/CI/gate/value/artifact/assertion/tool-fit gaps. D-10 numerical
budgets/retention/resources, D-11 graduation and D-12 intentional changes are
not selected by this approval. D-08's historical four-open snapshot and all
earlier receipts keep their original wording and limits.

This bounded update only records the approach in the three shared .NET docs.
It authorizes no installations, spike, execution or activation and performs
no SDK/peer research/review, agent dispatch, test/CI/live operations, personal
edits, A-01/evolving SDK result import, source vendoring/migration,
protected-rule/permission change, merge, deployment or release. Separately authorized
SDK work stays separate; no final SDK or whole-design closure is asserted.
Stop at publication; no D-10 work is requested.

## 11. Ordered continuation and workstream boundaries

1. **Checkpoint and activation receipt: recorded.** Section 2 identifies the
   corrected Java checkpoint, preserved gaps and explicit design-only signal.
   Java remains paused; publication is not design approval.
2. **Historical intake and D-01 through D-09 selections: recorded.** The
   [baseline](design-baseline.md) preserves the initial main-derived pin and
   distinguishes source declarations, package/preprocessor surfaces, structural counts,
   selected assertions and CI configuration from unmeasured behavior.
   D-01 now selects default main and CI-native baselines. A later bounded slice
   must evaluate the effective existing CI matrix and artifact identities,
   including Gateway/Direct and all repository SDK source. D-02 selects
   behavioral assurance and specs before implementation, not numeric targets.
   D-03 selects the CI-native gate/limit approach, not effective values or run
   approval. D-04 selects shared-versus-SDK ownership, not paths/formats/wiring
   or migration. D-05 selects reconciliation, atomic contracts, independent
   versioned authority and explicit dispute/lifecycle handling, not closure.
   D-06 selects the qualified ordinary-PR future merge model and non-merging
   initial qualification, not activation, permission changes or actual SDK
   governance verification. D-07 selects independent judgments/test challenge,
   risk expertise and final-candidate reconciliation plus the personal
   Router's written scope with explicit adaptations, not runtime proof or
   every personal heuristic/override. D-08 extends the always-visible matrix
   to six SDKs including JS/TS, with behavior/risk-dependent evidence depth
   and bounded full-manifest Router integration, not completed comparisons
   or peer-contract/runtime qualification. D-09 selects native-CI techniques,
   candidates and admission, not actual compatibility, versions/adapters or
   installation/execution. Exact identities/tools, factual
   mappings, operational implementation and graduation scope/criteria remain
   unclosed; D-10 through D-12 remain open.
   The coordinator reports A-01 complete and delivered to its
   Library; the report is not imported and full findings are not reconciled here.
   Reported audit completion is not verified whole-SDK assurance; this update
   does not duplicate/import it or authorize SDK execution.
3. **First gap draft: recorded; closure remains open.** The
   [whole-SDK matrix](domain-gap-matrix.md) retains all 31 shared navigation
   lanes, adds .NET-specific lanes and marks every atomic candidate proposed.
   Continue history/API/internal-workflow and assertion/scenario reconciliation
   against existing CI only within an explicitly bounded authorized slice; record
   pipeline/test improvement gaps, not Java denominators or a parallel platform.
   SDK-specific baseline/gap inputs and A-01 need controlled SDK-docs migration/
   indexing when separately authorized; retain published history and versioned
   references, not an expanding catalog here. Exact paths/formats/integration
   and retention/access remain pending.
4. **Specify before implementing; validate contracts and oracles.** For each
   authorized feature/bug change, including the separate SDK increment below,
   agents first document intended behavior,
   affected/interacting invariants, preservation/intentional changes, failure
   scenarios and the CI assertion plan in SDK docs, referencing versioned
   shared standards/templates. Then implement and obtain applicable
   proof; a retrospective summary cannot replace the spec. Resolve conflicts
   using attributable versioned contracts/specifications and appropriate
   independent oracles, without self-authorizing contract changes. Preserve
   disagreements and unresolved lifecycle states; do not rewrite expectations
   for green CI or qualify unresolved affected behavior. Unrelated well-grounded
   inventory/test improvements need not wait for whole-SDK factual closure.
5. **Reconcile gates/values and resolve remaining design.** Apply approved
   D-02 and the D-03 approach; reconcile actual gates, configured values,
   tolerances and run evidence without inventing approvals. Resolve catalog
   and receipt formats/integration using existing conventions and minimal
   missing metadata, plus actual D-09 tool/fixture admission and compatibility,
   benchmark admission,
   D-08's actual peer mappings/evidence and bounded integration, effective SDK/org policy access and compatible
   governance, protected-input integration and operations without activating
   the D-06 design. Source
   discovery and independent policy discussions may progress concurrently;
   this ordered list does not make them artificial implementation dependencies.
   Reconcile docs-path filters so assurance specs/policy/mappings do not gain
   a blanket bypass; no CI changes or run are authorized by this update.
6. **Keep design review and task authority separate.**
   Preserve findings/dispositions, unverified gaps and residual risk. No
   implementation, measurement campaign, shadow execution or merge authority
   follows merely from completing the document or selecting D-09. The separately
   authorized SDK increment below need not be reclassified as unauthorized;
   this workstream receives none of its execution scope.

Qualification initially remains non-merging under D-06; its actual scope and
graduation criteria remain D-11, not selected or executed here.
The later graduation model remains design -> whole-SDK measured baseline ->
whole-SDK shadow decisions -> qualified narrow merge scopes -> separately
qualified expansion. Any-domain shadow experiments can expose useful
`BLOCKED: missing contract/fixture/evidence` results before every fixture exists,
after design approval and authorized trustworthy baseline/receipt paths.
Experiment breadth never grants all-domain autonomy, and positive eligibility
requires every impacted obligation and global safeguard.

### 11.1 Separate SDK testing authorization context

Separately from D-05 approval, the coordinator reports that the user authorized
the existing SDK workstream to proceed after delivery of its two proposed
SDK-docs drafts. Relevant user request, verbatim:
"let's start the work on the .NET SDK repository to improve those gaps through extensive testing now"
and
"For a gap, we should aim for both a unit test (mocking if it demands), and an emulator or a live test that covers the gap. For the existing tests as well, we should have a unit test with mocking if required, and a live test that runs against emulator or prod account."

That workstream was resumed for a spec-first coherent implementation increment
with paired unit (mocking where required) and emulator or specifically
authorized isolated-live coverage, including existing assessed tests. The
request is not permission to select an arbitrary production account: no such
account was identified/authorized. No merge, release or permission authority
was granted. Applicable evidence must still be obtained and honestly reported;
authorization is not a completed test/fix or assurance result.

This is coordinator-reported scope/status context, not independent inspection
or import of those drafts, their plan or the audit. SDK implementation remains
with that separate workstream; this assignment changes only the three shared
documentation records and performs no SDK edits/execution, CI triggers,
live-account actions, agents/reviews or physical migration. Do not duplicate
the SDK work or infer that later authorization existed at older receipts.

At D-06 publication, the coordinator reported interim unit results from a first
increment and an outstanding integration/publication prerequisite. That status
is evolving and is not imported or independently verified here. It is not a
final SDK delivery, completed integration/live proof or autonomous qualification;
the separate workstream retains its spec-first paired-test scope.

### Current progress and stop condition

| Item | State |
|---|---|
| Context transfer | v0.1.0 persistent; v0.2.0 checkpoint/activation; v0.2.1 D-01; v0.2.2 D-02/spec-first; v0.2.3 D-03; v0.2.4 D-04; v0.2.5 D-05; v0.2.6 D-06; v0.2.7 D-07; v0.2.8 D-08; v0.2.9 D-09 native-CI technique/admission approach, no compatibility closure or activation |
| Final Java checkpoint | v0.2.3 accepted at `5d921060...`; Java paused with explicit incomplete closure |
| .NET-specific investigation | Historical design-only intake recorded; no new investigation by this update; separate SDK increment scoped above |
| D-01 baseline policy | Selected: default main, all repository SDK source, both connectivity modes, existing CI-derived matrices and pipeline/test improvements |
| D-02 behavioral assurance/spec-first policy | Approved: preserve comparable existing obligations, prove new/changed behavior, applicable testing evidence for every PR and agent-written specs before feature/bug implementation |
| D-03 CI-gate/limit approach | Approved approach: reuse existing CI gates/configured limits, strengthen demonstrated gaps, evidence/rationale for new tolerances, required passing evidence, permanent regression protection and bounded attempts; effective gates/values/run evidence unreconciled |
| D-04 ownership/layout approach | Selected: shared rules/templates/spec workflow/process in SuicideSquad, SDK-specific specs/mappings/results/audits in SDK docs; exact paths/formats/integration and physical migration pending |
| D-05 inventory/contract/oracle approach | Approved approach: whole-SDK reconciliation/dispositions, atomic contracts, attributable versioned authority and independent oracles, preserved disputes/lifecycle states; factual closure and exact owners/schema/tools pending |
| D-06 unattended-merge approach | Approved DESIGN ONLY: future qualified ordinary SDK PRs, independent Router approval, exact-candidate unit plus emulator/live evidence and separate restricted identity; no bypass/weakening, required evidence fail-closed, policy-owner suspension and initially non-merging qualification; no activation/permission change/SDK merge |
| D-07 independent review and Router scope | Selected: two independent judgments plus independent test challenge, explicit required-role passes, initial separation, risk expertise and final-candidate reconciliation; complete supplied written Router scope with thirteen source receipts and six adaptation boundaries, not runtime/installation/execution proof |
| D-08 cross-SDK scope and integration | Approved DESIGN ONLY: .NET/Java/Python/Go/Rust/JS/TS always visible, affected consumers added; semantic behavior/preservation comparisons, pinned evidence classes/per-cell dispositions/ownership and bounded full-manifest Router integration; no actual peer cells, new numerical caps, personal config changes or qualification |
| D-09 techniques and admission | Approved DESIGN ONLY: native MSTest/coverage/CI and behavior/risk-selected coverage/mutation/property/concurrency/fuzz techniques with baseline/defect/replay/artifact/case evidence and test-only shipping isolation; candidates are not adopted versions/adapters or verified fit; no installation/spike/execution/activation |
| .NET source/API/configuration/test/CI reconnaissance | E-01 through E-28 remain historical intake evidence; effective current CI/artifact reconciliation incomplete; no new SDK audit or execution |
| .NET atomic contracts and CI assertion/scenario mapping | Proposed/incomplete; selected baseline policy is not contract verification, CI sufficiency or capability qualification |
| Bootstrap migration/indexing | .NET baseline/gap inputs and A-01 are SDK-specific; eventual authority follows SDK-docs ownership; published inputs/Java freeze preserved, no physical migration |
| Separate SDK/CI reconciliation audit | A-01 reported complete/delivered to coordinator Library, unimported into either repo; full findings unreconciled; only relayed docs-filter concern recorded; not verified whole-SDK assurance |
| D-10 through D-12 | Three open decisions; exact identities/owners/permissions, numerical values, tool versions/adapters/compatibility, execution/operational implementation and graduation scope/criteria unclosed; D-04 details and factual/value gaps remain pending |
| .NET coverage, mutation, benchmark and performance results | Unmeasured / not run by this contribution |
| .NET overall design approval / this workstream's SDK execution | Not granted by approach selection; this workstream remains documentation-only |
| Separate SDK testing implementation | Spec-first paired unit/emulator-or-authorized-isolated-live increment, including existing assessed tests; D-06-era interim status is historical coordinator-reported context only, no refreshed/imported/independently verified result or final delivery |
| Effective SDK/org merge policies | Coordinator-reported policy read blocked by HTTP 403 Azure-org SAML SSO before branch/rules retrieval; not verified and not inferred from SuicideSquad documentation-merge rules |
| Earlier project documentation merges | User-directed PR4 then PR3 squash merges recorded in section 13.1; source-head and merge receipts preserved; not SDK governance implementation or qualification |
| D-06 publication and integration | PR5 source head `72e9f579...` was open/unmerged at publication; later verified MERGED at `01803bac...`, separately recorded in section 13.3; no new merge authority |
| D-07 publication and integration | PR6 source head `1fef335e...` was open/unmerged at publication; later verified MERGED at `cb16ba73...`, separately recorded in section 13.4; no new merge authority |
| D-08 publication and integration | PR7 source head `12c7cc3a...` was open/unmerged at publication; now verified MERGED at `c1c929b5...`, separately recorded in section 13.5; fresh D-09 branch, no new merge authority |
| Autonomous merging / releases | Not authorized; releases remain separate |

**Stop after publishing this bounded D-09 approach update and report its paths,
versions and immutable reference to the coordinator.** Do not expand it into exhaustive
closure, SDK execution or duplication of the separately authorized implementation.
Do not install/evaluate candidates, execute SDK work, activate the merge model,
dispatch research/review or append to merged PR3/PR5/PR6/PR7. No D-10 work is
requested. On resumption,
re-read this gate and current repository
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
three-document discovery at `2c67e23...`. D-01 was published at `fecb6db...`,
and D-02/spec-first at `a4af4bc...`; D-03 at `ccb094c...`;
D-04 at `3b141f8...`, D-05 at `532e240...`, D-06 at `72e9f579...`,
D-07 at `1fef335e...`, D-08 at `12c7cc3a...`. This D-09 approach revision changes
only `docs/dotnet/design-handoff.md`, `docs/dotnet/design-baseline.md` and
`docs/dotnet/domain-gap-matrix.md`; no root pointer or Java import is edited.
The D-06 worktree was clean when a fresh feature branch was created from
SuicideSquad main `b45999c818c29169fefbe2902155d2fd65fd284f`, containing the
separately user-directed documentation merges below. For D-07, PR5's actual
merged state was reconciled and a clean fresh feature branch created from main
`01803bacd42f9b66bc20e1af03dcb6bcc2a30dc7`, without extending the merged
PR3/PR5 branches. For D-08, live PR6/main state was reconciled and a fresh
clean feature branch created from main
`cb16ba73dca445f4a8520360ae7a07abd4168cd1`, without extending merged PR6.
For D-09, live PR7/main state was reconciled and a fresh clean feature branch
created from main `c1c929b5ab437aa3be8c67449a147b81c6ce604e`, without extending
merged PR7. Observed integrations are not merge actions by this workstream or
authority for later merges.
Documentation verification and the new publication commit/PR
receipt belong in the fresh feature PR/handoff, not an invented SDK
test report. The available tool catalog did not expose an `ado` server; no live
Azure DevOps pipeline or approval state was queried. The original source
inspection read pinned Git objects, not vendored payloads or the SDK's different
detached working revision. This follow-up preserves that evidence without new
SDK investigation, execution or an exhaustive CI audit. A-01's completion/
Library delivery and digest are coordinator-reported context; its report is
not imported and full findings are not reconciled, and only the relayed docs-filter
integration concern is recorded. No historical input or Java freeze is moved,
deleted or rewritten; no verified whole-SDK assurance or physical migration
is claimed. Separate SDK testing authorization is coordinator-reported context
only; no SDK drafts/plan/audit are imported and no completed tests/fixes are
asserted. Older receipts retain their original scope rather than receiving
retroactive authorization.

### 13.1 User-directed documentation merge receipts

The user separately requested merging the project documentation PRs. The
coordinator reports PR4 then PR3 were squash-merged under SuicideSquad's
existing rules, with source branches retained and no bypass/protection changes.
This workstream verified GitHub's merged state and exact source-head/merge
identities before creating the D-06 branch from current main:

| Project PR | Historical source head | Squash merge on SuicideSquad main | Merged at |
|---|---|---|---|
| [#4](https://github.com/kushagraThapar/SuicideSquad/pull/4) | `5d92106027629ec6c5022a7cd5ef2085014d6973` | `225cfa799bd7f41634d74a087dbe6ce520e749c8` | 2026-11-01T19:05:50Z |
| [#3](https://github.com/kushagraThapar/SuicideSquad/pull/3) | `532e2401be02da06becbbc459dd58b78ae9b35d4` | `b45999c818c29169fefbe2902155d2fd65fd284f` | 2026-11-01T19:06:03Z |

These are user-directed documentation integration receipts, not implementing
D-06, qualifying an SDK candidate or proving Azure SDK/org policy. Historical
open/unmerged-at-activation and no-merge-authorization statements remain true
for their recorded scopes; later explicit user-directed merges do not rewrite
that history. The Java design/research freeze and incomplete closure are
unchanged. The D-06 update grants no merge authority for its new feature PR.

### 13.2 Version history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-31 | Transfer the Java design framework, full-domain seeds, unresolved decisions and separately attributed recovery limits into a .NET-specific starting document; pin the historical initial Java import; record the non-vendoring correction; keep corrected final checkpoint and activation pending |
| 0.2.0 | 2026-11-01 | Record the accepted corrected Java v0.2.3 checkpoint, preserved recovery receipts and .NET design-only activation; select the independent .NET source pin; link the initial baseline and whole-SDK gap draft without closing the twelve decisions or authorizing execution/merges |
| 0.2.1 | 2026-11-01 | Record the user-selected D-01 default-main, all-repository SDK source and CI-native baseline policy with Gateway/Direct; preserve historical intake evidence and incomplete factual reconciliation; D-02 through D-12 remain open; no SDK audit, execution or changes |
| 0.2.2 | 2026-11-01 | Record user-approved D-02 behavioral assurance, every-PR testing evidence and change-proportionate specs before feature/bug implementation; preserve D-01/history and all quality dimensions; D-03 through D-12 remain open; separate audit not duplicated or claimed complete |
| 0.2.3 | 2026-11-01 | Record approved D-03 CI-gate/limit approach without inventing or approving values; preserve D-01/D-02, spec-first and evidence history; D-04 through D-12 remain open (nine); separate audit reported complete but report/findings not incorporated; no SDK investigation or execution |
| 0.2.4 | 2026-11-01 | Record selected D-04 ownership: shared agentic/spec process here, SDK-specific specs/mappings/results/audits in SDK docs, native CI formats/artifacts and durable result identities; exact paths/formats/wiring/migration pending; preserve bootstrap/Java history and D-01/D-02/D-03; A-01 unimported, relayed docs-filter concern only; D-05 through D-12 open (eight) |
| 0.2.5 | 2026-11-01 | Record approved D-05 reconciliation/atomic-contract/versioned-oracle/dispute/lifecycle approach, not factual closure or exact owners/schema/tools; D-06 through D-12 open (seven); preserve D-01 through D-04 receipts, pending details and qualified evidence; distinguish separately authorized spec-first paired SDK testing from this docs-only workstream without importing drafts/plan/audit or claiming tests/fixes |
| 0.2.6 | 2026-11-01 | Record approved D-06 DESIGN-ONLY qualified ordinary-PR future merge approach, independent exact-candidate Router/test proof and separate restricted identity without bypass/activation/permission change; initially non-merging qualification, six decisions D-07 through D-12 open; preserve D-01 through D-05/evidence and source-head/manual documentation merge receipts; portable reported SDK-policy SSO access gap, separate evolving SDK work unimported |
| 0.2.7 | 2026-11-01 | Record D-07 independent judgments/test challenge/risk/final-candidate approach and exact freeform Router-scope addition; distill all thirteen supplied scope areas and portable digests with six adaptation boundaries, not runtime proof/personal heuristic adoption; D-08 through D-12 open (five), prior receipts/evidence preserved; observed PR5 integration separate from source/publication, no reviewers/activation/SDK execution or result import |
| 0.2.8 | 2026-11-01 | Record approved D-08 DESIGN-ONLY six-SDK scope with JS/TS newly always visible, behavior/risk-dependent comparisons, pinned evidence/dispositions/ownership and bounded full-manifest Router integration; four D-09 through D-12 decisions open, exact D-01 through D-07 receipts and Router intake/history preserved; observed PR6 integration distinct from source/publication, no peer research/review/execution, config change or qualification |
| 0.2.9 | 2026-11-01 | Record approved D-09 DESIGN-ONLY native-CI technique/candidate/admission approach, exact request/question/selected label and attributed public-doc limits; no tool adoption/compatibility closure/install/spike/execution/activation. Three D-10 through D-12 decisions open; D-01 through D-08 receipts, D-07 intake, D-08 policy/four-open history and frozen evidence preserved; PR7 source/open publication/later merge remain distinct, no D-10 work |

### 13.3 D-06 integration and fresh D-07 branch receipt

The D-06 publication receipt identified source head
`72e9f57918ed81a38bd750f4a6aca58173877d7b` in then-open/unmerged
[#5](https://github.com/kushagraThapar/SuicideSquad/pull/5). Before starting
this update, live GitHub state instead showed PR5 MERGED at
2026-11-01T21:02:58Z, with merge commit/current main
`01803bacd42f9b66bc20e1af03dcb6bcc2a30dc7`. The source-head and integration
receipts are different identities; the historical publication state is not
rewritten as if merged then.

The three .NET records and applicable root guidance had unchanged blobs
between that source head and the observed main. This workstream began clean,
created a fresh D-07 feature branch from that main and did not extend the
merged D-06 branch. It performed no merge or permission/protection change and
does not infer SDK governance, qualification or authority for the new PR from
an observed project documentation merge.

### 13.4 D-07 integration and fresh D-08 branch receipt

The D-07 publication receipt identified source head
`1fef335ecb72e15e75518cffc2d39814c2e6bd13` in then-open/unmerged
[#6](https://github.com/kushagraThapar/SuicideSquad/pull/6). Before D-08
work began, live GitHub state instead showed PR6 MERGED at
2026-11-01T21:26:58Z, with merge commit/current main
`cb16ba73dca445f4a8520360ae7a07abd4168cd1`. Preserve the source/publication
and later integration receipts as distinct states, not as merged at publication.

The three .NET records and applicable root guidance had unchanged blobs
between that source head and the observed main. The D-08 worktree began clean
and a fresh feature branch was created from that main; no merged branch was
extended. This task performed no merge or permission/protection change and
does not infer SDK governance, peer qualification or authority for the new PR
from the observed documentation merge.

### 13.5 D-08 integration and fresh D-09 branch receipt

The D-08 publication receipt identified source head
`12c7cc3af87208d46a81b3f066262bcfdd3ceab2` in then-open/unmerged
[#7](https://github.com/kushagraThapar/SuicideSquad/pull/7). The coordinator
later observed, but did not perform, its merge. Before D-09 work, this workstream
independently verified PR7 MERGED at 2026-11-01T21:41:13Z, with merge commit/
current main `c1c929b5ab437aa3be8c67449a147b81c6ce604e`. The original source,
open publication and later observed integration remain distinct receipts;
the merge is not retroactively part of D-08 publication.

The three .NET records and applicable root guidance had unchanged blobs
between that source head and the observed main. The D-09 worktree began clean
and a fresh feature branch was created from that main; no merged branch was
extended. Neither observation nor publication grants further merge authority.
This task performed no merge, protection/permission change or activation and
does not infer SDK governance, tool fit or qualification from a documentation
merge.
