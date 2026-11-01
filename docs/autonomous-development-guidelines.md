# Autonomous-development guidelines

Evidence and policy recorded: **2026-10-31**. External observations below are
historical, first-party company reports, not independent benchmarks, performance
targets, or proof that the same outcomes transfer to this project.

## Scope and status

Suicide Squad is the canonical repository for this project's files and docs.
It is currently **design first**, with a research/design scope covering the full
Cosmos Java SDK feature and invariant surface, historical bug benchmarks, and
multidimensional non-regression coverage. This is not a retry-only or low-risk-only
pilot. Broad research scope does not grant autonomous execution authority over
that surface.

Independent PR Review Router review and separate merge authority remain part of
the project direction. Release automation is deferred. This documentation change
does not implement the platform, change SDK code, configure permissions, or grant
agents authority to merge, deploy, or release.

Existing design/inventory artifacts are managed separately. Their contents and
migration status are not asserted here; this assignment does not move or replace
them. Future documents should link to those artifacts once their owners publish
them here rather than inventing or duplicating their details.
The coordinated import's planned destinations are `docs/suicide-squad-design.md`
and `docs/research/java-sdk/`; these paths are not claimed to exist yet.

**Status vocabulary**

| Label | Meaning |
|---|---|
| Required contribution rule | Applies now to changes by humans and agents. |
| Proposed architecture | Design guidance requiring implementation, validation, and explicit authorization before use. |
| External observation | A bounded report from another organization, not a local capability or policy. |
| Implemented control | Requires inspectable code/configuration and enforcement evidence; prose alone never qualifies. |

The rules below are written policy. This repository does not yet implement the
execution controls described in the proposed architecture.

## Required contribution rule families

### 1. Define success independently of the implementation

Write observable acceptance criteria before implementation. Preserve approved
contracts and verification. Do not delete, weaken, skip, or rewrite tests or
criteria solely to make a run pass. Legitimate changes to contracts or tests must
be explicit, justified, and reviewed through existing policy. Agent-authored tests
are useful, but neither those tests nor another LLM's agreement alone establish
independent correctness.

For benchmark work, keep held-out scenarios outside the implementing agent's
write authority. Report potential evaluation contamination. Use deterministic
and reference/differential checks where suitable; LLM judgments may supplement
them, not replace all correctness or security checks. Validate simulator fidelity
and document differences from real dependencies.

