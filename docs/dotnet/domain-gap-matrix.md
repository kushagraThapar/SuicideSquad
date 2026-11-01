# Suicide Squad: .NET whole-SDK domain-gap matrix

[Source-pinned baseline and evidence index](design-baseline.md) |
[Shared design and handoff](design-handoff.md)

| Field | Value |
|---|---|
| Document version | 0.1.1 |
| Recorded | 2026-11-01 UTC |
| D-01 baseline policy | User-selected: default `main`, all repository SDK source, existing SDK CI-derived matrices, Gateway and Direct |
| Historical main-derived intake pin | `Azure/azure-cosmos-dotnet-v3@52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8`; not a forever-fixed project baseline |
| Status | INITIAL GAP DRAFT; ALL ATOMIC CANDIDATES PROPOSED / UNVERIFIED |
| Boundary | Design-only D-01 documentation update; historical reconnaissance retained; Java paused at corrected v0.2.3 checkpoint |

## 1. Reading this matrix

All 31 shared F-lanes remain in scope, with six additional .NET navigation
lanes. These **37 navigation lanes are not a complete feature or invariant
denominator**, a score, an approved catalog schema or a promise of availability.
A lane may contain many atomic obligations; overlapping lanes do not create
independent assurance credit. Missing counterparts are unresolved until
source/service/lifecycle evidence supports an explicit disposition.

