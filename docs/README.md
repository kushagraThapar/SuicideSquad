# Suicide Squad documentation

This repository is the canonical home for Suicide Squad project documents and
research. The project is **design-only**: SDK implementation, SDK test execution,
CI or permission changes, autonomous merging, deployments and releases are not
authorized by these documents.

**Current priority: .NET first. Java is paused at a versioned design/research
checkpoint with explicit remaining gaps**, the milestone selected by the user
on 2026-10-31. This is not a fully source-verified Java catalog or design
approval. The next .NET workstream must establish its own SDK-specific baseline,
contracts and tooling; Java findings are not automatically .NET guarantees.

**This is the assurance/orchestration project, not an SDK mirror.** Keep SDK
implementation, regression tests and build/CI files in their SDK repositories.
Agents access those repositories through code intelligence or isolated checkouts
at pinned revisions; Suicide Squad keeps catalogs, scenarios, benchmark
definitions, agent/review protocols, findings and evidence/source references.
See the [source-access boundary](research/java-sdk/source-access.json).

| Start here | Purpose |
|---|---|
| [Java design and checkpoint](suicide-squad-design.md) | Version 0.2.3, retained full-Java-SDK design, paused backlog and .NET-first sequencing |
| [Java SDK research checkpoint](research/java-sdk/README.md) | Findings, pinned upstream links, attribution and provenance; no vendored SDK source |
| [Parent-authored discovery checkpoint](research/java-sdk/recovery/discovery-checkpoint/README.md) | Original-intake discovery receipts; not recovered agent reports or semantic closure |
| [Report recovery status](research/java-sdk/reports/README.md) | What is missing; DS-14 is incomplete, not awaiting the old agents |
| [Checkpoint provenance](research/java-sdk/recovery/discovery-checkpoint/package-manifest.json) | Separate handoff, prior historical import and corrected source-link-only layout |
| [Paused-Java backlog](suicide-squad-design.md#194-stable-checkpoint-and-net-first-transition) | Resume Java only when explicitly reactivated; no new Java investigation is required to hand off |
| [.NET design context handoff](https://github.com/kushagraThapar/SuicideSquad/blob/d9d02138e7fa72b32bfcc72dd63028d208004297/docs/dotnet/design-handoff.md) | Immutable separate contribution; not a claim that the file is on the default branch or that SDK investigation has begun |

The imported design is the reference for this revision; session canvases should
link to it rather than fork it. A feature-branch PR is not default-branch
integration or approval of the design. Root contributor/agent instructions and
autonomous-development guidance are a separate contribution and are not
duplicated here.
