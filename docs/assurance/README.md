# .NET project specifications and historical evidence

This is the Suicide Squad-owned preservation of the project documentation
introduced in Azure/azure-cosmos-dotnet-v3 PRs
[Azure/azure-cosmos-dotnet-v3#6182](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6182),
[Azure/azure-cosmos-dotnet-v3#6184](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6184),
[Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185),
[Azure/azure-cosmos-dotnet-v3#6187](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6187) and
[Azure/azure-cosmos-dotnet-v3#6190](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6190).
See the [source/head/path and SHA-256 ledger](provenance.md).

## Current ownership and preservation scope

The user directed on 2026-11-09 that versioned contracts, invariants, project
documentation and development specifications live **only in SuicideSquad**;
SDK repositories retain tests and agent-facing instructions for running them.
This supersedes the earlier D-04 SDK-docs ownership/layout direction, not its
historical decision receipt or the remaining design and approval requirements.
Existing SDK executable dependencies are a separate relocation constraint below,
not permission to silently delete them.

This import changes no SDK source, test, build or CI file and adds no assurance
capability. It does not activate protected CI, admit an evaluator, run an
execution campaign, qualify coverage, authorize SDK deletions, merge or close
anything. Java remains paused. Copied authorizations, status reports and
commands are historical source context, not renewed permission or current
test-running instructions. Use the SDK's own current guide for test commands.

## Documents

| Document | Preserved scope |
|---|---|
| [Feature/behavior-to-test matrix](feature-behavior-test-matrix.md) | Upper #6184 layer, including I-03 additions and retained I-01/I-02 limits |
| [Remediation plan](remediation-plan.md) | Upper #6184 layer; historical failures, dependencies and unresolved gaps |
| [I-01 encryption patch](specs/i-01-encryption-patch-paired-tests.md) | Pre-implementation contract and separate native receipt |
| [I-02 Custom cache](specs/i-02-custom-cache-paired-tests.md) | Cache/cancellation contract, corrections and candidate-specific receipts |
| [I-03 Custom legacy](specs/i-03-custom-legacy-paired-tests.md) | Upper-layer spec and local/publication limitations |
| [M-01 foundation spec](specs/m-01-assurance-foundation.md) | Bounded original record/validator design and authorization |
| [M-01 record contract](history/6185/README.md#version-1-record-contract) | Original format semantics, validation limits and SDK-local command/CI context |
| [M-01 mapping JSON](specs/m-01-assurance-foundation.json) | Unmodified source bytes and original reference/hash semantics |
| [M-01 review-feedback addendum](specs/m-01-review-feedback.md) | Pre-correction requirements and original lineage |
| [Historical I-01 example](examples/i-01-64324.json) | Unmodified historical, unqualified example; not current candidate proof |
| [Retry response disposal ordering](specs/http-retry-disposal-ordering.md) | HTTP-DROP-ORDER/v1 unit-only contract and missing real-transport pair |
| [Local HTTP/2 fixture](specs/local-http2-disposal-fixture.md) | LOCAL-HTTP2-DISPOSAL/v1 prerequisite, not a qualified SDK/service pair |

Both lower and upper layers are retained, not collapsed into a claim that the
upper candidate executed the lower candidate's results:
[lower #6182 matrix](history/6182/feature-behavior-test-matrix.md),
[lower #6182 plan](history/6182/remediation-plan.md) and
[I-03 pre-code v0.1.0](history/6184-pre-code/specs/i-03-custom-legacy-paired-tests.md).
The pre-code specification retains the original narrower authorization and
pending checklist; its recorded freeze is not its later publication time.

## M-01 dependency blocker: preservation is not validator migration

**Later user-selected disposition (2026-11-09):** preserve the complete #6185
package as an inactive historical snapshot and close its SDK PR. The
[complete package and byte manifest](../dotnet/history/pr-6185/README.md) now
preserve the scripts, fixtures, records, YAML and guide addition without claiming
a runnable relocation. The following blocker remains accurate for a hypothetical
validator migration, but no such migration or retained active SDK validator is
required by the selected snapshot disposition. SDK PR closure is handled
separately by the coordinator, not performed by this preservation contribution.

At source head `cd33034ca645b2e487d428c96a37161002e27966`, the SDK's
[`scripts/Validate-Assurance.ps1`](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/scripts/Validate-Assurance.ps1)
defaults `RepositoryRoot` to the SDK checkout and `RecordsDirectory` to
`docs/assurance`; it recursively validates every JSON record there. Its
[self-checks](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/scripts/tests/Validate-Assurance.Tests.ps1)
also depend on that SDK-local layout.

The preserved JSON contains `repository: "self"` references, source-relative
paths and file-byte SHA-256 values for the original SDK Markdown, scripts and
assertions. `self` still describes the **source SDK context**, not this
repository. Copying these records to SuicideSquad does not rebind their
references, authenticate their evidence or make metadata validation pass here.
JSON is deliberately byte-identical; historical revisions, approval receipts,
cohorts, assertions and hashes have not been retargeted to manufacture success.
Markdown link-only relocation is recorded with separate preserved digests.
In particular, the original M-01 README format contract is archived under
`history/6185/README.md`, not replaced by this index as hash-equivalent content.

**Before SDK deletion:** the SDK owner must explicitly reconcile the validator's
record consumption, test-fixture assumptions, repository boundaries and hashed
reference paths with this ownership decision, or report a blocked dependency.
Do not silently remove records, change the validation directory to an empty or
smaller set, skip checks, recalculate historical receipts as current proof, or
claim that a remote link alone supplies local hashed files. This task does not
choose or implement that follow-up design, move executable scripts/fixtures,
or authorize their deletion. Protected invocation/admission remains pending.

## Source context and verification

Additional inactive snapshots preserve
[both in-memory emulator README source layers](../dotnet/history/in-memory-emulator/README.md)
before SDK trimming; practical run guidance remains in the SDK.

Imported Markdown retains substantive source text and source status; relative
links to SDK code/CI now use immutable source-head URLs, while preserved
document links resolve within this repository. Historical JSON references
remain data, not repaired Markdown hyperlinks. The original source README is
an archival contract, not a second maintained SDK execution guide.

The [ledger](provenance.md) records all five live heads, each source and
destination, both matrix/plan layers, the I-03 pre-code pin and exact source/
destination SHA-256 values. Checks cover preservation, JSON parsing and local
Markdown targets/anchors, not SDK test execution or M-01 validation.

For conceptual grounding, the canonical
[status/retry chapter, Overview](https://github.com/tvaron3/cosmosdb-design-docs/blob/69eaf23aa23830e1531b2e43911655282aee2b37/17-status-codes-and-sdk-retries.md#1-overview)
distinguishes SDK and gateway retry surfaces. That reference was refreshed
before preservation; this import does not reinterpret or expand either retry
contract.
