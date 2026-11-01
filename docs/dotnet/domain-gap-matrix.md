# Suicide Squad: .NET whole-SDK domain-gap matrix

[Source-pinned baseline and evidence index](design-baseline.md) |
[Shared design and handoff](design-handoff.md)

| Field | Value |
|---|---|
| Document version | 0.1.5 |
| Recorded | 2026-11-01 UTC |
| D-01 baseline policy | User-selected: default `main`, all repository SDK source, existing SDK CI-derived matrices, Gateway and Direct |
| D-02 assurance/workflow policy | User-approved: behavioral preservation, complete applicable new/changed evidence, every-PR testing coverage and design/spec before feature/bug implementation |
| D-03 CI-gate/limit approach | User-approved approach: existing CI gates/configured limits as the initial baseline, strengthen demonstrated gaps, comparable evidence/rationale for new numerical tolerances; effective values/run evidence unreconciled |
| D-04 ownership/layout approach | User-selected: shared agentic rules/spec workflow/templates in SuicideSquad; SDK-specific specs/mappings/results/audits in SDK docs; exact paths/formats/wiring and physical migration pending |
| D-05 inventory/contract/oracle approach | User-approved approach: whole-SDK reconciliation/dispositions, atomic contracts, attributable versioned authority and independent oracles, preserved disputes/lifecycle states; factual closure and exact owners/schema/tools pending |
| Historical main-derived intake pin | `Azure/azure-cosmos-dotnet-v3@52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8`; not a forever-fixed project baseline |
| Status | INITIAL GAP DRAFT; ALL ATOMIC CANDIDATES PROPOSED / UNVERIFIED |
| Boundary | Documentation-only D-05 update; SDK testing separately authorized, not executed/duplicated here; SDK-specific bootstrap inputs retained pending controlled migration/indexing; Java paused; A-01 unimported, relayed docs-filter concern only |

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

