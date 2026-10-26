---
name: isa-check
description: Evaluate a build, draft, or prototype against every Ideal State Criterion in a project's Ideal State Artifact. Runs assert-level tests through the shared iOS scripts, executes check steps, answers question sets against supplied screenshots or logs, grades rubrics, then writes Projects/<Project>/Evals/<date> Eval Run.md and updates each ISC's status in the ISA. Never edits the Ideal State, Constraints, or Criteria wording; intent changes are proposed, not made.
allowed-tools: Read Bash Grep Glob Write Edit Agent
disable-model-invocation: true
arguments: [project, evidence]
---

# ISA Check

You are running the test harness that the Ideal State Artifact defines. Method in `Craft/Ideal State Method/Method.md`.

**Project and evidence:** $ARGUMENTS

The second argument, if given, names what is being checked: a commit or tag, a TestFlight build number, a folder of screenshots, a log file, or a short description such as "draft 2 of the roster screen". If absent, assume the current working tree of the project's code repo and say so.

## Preparation

1. Read `Projects/<Project>/Ideal State.md` in full. If there are no ISCs, stop and say `/isa-criteria` has to run first.
2. Read the latest note in `Projects/<Project>/Evals/` for the prior baseline, if any.
3. Resolve the code repo path from the Development Log or MOC. Run `/Users/dwsjoquist/.claude/scripts/test.sh --help` and `/Users/dwsjoquist/.claude/scripts/build.sh --help` once to see the available flags. Use only these scripts for building and testing; never compose inline `xcodebuild` or `xcrun simctl` pipelines. If a script lacks a flag you need, say so and mark the affected ISCs as skipped rather than working around it.

## Running each ISC

Skip ISCs with status `dropped`. For every other ISC, by eval level:

- **assert.** Run the named test through `test.sh`. If the test does not exist, result is `skipped (no test)` and it goes under Gaps.
- **check.** Execute the numbered steps using the scripts. Capture what the steps say to capture into `Projects/<Project>/Evals/<date>/`. Apply the stated comparison.
- **questions.** Open the named evidence (Read the screenshots or logs). Answer each question yes or no with one line of justification. All yes is `pass`; any no is `fail`. If the evidence named by the Eval was not supplied, result is `skipped (no evidence)`.
- **judge.** Grade against the rubric, dimension by dimension, with a sentence of justification each and the overall grade against the pass bar. If the Eval says `judge-by-Doug`, result is `skipped (judge-by-Doug)` and the rubric plus the evidence pointer go under Gaps for him.

Record evidence for every result: the test output line, the capture path, the answered question set, the graded rubric.

## Writing back

1. Create `Projects/<Project>/Evals/<YYYY-MM-DD> Eval Run.md` from `Templates/Eval Run.md` (replace Templater tags by hand). If a run already exists for today, suffix the filename with ` 2`, ` 3`. Fill frontmatter counts and the Results table. Failures first in the Failures section, each with observed, required, and what changes next.
2. In the ISA, for each ISC checked: set `Status` to `done` on pass and `open` on fail; set `Last checked` to today's date and the result. A previously `done` ISC that now fails goes back to `open`; note the regression in the Eval Run.
3. Update `criteria_open`, `criteria_done`, and `updated:` in the ISA frontmatter. If status was `building` and this is the first run, set it to `checking`.
4. Do not change the wording of any Criterion, Constraint, or Ideal State sentence. If a result suggests the intent is wrong, write it under **Proposed Decisions** in the Eval Run. Doug writes Decisions into the ISA.

## Report

Lead with the counts on one line: passed, failed, skipped. Then the failures, each in two sentences at most. Then the gaps as a list of work. Then the proposed decisions, if any. Do not restate passes.

## Style

Doug's feedback rules apply: observation before judgment, no softening of a failure. One line per bullet, no hard wraps.
