# Suicide Squad: .NET source-pinned design baseline

[Shared design and handoff](design-handoff.md) |
[Whole-SDK domain-gap matrix](domain-gap-matrix.md) |
[Project scope](../../README.md)

| Field | Value |
|---|---|
| Document version | 0.1.3 |
| Recorded | 2026-11-01 UTC |
| Status | INITIAL DESIGN/DISCOVERY DRAFT; NOT APPROVED; NO SDK EXECUTION |
| Research repository | [Azure/azure-cosmos-dotnet-v3][sdk-tree] |
| D-01 baseline policy | User-selected: default `main`, all repository SDK source, existing SDK CI-derived matrices, Gateway and Direct |
| D-02 assurance/workflow policy | User-approved: preserve comparable obligations, prove new/changed behavior, applicable testing evidence for every PR and design/spec before feature/bug implementation |
| D-03 CI-gate/limit approach | User-approved approach: reuse existing CI gates/configured limits, strengthen demonstrated behavioral gaps and require comparable evidence/rationale for new numerical tolerances; effective values/run evidence unreconciled |
| Historical main-derived intake pin | `52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8`; pin each future assessment independently |
| Historical intake tree object | `2c89abbd9680af78d5072b523df277d8c46b755d` |
| Accepted Java checkpoint | [v0.2.3 at 5d92106027629ec6c5022a7cd5ef2085014d6973][java-checkpoint]; Java paused |
| Invariant / execution qualification | All candidates proposed or unresolved; no execution-verified or autonomy-qualified claim |

This is the bounded first .NET-specific design pass after the coordinator
confirmed Java's design/research handoff gate. It establishes a reproducible
source identity, selected source/API/configuration observations, literal
inventory receipts and a whole-SDK gap draft. It is not a complete feature,
public API, status-decision, invariant, assertion or supported-platform catalog.
Subsequent revisions record user-selected D-01, approved D-02/spec-first and
the approved D-03 approach without refreshing intake evidence, importing the
separate audit or starting another SDK/CI investigation.

## 1. Scope and observable acceptance

The accepted output is project-authored documentation in `docs/dotnet/`:
an updated handoff, this baseline and the linked matrix. Acceptance means
the pin is independently established, observations have immutable references,
all shared feature lanes remain in scope, .NET-specific lanes are explicit,
selected D-01/D-02 policies and the D-03 approach are distinguished from
incomplete factual/value reconciliation, D-04 through D-12 remain open (nine
decisions), and missing evidence is visible. D-04 is being discussed, not selected.

The whole SDK is in scope from the start, not a retry/deadline pilot. This
bounded pass samples implementation and assertion text across discovery
lanes; it does not pretend that reading representative paths closes every
lane. D-01 includes all SDK source across the repository, not just core.
Companion packages and staged/preview source remain in scope with separate
CI/artifact applicability and lifecycle gaps, not implicit exclusions.

