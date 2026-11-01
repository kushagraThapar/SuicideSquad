# Java SDK research input archive

[Project documentation](../../README.md) |
[Design and progress](../../suicide-squad-design.md) |
[Missing-report status](reports/README.md) |
[Resume checklist](recovery/README.md)

**Research inputs only.** This is a selected public-source archive, not a forked
SDK, a buildable checkout, a completed inventory, or evidence that tests passed.
Do not build the snapshots, run imported scripts, provision resources, or enable
agent permissions as part of this documentation import.

## Baselines and authority

| Input | Pinned revision |
|---|---|
| SDK source | [Azure/azure-sdk-for-java@42702a3a1421498ee457ff9cbe56713d0877d39f](https://github.com/Azure/azure-sdk-for-java/commit/42702a3a1421498ee457ff9cbe56713d0877d39f) |
| Cosmos concept grounding | [tvaron3/cosmosdb-design-docs@bcfbc786fa5296deebcccd11369efb583e63e48c](https://github.com/tvaron3/cosmosdb-design-docs/commit/bcfbc786fa5296deebcccd11369efb583e63e48c) |
| Original project-authored design | Version 0.2.1; SHA-256 `53f53195f6da2c04b3511824056d0042d9e8111e90d9459a47254c54c60263f8` |
| Portable canonical design | [Version 0.2.2](../../suicide-squad-design.md); import/portability edits only, no implementation approval |

The concept repository was synced before consultation. Its
[Session Tokens: Scope and Non-Goals](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/16-session-tokens.md#scope-and-non-goals)
and
[Status Codes and SDK Retries: Overview](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview)
remain grounding references, not automatic Java-specific test oracles. No
internal service source or concept-document copy is included in this archive.

## Preserved material and layout

| Location | Contents and limits |
|---|---|
| [Core changelog](snapshot/sdk/cosmos/azure-cosmos/CHANGELOG.md) | Full pinned changelog input; no semantic ledger was completed |
| `snapshot/sdk/cosmos/` | Selected core production/test, test-support, documentation and Maven configuration files, preserving upstream paths |
| `snapshot/eng/` | Selected public CI configuration, retained as data, not active project pipelines; one public emulator-default key literal is redacted |
| [Tree/module metadata](metadata/) | Four non-truncated recursive trees, module discovery and the historical download receipt |
| [Import manifest](import-manifest.json) | Every retained payload, all original cache paths, hashes, upstream provenance, transformations and exclusions |
| [Bounded import validation](import-validation.json) | File/hash, source-stability, document-link and publication-boundary results; no SDK execution or research-completeness claim |
| [Report status](reports/status.json) | Missing reports/ledger/domain matrix and explicitly unknown measurements |
| [Recovery guidance](recovery/README.md) | Resume checklist and preserved historical fetch helper; not executed |
| [Upstream license](snapshot/LICENSE.txt) | Microsoft MIT license for the retained upstream material |

Tree manifests enumerate files that were not downloaded. They do not prove
API/contract inspection or complete source capture. Encryption discovery metadata
is preserved, but companion encryption contracts and release-history
reconciliation remain incomplete. The saved download receipt contains 265 file
records, including an explicit `verified: false` record; it is historical input,
not the authority for this import's verification.

Snapshot documents are immutable upstream text. Their original relative links
may point to files outside this selected archive; read them in the pinned
upstream repository context recorded by the manifest. Project-authored index,
design and recovery links resolve within this repository. Validation distinguishes
those two link populations rather than changing upstream bytes or claiming the
archive is a full checkout.

## Import accounting

The frozen intake is the original research `source/` subtree only. A later
parent-authored `recovery/` subtree is unfinished and deliberately deferred to a
separate completed handoff. No adjacent session folder was migrated.

| Accounting item | Count |
|---|---:|
| Captured original research paths | 917 |
| Captured original bytes | 12,476,287 |
| Original paths retained, including the portable helper | 915 |
| Redundant identical cache copies deduplicated | 224 |
| Unverified cached paths excluded | 2 |
| Unique retained input payloads | 691 |
| Verified public additions: replacement blob and upstream license | 2 |
| Final research payload files, excluding authored index/status/manifest documents | 693 |

The exact resulting byte counts and per-file digests are in
[`import-manifest.json`](import-manifest.json). Deduplication preserves every
original path in each payload's `origins` array. Copies were collapsed only
when their retained bytes matched; no completed report or project-authored
analysis was discarded as a duplicate.

## Provenance and verification

The module tree IDs were rechecked through the public pinned GitHub directory.
All four cached recursive trees matched the public trees and reported
`truncated: false`. Retained SDK blobs match those trees; the three original CI
inputs were also compared byte-for-byte with public commit-scoped raw files.
One public development-fixture key literal was then redacted from the archival
CI payload; its original and imported hashes are explicitly distinct. The
upstream license was retrieved at the same commit and checked against its
contents-API blob ID.

Each manifest payload records its repository-relative path, size, SHA-256,
Git blob SHA-1, original source-relative paths and, for upstream material,
repository, commit, upstream path and expected original blob ID. Imported hashes
cover the actual retained bytes; declared transformations must not be mistaken
for byte-identical upstream snapshots. The Git blob algorithm is:
`SHA1("blob " + decimal_byte_length + NUL + content)` for a Git blob. The manifest
also records the original design digest and the intentionally updated canonical
design digest. It is an import ledger, **not** the missing changelog semantic
ledger or a runtime invariant/evidence schema.

Authenticated source reads encountered Azure organization SAML enforcement.
The requested CLI reauthentication could not replace an environment-supplied
token; public commit-scoped, credential-free reads supplied verification instead.
No token, authentication state or authorization URL is preserved here. No `ado`
server tools were exposed for this task; no live Azure DevOps pipeline history,
required checks or permissions were inspected or changed.

## Exclusions, transformations and recovery

| Category | Handling and recovery |
|---|---|
| Identical cached source copies | Retain one verified payload and every original path in the manifest; copy it to those paths to reconstruct the old cache layout |
| Two cached `RxGatewayStoreModel.java` copies | Exclude unverified bytes; retain original paths, lengths and digests, the saved `verified: false` receipt, and the verified pinned public replacement |
| One public emulator-default key literal in archival CI | Replace with `REDACTED_PUBLIC_EMULATOR_DEFAULT_KEY`; retain the original input digest and public pinned path for provenance, without publishing the literal here |
| Machine-specific helper paths | Use `gh` from `PATH` and repository-relative metadata/snapshot paths; retain the original helper's digest and describe the edits |
| Machine-local integration references in the design | Retain integration names, provenance limitations and pending versioning work, without private filesystem locations |
| New parent-authored recovery subtree | Not inspected or imported; receive a separately completed, provenance-bearing package later |
| Credentials, private payloads, chat transcripts, unrelated/temporary files and local agent configuration | Outside the import boundary; not uploaded, synthesized or recovered from adjacent folders |

The excluded Java cache bytes were 70,078 bytes in each of two paths, with
SHA-256 `17c9f6b52ca273312baf3f15aea158cf79a0ca9e78daaf4b719b9366207ad76b`
and Git blob `82bc1d4fc10d9cd0450b9a9bb35f8cab799f690a`. Their expected
public blob is `a25ba5c25d8b43f4edba7e9dec3006c1a839596d` (70,082 bytes), now
retained at
[`snapshot/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/RxGatewayStoreModel.java`](snapshot/sdk/cosmos/azure-cosmos/src/main/java/com/azure/cosmos/implementation/RxGatewayStoreModel.java).
The original designated inputs remain untouched outside the repository. Their
exact excluded bytes cannot be reconstructed from upstream; use the original
capture and recorded digests if inspecting that discrepancy later.

## Licensing and publication boundary

Upstream files remain copyright Microsoft and retain their original notices.
They are redistributed under the pinned
[Microsoft MIT license](snapshot/LICENSE.txt); this repository's
[project license](../../../LICENSE) does not erase upstream attribution.
Preserve both the notices and provenance when moving these snapshots.

Only the designated project design, classified public SDK inputs, a portable
project-authored helper and the minimal public license/replacement additions are
published. Public example identifiers, HTTP header constants and environment
variable references are source text, not live credentials. The public emulator
fixture key is redacted even though it is not a live-account secret. No imported Java,
Maven, TestNG, CI or historical helper code was executed.
