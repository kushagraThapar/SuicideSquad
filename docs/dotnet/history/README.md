# Inactive .NET historical snapshots

These are archival source packages, **not installed tools, runnable relocated
validators, active pipelines or current test-running instructions**.
The user selected "Preserve it as a snapshot and close #6185 (Recommended)";
this contribution preserves the package only. The coordinator handles any
separately authorized SDK PR closure. No SDK branch is edited here.

| Snapshot | Source | Inventory and hashes |
|---|---|---|
| [Complete M-01 package](pr-6185/README.md) | [Azure/azure-cosmos-dotnet-v3#6185](https://github.com/Azure/azure-cosmos-dotnet-v3/pull/6185), head `cd33034ca645b2e487d428c96a37161002e27966` | [Package manifest](pr-6185/manifest.json) |
| [In-memory emulator README layers](in-memory-emulator/README.md) | Lower `b578be79bf8c83a3fecf7dd0af1709f3d5fc628a` and upper `8f0ce99d3392551508e114293d55595c3b16eb40` | [Both source versions and hashes](in-memory-emulator/manifest.json) |

Original bytes, source-relative layout and historical links remain unchanged.
Use each manifest's immutable `sourceUrl` for original link context; unresolved
relative links within a snapshot are not instructions to vendor the surrounding
SDK. Current discoverability and ownership are in the
[project specification index](../../assurance/README.md). Imported Microsoft
material retains its [upstream MIT notice](../../assurance/UPSTREAM-LICENSE.txt).
There is no new assurance architecture, activation, campaign or qualification.

## Preservation verification

The source PR head/base were re-read through GitHub before and after import
and still matched the manifest. All 12 package files and both README versions
were independently checked against source Git blobs, SHA-256 values and byte
counts. The package manifest's source-path set exactly matches the complete
base-to-head PR diff. The separate guide patch matches the original base/head
diff; all JSON parses. Both YAML files exist only under this inactive archive.
New/current index links were checked; original archived relative links remain
unchanged and use manifest source URLs for context. No PowerShell validator,
SDK test, emulator build, pipeline or campaign was executed.

The stored guide diff intentionally retains three one-space blank context lines
from Git's patch format. An unfiltered staged `git diff --check` reports these
as trailing whitespace in `guide-addition.patch`; changing them would corrupt
the exact diff receipt. The staged whitespace check excluding that byte-verified
patch passes. No original source file was reformatted to hide the warning.