The [D-01 receipt](design-handoff.md#101-user-selected-d-01-baseline-policy)
selects existing SDK CI to derive build/runtime/platform/account/
service-capability baselines, with Gateway and Direct. Reuse and strengthen
those pipelines/tests rather than invent a parallel verification platform.
Effective matrix evaluation and assertion/scenario mapping remain incomplete;
missing coverage is work to improve there, not a scope exclusion or proof that
green current CI satisfies the assurance goals. This update does not perform
that audit or authorize SDK test/pipeline changes, execution or CI triggers.

The [D-02/spec-first receipt](design-handoff.md#102-user-approved-d-02-and-spec-first-requirement)
sets behavior preservation, including interacting features, above maximizing
percentages or test counts. Preserve assurance for comparable existing
obligations and require complete applicable evidence for new/changed behavior.
Unaffected/saturated dimensions may remain equal, not a claimed numerical
increase. Report full candidate counts and discovered debt honestly; discovery
is not numerical improvement. No gains offset critical regressions or qualify
unproven affected behavior; retirement/intentional changes still need D-12.

Every PR needs applicable testing coverage/evidence; existing sufficient tests
can supply it, without artificial new-test quotas or a documentation-only/
no-test waiver. Before feature/bug implementation, agents must produce a
change-proportionate design/spec covering intended behavior/contract (bug
reproduction and expected correction), affected/interacting features/invariants,
preservation and intended changes, failure/edge scenarios and a test plan mapped
to meaningful existing/new assertions in the established SDK CI. It is not a
retrospective summary, a substitute for test evidence or contract-change
authority. Storage/schema, thresholds, tolerances, tooling and quorum remain
unselected; the full quality vector remains diagnostic/supporting evidence.

The [approved D-03 approach](design-handoff.md#103-user-approved-d-03-approach)
reuses existing SDK CI gates and configured limits as the initial baseline
and strengthens them where the audit demonstrates missing behavioral protection.
New numerical tolerances require comparable evidence and an explicit rationale,
not arbitrary coverage-percentage targets. This selects the approach, not
effective gates, configured values, benchmark/resource tolerances or run
evidence; those remain unreconciled. Additional agent/cost budgets and
operational details remain D-10 work.

Source is accessed in the target SDK repository at the pin, not copied into
SuicideSquad. No SDK code, reproducer, exporter, build, test, coverage,
mutation or benchmark was executed. No dependencies were installed and no SDK
checkout, CI, credentials, accounts, permissions, merge settings, deployments
or releases were changed. No agents were launched. Verification of these
project-authored records is not an SDK execution receipt.

## 2. Baseline identity and source-access boundary

The public upstream `refs/heads/main`, the local `origin/main` object and
GitHub semantic-search index agreed on `52ff1383...` at intake. The commit
is dated `2026-10-30T09:54:09-07:00`: "Query: Fixes hybrid search ranking by
reverting ordinal ranks"
([Azure/azure-cosmos-dotnet-v3#6177](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6177)).
That historical intake head remains frozen in these receipts; it is not a
forever-fixed project baseline. D-01 selects default `main` for future code/
feature/bug assessments. Each assessment must record the exact main/base/
candidate/actual merge-candidate, CI/configuration and artifact identities,
then keep them fixed for the run. A moving ref must not change an assessment
mid-run or silently rewrite E-01 through E-28.

The existing target checkout was detached at
`dd07c97774fe093accdfd554e253c5ecfd88b7d6`, a different revision. Its HEAD and
pre-existing untracked files were left unchanged. Reads used Git objects
of the form `git show 52ff1383...:<repository-relative-path>`; the tree
inventory used `git ls-tree`. Semantic results were checked for the matching
indexed commit. Local working-tree bytes were not substituted for the pin.

Authenticated GitHub API access was unavailable for this source repository;
public upstream Git access and locally available immutable objects provided
the baseline identity and source evidence. No live Azure DevOps pipeline,
required-check, service-connection or branch-governance state was inspected.
The available tool catalog did not expose an `ado` server.

The historical pin is not a shipped NuGet identity or an evaluated CI matrix.
D-01 selects the baseline policy, not proof of artifact/platform qualification.
At this pin root properties declare GA `3.63.0` and preview `3.64.0-preview.0`, while
history and saved API text include later hotfix/preview labels. Those records
have different purposes. Do not select the largest filename as the current
compiled API, or describe all source changes as already released.
`Directory.Build.props` can also import an above-directory properties file;
evaluated imports, overrides, dependencies and build environment still need
candidate-bound receipts in a later authorized phase.

## 3. Observed project, package and framework topology

These are declarations at the pin, not evaluated builds or a supported
runtime/OS/account matrix.

| Surface | Source-observed declaration | Important unresolved boundary |
|---|---|---|
| Core `Microsoft.Azure.Cosmos` | `netstandard2.0`; assembly `Microsoft.Azure.Cosmos.Client`; GA/preview version properties; `PREVIEW` and `ENCRYPTIONPREVIEW` depend on build flags. [E-01](#e-01) | Runtime/OS/architecture support, package/artifact identity and all conditional public surfaces |
| Direct and native query planning | Default core project references Direct `3.44.1` and HybridRow; packs Direct/HybridRow assemblies and Windows native payloads. [E-17](#e-17) | Dependency/native source and artifact provenance, eligible fallback paths, instrumentation and platform coverage |
| Staged managed Direct source | Separate `Direct/src` project says staged import, `netstandard2.0`, `IsPackable=false`; default SDK still uses the original Direct package. [E-17](#e-17) | Its source presence is not proof it is the shipped transport or a complete transport implementation |
| Encryption | `netstandard2.0`; version properties `2.0.5` / `2.1.0-preview5`; conditional SDK NuGet versus project references and `SDKPROJECTREF` symbol. [E-16](#e-16) | Actual supported SDK ranges, GA/preview/package-reference parity, crypto/key-service and consumer contracts |
| Encryption.Custom | `netstandard2.0;net8.0`; version property `1.1.0-preview01`; default SDK reference `3.41.0-preview.0`; separate project-reference path. [E-16](#e-16) | Package audience/support, TFM-specific public/lifetime behavior and dependency compatibility; do not silently exclude the lane |
| FaultInjection | Source project writes `TargetFramework` as `net6`, references core source by default and Direct/HybridRow conditionally. [E-24](#e-24) | Evaluated framework/build, injection fidelity, supported failure origins and package coupling |
| Core unit and emulator projects | `net6.0`; MSTest `3.7.3`, Test SDK `17.12.0`; unit project references Coverlet MSBuild `2.8.1`. [E-18](#e-18) | Actual discovery, runner/configuration compatibility, exclusions, assertions and complete candidate production denominator |
| Fuzz project | `net10.0` executable with SharpFuzz `2.3.0`, seed/config inputs and a core project reference. [E-24](#e-24) | Registration, instrumented assemblies, corpus/oracle quality and bounded execution policy |

Per the user's context, Direct source migration is separate ongoing work
intended to remove the external Direct DLL dependency, not a completed change
or an implementation task here. The table preserves the intake revision's
actual declarations. Follow actual CI/artifact wiring as that migration lands;
do not infer completion from source presence or copy the source here.

Existing public dependencies are baseline contracts to inventory, not
implicitly remove. New customer-facing exposure of third-party implementation
types remains a blocker under the shared requirements. A dependency reference
alone does not establish whether a type is exposed in an API.

## 4. Selected literal source-tree inventory

The following counts enumerate tracked paths ending in `.cs` under the exact
prefixes shown, recursively, at the pinned tree. They include helpers,
generated/conditional code and supporting types. They are **not** API,
executable-line, test-case, assertion, compiled-assembly or coverage counts.
They must not be added into an assurance score.

| Repository-relative prefix | Tracked `.cs` paths |
|---|---:|
| `Microsoft.Azure.Cosmos/src/` | 1,446 |
| `Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/` | 421 |
| `Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.EmulatorTests/` | 203 |
| `Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Performance.Tests/` | 51 |
| `Microsoft.Azure.Cosmos.Encryption/src/` | 135 |
| `Microsoft.Azure.Cosmos.Encryption.Custom/src/` | 100 |
| `Microsoft.Azure.Cosmos/FaultInjection/src/` | 34 |
| `Microsoft.Azure.Cosmos/FaultInjection/tests/` | 8 |
| `Microsoft.Azure.Cosmos/Direct/src/` | 280 |
| `Microsoft.Azure.Cosmos.FuzzTests/` | 10 |

For orientation, core source contains Query, LINQ, Pagination, ReadFeed,
ChangeFeed/Processor, Batch, DistributedTransaction, Authorization, Routing,
HttpClient, Serializer/Json, Telemetry/Tracing and resource/policy trees.
The 1,446 core paths include 241 under `src/OSS/`; neither that subtree nor
the staged Direct tree is an automatically approved coverage denominator.
Samples/tools, companion tests, linked/generated sources, compile-item
conditions and external dependency/native obligations still need
reconciliation. [E-28](#e-28) records path-discovery evidence, not semantics.

## 5. History discovery receipts, not semantic closure

Four histories were located, read selectively, and fingerprinted in full
without copying their payloads. Counts below are literal full-file structure:
version-anchor heading occurrences matching a Markdown heading followed by
`<a name="` and a digit, plus lines starting exactly `- `. These are not
normalized release/change/feature/invariant counts.

| History | Lines / bytes | Version-anchor headings | Raw `- ` lines |
|---|---|---:|---:|
| [Core][core-history] | 2,192 / 229,150 | 213 | 997 |
| [Encryption][encryption-history] | 212 / 13,444 | 36 | 53 |
| [Encryption.Custom][custom-history] | 92 / 21,382 | 8 | 51 |
| [FaultInjection][fault-history] | 51 / 4,694 | 3 | 22 |

The core history has one version at heading level two (`3.54.0-preview.2`,
line 419); counting only level-three versions would miss it. Encryption
contains two `2.0.3` anchor occurrences, so 36 headings are not 36 distinct
versions. Custom's version heading at line 6 is also marked Unreleased;
version and unreleased categories are not disjoint. Raw dash-line counts
include every full-file section, not just admitted release obligations.
Preserve these irregularities and nested text when designing a later ledger.

| Pinned history | SHA-256 of exact upstream bytes |
|---|---|
| Core | `1698198c218c29976b5398640a1342ee8a8358aebe53cce0813401fc33f250fc` |
| Encryption | `4b082b9803a2bfed114e0ba5facc4e6eaa2c010b7b34873a73e4c0a2ddd64301` |
| Encryption.Custom | `4e46c09f0d7e30598426146246291d53a202e999c04cf64412e72aaf93bc657c` |
| FaultInjection | `7a431ad7f9e40eece36b3a8d6f6d0298d282b3cfc97861d125d90e2743bc9294` |

No history item is admitted as a verified atomic obligation or historical
benchmark by this pass. Full semantic mapping, lifecycle exclusions,
preview/hotfix/Other Changes reconciliation, duplicates, nested obligations
and current-source backreferences remain open. This does not claim that the
upstream SDK has no tests or contracts.

Selected leads include read-strategy/hub routing, barrier `408/21013`,
throughput buckets and bulk incompatibilities, thin-client subrange/refresh
behavior, query ranking/plans, change-feed lease topology, distributed
transaction result/replay identity, and custom-encryption streaming/cache/
disposal behavior. [E-14](#e-14) and [E-15](#e-15) are provenance for questions,
not independent proof of root cause, fix completeness or released behavior.
No linked issue/PR was admitted merely because it was closed or mentioned.

## 6. Source/API observations that shape the .NET design

`S` here means a local declaration/body was observed, not an approved contract
or proof of its complete dispatch path. The matrix separates these witnesses
from paths merely discovered and historical prose.

| Observation | Evidence | Consequence / limit |
|---|---|---|
| `CosmosClientOptions` constructor selects Direct/TCP; policy translation copies options, and `Clone` uses `MemberwiseClone` | [E-03](#e-03) | Independently trace effective capability routing, nested defaults, environment overrides and mutable/reference ownership; no Java default is imported |
| Public `ReadConsistencyStrategy` has five enum values; request handler prefers request over client strategy and has a single-write-region hub branch | [E-04](#e-04), [E-05](#e-05) | Legacy consistency, account eligibility, request/resource/operation scope, session behavior and all transports still need contract/oracle closure |
| `ClientRetryPolicy` distinguishes barrier substatus and DTX from generic timeout health handling; other branches inspect operation/session/substatus/state | [E-06](#e-06) | A .NET-specific witness for a full decision key, not an HTTP-only retry table or proof of the complete producer/outer-policy chain |
| Serializer setters reject conflicting selections; serializer core has distinct properties/custom/query-spec paths | [E-11](#e-11) | Map typed/stream, parameter, metadata, patch, LINQ and companion behavior separately |
| Bulk validation rejects request-level throughput buckets and several other per-item options before materialization | [E-09](#e-09) | Do not assume options supported by normal point/read-many/query requests work for bulk point operations |
| Ordinary feed and change-feed iterators have different continuation/304 handling; change-feed constructs a versioned, RID-associated continuation | [E-10](#e-10) | No common end-of-feed, snapshot, globally ordered or exactly-once oracle; token/resume scope and compatibility remain unverified |
| Transactional batch captures one container/key; separate distributed read/write factories are public only under `PREVIEW` | [E-07](#e-07), [E-09](#e-09), [E-13](#e-13) | Bulk is still not a cross-partition transaction. Preview distributed transactions require their own capability, outcome and protocol lane |
| Distributed committer checks retry count/delay budgets and selects replay token rotation from durable-abort state | [E-13](#e-13) | Separate same-token replay, terminal abort/new-token submission, read/write dispatch and nonterminal response semantics; not a universal write retry rule |
| LINQ has an expression evaluator/translator surface in addition to query iterators | [E-07](#e-07), [E-12](#e-12) | Add .NET expression/serializer translation, unsupported expression and differential-oracle work; do not transpose Java query APIs |
| `ICosmosEmbeddingGenerator` is preview-gated; its remarks explicitly defer the SDK call site. Reranking has a separate inference implementation | [E-26](#e-26) | A declared API, query-plan field or example does not prove runtime support. Call-site absence/availability was not exhaustively audited |

Current public API enforcement uses framework-specific JSON reflection
baselines, with GA, preview and telemetry paths. Saved `contracts/API_*.txt`
release files are not by themselves the current compiled API inventory.
The inspected tracked fixture directory contains `net6` JSON baselines;
comments discussing `net8` are not execution or committed-fixture proof.
Generation, framework overrides and live registration need reconciliation,
not an unsupported claim that the `net8` path is broken. [E-02](#e-02)

## 7. Test, coverage and CI arrangements observed read-only

These are repository configuration observations, not live required checks or
successful runs. Existing facilities are prior art to reuse and qualify, not
a newly implemented SuicideSquad platform.
Under the selected D-01 policy they are the baseline for future agent PR
verification and improvements to tests/pipelines. The historical observations
below do not enumerate the effective current matrix. Derive and evaluate that
matrix from the SDK CI, not a replacement runtime/platform/account matrix.
Missing coverage must become explicit improvement work in that CI.
Under approved D-02, these arrangements must eventually supply meaningful
behavioral and cross-feature evidence linked to the pre-implementation spec
and test plan. Coverage metrics diagnose gaps; green percentages or test counts
alone do not prove correctness.

D-03 requires applicable existing checks and spec-required test evidence to
pass; missing, skipped or inconclusive required evidence cannot count as
success. Added regression checks are permanent protection, not checks to
weaken for green CI. Runs, retries and agent repair must be bounded, with first
failures and per-attempt evidence visible; exhaustion is blocked/inconclusive,
not passing. No new limit/tolerance value is selected here, and legitimate
changes still need protected D-12 handling.

| Arrangement | Actual pinned evidence | Remaining gap |
|---|---|---|
| Main PR entry | YAML includes `main` / `releases/*`, excludes Markdown/docs/contracts paths, and references core, preview/internal, samples/package, thin-client, fault and AAD templates. [E-19](#e-19) | Live pipeline registration, branch rules, required contexts and path-filter effects; no assumed review/merge authority |
| Unit/emulator discovery | MSTest projects and category-based template filters; emulator buckets differ from unit/Flaky/live-account buckets. [E-18](#e-18), [E-20](#e-20) | Exact discovered/selected/executed cases, fixture prerequisites and assertions by invariant/configuration |
| Coverage collection | Core coverage job invokes unit tests in Debug with `CollectCoverage=true`, Cobertura and ReportGenerator; unit project declares Coverlet. [E-18](#e-18), [E-20](#e-20) | No score measured. Full assembly/never-loaded-code denominator, branch data, exclusions and candidate/artifact binding unverified; inspected job is not the nine-dimensional gate |
| Flakes/quarantine/retries | Normal and Flaky jobs have distinct filters and configured task retry counts (2 and 4 in selected jobs). [E-19](#e-19), [E-20](#e-20), [E-21](#e-21) | Preserve first-run failures, per-attempt provenance and quarantine debt; retry-assisted success is not a reliability score |
| GA/preview/internal/parity | Preview template runs core tests with `IsPreview=true`, builds companion project-reference and NuGet-surface parity variants; internal template sets `INTERNAL`. [E-21](#e-21) | Every compiled surface, actual artifact and consumer/package combination; declarations do not establish parity results |
| Platform/runtime lanes | Selected core jobs install .NET 6 runtime and .NET 8 SDK; internal also installs .NET 9 SDK. Cron passes MacOS/Linux/Windows OS/image parameters, while selected template jobs use OneES pools. [E-20](#e-20), [E-21](#e-21), [E-22](#e-22) | Resolve effective host OS/images and framework overrides; passing parameters or reading stale examples does not prove cross-platform execution |
| AAD live-account lane | Conditional job requires Windows/nonempty service-connection parameter; StrictMode is passed and a TRX guard rejects missing/empty/nonpassing leaf results when the job runs. [E-23](#e-23) | Configuration, fixture isolation, selected candidate and actual run evidence unknown; a skipped job cannot qualify an impacted auth obligation |
| FaultInjection lane | Main PR entry invokes its template with `IncludeIntegration:false`; package source declares Direct/core coupling. [E-19](#e-19), [E-24](#e-24) | No live fault test or origin-fidelity claim. Injection correctness itself needs independent assertions |
| Performance and fuzz | Core template declares a GateBenchmark/BaselineValidation invocation; fuzz project has SharpFuzz and seed/config inputs. [E-20](#e-20), [E-24](#e-24) | No performance or fuzz result. No fuzz invocation literal was found in the main PR entry/templates searched; this is not a complete CI-registration audit |
| API checks and negative control | Reflection baseline selection and an assertion that deliberately different JSON fails were read. Builder tests assert strategy round-tripping. [E-02](#e-02), [E-25](#e-25) | Assertion-text witnesses only; independent oracle approval, production-case mapping, mutation challenge and execution remain absent from this project |

The historical inspection did not select policy. The user has since selected
D-01, approved D-02 behavioral nonregression/spec-first and the D-03 approach,
not evaluated/approved effective gates, configured values, benchmark/resource
tolerances or run evidence. Mutation tools, quorum, autonomy sample sizes and
additional agent/cost/operational budgets remain unselected.
The selected coverage command does not establish an enforced threshold
elsewhere. GitHub Actions,
remaining templates, all exclusions, actual service capabilities, native
dependencies and live governance were not exhaustively audited.

## 8. Pinned evidence index

E-01 through E-28 remain historical intake evidence from main, unchanged by
the D-01/D-02 policies or D-03 approach. Every upstream link below uses the
same immutable intake commit. `S` is selected source/configuration text observed,
`A` is actual assertion text observed,
`H` is historical prose and `P` is path/fixture identity only. None promotes an
invariant past `proposed` without independent contract/oracle work.

| ID | Evidence and scope |
|---|---|
| <a id="e-01"></a>E-01 S | [Root properties][build-props], lines 3-18; [core project][core-project], lines 10-45, 120-168 and 192-198: versions, flags, TFM, dependencies and packaging |
| <a id="e-02"></a>E-02 S/A/P | [Contract tests][contract-tests], lines 11-60 and 68-142; [enforcement][contract-enforcement], lines 399-465; [tracked fixture tree][contract-tree] P: framework-specific GA/preview/telemetry and negative-control assertions |
| <a id="e-03"></a>E-03 S | [Client options][client-options], lines 46-96, 360-558 and 1235-1339: source defaults, validation, conditional options, clone and policy translation |
| <a id="e-04"></a>E-04 S | [Request invoker][request-invoker], lines 530-633: strategy, priority and bucket precedence/header branches |
| <a id="e-05"></a>E-05 S | [Read strategy enum][read-strategy], lines 20-58; [session container][session-container], lines 84-179: declaration, RID/name/range and parent-token witnesses, not complete service/token algebra |
| <a id="e-06"></a>E-06 S | [Client retry policy][client-retry], lines 486-634; [throttle policy][throttle-retry], lines 26-38 and 94-114: selected status and budget branches |
| <a id="e-07"></a>E-07 S | [Container][container-api]: selected public declarations at lines 339-722, 947-1488 and 1648-1678; not a complete exported API inventory |
| <a id="e-08"></a>E-08 S/P | [CosmosClient][client-api]: constructor/lifecycle/API sites at lines 197-318, 608-710 and 1490-1514; body-level lifetime/concurrency closure not performed |
| <a id="e-09"></a>E-09 S | [BatchCore][batch-core], lines 16-58; [bulk executor][bulk-executor], lines 165-187 and retry/partition sites: bound batch input and unsupported bulk options |
| <a id="e-10"></a>E-10 S | [Feed iterator][feed-iterator], lines 74-134; [change-feed iterator][change-iterator], lines 29-83 and 249-340: selected entry, cancellation, continuation and 304 handling |
| <a id="e-11"></a>E-11 S | [Client options][client-options], lines 597-611 and 817-865; [serializer core][serializer-core], lines 24-113: mutual exclusion and distinct serializer paths |
| <a id="e-12"></a>E-12 S | [LINQ evaluator][linq-evaluator], lines 20-95; [Container][container-api], line 1309: expression and public LINQ entry witnesses |
| <a id="e-13"></a>E-13 S | [Client factories][client-api], lines 1175-1200; [committer][dtx-committer], lines 120-200; [response][dtx-response], lines 164-189: preview gate and replay/abort distinctions |
| <a id="e-14"></a>E-14 H | [Core history][core-history], especially lines 18-115; full-file byte/structural receipts in section 5, not full semantic reconciliation |
| <a id="e-15"></a>E-15 H | [Encryption history][encryption-history], [Custom history][custom-history] and [FaultInjection history][fault-history]: full-file identities, selected entries and explicit lifecycle leads |
| <a id="e-16"></a>E-16 S | [Encryption project][encryption-project], lines 3-81; [Custom project][custom-project], lines 3-77: frameworks, dependency/reference modes and symbols |
| <a id="e-17"></a>E-17 S | [Staged Direct project][direct-project], lines 2-28; [core project][core-project], lines 120-168: staged source versus default shipped dependency/native payloads |
| <a id="e-18"></a>E-18 S | [Unit project][unit-project], lines 6-14 and 42-72; [emulator project][emulator-project], lines 2-23 and 55-70: test frameworks and references |
| <a id="e-19"></a>E-19 S | [PR entry][pr-pipeline], lines 1-106: triggers, filters and template parameters; not live branch protection |
| <a id="e-20"></a>E-20 S | [Core test template][test-template], lines 3-134; selected performance/emulator job declarations through line 451: selection, retries and instrumentation configuration |
| <a id="e-21"></a>E-21 S | [Preview template][preview-template], lines 83-123 and 247-287; [internal template][internal-template], lines 20-46: compile/test surface variants |
| <a id="e-22"></a>E-22 S | [Cron entry][cron-pipeline], lines 6-51; [core template][test-template], lines 23-26: declared platform inputs versus effective pool/runner gap |
| <a id="e-23"></a>E-23 S | [AAD template][aad-template], lines 37-52, 98-106 and 119-188: conditional lane, strict flag and actual TRX guard |
| <a id="e-24"></a>E-24 S/P | [Fault project][fault-project], lines 10-55; [fuzz project][fuzz-project], lines 3-32; test/corpus paths P, no execution or fault-fidelity proof |
| <a id="e-25"></a>E-25 A | [Options unit tests][options-tests], lines 231-279: actual default/strategy round-trip assertions against a mock client; no service-consistency proof |
| <a id="e-26"></a>E-26 S | [Embedding interface][embedding-api], lines 11-58; [Container][container-api], lines 1760-1768; [inference service][inference-service], lines 22-84: declared versus deferred/separate runtime surfaces |
| <a id="e-27"></a>E-27 S, secondary | [Contributing][sdk-contributing], lines 16-27, 56-88; [CI guide][ci-guide], sections Concepts/PR validation/Core test template; cross-check against actual projects/YAML above |
| <a id="e-28"></a>E-28 P | [Pinned SDK tree][sdk-tree], [core source tree][core-source-tree], [tests tree][tests-tree] and [release API text tree][release-api-tree]: complete Git path enumeration for counts/discovery, not complete behavioral source reading |

## 9. Remaining design work and stop boundary

The full [D-01 through D-12 queue](design-handoff.md#10-decision-queue-carried-forward)
is retained. D-01/D-02 and the D-03 approach are selected; effective CI
matrix/gate/value/artifact evaluation, benchmark/resource tolerances, run
evidence and assertion/scenario reconciliation are still incomplete facts
to establish. D-04 through D-12 remain open (nine decisions).
D-04 is being discussed, not selected; documentation paths do not select a
runtime catalog/schema.

Any later authorized reconciliation must establish the existing SDK CI's
build/runtime/platform/account/service-capability cells for all repository SDK
source and Gateway/Direct, bind artifacts, and map actual assertions/scenarios.
Do not invent a separate matrix; identify gaps to improve in those pipelines
and tests while retaining every whole-SDK obligation. The coordinator reports
the separate read-only SDK/CI reconciliation audit complete; its authored
report/findings are not incorporated or reconciled here. This update does
not duplicate or import it; reported completion is not verified whole-SDK
assurance.
Reconcile history/API/internal obligations in both
directions, independently validate atomic contracts/oracles, and map actual
assertions and fixtures. Apply approved D-02 to honest comparable/full-candidate
evidence and spec-before-implementation order, and D-03 to existing gates/limits,
demonstrated gaps and evidence/rationale for new tolerances, without inventing
value approval. Resolve .NET tooling feasibility, independent Router governance
and candidate receipts, cross-SDK breadth, privacy/cost/cleanup and benchmark/shadow
qualification. No such plan authorizes an execution campaign.

The [matrix](domain-gap-matrix.md) preserves all shared feature lanes and the
new .NET lanes, plus eight explicit **proposed** atomic candidates. Its gaps
are not an approved exclusion list. The [shared handoff](design-handoff.md),
including all twelve general database scenario families and the nine-dimensional
quality vector, remains applicable. Conceptual grounding and its qualifications
are in [handoff section 12](design-handoff.md#12-canonical-concept-references-and-qualifications):
chapters 04, 05, 06, 07, 11, 12, 16 and 17 at `bcfbc786...`; .NET examples
and generic retry summaries do not replace current SDK/service evidence.

Stop after publishing this bounded D-03 documentation update; no audit import,
new SDK/CI audit or investigation campaign is included. Do not claim exhaustive
semantic closure, measured coverage, an admitted historical benchmark, design approval,
implemented controls, SDK readiness or autonomous merge eligibility.
PR publication and the Java handoff gate authorize neither PR's merge.

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-01 | Initial independently pinned .NET source/API/configuration/history/test/coverage/CI discovery and provenance draft; no SDK execution or closure claim |
| 0.1.1 | 2026-11-01 | Record user-selected D-01 main/whole-repository/CI-native/Gateway-and-Direct policy; preserve intake pin and E-01 through E-28 as history, ongoing Direct migration context and incomplete effective CI/artifact/assertion reconciliation; no new SDK investigation or execution |
| 0.1.2 | 2026-11-01 | Record approved D-02 behavioral preservation, every-PR testing evidence and pre-implementation specs; retain all quality dimensions, D-01 and historical evidence; ten decisions remain open; no separate-audit duplication or SDK execution |
| 0.1.3 | 2026-11-01 | Record approved D-03 CI-gate/limit approach, required passing evidence, permanent regression protection and bounded visible attempts; no values approved; D-04 through D-12 open (nine); preserve D-01/D-02/history; separate audit reported complete, not incorporated; no SDK investigation/execution |

[sdk-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8
[java-checkpoint]: https://github.com/kushagraThapar/SuicideSquad/blob/5d92106027629ec6c5022a7cd5ef2085014d6973/docs/suicide-squad-design.md
[build-props]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Directory.Build.props
[core-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Microsoft.Azure.Cosmos.csproj
[core-source-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src
[tests-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests
[release-api-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/contracts
[contract-tests]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/Contracts/ContractEnforcementTests.cs
[contract-enforcement]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/Contracts/ContractEnforcement.cs
[contract-tree]: https://github.com/Azure/azure-cosmos-dotnet-v3/tree/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/Contracts
[client-options]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/CosmosClientOptions.cs
[request-invoker]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Handler/RequestInvokerHandler.cs
[read-strategy]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Settings/ReadConsistencyStrategy.cs
[session-container]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/SessionContainer.cs
[client-retry]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ClientRetryPolicy.cs
[throttle-retry]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ResourceThrottleRetryPolicy.cs
[container-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/Container/Container.cs
[client-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/CosmosClient.cs
[batch-core]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Batch/BatchCore.cs
[bulk-executor]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Batch/BatchAsyncContainerExecutor.cs
[feed-iterator]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Resource/FeedIterators/FeedIteratorCore.cs
[change-iterator]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ChangeFeed/ChangeFeedIteratorCore.cs
[serializer-core]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Serializer/CosmosSerializerCore.cs
[linq-evaluator]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Linq/DocumentQueryEvaluator.cs
[dtx-committer]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/DistributedTransaction/DistributedTransactionCommitter.cs
[dtx-response]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/DistributedTransaction/DistributedTransactionResponse.cs
[core-history]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/changelog.md
[encryption-history]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos.Encryption/changelog.md
[custom-history]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos.Encryption.Custom/changelog.md
[fault-history]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/FaultInjection/changelog.md
[encryption-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos.Encryption/src/Microsoft.Azure.Cosmos.Encryption.csproj
[custom-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos.Encryption.Custom/src/Microsoft.Azure.Cosmos.Encryption.Custom.csproj
[direct-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/Direct/src/Microsoft.Azure.Cosmos.Direct.csproj
[unit-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/Microsoft.Azure.Cosmos.Tests.csproj
[emulator-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.EmulatorTests/Microsoft.Azure.Cosmos.EmulatorTests.csproj
[pr-pipeline]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/azure-pipelines.yml
[test-template]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/templates/build-test.yml
[preview-template]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/templates/build-preview.yml
[internal-template]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/templates/build-internal.yml
[cron-pipeline]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/azure-pipelines-cron.yml
[aad-template]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/templates/build-test-aad.yml
[fault-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/FaultInjection/src/FaultInjection.csproj
[fuzz-project]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos.FuzzTests/Microsoft.Azure.Cosmos.FuzzTests.csproj
[options-tests]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/tests/Microsoft.Azure.Cosmos.Tests/CosmosClientOptionsUnitTests.cs
[embedding-api]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/ICosmosEmbeddingGenerator.cs
[inference-service]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/Microsoft.Azure.Cosmos/src/Inference/InferenceService.cs
[sdk-contributing]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/CONTRIBUTING.md
[ci-guide]: https://github.com/Azure/azure-cosmos-dotnet-v3/blob/52ff1383daf7a1a0e8f2d77da0ce819c8ea2f2c8/docs/builds-and-pipelines.md
