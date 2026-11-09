# .NET specification preservation provenance

Recorded 2026-11-09. Destination baseline: SuicideSquad default branch
`79fe48b9cb00896e1bb04095ae2fde684b480914`, fetched and fast-forward checked in
the isolated preservation worktree before import.

The [preservation index](README.md) defines current ownership and dependency
limits. Sources below were independently resolved from the live SDK PR APIs
and fetched as Git objects; no SDK branch was edited. Full source and preserved
file-byte SHA-256 values distinguish original evidence from link relocation.
JSON is byte-identical. Markdown changes are limited to link targets; the body,
versions, contracts, assertions, failed attempts, historical authorizations,
unqualified outcomes and unresolved gaps remain source material, not new approval.

The current matrix and remediation plan come from the upper
Azure/azure-cosmos-dotnet-v3#6184 layer, whose base is exactly the captured
Azure/azure-cosmos-dotnet-v3#6182 head. Both lower-layer documents are also
retained separately. I-01 and I-02 spec blobs in that upper tree are identical
to the captured lower head. The I-03 pre-code specification at
`721e7b2f51239895bb99cafa0eb91ae6afd5d082` is retained separately from the
upper head's v0.1.3, preserving its original pending checklist and narrower
automatic-only CI authorization. Its earlier freeze and later publication
remain distinct. None of those historical permissions authorizes a new run.

The M-01 source README is retained as a historical format-contract snapshot,
not the current repository index or a second agent test-running guide.
Executable SDK tests, validator scripts, fixtures and CI configuration were
not imported. Source paths and immutable references to those files remain SDK
references, not claims that executable dependencies exist in SuicideSquad.
SDK `docs/builds-and-pipelines.md` changes are test/CI-running guidance and
remain in the SDK; this import does not replace or copy that guide.

## Verification scope

The import checks every destination against source Git bytes after only
deterministic Markdown link-target relocation; JSON bytes remain unchanged.
Local Markdown file targets and anchors are checked, and SDK-relative targets
are converted to immutable source-tree URLs after checking their existence.
Those immutable SDK links intentionally retain source context and are not
claims of present SDK layout after trimming. JSON references and hashes retain
their original meaning and dependencies; see the M-01 blocker in the index.
No SDK tests, validator execution, CI campaign or protected admission is
performed by this preservation task.

### Preservation check results

At publication preparation on 2026-11-09, all five PR heads and the destination
default branch were re-read through the GitHub API and still matched this
ledger and baseline. The 15 imported documents matched the deterministic
source-byte/link-relocation comparison; both JSON records were byte-identical
and parsed with duplicate-key rejection. All 155 local links/anchors across
16 Markdown files (including the documentation index) resolved. The lower
I-01/I-02 spec blobs were also compared directly with the upper tree and were
identical. `git diff --check` passed.

The local checks used Python 3 standard-library JSON/hash/path handling and Git
source objects, without installing tooling or running the SDK/PowerShell
validator. No relevant `ado` server is exposed in the available tool catalog;
the source-only GitHub task used `/opt/homebrew/bin/gh` and Git. The required
canonical concept checkout was fast-forward refreshed on `main` to
`69eaf23aa23830e1531b2e43911655282aee2b37`; chapter 17, section 1 was
consulted without changing any source contract.

Imported Microsoft documentation retains the upstream
[MIT copyright and permission notice](UPSTREAM-LICENSE.txt), copied from
[`LICENSE` at the captured M-01 head](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/LICENSE).

## Imported file ledger

