# Instructions for contributing agents

Suicide Squad is **design first**. Start with the [README](README.md) for scope.
This repository holds project files and documentation; that does not mean an
autonomous execution platform or its controls already exist.

## Required reading

- [Contribution workflow and checklist](CONTRIBUTING.md): requirements for every change.
- [Autonomous-development guidelines](docs/autonomous-development-guidelines.md):
  detailed rules, proposed architecture, evidence, and limits of external examples.
- [Cosmos DB concept reference](https://github.com/tvaron3/cosmosdb-design-docs):
  consult relevant numbered documents for Cosmos-specific work; cite the document
  and section and cross-check implementation-specific claims in the target SDK.

## Essential rules

These are contribution requirements, not claims of automated enforcement.

- You MUST define scope and observable acceptance criteria before implementation.
  Work incrementally; preserve unrelated changes and existing contracts.
- You MUST inspect applicable repository and directory instructions, establish
  the baseline, and use the smallest relevant checks before broader checks.
  Report actual evidence, failures, platform limits, and untested gaps accurately.
- You MUST NOT weaken verification, delete failing tests, alter acceptance
  criteria, or silently change contracts just to obtain green results. Legitimate
  changes require explicit justification and review under existing policy.
- You MUST use isolated, reproducible workspaces and least privilege. A git
  worktree is NOT a security sandbox. Do not use secrets or production access
  by default; never commit credentials or sensitive operational data.
- You MUST bound delegated work, retries, CI attempts, resource use, and spending
  within authorized limits. Stop and report blocked, failed, or escalated work;
  never return success-shaped fallbacks.
- You MUST preserve durable handoff evidence and verify state before resuming.
  Do not blindly replay operations with external side effects.
- You MUST use a feature branch and a pull request, never push directly to
  `main`/`master`. After committing, push immediately to the remote feature branch.
- You MUST route PR reviews and re-reviews through **PR Review Router**, preserve
  independent review/merge authority and existing approval requirements, and stop
  if the required reviewer is unavailable. CI or agent consensus grants no
  merge, deployment, or release permission.
- You MUST distinguish current requirements from proposed designs and historical
  experiments. Update directly related documentation; do not claim a control,
  migration, benchmark result, or completed feature without evidence.

Use the detailed guidance as the single source for rationale. Keep this map
short; place specialized knowledge in linked, scoped documents rather than
expanding a universal instruction manual.
