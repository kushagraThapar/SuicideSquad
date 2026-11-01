# Java SDK design/research checkpoint

[Project documentation](../../README.md) |
[Design and progress](../../suicide-squad-design.md) |
[Report status](reports/README.md) |
[Recovery package context](recovery/README.md)

**SDK source does not belong in this repository.** Suicide Squad holds the
contracts, scenarios, benchmark definitions, orchestration/review design,
research findings and provenance needed to make agents trustworthy. Agents
inspect and later change SDK code in the target SDK repository, through code
intelligence or a separate checkout at an exact revision. Copying that SDK into
Suicide Squad is not required for autonomous investigation, development or review.

**Java is paused at the user-selected stable design/research checkpoint; .NET
is the next SDK priority.** The stopping point has explicit gaps, not full Java
catalog closure. No SDK implementation, test execution, permissions, merging,
deployments or release work is authorized here.

## Source references, not source copies

| Reference | Pinned revision |
|---|---|
| SDK repository | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) |
| Java source baseline | [42702a3a1421498ee457ff9cbe56713d0877d39f](https://github.com/Azure/azure-sdk-for-java/tree/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos) |
| Core changelog | [Pinned upstream input](https://github.com/Azure/azure-sdk-for-java/blob/42702a3a1421498ee457ff9cbe56713d0877d39f/sdk/cosmos/azure-cosmos/CHANGELOG.md) |
| Cosmos concept grounding | [tvaron3/cosmosdb-design-docs@bcfbc786fa5296deebcccd11369efb583e63e48c](https://github.com/tvaron3/cosmosdb-design-docs/commit/bcfbc786fa5296deebcccd11369efb583e63e48c) |
| Current Java design | [Version 0.2.3](../../suicide-squad-design.md), paused backlog and .NET-first sequencing |

[`source-access.json`](source-access.json) specifies the ownership/access
boundary and how to resolve pinned source identities. For each historical
upstream record in the [original manifest](import-manifest.json), use
`upstream.repository`, `upstream.commit`, `upstream.path` and
`upstream.git_blob_sha`. Its immutable source URL is:

```text
https://github.com/{repository}/blob/{commit}/{path}
```

The manifest's `snapshot/` paths describe an earlier archive commit, **not
current local files**. Its imported-payload hashes also describe historical
bytes; for public source use the upstream blob identity, particularly for the
explicitly redacted historical CI input. Do not copy SDK code back into this
project to satisfy an old cache path.

The concept repository was consulted at the pinned revision. Its
[Session Tokens: Scope and Non-Goals](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/16-session-tokens.md#scope-and-non-goals)
and
[Status Codes and SDK Retries: Overview](https://github.com/tvaron3/cosmosdb-design-docs/blob/bcfbc786fa5296deebcccd11369efb583e63e48c/17-status-codes-and-sdk-retries.md#1-overview)
remain domain grounding, not automatic Java- or .NET-specific oracles. No
internal service source or concept-document copy is included.

## What this repository retains

| Location | Purpose and limit |
|---|---|
| [Canonical design](../../suicide-squad-design.md) | Java-lane design, reusable evidence/governance model, transition and paused backlog |
| [Source access](source-access.json) | Pinned source identities and target-repository workspace ownership |
| [Tree/module metadata](metadata/) | Structural discovery and the historical download receipt, not SDK source or API closure |
| [Original import manifest](import-manifest.json) | Historical cache identities, hashes, deduplication and exclusions at the initial commit |
| [Original import validation](import-validation.json) | Historical results for that initial archive; not current source-file presence |
| [Recovery context](recovery/README.md) | Outer provenance note explaining the four unchanged historical receipts |
| [Discovery package](recovery/discovery-checkpoint/README.md) | Parent-authored report, two discovery exports and offline exporter, all byte-identical to the handoff |
| [Checkpoint provenance](recovery/discovery-checkpoint/package-manifest.json) | Exact package digests, original history and current checkpoint/status |
| [Current checkpoint validation](checkpoint-validation.json) | Source-reference, document-link, receipt and publication-boundary checks |
| [Report status](reports/status.json) | Missing semantic/domain/test closure and unknown measurements |
| [Upstream attribution](UPSTREAM-LICENSE.txt) | Microsoft MIT license for retained derived changelog/research material |

SDK Java files, test source, Maven files, SDK documentation copies and SDK
pipeline snapshots are absent from the current tree. The obsolete downloader
that wrote SDK snapshots into this project is also removed. Project-authored
research tooling is not SDK implementation and was not executed during promotion.

## Discovery results and limits

The four-file parent-authored handoff totals **1,313,021 bytes**. It preserves
145 core release headings and 721 top-level changelog bullets. Of those bullets,
705 have lexical family hints; **all 721 remain semantically unverified**.
The 183 exported-package Java file records are file enumeration, not resolved
APIs, contracts, assertions or behavioral coverage.

The receipt describes 903 matching and two mismatching copies out of 905
Java/XML/Markdown copies in four original cache buckets. The original intake's
917-path population additionally included top-level changelog, metadata, CI and
a helper. These are different denominators, not competing coverage results.
`cache_path` values identify old inputs; they do not require local duplicates.

The report's source-local leads retain their qualifications. In particular,
the partial-trace 408/21013 discrepancy is an unresolved oracle question, not
a verified production defect or a passing test oracle. Companion encryption
history, atomic semantic mappings, resolved API/internal-path reconciliation,
the whole-SDK domain matrix and test/fixture closure remain incomplete.

The original four agents still have no completed persisted reports. This
package is new parent-authored recovery from original inputs, not recovered
agent output. No new whole-Java or .NET-specific investigation was performed by
this promotion.

## Original history and layout correction

The first import at immutable commit
`a10d3042a61540b907edbe17b710c6294b997a7f` archived research inputs. The user
clarified that a link to the SDK repository suffices; that vendoring decision
is corrected in the current tree without rewriting the earlier history.

The initial capture accounted for 917 paths / 12,476,287 bytes, collapsed 224
identical copies, and excluded two unverified `RxGatewayStoreModel.java` cache
copies. Their Git blob was `82bc1d4fc10d9cd0450b9a9bb35f8cab799f690a`;
the intended pinned public blob is
`a25ba5c25d8b43f4edba7e9dec3006c1a839596d`. Original digests and the
`verified: false` download receipt remain provenance, not contract evidence.

All **685 archived `snapshot/` paths, including 671 Java source/test files**, are
removed from the current tree; the MIT license is retained separately as
attribution. The original manifest/validation remain unchanged
historical receipts and retain the original 0.2.2 design digest. The new
checkpoint manifest describes the current design and source-link-only layout.
Original imported bytes can be inspected at the old commit if genuinely needed;
the untouched parent capture is required for the two excluded mismatching byte
sequences. No parent files or old commits were modified.

The unchanged recovery report contains pre-correction snapshot-replacement
statements, and its exporter expects the old local cache layout. Read those as
historical descriptions, not instructions to recreate SDK copies here. See the
[outer recovery note](recovery/README.md) before using any receipt.

## Attribution and publication boundary

Retained derived public-SDK material remains subject to Microsoft's
[MIT license](UPSTREAM-LICENSE.txt), alongside the
[project license](../../../LICENSE). Source notices remain in the upstream
repository; retain license/provenance when using those sources.

No credentials, private payloads, customer diagnostics, chat transcripts,
unrelated session files or local agent configuration are published. No imported
exporter or SDK code was executed, and no CI/permission/merge policy was changed.
No live Azure DevOps history or required-check state was inspected. The current
checkpoint is design/research evidence, not implementation or merge authority.