The [user-selected D-01 policy](design-handoff.md#101-user-selected-d-01-baseline-policy)
includes all SDK source across the repository, not just core, with Gateway
and Direct. Derive build/runtime/platform/account/service-capability baselines
from the established SDK CI; reuse and strengthen its pipelines/tests rather
than build a parallel verification platform or invent a replacement matrix.
Evaluate effective wiring/artifacts and map assertions/scenarios in a later
bounded slice. Missing current CI coverage is an improvement gap, not an
exclusion or proof that green CI already establishes correctness.

All witnesses below remain historical E-01 through E-28 intake evidence.
Future assessments resolve default main and record exact main/base/candidate/
actual merge-candidate, CI/configuration and artifact identities, fixed
within each run; the selected policy does not rebase these old witnesses.

Evidence labels follow the [baseline index](design-baseline.md#8-pinned-evidence-index):
`S` = selected source/configuration observed; `A` = actual assertion text
observed; `H` = historical prose; `P` = pinned path identity only.
An `S` for a narrow witness does not mean every behavior in that row was read
or verified. Path-only links below have not been treated as behavioral proof.

**Global evidence gaps apply to every row:** no SDK execution by this pass;
no measured line/branch/mutation/performance score; no admitted bug benchmark;
no autonomy qualification. Full test/assertion mapping and independent oracle
approval are incomplete even where selected existing assertions were read.
Unknown is not zero, unsupported, N/A, passed or an approved exclusion.

## 2. Whole-SDK domain and gap inventory

The shared F-IDs preserve navigation to the handoff's Java-derived scope,
not Java API/default/retry semantics. Each .NET witness is independently
identified at the selected pin.

| Lane | Scope retained | .NET witness and evidence depth | Remaining contract / assertion / applicability gap |
|---|---|---|---|
| F-01 | Client construction, initialization, concurrency, ownership, dispose/shutdown | S/P [E-08](design-baseline.md#e-08), S clone/policy [E-03](design-baseline.md#e-03) | Failed/lazy construction, shared/external resource ownership, post-dispose calls, concurrent shutdown and every async path |
| F-02 | Defaults, validation, precedence, environment/capability flags | S [E-03](design-baseline.md#e-03), [E-04](design-baseline.md#e-04); A [E-25](design-baseline.md#e-25) | Enumerate all options and null/unset/zero states, evaluated defaults and override/clone/resume boundaries; N-I01/N-I02 are only two candidates |
| F-03 | Credentials, authorization, refresh/rotation, restricted resources and privacy | P [TokenCredentialCache][auth-cache]; S conditional AAD CI [E-23](design-baseline.md#e-23) | Actual key/resource-token/Entra branches, refresh/revocation/concurrency, scopes and redaction; CI declaration is not auth correctness |
| F-04 | Database/container/resource lifecycle, create races and recreate identity | S selected client/container declarations [E-07](design-baseline.md#e-07), [E-08](design-baseline.md#e-08); P [Database][database-api] | Source-backed create-if-not-exists races, stale handles, metadata refresh, delete/recreate and identity-specific assertions |
| F-05 | Typed/stream CRUD, read-many, keys/identity, conditionals and metadata | S selected Container declarations [E-07](design-baseline.md#e-07); P [ReadManyHelper][read-many], [ReadManyQueryHelper][read-many-query] | Per-overload semantics, actual request/response propagation, bodyless results, limits, order/correlation and continuation applicability |
| F-06 | Serialization, parameters, projections, patch, metadata, JSON boundaries and streams | S [E-11](design-baseline.md#e-11); H companion leads [E-15](design-baseline.md#e-15) | Independent round-trip/representation and ownership oracles across custom/STJ/default/binary/companion paths, including failure/short-read cases |
| F-07 | Logical/hierarchical keys, prefixes, hashes, EPK/feed ranges and topology | P [PartitionKeyBuilder][partition-key-builder], [FeedRange tree][feed-range-tree]; S batch key binding [E-09](design-baseline.md#e-09) | Complete key extraction/encoding, prefixes and boundary vectors, partial range identity, split/merge and supported API combinations |
| F-08 | Metadata/name/RID/range/address/query-plan caches, races and sharing | S selected session identity [E-05](design-baseline.md#e-05); P [Routing tree][routing-tree] | Cache inventory and owners, invalidation/coalescing, stale refresh ordering, recreate/account isolation and shared-client lifetime |
| F-09 | Account/client/request consistency and automatic/explicit session state | S [E-04](design-baseline.md#e-04), [E-05](design-baseline.md#e-05); A builder only [E-25](design-baseline.md#e-25) | Service eligibility, legacy consistency interaction, actual wire/routing paths, versioned token algebra/scope and topology; N-I03 is a proposed header case only |
| F-10 | Full status/substatus decisions, nested budgets, deadlines, cancellation and write ambiguity | S [E-06](design-baseline.md#e-06), [E-13](design-baseline.md#e-13); H [E-14](design-baseline.md#e-14) | Constants/producers/transformations/handlers and default paths by operation, origin, mode, commit ambiguity and budget; no HTTP-only table; N-I05 is one proposed cell |
| F-11 | Regional selection/exclusion/discovery, writer topology and outage/recovery | P [GlobalEndpointManager][endpoint-manager]; S selected hub/status branches [E-04](design-baseline.md#e-04), [E-06](design-baseline.md#e-06) | Endpoint eligibility, no-region cases, account refresh, partition versus region health, single/multi-writer guarantees and recovery oracles |
| F-12 | Availability/hedging/circuit breaking, winners/losers, probes and isolation | P [CrossRegionHedgingAvailabilityStrategy][hedging]; H [E-14](design-baseline.md#e-14) | Actual capability enablement and ownership, terminal races, failed/cancelled losing arms, cooldown and impact on unrelated partitions/clients |
| F-13 | Direct transport, framing/TLS/pooling/timeouts/partial I/O and shutdown | S staged-source/default-package distinction [E-17](design-baseline.md#e-17) | Follow actual CI/artifact wiring as the separate ongoing Direct source migration lands; no completed DLL replacement claimed. Pinned implementation access, protocol and failure-origin contracts remain gaps; 280 paths do not close this lane |
| F-14 | Gateway/HTTP protocols, proxy/factory/pooling/streaming/local health | P [CosmosHttpClientCore][http-client]; S policy options [E-03](design-baseline.md#e-03) | Actual protocol/runtime support, ownership, acquisition/request timeouts, local versus regional failures, malformed/partial responses and cancellation |
| F-15 | Thin-client/capability detection, fallback, probes and account refresh | P [ThinClientStoreModel][thin-client]; H [E-14](design-baseline.md#e-14); S template reference [E-19](design-baseline.md#e-19) | Source-backed activation/default/fallback matrix, unsupported account behavior, subrange and diagnostics contracts; no Java flag/default transposition |
| F-16 | SQL/query plans, partition scope, ordering/ties, aggregates/distinct/grouping and limits | P [CosmosQueryClientCore][query-client], [Query tree][query-tree]; S iterator declarations [E-07](design-baseline.md#e-07) | Native versus gateway planner, parameters/options, supported operators, independent fixed/concurrent-data oracles and continuation limitations |
| F-17 | Vector/full-text/hybrid queries, policies, component ranking/alignment and limits | H [E-14](design-baseline.md#e-14); P [Query tree][query-tree]; S separate N-03 witnesses | Runtime/capability availability, ranking/tie/dense-versus-ordinal history, empty/partial component outcomes and score oracle; API/plan metadata is insufficient |
| F-18 | Feed/iterator/stream paging, hints, empty pages, resume, repeat use and tokens | S [E-10](design-baseline.md#e-10); P [Pagination tree][pagination-tree] | Per-API terminal/cancellation/disposal and token identity/compatibility, option preservation and concurrent-mutation allowances; no snapshot assumption |
| F-19 | Single-container/key transactional batch, limits, results, conditionals and atomicity | S [E-07](design-baseline.md#e-07), [E-09](design-baseline.md#e-09); P [TransactionalBatch][transactional-batch] | Actual service atomicity/rollback, ordered results/dependent errors, bodyless and malformed responses, retry safety and limit boundaries; distinct from N-02 |
| F-20 | Bulk scheduling/backpressure/concurrency, per-item results, retries/topology and cleanup | S selected executor [E-09](design-baseline.md#e-09); H [E-14](design-baseline.md#e-14) | Per-item correlation/RetryAfter and absent responses, limits/resource ownership, cancellation/partition changes and rejected options; N-I04 is one proposed pre-I/O case |
| F-21 | Patch operation/path/filter/ETag, invalid combinations and replay restrictions | P [PatchOperation][patch-operation], [PatchItemRequestOptions][patch-options]; S public declarations [E-07](design-baseline.md#e-07) | Non-idempotent lost-response behavior, serializer/expression and distributed/batch variants, conditions and source-backed limits |
| F-22 | Change-feed pull modes, start/resume/retention, 304, ranges and capabilities | S [E-10](design-baseline.md#e-10); H [E-14](design-baseline.md#e-14) | Mode-specific service contracts, RID/version compatibility, split/merge/start-time/retention, cancellation and option preservation; N-I06 does not prove all modes |
| F-23 | Processor leases, ownership/renewal/rebalance, callbacks, checkpoints and estimator | P [ChangeFeedProcessorCore][processor]; S public builder declarations [E-07](design-baseline.md#e-07); H [E-14](design-baseline.md#e-14) | Lease/topology state machine, callback failure/replay, manual/automatic checkpoints, ownership transfer, restart/estimator and bounded shutdown |
| F-24 | Throughput/autoscale/shared capacity, priority/buckets, skew and throttling | S [E-04](design-baseline.md#e-04), [E-07](design-baseline.md#e-07), [E-09](design-baseline.md#e-09) | All resource/operation-specific headers/options and capability limits, hot partition attribution and metadata transitions; no imported Java throughput-control promise |
| F-25 | Container/indexing/spatial/composite/vector/full-text/unique-key/TTL/conflict/computed policies | P [ContainerProperties][container-properties], [Spatial tree][spatial-tree]; H [E-14](design-baseline.md#e-14) | Complete public/wire policy catalog, defaults/validation/lifecycle and supported combinations; TTL is not an exact client-clock liveness deadline |
| F-26 | Scripts/triggers/UDFs, users/permissions, conflicts and child resources | P [Scripts][scripts-api], [User][user-api], [Permission][permission-api], [Conflicts][conflicts-api] | Actual per-resource operations, parameters/body/permissions, paging/serializer paths, error mapping and atomicity boundaries |
| F-27 | Dedicated gateway/integrated cache, staleness/consistency, bypass and metadata | P [DedicatedGatewayRequestOptions][gateway-options]; S bulk option rejection [E-09](design-baseline.md#e-09) | Applicable account/transport/operation cells, cache freshness and unsupported combinations; no inference from the option's presence |
| F-28 | Diagnostics/errors, charge/activity/retry attribution, tracing/metrics/hooks and privacy | P [Diagnostics tree][diagnostics-tree], [Telemetry tree][telemetry-tree]; H [E-14](design-baseline.md#e-14) | Actual field/cardinality/redaction/error/lifetime contracts, failing observers, bounded overhead and per-attempt evidence; no measured resource budget |
| F-29 | .NET async/concurrency/cancellation/context/repeat use and request-state isolation | S selected clone/iterator/DTX paths [E-03](design-baseline.md#e-03), [E-10](design-baseline.md#e-10), [E-13](design-baseline.md#e-13) | Per-overload token forwarding, terminal races, sync context, mutable options/shared state, clocks/timers, prefetch and disposal; not Reactor semantics |
| F-30 | Source/API/binary/package/wire/token/runtime/dependency and consumer compatibility | S [E-01](design-baseline.md#e-01), [E-02](design-baseline.md#e-02), [E-16](design-baseline.md#e-16), [E-17](design-baseline.md#e-17), [E-21](design-baseline.md#e-21) | GA/preview/internal/TFM/package-reference and native consumer matrix, inherited/abstract APIs, current exports, and independent compatibility evidence |
| F-31 | New/preview metadata and service features, GSI/encryption metadata if present | P [ContainerProperties][container-properties], resource/settings tree via [E-28](design-baseline.md#e-28); H [E-14](design-baseline.md#e-14) | Reconcile every new capability and lifecycle; GSI presence/semantics are unresolved, not established or ruled out by Java leads or a filename search |
| N-01 | .NET LINQ expression/serializer translation and queryable execution | S [E-12](design-baseline.md#e-12), [E-07](design-baseline.md#e-07) | Expression subset, naming/converters/null/numerics, custom serializers, async/scalar paths and differential translation/result oracles |
| N-02 | Preview distributed read/write transactions across the coordinator surface | S [E-13](design-baseline.md#e-13), H [E-14](design-baseline.md#e-14) | Capability/scope/limits, operation snapshot, read/write dispatch, FastResponse/nonterminal outcomes, token/session/result identity and abort/replay budgets; N-I07/N-I08 are proposed |
| N-03 | Preview embedding extension and separate semantic reranking/inference | S [E-26](design-baseline.md#e-26), H [E-14](design-baseline.md#e-14) | Declared versus wired runtime support, authentication/endpoints/timeout, generator ownership, ordering/errors/cancellation/cost and companion overrides |
| N-04 | `Microsoft.Azure.Cosmos.Encryption` companion | S project/reference modes [E-16](design-baseline.md#e-16), H [E-15](design-baseline.md#e-15); implementation P | Keys/wrap/rewrap/cache, query/serialization and operation combinations, privacy, GA/preview/source-versus-package and consumer compatibility |
| N-05 | `Microsoft.Azure.Cosmos.Encryption.Custom` companion | S multi-TFM/dependency declarations [E-16](design-baseline.md#e-16), H streaming/cache/disposal leads [E-15](design-baseline.md#e-15) | .NET 8 opt-in versus default path, pooled plaintext cleanup, short-read/representation fidelity, multi-provider/distributed-cache isolation and lifetime contracts |
| N-06 | `Microsoft.Azure.Cosmos.FaultInjection` companion and test-control fidelity | S project/CI parameters [E-24](design-baseline.md#e-24), [E-19](design-baseline.md#e-19); H [E-15](design-baseline.md#e-15) | Fault origin/stage/status fidelity, probability/NaN/bounds/concurrent hit limits, activation/lifetime cleanup and Direct/version coupling |

These additional lanes do not authorize every preview/companion combination.
In particular, ordinary `TransactionalBatch`, bulk batching and preview
distributed transactions have different contracts. Their obligations and
denominators must not be merged because all contain the word "batch".

## 3. Explicit proposed atomic-invariant candidates

Every row below has verification state **`proposed`**, with contract authority
and independent oracle **not yet approved**. Expected outcomes are candidates
for review, not new SDK guarantees. A source observation could itself be wrong.
No candidate was executed or admitted to a protected assurance denominator.

Each condition must become a concrete operation/configuration/sequence cell;
parameterized alternatives are separate cases, not a family-level pass.
The oracle plans must be independently implemented/reviewed rather than
calling the same production decision/serialization helper being assessed.

| Candidate | Preconditions and proposed atomic obligation | Independent oracle plan | Evidence / unresolved proof |
|---|---|---|---|
| N-I01 | One of `Serializer`, `SerializerOptions` or `UseSystemTextJsonSerializerWithOptions` is non-null; setting a different non-null selection must reject the conflicting selection with `ArgumentException`, not silently replace it | Independently reviewed public option-selection table, with both assignment orders and each pair as separate cases | S [E-11](design-baseline.md#e-11); actual assertion mapping, null/reset edge cases, authority and execution unresolved |
| N-I02 | For one supported `ReadConsistencyStrategy` enum value, applying the builder strategy and constructing the mock-backed client must preserve that selected value in `ClientOptions` | Public builder/enum contract checked by an independent observer; no service-consistency inference from the mock | A [E-25](design-baseline.md#e-25) includes real round-trip assertions; scope/authority and candidate execution unverified; this is not full read precedence |
| N-I03 | For a non-bulk document read in a supported account/mode, with legacy consistency unset and valid distinct client/request strategies, the emitted strategy must select the request-level value | Independently specified precedence cases plus outbound request observation, not the handler's own selection helper | S [E-04](design-baseline.md#e-04); promoted options, all entry paths, account eligibility, actual assertions and wire/service evidence unresolved |
| N-I04 | Bulk point-operation path with an otherwise valid non-null request-level throughput bucket must reject the unsupported option before operation dispatch, not silently use/drop it | Public bulk-option contract/history reconciled independently; dispatch/materialization observer and adjacent client-level/non-bulk cases | S [E-09](design-baseline.md#e-09), H [E-14](design-baseline.md#e-14); pipeline scope, actual assertions and execution unresolved |
| N-I05 | Isolated non-DTX Direct barrier-throttling signal `408/21013` enters the inspected retry branch; that signal must not itself invoke partition-endpoint unavailability marking | Independently approved failure-origin classification and health-state observer, with generic timeout as a distinct neighbor case | S [E-06](design-baseline.md#e-06); shipped producer/artifact, outer policies, fixtures and assertions unresolved; no universal retry outcome claimed |
| N-I06 | A supported change-feed range enumerator returns a not-modified page with valid state/RID; the surfaced 304 must still provide continuation state usable for the same approved resume scope | Independent writer/range journal and public resume behavior, not an assertion that undocumented opaque bytes are a public format | S [E-10](design-baseline.md#e-10); mode/version/topology authority, fixture, actual assertions and execution unresolved |
| N-I07 | In the preview coordinator path, frozen operations receive a retriable, non-durably-aborted outcome with retry budgets remaining; the next submission must retain the current idempotency token | Independently approved coordinator protocol/state model with a request journal; do not derive expected token choice from committer code | S [E-13](design-baseline.md#e-13); service/capability authority, token-scoped dispatch, actual assertions and execution unresolved |
| N-I08 | In that preview path, a durably aborted, retriable outcome permits another attempt within remaining budgets; the next submission must use a new token, not replay the terminally aborted token | Independently approved terminal-abort protocol and request journal, distinct from N-I07 and ambiguous/in-progress outcomes | S [E-13](design-baseline.md#e-13); service/capability authority, result/session identity, actual assertions and execution unresolved |

The existing builder assertions are useful evidence of what a test checks,
not proof that the service behavior, all callers, all enum/account combinations
or any executed candidate are correct. Other domains still need atomic
candidate expansion; eight examples are not whole-SDK invariant closure.

## 4. Cross-cutting gaps and design-only continuation

The evidence chain remains
`feature -> behavior -> atomic invariant -> scenario -> test/assertion ->
exact execution -> independent Router review -> restricted merge receipt`.
The states `proposed`, `contract-verified`, `test-mapped`,
`execution-verified` and `autonomy-qualified` must not collapse into one
"covered" label.

| Gap | Work still required; no execution authorized |
|---|---|
| Applicability and lifecycle | D-01 policy selected; evaluate existing CI-derived build/runtime/platform/account/service-capability cells for all repository SDK source and Gateway/Direct, GA/preview/internal/staged/package applicability and source-to-artifact identity; do not invent a replacement matrix or exclude missing CI coverage |
| Inventory and authority | Reconcile every history/API/option/internal workflow obligation both ways, split semantic changes into atomic records, resolve specification/source conflicts and independently approve oracles under D-05 |
| Status and write safety | Use operation/resource, HTTP+substatus, origin, mode, transmission/possible commit, consistency/session, options/topology/capability and remaining budgets; unknown required cells block eligibility |
| Scenarios and data | Retain all 28 critical seeds and twelve general database families from the handoff; specify constrained pairwise/critical sequences, concurrency schedules, data/representation extremes and reproducible minimization |
| Test/fixture fidelity | Map established SDK CI assertions/scenarios and selection to every affected obligation; improve pipeline/test gaps there, not in a parallel verification platform; distinguish mock/emulator/live/native evidence, flakes/quarantine, negative controls and controlled clocks |
| Measurement and ratchets | Preserve the full nine-dimensional vector and honest old/new denominators; settle saturation, N/A, discovery-only changes, thresholds and tolerances under D-02/D-03/D-09, without inventing scores |
| Historical regressions | Use public provenance and sanitized reproductions; require a real assertion failure on the affected revision and pass on the fixed candidate plus neighbors/variants; no benchmark admitted here |
| Independent review and governance | PR Review Router-led semantic judgment, risk/quorum/independence and bounded Java/.NET/Python/Go/Rust comparison, JS/TS/consumers when relevant; existing human approval rules remain; D-06/D-07/D-08 open |
| Candidate-bound trusted evidence | Protect policy/oracles/selection; bind exact main/base/head/actual merge candidate, CI/artifacts/configuration/cohorts, discovered/executed cases, raw outcomes and reviewer receipts for each frozen assessment; missing/stale/malformed evidence fails closed |
| Privacy, ownership and budgets | Design secretless untrusted execution versus separately authorized live work, bounded retries/cost, shared-account namespace/fault/capacity ownership, cleanup/outage/stop/recovery and retention; D-10 open |
| Qualification and contract changes | Resolve D-11 samples/strata/uncertainty and D-12 protected changes/exceptions; any-domain shadow experiments can produce useful BLOCKED findings but never create all-domain merge authority |

D-01's initial baseline policy is selected; its effective matrix, artifact and
assertion/scenario reconciliation remain incomplete.
[D-02 through D-12](design-handoff.md#10-decision-queue-carried-forward)
remain open. The proposed comparable-cohort component-wise nonregression
policy is still unapproved. No row above may compensate for another domain's
critical gap, and no new obligation disappears because it reduces a reported
ratio.

Keep timeout/cancellation write ambiguity, non-snapshot pagination, bulk
transaction boundaries and partition/mode-scoped change feed explicit.
Preview distributed-transaction scope must be established independently;
it does not weaken those ordinary API non-guarantees. Virtual-time evidence
would apply only to actually controlled clocks/timers/schedulers.

Ordered continuation is effective existing-CI/artifact/applicability
reconciliation under D-01, source-backed atomic/oracle closure and CI assertion/
scenario mapping, then measurement/review/operations decisions and independent
design review. Keep the nine-dimensional assurance goals and independent
Router-led review; green current CI alone is not proof of sufficient coverage
or merge authority. This bounded documentation update stops at publication;
it starts no new SDK/CI investigation and grants no SDK source/test/pipeline
edits or execution, CI triggers, live accounts, agents/reviews, source vendoring,
governance changes, merges, deployments or releases. The .NET design and both
project PRs remain unapproved for merge.

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-01 | Whole-SDK navigation/gap draft with independently pinned .NET witnesses, six additional lanes and eight explicitly unverified atomic candidates |
| 0.1.1 | 2026-11-01 | Record selected D-01 main/all-repository/CI-native/Gateway-and-Direct policy and separate ongoing migration; preserve historical witnesses/candidates and incomplete effective CI/artifact/assertion gaps; D-02 through D-12 remain open |

[auth-cache]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Authorization/TokenCredentialCache.cs
[database-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Database/Database.cs
[read-many]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ReadManyHelper.cs
[read-many-query]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ReadManyQueryHelper.cs
[partition-key-builder]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/PartitionKeyBuilder.cs
[feed-range-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/FeedRange
[routing-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Routing
[endpoint-manager]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Routing/GlobalEndpointManager.cs
[hedging]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Routing/AvailabilityStrategy/CrossRegionHedgingAvailabilityStrategy.cs
[http-client]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/HttpClient/CosmosHttpClientCore.cs
[thin-client]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ThinClientStoreModel.cs
[query-client]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Query/v3Query/CosmosQueryClientCore.cs
[query-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Query
[pagination-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Pagination
[transactional-batch]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Batch/TransactionalBatch.cs
[patch-operation]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Patch/PatchOperation.cs
[patch-options]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/RequestOptions/PatchItemRequestOptions.cs
[processor]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ChangeFeedProcessor/ChangeFeedProcessorCore.cs
[container-properties]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Settings/ContainerProperties.cs
[spatial-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Spatial
[scripts-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Scripts/Scripts.cs
[user-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/User/User.cs
[permission-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Permission/Permission.cs
[conflicts-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Conflict/Conflicts.cs
[gateway-options]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Settings/DedicatedGatewayRequestOptions.cs
[diagnostics-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Diagnostics
[telemetry-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Telemetry