| Source PR / revision | Source path | Destination | Source SHA-256 | Preserved SHA-256 |
|---|---|---|---|---|
| [Azure/azure-cosmos-dotnet-v3#6182](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6182) / `7330088136240c8586ed5eea63f2a4f9a0c366e5` | [docs/assurance/feature-behavior-test-matrix.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/7330088136240c8586ed5eea63f2a4f9a0c366e5/docs/assurance/feature-behavior-test-matrix.md) | [history/6182/feature-behavior-test-matrix.md](history/6182/feature-behavior-test-matrix.md) | `8148ed4b6c5f83ad9e6386805433df912018415671548e5808a45be5f9ae9f11` | `dd3376e4f1d7e4530decb4c1ad34d18f90b536f5599a2c314a1fb80f909fdba4` |
| [Azure/azure-cosmos-dotnet-v3#6184](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6184) / `cd7489e84f9fb7e308b23d3070d4278c70c7eec0` | [docs/assurance/feature-behavior-test-matrix.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd7489e84f9fb7e308b23d3070d4278c70c7eec0/docs/assurance/feature-behavior-test-matrix.md) | [feature-behavior-test-matrix.md](feature-behavior-test-matrix.md) | `f37c95ba9b0e8c65afccdf6d4e1ac1ce1375c8b57f1642a0703770eb5f730987` | `f37c95ba9b0e8c65afccdf6d4e1ac1ce1375c8b57f1642a0703770eb5f730987` |
| [Azure/azure-cosmos-dotnet-v3#6182](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6182) / `7330088136240c8586ed5eea63f2a4f9a0c366e5` | [docs/assurance/remediation-plan.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/7330088136240c8586ed5eea63f2a4f9a0c366e5/docs/assurance/remediation-plan.md) | [history/6182/remediation-plan.md](history/6182/remediation-plan.md) | `95bcdfba1b7ed1b0d58614720b1ec3875854231669ad80899b9e07678579159d` | `b48fa19450a12c334f47d946512cdf86ae81ac605581a71a89abd462fc877ec2` |
| [Azure/azure-cosmos-dotnet-v3#6184](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6184) / `cd7489e84f9fb7e308b23d3070d4278c70c7eec0` | [docs/assurance/remediation-plan.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd7489e84f9fb7e308b23d3070d4278c70c7eec0/docs/assurance/remediation-plan.md) | [remediation-plan.md](remediation-plan.md) | `0e943190f19f1c4c906535bd3a7c4a7a9cc4f7342a22b17426b56812b3e959d7` | `3e0e79509142317ccd0aa0ad8b83024f46d2a1a9815fdd1b9fb137b3fb308167` |
| [Azure/azure-cosmos-dotnet-v3#6182](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6182) / `7330088136240c8586ed5eea63f2a4f9a0c366e5` | [docs/assurance/specs/i-01-encryption-patch-paired-tests.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/7330088136240c8586ed5eea63f2a4f9a0c366e5/docs/assurance/specs/i-01-encryption-patch-paired-tests.md) | [specs/i-01-encryption-patch-paired-tests.md](specs/i-01-encryption-patch-paired-tests.md) | `21ce9d37caa9c1a919f2de873c6d03d6027e10b9f4c2ec62303f639936867c2c` | `1a3fbbd07399a22f5774742f3e3f09244267df7d6f13803c4ee54d3025cc74be` |
| [Azure/azure-cosmos-dotnet-v3#6182](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6182) / `7330088136240c8586ed5eea63f2a4f9a0c366e5` | [docs/assurance/specs/i-02-custom-cache-paired-tests.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/7330088136240c8586ed5eea63f2a4f9a0c366e5/docs/assurance/specs/i-02-custom-cache-paired-tests.md) | [specs/i-02-custom-cache-paired-tests.md](specs/i-02-custom-cache-paired-tests.md) | `de17d6514af4c8a4b48cf88b748eb09fdcf2bbfa1ea7ff20dec8b87002f8ff10` | `de17d6514af4c8a4b48cf88b748eb09fdcf2bbfa1ea7ff20dec8b87002f8ff10` |
| [Azure/azure-cosmos-dotnet-v3#6184](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6184) / `cd7489e84f9fb7e308b23d3070d4278c70c7eec0` | [docs/assurance/specs/i-03-custom-legacy-paired-tests.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd7489e84f9fb7e308b23d3070d4278c70c7eec0/docs/assurance/specs/i-03-custom-legacy-paired-tests.md) | [specs/i-03-custom-legacy-paired-tests.md](specs/i-03-custom-legacy-paired-tests.md) | `12d4587a33e327cdb7fcc791b26c6e1e9414abd53def166594fe5ab948775c5e` | `2a95510a39e4eb8d655d8b7913f9633f5ac8224cb9d0e35c9c602a66b89ad5ab` |
| [Azure/azure-cosmos-dotnet-v3#6184](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6184) / `721e7b2f51239895bb99cafa0eb91ae6afd5d082` | [docs/assurance/specs/i-03-custom-legacy-paired-tests.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/721e7b2f51239895bb99cafa0eb91ae6afd5d082/docs/assurance/specs/i-03-custom-legacy-paired-tests.md) | [history/6184-pre-code/specs/i-03-custom-legacy-paired-tests.md](history/6184-pre-code/specs/i-03-custom-legacy-paired-tests.md) | `fc42ebd194dae1603c98d433aeda49f46c1e34e7b3f7f9486c4c436d2688a8b4` | `95098bc647d38b7cb1b038004179a5e15d5a9e2d1017a356be8692b0e5c8d3a3` |
| [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185) / `cd33034ca645b2e487d428c96a37161002e27966` | [docs/assurance/specs/m-01-assurance-foundation.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/docs/assurance/specs/m-01-assurance-foundation.md) | [specs/m-01-assurance-foundation.md](specs/m-01-assurance-foundation.md) | `a57cc64c75105d7a6630e45984a9e5ae95ec7e13ccf047648c1b15360516be77` | `305e9cfd0722c94db4739278567669891ac646d3cffe0b31285aff34965ffa42` |
| [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185) / `cd33034ca645b2e487d428c96a37161002e27966` | [docs/assurance/specs/m-01-assurance-foundation.json](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/docs/assurance/specs/m-01-assurance-foundation.json) | [specs/m-01-assurance-foundation.json](specs/m-01-assurance-foundation.json) | `7b7db6fa84ce0553e4bbc8ff5f8c5546c6c04d2c8bc5906856ae1cccfe0a8c2e` | `7b7db6fa84ce0553e4bbc8ff5f8c5546c6c04d2c8bc5906856ae1cccfe0a8c2e` |
| [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185) / `cd33034ca645b2e487d428c96a37161002e27966` | [docs/assurance/specs/m-01-review-feedback.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/docs/assurance/specs/m-01-review-feedback.md) | [specs/m-01-review-feedback.md](specs/m-01-review-feedback.md) | `a779dea45d068011256a769dfd64adb08635c86b7dc4503c0998be6bf2af242e` | `1a87a318e1b8f4e0bcfdf04160f925e665cb8b31e6c1d03834acbad2b6cc3ec7` |
| [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185) / `cd33034ca645b2e487d428c96a37161002e27966` | [docs/assurance/examples/i-01-64324.json](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/docs/assurance/examples/i-01-64324.json) | [examples/i-01-64324.json](examples/i-01-64324.json) | `c0601b16dc39985c3aa2adb24a3959775fa81200953469024b6c69e9b7404770` | `c0601b16dc39985c3aa2adb24a3959775fa81200953469024b6c69e9b7404770` |
| [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185) / `cd33034ca645b2e487d428c96a37161002e27966` | [docs/assurance/README.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/cd33034ca645b2e487d428c96a37161002e27966/docs/assurance/README.md) | [history/6185/README.md](history/6185/README.md) | `efbcde81f73a145bcba9f72737057b1855ac3907f2c0ffe5cd549022a9bb8f1d` | `6603cc8129e437f3ded41225ac11eb9ae7bc30d1e9f89f9bf07b421a5ac083e6` |
| [Azure/azure-cosmos-dotnet-v3#6187](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6187) / `650db04e6d43c25e14c67b2df44ad743a8c2e557` | [docs/assurance/specs/http-retry-disposal-ordering.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/650db04e6d43c25e14c67b2df44ad743a8c2e557/docs/assurance/specs/http-retry-disposal-ordering.md) | [specs/http-retry-disposal-ordering.md](specs/http-retry-disposal-ordering.md) | `0511e61635f580bda26de5bfbc952e7f9bceade3c1e5c44178c04611a3243f8a` | `0511e61635f580bda26de5bfbc952e7f9bceade3c1e5c44178c04611a3243f8a` |
| [Azure/azure-cosmos-dotnet-v3#6190](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6190) / `7fffa11f89cc68b86ad505c64c553d9eaa854a8b` | [docs/assurance/specs/local-http2-disposal-fixture.md](https://github.com/Azure/azure-cosmos-dotnet-v3/blob/7fffa11f89cc68b86ad505c64c553d9eaa854a8b/docs/assurance/specs/local-http2-disposal-fixture.md) | [specs/local-http2-disposal-fixture.md](specs/local-http2-disposal-fixture.md) | `692718285c74349d0be427d11b97a17aa40d0048bf9f26dae28eb38ab9418081` | `692718285c74349d0be427d11b97a17aa40d0048bf9f26dae28eb38ab9418081` |
