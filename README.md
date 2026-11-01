# SuicideSquad
Suicide Squad is a project to help AI agents develop Cosmos DB SDKs without much human intervention.

This is the canonical repository for Suicide Squad project files and documentation.
The project is currently **design first**: its research/design scope includes full
Cosmos Java SDK feature and invariant coverage, historical bug benchmarks, and
multidimensional non-regression coverage. Broad coverage goals do not grant
autonomous execution or merge authority. Release automation is deferred.

## Start here

- **Coding agents:** read [AGENTS.md](AGENTS.md), the short map of essential rules.
- **All contributors:** follow [CONTRIBUTING.md](CONTRIBUTING.md) and its PR checklist.
- **Designers and evaluators:** consult the
  [autonomous-development guidelines](docs/autonomous-development-guidelines.md)
  for required rule families, proposed controls, and first-party evidence.
- **Cosmos-specific work:** consult the
  [canonical concept reference](https://github.com/tvaron3/cosmosdb-design-docs).

Written policies are not implemented mechanical controls. Independent PR Review
Router review, separate merge authority, and existing approval requirements must
be preserved; passing CI or agent consensus is not permission to merge or release.
Separately managed design/inventory artifacts are not claimed to have been
migrated here.

The coordinated import plans to publish the design at
`docs/suicide-squad-design.md` and Java SDK research under
`docs/research/java-sdk/`. These are planned destinations, not yet available
documents or evidence of completed inventories; link them here when published.
