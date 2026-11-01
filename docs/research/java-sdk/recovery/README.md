# Recovery receipts: historical context and current boundary

[Research index](../README.md) |
[Current status](../reports/README.md) |
[Source access](../source-access.json) |
[Canonical design](../../../suicide-squad-design.md)

**Java is paused; .NET is next. SDK source belongs in its target repository,
not in Suicide Squad.** The stable Java milestone is a versioned design/research
checkpoint with explicit gaps. DS-14 remains incomplete and implementation,
SDK test execution, policy changes, merging and releases are not authorized.

## Four unchanged parent-authored receipts

The files in [`discovery-checkpoint/`](discovery-checkpoint/) are a bounded
parent-authored recovery from the original cached inputs, not reports produced
by the four unavailable agents:

| File | Meaning |
|---|---|
| [README.md](discovery-checkpoint/README.md) | Discovery narrative, qualified source-local observations, unresolved oracle questions and backlog |
| [changelog-discovery-ledger.json](discovery-checkpoint/changelog-discovery-ledger.json) | 145 release headings / 721 bullets; 705 lexical hints, all 721 semantically unverified |
| [source-discovery-inventory.json](discovery-checkpoint/source-discovery-inventory.json) | Original cache identities, exported-package file enumeration and numeric declarations, not API/test coverage |
| [recover_inventory.py](discovery-checkpoint/recover_inventory.py) | Historical offline exporter requiring the original input layout; preserved as data and not executed |

Their handoff bytes are unchanged: **four files / 1,313,021 bytes**. The
[package manifest](discovery-checkpoint/package-manifest.json) records exact
digests, original-intake semantics and current checkpoint provenance.

## Do not confuse historical paths with the current layout

The copied report predates the source-link-only correction. It describes the
importer's then-planned snapshot replacement and contains a reproduction command
against the original cache. Those statements are preserved history, **not claims
that canonical `snapshot/` files still exist** and not instructions to vendor SDK
code again.

The exporter expects `source/CHANGELOG.md`, tree manifests and the old
`changelog`, `contracts`, `data` and `client` cache buckets. Its `cache_path`
values and manifest filenames are historical input identifiers. It cannot be
pointed at the normalized project metadata as though the old source tree were
present. Do not run it or regenerate its receipts against corrected sources to
make the original two mismatches disappear.

Use the [historical import manifest](../import-manifest.json) to resolve original
identities and the [source-access record](../source-access.json) to locate
immutable upstream paths/blob IDs. Inspect source through code intelligence or
a separate target-SDK checkout when later work is authorized. No SDK code copies
are required in Suicide Squad.

The initial archive and its earlier recovery guide/downloader remain available
at commit `a10d3042a61540b907edbe17b710c6294b997a7f`; current source snapshots
and that obsolete downloader have been removed. The original manifest and
validation are unchanged historical receipts, not live local-file guarantees.
The two excluded mismatching cache byte sequences were never published; only
their untouched original capture can reproduce those exact bytes.

## Remaining gaps and later resumption

- [ ] Resume Java only after explicit reactivation; the checkpoint is not a
      request for further Java investigation before the .NET transition.
- [ ] Split preserved changelog bullets into atomic semantic obligations with
      verified lifecycle/source/contracts. Lexical hints are navigation only.
- [ ] Reconcile companion encryption history, resolved APIs/options/internal
      workflows, the domain matrix and independent Java-specific oracles.
- [ ] Resolve Java/version retry guidance and the partial-trace 408/21013 oracle
      discrepancy before treating either as a passing invariant or product bug.
- [ ] Map assertions and fixture capabilities; measure candidate-specific
      execution only after separate authorization. Keep unknown measurements
      unknown and retain DS-13 design/implementation approval gates.

No exporter or SDK code was run during this promotion. The report's references
to whole-Java-pilot experiments remain the paused Java lane's design context,
not current execution or merging permission. Transfer the reusable assurance
model to .NET, not Java defaults or SDK source files.
