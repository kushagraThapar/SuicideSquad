# Contributing

Read [AGENTS.md](AGENTS.md) and the
[autonomous-development guidelines](docs/autonomous-development-guidelines.md).
These requirements apply to humans and coding agents. They do not establish new
merge permissions or imply branch protections or automated gates are configured.

## Workflow

1. **Establish the baseline.** Read relevant instructions, design decisions, and
   affected files. Inspect existing work without overwriting it. Record the
   source revision and relevant environment. Define the requested outcome,
   acceptance criteria, constraints, and explicit non-goals before changing code.
2. **Check readiness.** Identify the target repository's exact setup, build, lint,
   and test commands, required dependencies, supported platforms, and access
   limits. Run an appropriate baseline smoke check before incremental coding or
   resuming a task. Missing tooling or permissions means blocked or partially
   verified, not successful.
3. **Implement one verifiable slice.** Use a feature branch or the session's
   existing isolated feature branch. Respect ownership and dependencies. Keep
   changes focused, preserve unrelated work, and update directly related docs.
   Do not add a framework, agent hierarchy, or tools without a demonstrated need.
4. **Verify the outcome.** Run the smallest relevant checks, then escalate when
   warranted. Include regression, negative, and failure cases and end-user
   behavior where applicable. Explain intentional contract/test changes.
   Preserve acceptance criteria and evaluator independence.
5. **Leave an auditable handoff.** Record changes, source revision, commands and
   results, relevant configuration, decisions, known limitations, and remaining
   work in the PR or approved durable task store. Exclude secrets. A completion
   assertion without evidence is not verification.
6. **Submit for independent review.** Commit only intended files; push committed
   changes immediately to the remote feature branch and open a PR. Route every
   PR review/re-review through PR Review Router. Honor existing approvals and
   branch protections. If review tooling is unavailable, stop and report it;
   do not substitute agent self-approval. Release automation remains deferred.

## Validation available in this repository

At the introduction of these guidelines this repository contains documentation
and a license, with no executable application, dependency manifest, or configured
build/test/lint commands. For documentation-only changes, inspect the diff,
relative links/anchors, Markdown structure, source attribution, and consistency
between current requirements and proposals. Do not invent a passing test suite.
Update this section with exact supported commands when executable code is added.

## PR checklist

- [ ] Scope, acceptance criteria, non-goals, and affected contracts are explicit.
- [ ] Applicable guidance and relevant first-party sources were consulted;
      Cosmos-specific claims cite the canonical concept document and section.
- [ ] Baseline and final evidence are recorded, including unavailable checks,
      failures, environment/platform constraints, and untested gaps.
- [ ] Tests/acceptance criteria were not weakened for a green result; intentional
      changes are justified and submitted for independent review.
- [ ] Isolation, least privilege, authorized budgets, and safe recovery were
      respected; no secrets or production data were added.
- [ ] Changes and documentation form a focused, independently verifiable slice;
      parallel work has explicit ownership and dependencies.
- [ ] Current behavior, written policy, proposed controls, and experimental
      evidence are labeled accurately.
- [ ] The feature branch is pushed and the PR states the required independent
      review path; no merge/deploy/release authority is inferred from CI.

For rationale and source provenance, see the
[rule families](docs/autonomous-development-guidelines.md#required-contribution-rule-families).