The [approved D-02/spec-first policy](design-handoff.md#102-user-approved-d-02-and-spec-first-requirement)
preserves assurance for comparable existing obligations and requires complete
applicable evidence for new/changed behavior, including cross-feature effects.
Unaffected/already-saturated dimensions may remain equal, not a numerical
increase. Report full candidate counts and discovered debt honestly; discovery
is not numerical improvement. Critical regressions cannot be offset by gains
elsewhere, and unproven affected behavior remains ineligible. Retirement or
intentional contract changes still require D-12.

Every PR needs applicable testing coverage/evidence. Existing sufficient tests
may supply proof; no artificial new-test quota or documentation-only/no-test
waiver is approved. Before implementing any feature or bug fix, agents must
write a change-proportionate design/spec covering intended behavior/contract
(bug reproduction and expected correction), affected/interacting features/
invariants, preservation and explicit intended changes, failure/edge scenarios,
and a plan mapping meaningful existing/new assertions to established SDK CI.
This is not a retrospective PR summary, new storage/schema mandate, substitute
for tests or authority to change contracts. Metrics support the behavioral
goal, not maximizing percentages/test counts; retain all nine dimensions.

The [approved D-03 approach](design-handoff.md#103-user-approved-d-03-approach)
starts with existing SDK CI gates and configured limits, strengthened where
the audit demonstrates missing behavioral protection. New numerical tolerances
require comparable evidence and an explicit rationale, not arbitrary
coverage-percentage targets. Applicable existing checks and spec-required test
evidence must pass; missing, skipped or inconclusive required evidence is not
success. Added regression checks become permanent protection, not checks to
weaken for green CI. Bound runs, retries and agent repair, preserve first
failures and per-attempt evidence, and treat exhaustion as blocked/inconclusive,
not passing. Effective gates/values, benchmark/resource tolerances and actual
run evidence remain unreconciled; additional budgets/operations remain D-10.
Legitimate contract/test changes remain protected under D-12.

The [selected D-04 approach](design-handoff.md#104-user-selected-d-04-ownership-and-layout-approach)
keeps shared agentic coding standards/rules, spec-driven workflow/templates
and cross-SDK process guidance in SuicideSquad. Actual SDK feature/bug specs,
invariant/scenario/test mappings, benchmark result records, historical bug
references/sanitized reproductions/fix links/regression evidence and SDK-specific
audit/reconciliation records belong in each SDK repository's docs area.
Executable SDK tests and established pipelines remain in their normal SDK
locations, not copied into docs or SuicideSquad.

Use existing suitable SDK docs conventions and CI report/artifact formats,
with only minimal missing traceability metadata, not a second test database or
duplicate pipeline definition. Durable SDK-docs records/summaries retain
reproducibility, result/configuration identities and appropriately retained
artifact references; large/raw CI artifacts stay in the existing CI artifact
system. SDK-docs records must not be empty lists of moving links. Shared
rules/templates and SDK records/results need versioned references.
Retention/access remains D-10;
this update creates no numerical results or executed evidence.

This matrix's SDK-specific gap inputs, the baseline and A-01 eventually belong
in SDK docs, not an expanding catalog here. Preserve published inputs and the
Java freeze pending controlled migration/indexing. Exact paths/formats/schema,
integration and physical migration remain pending; no SDK edits or report
import occur in this task.

The [approved D-05 approach](design-handoff.md#105-user-approved-d-05-approach)
reconciles whole-SDK APIs/options, internal workflows, changelogs, historical
bugs, existing tests and CI, with every obligation explicitly disposed.
Atomic contracts identify preconditions, applicable configurations, allowed/
forbidden outcomes, interacting features, positive/negative/boundary scenarios
and actual assertions. Expected results need attributable versioned contracts/
specifications supported by appropriate independent reference models, golden
vectors, properties or verified service fixtures. Code and existing tests are
evidence, not automatically correctness authority.

Preserve and explicitly resolve code/test/documentation/service disagreements,
not expectation changes merely for green CI. Unresolved affected behavior
stays ineligible for autonomous qualification without blocking unrelated
well-grounded inventory/test improvements within authorized scope. Retain
supported/preview/deprecated/removed/unsupported/unresolved lifecycle states
and versioned rationale; unknown never silently becomes unsupported or an
exclusion. This approves an approach, not factual inventory/oracle/assertion/
execution closure or exact oracle owners/schema/tools. It adds no routine human
sign-off; reviewer roles/quorum remain D-07 and intentional changes/retirement D-12.

The coordinator separately reports a user-authorized spec-first coherent SDK
testing increment after two proposed SDK-docs drafts were delivered: paired
unit (mocking where required) and emulator or specifically authorized
isolated-live coverage, including existing assessed tests. The exact request
and limits are in [handoff section 11.1](design-handoff.md#111-separate-sdk-testing-authorization-context).
No arbitrary production account was identified/authorized, and no merge/release/
permission authority was granted. This documentation workstream does not
duplicate that implementation, inspect/import its drafts/plan/audit or claim
completed tests/fixes. D-05 approval alone grants none of that execution scope;
older receipts retain their historical limits.

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

## 4. Cross-cutting gaps and workstream boundaries

The workflow requires
`change intent -> pre-implementation design/spec and test plan -> implementation
-> applicable testing evidence -> independent review`.
The spec links to
`feature -> behavior -> atomic invariant -> scenario -> existing/new assertion
-> exact execution -> independent Router review -> restricted merge receipt`.
Its behavioral obligations and test plan precede implementation, not a
retrospective PR summary; neither spec nor implementation supplies its own
contract-change approval.
The states `proposed`, `contract-verified`, `test-mapped`,
`execution-verified` and `autonomy-qualified` must not collapse into one
"covered" label.

| Gap | Work still required; no execution in this documentation assignment |
|---|---|
| Applicability and lifecycle | D-01 policy selected; evaluate existing CI-derived build/runtime/platform/account/service-capability cells for all repository SDK source and Gateway/Direct, GA/preview/internal/staged/package applicability and source-to-artifact identity; do not invent a replacement matrix or exclude missing CI coverage |
| Inventory and authority | Apply approved D-05: reconcile whole-SDK APIs/options/internal workflows/changelogs/historical bugs/tests/CI both ways, with an explicit disposition for every discovered obligation; 37 lanes are navigation, not completeness or a closed denominator |
| Atomic contracts and oracles | Identify preconditions/configurations, allowed/forbidden outcomes, interacting features, positive/negative/boundary scenarios and actual assertions; attributable versioned contracts/specifications with appropriate independent models/vectors/properties/verified service fixtures, not automatic authority from current code/tests; exact owners/schema/tools and factual closure pending |
| Disputes and lifecycle | Preserve and explicitly resolve competing code/test/documentation/service claims with versioned rationale, not changed expectations for green CI; unresolved affected behavior is ineligible for autonomous qualification, not a bar to unrelated well-grounded improvements; preserve supported/preview/deprecated/removed/unsupported/unresolved, unknown never excluded; D-07 roles/quorum and D-12 changes/retirement remain open |
| Spec-first change plan | Before agent implementation, record intended behavior/bug reproduction and correction, affected/interacting invariants, preservation/intended changes, failure/edge scenarios and meaningful existing/new CI assertions in SDK docs, referencing versioned shared rules/templates in SuicideSquad; exact paths/formats/wiring pending, no approval mechanism selected |
| Ownership, results and integration | D-04 selected: SDK-specific mappings/results/history/audits in SDK docs, shared standards/process here, normal tests/pipelines in place; native CI formats plus minimal missing metadata, durable result/configuration identities and retained raw-artifact references; no second test database/duplicated pipeline; controlled bootstrap/A-01 migration/indexing pending |
| Assurance docs and CI filters | Coordinator-relayed A-01 concern and historical E-19 identify Markdown/docs path filters; specs/policy/test mappings under docs must not silently gain a blanket docs-only bypass; future existing-CI wiring work, not permission to change filters now |
| Status and write safety | Use operation/resource, HTTP+substatus, origin, mode, transmission/possible commit, consistency/session, options/topology/capability and remaining budgets; unknown required cells block eligibility |
| Scenarios and data | Retain all 28 critical seeds and twelve general database families from the handoff; specify constrained pairwise/critical sequences, concurrency schedules, data/representation extremes and reproducible minimization |
| Test/fixture fidelity | Every PR needs applicable testing evidence; sufficient existing tests can prove obligations without artificial new-test quotas or a documentation-only/no-test waiver. Applicable existing checks and spec-required evidence must pass; required missing/skipped/inconclusive evidence is not success. Map assertions/scenarios and improve gaps in existing CI; retain fixture fidelity/negative controls/controlled clocks |
| Measurement and ratchets | Apply D-02 to comparable old obligations and complete new/changed evidence; equality for unaffected/saturated dimensions is not an increase; report full candidate counts/debt without offsets and retain all nine diagnostic dimensions. D-03 approach reuses existing CI gates/limits, strengthens demonstrated gaps and requires comparable evidence/rationale for new numerical tolerances; effective gates/values/run evidence unreconciled, tooling still D-09 |
| Historical regressions | Use public provenance and sanitized reproductions; require a real assertion failure on the affected revision and pass on the fixed candidate plus neighbors/variants; retain added regression checks as permanent protection, not weakened for green CI; no benchmark admitted here |
| Independent review and governance | PR Review Router-led semantic judgment, risk/quorum/independence and bounded Java/.NET/Python/Go/Rust comparison, JS/TS/consumers when relevant; existing human approval rules remain; D-06/D-07/D-08 open |
| Candidate-bound trusted evidence | Protect policy/oracles/selection; bind exact main/base/head/actual merge candidate, CI/artifacts/configuration/cohorts, discovered/executed cases, raw outcomes and reviewer receipts for each frozen assessment; missing/stale/malformed evidence fails closed |
| Privacy, ownership and budgets | Bound runs/retries/agent repair with visible first failures and per-attempt evidence; exhaustion is blocked/inconclusive, not passing. Additional agent/cost budgets, secretless untrusted execution versus separately authorized live work, shared-account namespace/fault/capacity ownership, cleanup/outage/stop/recovery and retention remain D-10 |
| Qualification and contract changes | Resolve D-11 samples/strata/uncertainty and D-12 protected changes/exceptions; any-domain shadow experiments can produce useful BLOCKED findings but never create all-domain merge authority |

D-01/D-02 and the D-03/D-04/D-05 approaches are selected; effective matrix/gate/value/
artifact, benchmark/resource tolerance, run and assertion/scenario
reconciliation remain incomplete.
[D-06 through D-12](design-handoff.md#10-decision-queue-carried-forward)
remain open (seven decisions); D-06 is under discussion, not selected.
D-05 selects the approach, not factual inventory/contract/oracle/assertion/
execution closure or exact oracle owners/schema/tools.
D-04 ownership is selected, not exact
paths/formats/schema, SDK integration or completed physical migration.
Approved policy is not an implemented gate or proof that current CI suffices.
No row may compensate for another domain's
critical gap, and no new obligation disappears because it reduces a ratio.

Keep timeout/cancellation write ambiguity, non-snapshot pagination, bulk
transaction boundaries and partition/mode-scoped change feed explicit.
Preview distributed-transaction scope must be established independently;
it does not weaken those ordinary API non-guarantees. Virtual-time evidence
would apply only to actually controlled clocks/timers/schedulers.

Ordered continuation is effective existing-CI/artifact/applicability
reconciliation under D-01, D-05's source-backed atomic/oracle and CI assertion/
scenario mapping, then factual gate/value reconciliation under D-03,
remaining review/operations decisions and independent
design review. These are not artificial prerequisites to unrelated well-grounded
inventory/test improvements within authorized scopes. For authorized changes,
including the separate SDK increment, a design/spec and test plan must
precede agent implementation and applicable proof; actual SDK specs/mappings/
results belong in SDK docs under D-04 with versioned shared-rule references.
Controlled bootstrap migration/indexing and assurance-docs CI wiring are
follow-up, with no physical move or filter changes now.
The separate read-only SDK/CI reconciliation audit A-01 is reported complete
and delivered to the coordinator's Library; its report has not been imported
into either repo and full findings are unreconciled. Only the relayed docs-filter
integration concern is recorded; its SDK investigation is not duplicated.
Reported audit completion is not verified whole-SDK
assurance. Keep the nine-dimensional assurance goals and independent Router-led
review; green current CI alone is not proof of sufficient coverage or merge
authority. This bounded D-05 documentation update stops at publication;
it does not import A-01, physically migrate records or select tooling, concrete
schemas, reviewers, human sign-off, enforcement or merge authority.
It starts no new SDK/CI investigation and
grants this workstream no SDK source/test/pipeline
edits or execution, CI triggers, live accounts, agents/reviews, source vendoring,
governance changes, merges, deployments or releases. The .NET design and both
project PRs gain no overall design or merge approval from this policy selection.
The separately authorized SDK testing work remains distinct; this record
imports none of its drafts/plan/audit and asserts no completed tests/fixes.

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-01 | Whole-SDK navigation/gap draft with independently pinned .NET witnesses, six additional lanes and eight explicitly unverified atomic candidates |
| 0.1.1 | 2026-11-01 | Record selected D-01 main/all-repository/CI-native/Gateway-and-Direct policy and separate ongoing migration; preserve historical witnesses/candidates and incomplete effective CI/artifact/assertion gaps; D-02 through D-12 remain open |
| 0.1.2 | 2026-11-01 | Record approved D-02 behavioral assurance, every-PR applicable testing and specs before implementation; preserve all dimensions, D-01 and historical candidates/evidence; D-03 through D-12 remain open; separate audit not duplicated |
| 0.1.3 | 2026-11-01 | Record approved D-03 existing-CI gate/limit approach without numerical value approval; required passing evidence, permanent regression protection and bounded visible attempts; D-04 through D-12 open (nine); preserve D-01/D-02/history; audit reported complete, not imported |
| 0.1.4 | 2026-11-01 | Record selected D-04 shared-process/SDK-docs ownership, durable result identities/native artifacts and versioned references; controlled bootstrap/A-01 migration/indexing and exact paths/formats/wiring pending; relayed docs-filter concern, no import; preserve all candidates/evidence and D-01/D-02/D-03; D-05 through D-12 open (eight) |
| 0.1.5 | 2026-11-01 | Record approved D-05 reconciliation/atomic-contract/versioned-oracle/dispute/lifecycle approach, not factual closure or exact owners/schema/tools; D-06 through D-12 open (seven); preserve all lanes/candidates/evidence and D-01 through D-04; distinguish separate spec-first paired SDK testing authorization from this docs-only assignment, without implementation duplication or drafts/plan/audit/result import |

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
