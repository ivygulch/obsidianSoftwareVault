---
name: isa-criteria
description: Derive or refresh the Ideal State Criteria (ISCs) in a project's Ideal State Artifact from its Ideal State prose and Constraints. Each ISC is atomic, testable, and carries its own eval at the cheapest level that can fail (assert, check, questions, judge). Presents candidates for approval in grilling-style rounds, then writes them into Projects/<Project>/Ideal State.md and updates the counts. Re-run after the Ideal State changes; it diffs against existing ISCs.
allowed-tools: Read Bash Grep Glob Write Edit Agent
disable-model-invocation: true
arguments: [project]
---

# ISA Criteria

You are turning a project's Ideal State and Constraints into Ideal State Criteria with evals. Method in `Craft/Ideal State Method/Method.md`; read the eval-ladder table before starting.

**Project:** $ARGUMENTS

## Preparation

1. Read `Projects/<Project>/Ideal State.md` in full. If the Ideal State section is empty or a single paragraph, stop and say `/isa-discuss` has to run first.
2. If the Development Log or MOC names a code repo, list its test targets and existing test names so `assert` evals can point at real tests or name missing ones precisely. Use `ls`, `find`, and `grep`; never run builds here.
3. Read the most recent note in `Projects/<Project>/Evals/` if any, so statuses and known gaps are not lost.

## Deriving candidates

- Every sentence in the Ideal State that makes a claim about behavior, appearance, or outcome is a candidate.
- Every Constraint is a candidate, usually a negative one (`never`, `no more than`).
- Split anything compound. One criterion tests one thing.
- Reject wishes: if you cannot name an eval that can fail, the sentence stays prose and is not a criterion. Say which sentences were rejected and why.

For each surviving candidate, assign the cheapest eval level that can actually fail:

| Level | Write the Eval as |
|-------|-------------------|
| `assert` | The test name (`ISC_<n>_<camelCaseName>`), the target it belongs in, and the one assertion it makes. Mark `(missing)` if the test does not exist yet. |
| `check` | Numbered steps using the scripts in `/Users/dwsjoquist/.claude/scripts/` (build, run-sim, test), what is captured, and the comparison that decides. |
| `questions` | Three to seven yes/no questions. All must be yes. Name the evidence they are answered against (screenshot of which screen, which log). |
| `judge` | A rubric with named dimensions and an explicit pass bar. Say whether Claude grades it or it is `judge-by-Doug`. |

Set `Scope` to the version the Ideal State is describing unless the prose marks something as later.

## Approval rounds

Present candidates in batches of at most eight, in the grilling format:

```
**C1 · ISC-<n> <short name>** — <criterion>. `<level>`: <eval>. ➡️ keep
```

One candidate per line, at most three lines each, no blank lines between candidates, so a batch fits on one screen. Word each so "yes" accepts. Offer `drop`, `merge with`, or `rewrite` as the alternatives. When the ISA already has ISCs, the first round is a diff: for each existing ISC, `keep`, `drop` (with reason), or `rewrite`; for each new candidate, `add`. Wait for answers before the next batch.

If a candidate exposes an ambiguity in the Ideal State prose, ask about it as its own question, and when answered, record a Decisions entry. Never edit the Ideal State prose yourself to resolve it.

## Writing back

- Append approved ISCs under **Criteria** using the template's heading-and-field block. Numbers continue from the highest existing ISC; never renumber.
- Dropped ISCs keep their block with `Status: dropped` and a Decisions entry naming the reason.
- Update `criteria_open` and `criteria_done` in frontmatter (dropped ones count in neither).
- If status was `drafting`, set it to `building`.
- Update `updated:`.

## Ending

Print the final table: ISC id, short name, level, status. List the `(missing)` asserts as a block of work for the code repo. State that `/isa-check <Project>` is the next step once a build exists.

## Style

Doug's feedback rules apply: no praise, observation before judgment. Recommended answers are opinions and labeled. One line per bullet, no hard wraps.
