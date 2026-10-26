---
type: method
created: 2026-10-26
updated: 2026-10-26
---

# Ideal State Method

## Premise

Fidelity drops twice on the way from a thought to a running app: once when the thought is written down (articulation), and again when the writing is turned into code (implementation). Most failures with AI-assisted building are articulation failures, not execution failures. So the writing, not the code, is the source of truth. Code is precise but can be precisely wrong; writing is less precise but closer to what was meant. When the code and the writing disagree, the writing wins: either the code is corrected, or the writing is changed on purpose and the change is recorded with its reason.

Two loops run at once. Intent and writing refine each other (talking it through sharpens the document). Writing and implementation refine each other (building reveals what the document left out). Both loops write back into one document.

## The artifact

Each project carries `Projects/<Project>/Ideal State.md`, the Ideal State Artifact (ISA), created from [[Templates/Ideal State Artifact|the template]]. Four sections:

1. **Ideal State.** Prose describing the project as if it already exists and works. Who is using it, in what moment, what they do, what happens. A few paragraphs at minimum. Built up by interview with `/isa-discuss`.
2. **Constraints.** What must hold and what must not be built.
3. **Decisions.** Dated log of changes to the Ideal State or the Criteria, with reasons. Iteration is recorded here, not buried in commits.
4. **Criteria.** Ideal State Criteria (ISCs): atomic, testable requirements, each with its own eval written next to it. They are the build target and the test harness at once.

## How it fits the existing project pages

| Page | Holds | Question it answers |
|------|-------|---------------------|
| `Brief.md` | Business overview: concept, why now, market, risks, success criteria for the venture | Why do this at all? |
| `Ideal State.md` | Product intent, constraints, decisions, criteria with evals | What is this thing, and how would we know it is right? |
| `Design.md` | How: modes, architecture choices, monetization mechanics, UI decisions | How are we building it? |
| `Development Log.md` | What happened, by date | What did we do? |
| `Evals/` | One note per eval run against the ISA | Did a given build meet the criteria? |
| Code repo | The implementation, including the `assert`-level tests | |

The Brief's "Success criteria" stay venture-level (license secured, revenue band). ISCs are product-level and testable. Do not duplicate one in the other.

## The eval ladder on the iOS stack

Each ISC names the cheapest eval level that can actually fail. Cost rises down the list.

| Level | What it is | On this stack |
|-------|-----------|---------------|
| `assert` | A plain code test | Swift Testing test in the SPM package, named after the ISC (`ISC_3_rosterFitsOneScreen`). Run via `/Users/dwsjoquist/.claude/scripts/test.sh`. |
| `check` | A scripted multi-step check | Build, launch in simulator, drive a flow, capture, compare. Uses the scripts in `/Users/dwsjoquist/.claude/scripts/`; never inline `xcodebuild` pipelines. |
| `questions` | A fixed yes/no question set, 3 to 7 questions, all must be yes | Claude answers against a screenshot, log, or output supplied to `/isa-check`. Doug can answer the same set by eye. |
| `judge` | A written rubric with a pass bar | Graded by Claude (Fable) with justification, or marked `judge-by-Doug` when the rubric says taste decides. |

A criterion with no eval that can fail is a wish, not a criterion. It goes back to the Ideal State prose or gets rewritten.

## The loop

1. **Discuss.** `/isa-discuss <project>` interviews Doug in rounds (the grilling pattern: frontier questions, recommended answers, "yes" accepts) and writes the answers into the ISA as prose and constraints. Facts are the skill's job to look up; decisions are Doug's.
2. **Derive criteria.** `/isa-criteria <project>` turns the Ideal State and Constraints into ISCs, assigns each an eval level and a concrete eval, and presents them for approval. Re-run whenever the Ideal State changes; it diffs against the existing ISCs and proposes adds and drops.
3. **Build.** Doug builds (per the working mode in memory: Doug drives iOS code, Claude assists), or Claude implements when the project says so. Builders read the ISA, not a summary of it.
4. **Check.** `/isa-check <project> [build or evidence]` runs every ISC's eval, writes `Evals/<date> Eval Run.md`, and updates each ISC's status in the ISA. Drafts are checked against the ISA, never against the previous draft.
5. **Decide.** Anything the build or the check revealed about the intent becomes a dated Decision in the ISA, written by Doug. Then back to step 2 or 3.

The code is disposable in this model. A bad build can be discarded and rebuilt against the same ISA and the same evals.

## Rules

- The ISA wins. Code that fails an ISC is corrected or removed. If the failure shows the intent was wrong, change the ISA first and log the Decision.
- Every change to Ideal State or Criteria gets a dated Decisions entry with a reason. No silent edits.
- ISCs are never renumbered. Dropped ones stay in place with status `dropped`.
- Skills never rewrite the Ideal State prose on their own. `/isa-discuss` writes what Doug answered; `/isa-criteria` and `/isa-check` propose and ask.
- One ISA per project. Versions are expressed with the optional `Scope` field on each ISC (`v1`, `v1.1`, `later`), not with separate documents.

## Pointing the code repo at the ISA

The ISA lives in the vault, not the repo, so Claude Code sessions in the repo need to be told where it is. Add to the repo's `CLAUDE.md`:

```markdown
## Ideal State Artifact
The source of truth for what this app is for lives in the vault: `/Users/dwsjoquist/ivygulch/vault/Projects/<Project>/Ideal State.md`. Read it before planning or implementing. Criteria there (ISC-n) are the acceptance tests; name `assert`-level tests after them. If an implementation choice conflicts with the ISA, stop and say so rather than deviating.
```

And start sessions in the repo with the vault as an additional directory:

```
claude --add-dir /Users/dwsjoquist/ivygulch/vault
```

## Relation to Spec Kit

Spec Kit (`/speckit.*`) produces per-feature `spec.md`, `plan.md`, and `tasks.md` in the repo and drives implementation. The ISA sits above it: one per project, intent rather than features. Where Spec Kit continues to be used, each feature spec cites the ISC ids it serves, and acceptance criteria in the spec reference ISCs instead of restating them. `/speckit.clarify` and `/isa-discuss` overlap in form but not in target: clarify sharpens one feature spec; discuss sharpens the whole project's intent. Where Doug is building by hand with Claude spot help, the ISA plus the repo's tests is enough and Spec Kit is not needed.
