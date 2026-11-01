# Research recovery and continuation

[Research index](../README.md) |
[Incomplete reports](../reports/README.md) |
[Canonical design](../../../suicide-squad-design.md)

This is a documentation/research recovery checklist, not permission to implement
SDK changes, execute SDK tests, change governance or merge. The four original
agents are unavailable; the preserved files are their inputs, not their reports.
The parent owns a later bounded research handoff separately from this import.

## Resume checklist

- [ ] Read the canonical design's scope, decisions and DS-13/DS-14/DS-15 status.
- [ ] Check the import manifest and payload hashes before treating a cached file
      as evidence. Use the verified replacement, not the two excluded
      `RxGatewayStoreModel.java` cache copies.
- [ ] Keep this immutable SDK baseline distinct from any future upstream refresh;
      give a refresh its own revision and provenance.
- [ ] Receive any later completed parent recovery package in a separate
      contribution. Inspect its content, attribution, baseline and completeness;
      retain its actual authorship rather than claiming the old agents finished.
- [ ] Produce or recover bounded domain discovery reports from verified inputs.
      Keep source enumeration, contract verification, test mapping, execution and
      autonomy qualification in separate columns.
- [ ] Reconcile the entire pinned core changelog and companion encryption history
      into semantic records with source line spans, classification, lifecycle,
      feature/invariant links, verification strength and unresolved entries.
- [ ] Reconcile current exported APIs/options/internal workflows in the other
      direction; retain explicit unknown, unmapped, deprecated and removed cases.
- [ ] Complete the whole-SDK domain matrix and independent Java-specific atomic
      contract/oracle verification. Family-level seed catalogs are not closure.
- [ ] Update progress only when acceptance evidence exists; leave unmeasured
      values unknown. Resolve design decisions and obtain DS-13 approval before
      any implementation or SDK execution work.

No step above was completed merely by preserving inputs. In particular, do not
create empty reports or an all-green ledger to satisfy file-presence checks.

## Reconstructing the old cache layout

The [import manifest](../import-manifest.json) records each retained payload's
original source-relative paths in `origins`. For an untransformed record, copying
its verified bytes to each listed path reconstructs identical old cache copies.
Use a new empty research workspace, reject absolute/traversing paths, verify
SHA-256, and never overwrite unrelated files. No reconstruction was run here.

Three exceptions are deliberate and explicit:

1. The two mismatching Java cache copies are represented by exclusion records,
   not retained bytes. Inspect their untouched original capture if needed; the
   public pinned replacement recovers the intended source, not the excluded
   original content.
2. The historical helper has portable path edits. Its original size/digest are
   retained in the manifest, while its imported bytes have their own digest.
   The untouched original capture is the source for exact historical bytes.
3. One archival CI input redacts a public emulator-default key literal. Its
   `upstream.git_blob_sha` and `origin_sha256` identify the original; its payload
   `git_blob_sha` and `sha256` identify the redacted research copy.

Pinned upstream content is also recoverable from the `upstream.repository`,
`upstream.commit` and `upstream.path` fields. Fetch only that immutable public
path, then validate the expected original Git blob and, where present, original
SHA-256. Reapply declared redactions before publication and validate the imported
digest separately. A moving default-branch download is not equivalent evidence.

## Preserved historical helper

[`fetch_surface.py`](fetch_surface.py) originally downloaded a selected
top-level/model/util Java API surface plus a few internal constants. Its
selection, pin and blob-verification logic are preserved; only executable and
input/output paths were made portable.

It now resolves `gh` from `PATH`, reads `metadata/core-tree.json`, and targets
`snapshot/sdk/cosmos/azure-cosmos/` relative to this research directory. It does
not recover domain reports, classify changelog entries, enumerate the whole SDK
or produce test evidence. A failed authentication, unavailable source or hash
mismatch remains an explicit error.

The helper is not executable by file mode and was not run during this import.
Inspection and syntax-only parsing do not constitute execution. Any later use
must be a separately scoped research action; do not install dependencies, supply
credentials, run Maven, or build/execute snapshots just because this file exists.