Sources: [StrongDM factory](https://factory.strongdm.ai/),
[StrongDM techniques](https://factory.strongdm.ai/techniques),
[Anthropic compiler experiment](https://www.anthropic.com/research/building-c-compiler).
The protected evaluator service and dependency digital twins are proposals,
not systems this repository already provides.

### 2. Bound execution and surface failure

Define an owner, scope, permitted actions, completion evidence, and finite
resource/time/cost/retry limits for an autonomous task. Use the authorized budget;
if none exists, do not initiate an open-ended or billable agent campaign.
Local fast feedback should precede expensive remote checks. Stop and report
blocked, failed, or escalated work instead of retrying indefinitely, silently
degrading behavior, or returning a success-shaped fallback.

Reasoning belongs inside bounded steps; permission changes and gate decisions
must not depend only on an agent's prose. Do not copy another organization's
retry count as a universal policy.

Sources: [Stripe part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents),
[Stripe part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2),
[Microsoft runtime experience](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/).

### 3. Isolate work and minimize authority

Use reproducible task environments with scoped access. A worktree prevents some
file conflicts but is not a security sandbox. Do not use production services,
production data, secrets, or broad credentials by default. Never commit secrets.
Any required access must be explicitly authorized and least-privileged, with
scoped short-lived credentials where available. Tools and network destinations
must stay within approved scope; sandboxing and egress enforcement must not be
claimed unless actually configured.

Sources: [Stripe part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2),
[Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent),
[OpenAI harness engineering](https://openai.com/index/harness-engineering/).

### 4. Make task state durable and recovery safe

Preserve source revision, environment/configuration, acceptance criteria, task
ownership, dependencies, decisions, checkpoints, and verification evidence in an
approved durable location, without credentials or sensitive data. On resume,
reconcile that state with current git/environment state and run an appropriate
baseline smoke check. Compaction and an agent's remembered progress are not
durable completion evidence.

Make retryable operations idempotent where appropriate. Before retrying an
external side effect, check whether it already happened; an interrupted response
is not proof of failure. Do not blindly replay pushes, PR creation, permission
changes, provisioning, or deployment operations.

Sources: [Anthropic long-running harnesses](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents),
[Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent).
Side-effect reconciliation is this project's safety requirement, not a claim
that these reports implement a general exactly-once protocol.

### 5. Prefer small slices and workload-appropriate coordination

Keep changes independently verifiable. Give parallel tasks explicit ownership
and dependencies, and parallelize only genuinely independent work within resource
and review-capacity limits. Use the simplest topology that works for measured
task independence. Avoid shared-file contention, duplicated investigations,
unbounded fan-out, and giant integration branches. Do not mandate a planner,
integrator, or lock scheme for every workload.

Sources: [Cursor scaling experiments](https://cursor.com/blog/scaling-agents),
[Anthropic compiler experiment](https://www.anthropic.com/research/building-c-compiler),
[GitHub runtime migration](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/).

### 6. Verify behavior and describe gaps honestly

Establish readiness before coding: exact repository commands, required feeds and
dependencies, supported platforms, access limits, and a baseline. Run the smallest
appropriate checks and widen when needed. Test behavior, negative/failure paths,
and regressions, including end-user flows when relevant. Retain concise evidence
of commands, results, configuration, and unsupported paths. Missing dependencies,
firewall access, or platform support are explicit limitations, not passing tests.

Keep feature/invariant coverage, historical bug reproduction, behavioral
correctness, performance/resource use, and failure handling distinguishable.
Do not collapse multidimensional non-regression into one coverage score or change
coverage denominators to make progress appear larger. SDK-specific dimensions and
thresholds belong in reviewed design/inventory documents, not invented here.

Sources: [Microsoft runtime experience](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/),
[Anthropic compiler experiment](https://www.anthropic.com/research/building-c-compiler),
[GitHub runtime migration](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/).

### 7. Keep knowledge discoverable, scoped, and maintained

Keep root [AGENTS.md](../AGENTS.md) short and link to versioned, scoped guidance.
Record provenance, dates, assumptions, and limitations; refresh stale claims when
affected work exposes them. Update related docs with code and perform focused
maintenance instead of letting generated bad patterns spread. Prefer existing
mechanisms and small improvements over speculative abstractions or tool sprawl.

For Cosmos-specific reasoning, consult the canonical
[concept index](https://github.com/tvaron3/cosmosdb-design-docs/blob/main/00-overview.md)
and relevant numbered document, cite its section, and verify SDK implementation
details separately. This guideline is not a substitute for the feature inventory.

Sources: [OpenAI harness engineering](https://openai.com/index/harness-engineering/),
[Stripe part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2),
[Microsoft Copilot harness announcement](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/).

### 8. Separate implementation from review and permission

Use a feature branch and PR; never push directly to `main`/`master`. Push commits
immediately to the remote feature branch. Route PR review and re-review through
PR Review Router, retaining independent review/merge authority and existing
approval requirements. Stop if that review path is unavailable. Passing CI,
passing scenarios, or agent consensus does not grant merge/deploy/release
permission. Do not modify approval or evaluator controls to approve your own work.

Risk-tiered future autonomy is a proposal requiring separately approved policy
and enforced boundaries, not a current exception. External reports of human-free
review are not permission to remove this project's human approval requirements.

Sources: [Stripe part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents),
[Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent),
[Microsoft runtime experience](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/).
The branch and Router requirements are local project policy; external sources
support the separation principle, not the choice of a particular review tool.

### 9. Measure accepted outcomes, not generated volume

For evaluations, define an accepted outcome and the eligible task population
before reporting results. Include failed, abandoned, and escalated runs in the
unattended-success denominator; state the measurement window and exclusions.
Track accepted outcomes per dollar, human minutes per accepted task, escaped
defects, rollbacks, and time to verified outcome. Report review load and resource
cost as well as success. Keep coverage populations and denominators stable or
explain changes explicitly. LOC, PR volume, or a judge's score alone is not
evidence of quality.

Sources motivating this project metric policy:
[Microsoft runtime experience](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/),
[Stripe part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2),
[Anthropic compiler experiment](https://www.anthropic.com/research/building-c-compiler).
These metrics are required reporting guidance when running evaluations; no
project telemetry implementation or numerical target is claimed.

## Proposed architecture, not implemented controls

Future designs should reuse mature execution primitives and focus project-owned
logic on orchestration, policy, and evaluation. Candidate controls include:

- A deterministic control plane for task ownership, dependency/state transitions,
  permissions, budgets, retry limits, and gates. Explicit states should include
  blocked, failed, and escalated as well as active and verified completion.
- An isolated reproducible execution environment with approved tools and egress,
  short-lived scoped access, and usable app/test/browser/telemetry feedback.
- Durable checkpoints and side-effect reconciliation before retries or recovery.
- A protected evaluation plane with separate write/approval authority, scenario
  provenance, deterministic and differential checks, and simulator fidelity tests.
- Mechanical dependency-boundary/structural checks and documentation freshness
  checks, where their value has been demonstrated.
- Bounded concurrency and review backpressure, observable costs and outcomes,
  and a separately authorized risk-tier policy before any future autonomy change.

Each proposal needs a reviewed design, owner, failure/recovery behavior,
enforcement evidence, and acceptance tests before it can be labeled implemented.
Source support: [OpenAI](https://openai.com/index/harness-engineering/),
[Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2),
[StrongDM](https://factory.strongdm.ai/techniques),
[Microsoft harness](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/).

## External evidence and limits

The URLs in this table and rule families are first-party provenance. Figures are
historical company-reported snapshots from the linked reports, not local results,
targets, or independent comparisons. Source pages may evolve after this record.

| Source | Reported observation | Transfer limit |
|---|---|---|
| [OpenAI harness engineering](https://openai.com/index/harness-engineering/) | An internal product with no manually written code; humans steered acceptance. A short AGENTS map, progressive disclosure, structural checks, per-worktree feedback, and gardening helped; giant manuals and spreading bad patterns did not. | Optional human review/minimal merge gates were specific to that repository, not a blanket policy. |
| [Stripe part 1, Feb 9 2026](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents), [part 2, Feb 19 2026](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2) | Unattended task-to-PR work with human review; 1,300+ merged PRs/week at part 2. Deterministic blueprints, isolated prewarmed devboxes, curated tools, local feedback, and at most two CI rounds before human scrutiny. | Human review remains central. Their two-round limit illustrates a finite budget, not the universal correct retry count. |
| [Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent) | Approximately 30% of merged frontend/backend PRs at the post snapshot; complete sandboxed VMs, prewarming, durable sessions, collaboration, and separate authorship/approval. | Not evidence of human-free releases or permission for unbounded agents, broad credentials, or unrestricted concurrency. |
| [StrongDM factory](https://factory.strongdm.ai/), [techniques](https://factory.strongdm.ai/techniques) | Explicitly no human-written code or human code review in their factory; humans specified scenarios. Tests were gamed or rewritten; held-out scenarios and dependency digital twins addressed evaluation concerns. | Experimental precedent, not a mandate to remove approvals. Protect evaluator authority, check simulator fidelity, and retain deterministic checks. Their $1,000/day spend suggestion is not our budget policy. |
| [Cursor scaling agents](https://cursor.com/blog/scaling-agents) | Long-running experiments with hundreds of agents. Flat shared-file/lock coordination bottlenecked; planner/worker/judge cycles and fresh starts helped, while an integrator role bottlenecked. | Experiments are not universal production readiness. Coordination topology depends on workload. |
| [Anthropic C compiler](https://www.anthropic.com/research/building-c-compiler) | 16 agents, roughly 2,000 sessions, about $20,000 API cost. Human work concentrated on tests/environment. A GCC reference oracle helped split a monolithic kernel bottleneck; simple task locks were useful. | A capability experiment with documented unsupported paths, not a production-complete compiler. Lock success here does not contradict workload-specific failures elsewhere. |
| [Anthropic long-running harnesses](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Initializer and incremental sessions used durable feature/progress/git state and baseline smoke checks to counter half-built features and premature completion. | Compaction alone does not solve continuity; explicit acceptance and verified completion are still required. |
| [Microsoft .NET runtime](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/) | 878 CCA PRs, 535 merged; 67.9% merged/(merged + closed), excluding open. Setup improvements correlated with 38.1% versus 69% success. Nine PRs created 5-9 hours of review work. | Human-requested and expert-reviewed work. Setup correlation is not a controlled causal benchmark; denominators and review backpressure matter. |
| [Microsoft Copilot harness, Oct 28 2026](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/) | A shared multi-model harness reused across products. | A platform announcement, not proof of human-free development. Reuse primitives rather than reinventing every agent loop. |
| [GitHub runtime migration](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/) | 128 migration PRs; incremental replacement shipped under existing end-to-end tests while development continued. | Supports verifiable slices, not a recommendation for big-bang rewrites or evidence that PR count measures quality. |

## Maintenance

When modifying a rule, update its rationale, source/date, and any affected links
or checklist items. Mark project-specific deductions as policy rather than
attributing them to an external company. If a proposed check is implemented,
link its actual code/configuration and evidence before changing its status.
Keep authoritative wording in one place and use scoped links rather than copies.
