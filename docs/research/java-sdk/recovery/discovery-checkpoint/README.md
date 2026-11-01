# Java SDK inventory recovery: discovery, not closure

**Status: incomplete.** These are new, parent-authored recovery outputs produced
directly from the saved source inputs. They are not reports recovered from the
unavailable background agents. They do not complete DS-14, admit historical
benchmarks, measure SDK coverage, or authorize implementation or unattended
merging. Release work remains out of scope.

The SDK baseline is
[`Azure/azure-sdk-for-java@42702a3a1421498ee457ff9cbe56713d0877d39f`](https://github.com/Azure/azure-sdk-for-java/tree/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos).
All Java source citations below refer to that revision, including unreleased
behavior. Discovery in this baseline is not evidence that the same behavior is
available in every supported release or account.

## What was recovered

| Artifact | Purpose and limit |
|---|---|
| [changelog-discovery-ledger.json](changelog-discovery-ledger.json) | Every top-level core changelog bullet, its exact text/span/release/heading, original GitHub references, and explicitly lexical family/invariant hints. Not an atomic semantic ledger. |
| [source-discovery-inventory.json](source-discovery-inventory.json) | Module/file counts, original cache byte identities, exported-package file enumeration, and numeric status/substatus declarations. Not resolved API enumeration or behavioral coverage. |
| [recover_inventory.py](recover_inventory.py) | Offline, standard-library exporter. Reads saved inputs, checks manifest relationships and blob identities, and writes these discovery exports; never executes SDK source or downloaded scripts. |

The core changelog contains **145 release headings and 721 top-level bullets**.
All **1,165 nonempty lines** are accounted for as headings, bullet bodies,
nested/continuation text, or release notes/preamble. Nested behavioral changes are
preserved inside their parent bullet; one bullet can require multiple contracts.
Hotfix/repeated entries remain distinct with their source spans.

| Source heading classification | Top-level bullets |
|---|---:|
| Features Added / New Features | 208 |
| Bugs Fixed | 314 |
| Breaking Changes | 3 |
| Other Changes | 195 |
| No section heading | 1 |
| Total | 721 |

These are classifications copied from headings, not independently verified
change types. For example, a "Bugs Fixed" bullet can say that the release made no
functional change. The three top-level breaking-change bullets contain nested
details; this does not mean that only three breaking behaviors existed.

**705 bullets have keyword-family hints; 16 have no hint. All 721 still lack
verified atomic semantic mappings in this export.** The 16 are not the complete
unresolved backlog, and 705/721 must not be presented as a contract-coverage score.
No entry has test or execution evidence attached. The companion encryption
changelog is absent from the saved inputs and is not included in the 721.

Core changelog SHA-256:
`a50ecbde915a123a7190ca80ceb87ce0b32e2928657bdce47556ff38e0296b79`.

## Structural breadth and source integrity

All four saved recursive module manifests explicitly report `truncated=false`
and match their saved module-tree references.

| Module | All blobs | `src/main/java` files | `src/test/java` files |
|---|---:|---:|---:|
| `azure-cosmos` | 1,317 | 1,287 | 0 |
| `azure-cosmos-tests` | 565 | 0 | 515 |
| `azure-cosmos-test` | 37 | 31 | 0 |
| `azure-cosmos-encryption` | 98 | 54 | 19 |

These are source-file counts, including package/module descriptors and helpers
where present, not numbers of public APIs, executable classes, test cases,
assertions, or covered lines. The separate test module explains why zero tests
appear under core; it does not demonstrate a testing gap by itself.

Core `module-info.java` has three unqualified exports. Their source-file
inventory is complete relative to the saved tree:

| Exported package | Java files |
|---|---:|
| `com.azure.cosmos` | 60 |
| `com.azure.cosmos.models` | 115 |
| `com.azure.cosmos.util` | 8 |
| Total | 183 |

Every one of these 183 files has at least one byte-matching cached copy. This is
not 183 customer APIs: package descriptors, implementation bridge types,
visibility, overloads, inheritance, annotations, and methods still need API-level
reconciliation. Qualified module exports and companion-package contracts are
additional surfaces, not covered by this three-package enumeration.

Among the four original research caches, **903 of 905 Java/XML/Markdown copies**
match saved upstream blob IDs. They represent **679 distinct upstream paths with
at least one matching copy**. The two mismatches are identical cached copies of
`RxGatewayStoreModel.java`, not two different SDK files:

- Actual cached Git blob: `82bc1d4fc10d9cd0450b9a9bb35f8cab799f690a`.
- Expected pinned Git blob: `a25ba5c25d8b43f4edba7e9dec3006c1a839596d`.

Neither mismatched copy is used as contract evidence here. The repository
importer independently identified this problem and is preserving the old receipt
while replacing imported source bytes with the verified public pinned blob.
This export describes the **original intake**, not the post-replacement state.
`cache_path` values are original intake identifiers, not promises that every
duplicate or excluded byte sequence exists at that path in the canonical repo.

The status inventory records **19 non-range HTTP status declarations, three
range markers, and 53 substatus declarations** from verified `HttpConstants.java`
bytes. Substatus numbers overlap across HTTP statuses. This is not a list of 53
universally applicable status/substatus pairs, nor a retry decision matrix.

## Consequential contract leads for the whole-SDK pilot

The original design's F-01 through F-31 remain useful family labels, not atomic
contract closure. The findings below strengthen those families. "Source-local"
means the named code or API documentation was read and its bytes matched the
saved tree; it does not mean the complete runtime path was executed or verified.

### 1. Consistency requires two distinct matrices

**Source-local:** `ReadConsistencyStrategy` is separate from the five account
consistency levels. Its values are `DEFAULT`, `EVENTUAL`, `SESSION`,
`LATEST_COMMITTED`, and `GLOBAL_STRONG`. The enum documents support across
connection modes; its effective-strategy helper returns `DEFAULT` for
non-document resources and writes, then prefers a non-null operation strategy
over the client strategy.

See
[`ReadConsistencyStrategy.java`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/ReadConsistencyStrategy.java#L14-L146)
and
[`CosmosReadManyByPartitionKeysRequestOptions.java`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/models/CosmosReadManyByPartitionKeysRequestOptions.java#L144-L165).

**Changelog lead:** CL-0074 records that invalid ordinary request-consistency
upgrades are ignored rather than rejected in some Gateway paths. CL-0105 records
client-side HTTP 400 for `GLOBAL_STRONG` against a non-Strong account. These must
not be collapsed into one "all stronger requests throw" invariant.

Required expansion: account level x client level x request level x strategy x
operation/resource x transport x account topology, including explicit `DEFAULT`
versus unset, default Session accounts, session-token scope, and unsupported
combinations. Verify exact Java behavior and diagnostics before assigning an
oracle. Families: F-02, F-09, F-10, F-14, F-15.

### 2. Canonical retry guidance needs a version/SDK boundary

The canonical concept reference
[`17-status-codes-and-sdk-retries.md`, sections 1-2 and 6](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md)
is important background on layered retries, but includes .NET examples and a
Gateway-449/no-client-retry summary. Java changelog **CL-0104 (4.81.0)** instead
records consistent client-side orchestration for 449 in Gateway V1 and V2.

Treat this as a Java/version-specific reconciliation requirement, not permission
to use the generic table or assume that Direct is always a retry superset.
Resolve both orchestration and replay-safety rules from verified current Java
source, service constraints, and tests. The mismatched original
`RxGatewayStoreModel.java` cache cannot settle this question. Families: F-10,
F-13, F-14, F-15, F-21.

### 3. HTTP 408 / 21013 exposes an unresolved oracle discrepancy

**Source-local:** `ClientRetryPolicy.shouldRetryOnRequestTimeout` explicitly
returns no retry for `SERVER_WRITE_BARRIER_THROTTLED` and avoids endpoint
mark-down/PPAF in that branch. `ResourceThrottleRetryPolicy.shouldRetry` admits
429, not generic 408.

See
[`ClientRetryPolicy.java:529-536`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/ClientRetryPolicy.java#L529-L536)
and
[`ResourceThrottleRetryPolicy.java:70-81`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/ResourceThrottleRetryPolicy.java#L70-L81).

**Changelog lead:** CL-0080 describes yielding from barrier throttling with
429 for reads or 408/21013 for writes, and says this allows built-in throttle
backoff. These selected source observations do not establish that full behavior.
Trace the complete verified barrier-to-outer-policy path and resolve the intended
contract before encoding a passing oracle. Do not silently choose the changelog
or the implementation as truth, and do not infer a production defect from this
partial trace. Include the opt-out configuration and N-region commit variants.
Families: F-09, F-10, F-11, F-12, F-24.

### 4. Local HTTP/2 recovery is not region-wide endpoint poisoning

**Source-local:** `ClientRetryPolicy` distinguishes substatus
`GATEWAY_HTTP2_PING_TIMEOUT_CHANNEL_CLOSED` (10006) from generic unavailable
Gateway endpoints. It delegates the PING-close case to the Gateway-timeout path,
whose documented intent avoids endpoint mark-down. That does not imply the
next read must use the same region; preferred-location retry can select another.

See
[`ClientRetryPolicy.java:134-163`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/ClientRetryPolicy.java#L134-L163).

Required cases include active child-stream traffic versus an idle parent,
missed ACK thresholds, stream resets/GOAWAY, read versus ambiguous write,
one/multiple preferred regions, and cancellation/close/buffer ownership.
Families: F-10, F-11, F-14, F-28, F-29.

### 5. A plain 404 is not globally terminal or globally retryable

**Source-local:** `isPartitionKeyRangeMetadataNotAvailable` only admits
404/0, 404/1003, and 404/1013 when the request is a `ReadFeed` of
`PartitionKeyRange`. This is not permission to retry missing item reads.

See
[`ClientRetryPolicy.java:268-289`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/ClientRetryPolicy.java#L268-L289).

CL-0083 additionally records bounded post-creation metadata recovery and final
404/1024 rather than an internal exception. Reconcile this with name/RID reuse,
cache refresh, metadata-specific throttling, and nested deadlines. Families:
F-04, F-08, F-10.

### 6. Read-many contains multiple different contracts

**Source-local:** `CosmosReadManyByPartitionKeysRequestOptions` is distinct from
the identity-list read-many options. It documents continuation tied to the same
container, partition-key set, and custom query; validates batch/prefetch lower
bounds; and distinguishes backend continuation size from the larger composite
public token.

See
[`CosmosReadManyByPartitionKeysRequestOptions.java:20-210`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/models/CosmosReadManyByPartitionKeysRequestOptions.java#L20-L210).

Required cases: empty pages, mixed present/missing identities, nested and
hierarchical keys, duplicates, explicit session tokens, consistency strategies,
batching/prefetch limits, continuation identity, and delete/recreate. CL-0023 adds
automatic `/id` tail completion for applicable hierarchical-key point, bulk, and
read-many operations; independently verify its extraction and mismatch rules.
Families: F-05, F-07, F-09, F-16, F-18, F-20.

### 7. Resume/clone/copy is a cross-cutting invariant, not a paging detail

**Source-local:** `CosmosChangeFeedRequestOptions.withCosmosPagedFluxOptions`
reconstructs token-encoded fields and delegates non-token field inheritance
before applying page-size overrides. The delegated inheritance method still
needs field-by-field verification; reading the caller is not proof of every
field's retention.

See
[`CosmosChangeFeedRequestOptions.java:435-465`](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/models/CosmosChangeFeedRequestOptions.java#L435-L465).

CL-0096 records lost end-LSN, serializer, excluded-region, strategy, and other
configuration on resume; CL-0077 records lost authorization/routing/deadline/
throughput/metadata state in hedged request clones. Enumerate propagation
obligations at every rebuild boundary, with independent subscriptions and
success/failure/cancellation. Families: F-02, F-03, F-06, F-12, F-18, F-22, F-29.

### 8. Transport and metadata features need independent denominators

Changelog leads that must not disappear inside broad "CRUD works" tests:

| Entry | Required discovery work |
|---|---|
| CL-0011 | Effective-partition-key sub-range isolation through query fan-out, ORDER BY, splits, and resume. |
| CL-0012, CL-0111 | Additional-header propagation and Direct workload-ID token/type encoding, not only HTTPS header presence. |
| CL-0084 | Process-shared partition-range cache, disable switch, account/container identity, multi-client lifecycle, concurrency, and delete/recreate. |
| CL-0137, CL-0112 | N-region synchronous commit, barrier behavior, and unknown RNTBD token/capability handling. |
| CL-0089 | GSI model/lifecycle and unsupported-account behavior; a public model is not universal service support. |
| CL-0022 | Throughput-bucket GA lifecycle, priority interactions, and wire/options propagation. |

Other history to reconcile includes custom serializers for items versus query
parameters/internal query structures, full-text score scope and weighted RRF,
vector quantization/shard settings, diagnostics privacy/cardinality and optional
tags, metadata-snapshot JSON serialization, account-scoped auth audience
fallback, initial class-loading races, shared schedulers, and emulator-only TLS
escape hatches. These remain discovery leads, not verified oracles.

### 9. Change-feed/processor scenarios need mode and capability scope

The canonical references
[`12-change-feed.md`, "Partition Merge + StartFrom Timestamp"](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/12-change-feed.md)
and
[`05-replication-consistency.md`, "Consistency Levels"](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/05-replication-consistency.md)
provide scenario families, not execution evidence. In particular, chapter 12
explicitly contains hypotheses needing verification; its asserted replay/cost
multipliers must not become universal acceptance criteria without a Java/service
oracle.

Required decomposition includes latest-version versus all-versions/deletes,
retention, start-time plus merge capability, parent/child continuation seeding,
304 checkpoint progress, mode/prefix conflict rejection, acquisition limits,
rebalance after stalled callbacks, manual checkpointing, lease expiry, restart,
and bounded shutdown. Preserve documented replay rather than invent exactly-once
or global ordering guarantees. Families: F-07, F-09, F-18, F-22, F-23, F-24, F-29.

## What still blocks inventory/design closure

1. Split every preserved changelog bullet into semantic obligations, classify
   lifecycle against the chosen release matrix, verify current source, and give
   each obligation an atomic invariant or a justified exclusion. Lexical hints
   are navigation only; they do not discharge this gate.
2. Obtain and reconcile companion encryption history and end-to-end contracts,
   including key resolution/rotation/rewrap/cache behavior, serialization,
   queries, supported operation combinations, errors, and sensitive-data
   boundaries. Core encryption-policy/key metadata alone is insufficient.
3. Finish resolved API/option enumeration, qualified exports, internal workflows,
   hidden settings/capabilities, precedence, default values, and cross-domain
   interactions. Full file trees are necessary, not sufficient.
4. Resolve the 408/21013 oracle discrepancy and Java-versus-generic retry guidance
   before treating either as a green sentinel. Status constants alone do not
   specify safe replay or failure origin.
5. Map actual assertions and fixture capabilities; neither 515 test-module Java
   files nor API byte-cache completeness demonstrates behavioral coverage.
6. Measure coverage and mutation/scenario evidence only on exact candidate
   bytecode with valid denominators, and retain all previously open design
   decisions, repository governance gates, and Router independence requirements.

The whole-SDK pilot still admits experiments from any domain. Missing contracts
or evidence make those experiments **blocked**, not silently out of pilot and
not eligible for unattended merging.

## Reproduction and promotion

Against the original saved research layout, from its inventory root:

```bash
python3 recovery/recover_inventory.py --source-dir source --output-dir recovery
```

The exporter rejects mismatched changelog/status-constant bytes, truncated trees,
tree-reference disagreement, and unaccounted nonempty changelog lines. Other
cached-source mismatches are recorded rather than hidden.

The original import session deliberately froze its intake before this recovery
directory existed. Promotion of this package is a follow-up documentation task;
it must preserve the already imported design, licensing/provenance, and the
truthful incomplete inventory state. Adapt input paths if the canonical import
normalizes them. Regenerating after source replacements will legitimately change
the cache-integrity counts and must not overwrite the original intake history
without recording that distinction.
