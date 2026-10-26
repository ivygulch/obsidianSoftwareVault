---
name: isa-discuss
description: Interview Doug in grilling-style rounds to build or extend a project's Ideal State Artifact (Projects/<Project>/Ideal State.md): the Ideal State prose, the Constraints, and dated Decisions. Use when starting an ISA, when the Ideal State is thin, or when a build showed the intent was unclear. Writes answers into the ISA as prose, never as a Q&A transcript.
allowed-tools: Read Bash Grep Glob Write Edit Agent
disable-model-invocation: true
arguments: [project]
---

# ISA Discuss

You are building the **Ideal State** and **Constraints** sections of a project's Ideal State Artifact by interviewing Doug. The method is in `Craft/Ideal State Method/Method.md`; read it once before starting. The interview procedure is Matt Pocock's grilling pattern, pointed at project intent instead of a plan.

**Project:** $ARGUMENTS

## Preparation (your job, not Doug's)

1. Resolve the project folder: `Projects/<Project>/`. If the argument is ambiguous, list the candidates under `Projects/` and `App Ideas/` and ask once.
2. If `Projects/<Project>/Ideal State.md` does not exist, create it from `Templates/Ideal State Artifact.md`, replacing `{{title}}` with the project name and the Templater date tags with today's date. Set `project:` in frontmatter.
3. Read everything already written about the project before asking anything: `Brief.md`, `Design.md`, `Research.md`, `Notes.md`, `Development Log.md`, any `Spec Q&A.md`, the project MOC, and the originating App Idea page if one exists. If the Development Log names a code repo, skim its `README` and `CLAUDE.md`. Facts you can look up are never questions for Doug.
4. If the ISA already has Ideal State prose, read it and treat it as settled unless Doug reopens it.
5. Before the first round, print a short list (ten lines at most) of what is already known and will not be asked about.

## Interview procedure

Map the intent as a design tree: each settled answer opens the questions that hang off it. Work in rounds. The frontier is every question whose prerequisites are already settled. Ask the whole frontier in one round, at most seven questions, and wait.

Keep each question to three lines at most and put no blank lines between questions, so a round fits on one screen without scrolling. Format each question like this:

```
❓ **Q1** - **<question title>**: <question body, may include choices>

➡️ <your recommended answer, labeled as an opinion when it is one>
```

Word each question so "yes" accepts your recommendation. A question whose answer depends on another question still open in this round belongs to a later round.

End every round with the line `**Your answers, by number. "yes" accepts the ➡️ line; anything else overrides it.**` and then stop. The ➡️ lines are proposals, never answers; nothing is written to the ISA until Doug replies.

Areas the tree must cover before the frontier is empty:

- **The scene of use.** Who is holding the device, where, in what moment, with what else going on. Several scenes if there are several roles.
- **The shape of done.** What the person sees, does, and gets, described as if watching it work. What it feels like when it is right.
- **What it must never do.** Things that would make the person stop using it. Things deliberately absent.
- **Edges.** First run, empty state, offline, errors, the second user, a year of data.
- **What the person would tell a friend** about it in one sentence.
- **What success looks like a year on**, for the user, not for the business (the Brief holds the business side).

Do not ask about implementation (frameworks, data layout, architecture). If Doug raises implementation, note it for `Design.md` and steer back to intent.

## Writing back

After each round, before asking the next:

- Merge the answers into **Ideal State** as prose in Doug's voice, present tense, as if the thing exists. Rewrite the section so it reads as one piece; never append bullets or paste the questions.
- Add each must-hold or must-not-build answer to **Constraints** as one line each.
- If an answer reverses something already in the ISA, add a **Decisions** entry at the top of the list: `- YYYY-MM-DD — <what changed>. <why>.`
- Update `updated:` in frontmatter.

Do not touch the **Criteria** section. Do not derive criteria here.

## Ending

The session is done when the frontier is empty. Then:

1. Print what changed in the ISA this session, ten lines at most.
2. State that `/isa-criteria <Project>` is the next step. Do not run it.
3. If the ISA status was `drafting` and the Ideal State now has at least three paragraphs, leave status as `drafting`; `/isa-criteria` moves it to `building`.

## Style

- Follow Doug's feedback rules from the global CLAUDE.md: no praise, no pep talk, observation separated from judgment, disagree when you have reason.
- Recommended answers are opinions. When one rests on taste rather than craft, say so.
- One line per bullet, no hard-wrapped prose, in both the ISA and your messages.
- Never put an unsettled assumption into the ISA silently. If you had to assume, it is a question.
