---
type: research
confidence: verified
tags: [method, ai-assisted-development, specs, evals]
created: 2026-10-26
updated: 2026-10-26
---

# Article Notes — Writing Is Closer to Thought Than Code

## Summary

Daniel Miessler argues that written intent, not code, should be the source of truth for AI-assisted projects. His position is a reply to Matt Pocock's "the code, not the spec" view, and he leans on Sutton's Bitter Lesson: as models improve, effort should move toward saying what you want rather than steering the steps.

The core claims:

- Fidelity drops at each step: idea → writing (articulation) → code (implementation). Most AI failures are articulation failures.
- Accuracy versus precision: code is precise but can be precisely wrong; writing is less precise but more accurate to the target.
- Writer's blindness (the curse of knowledge): the author believes the thinking is captured when it is not. The fix is in the articulation.
- Two loops: intent ↔ writing, and writing ↔ implementation.

## The Ideal State Artifact

One living document per project with four sections: Ideal State (prose, from a few paragraphs to thousands of words, built with a "Discuss" skill modeled on Pocock's grill-me), Constraints (what not to build or what must hold), Decisions (a dated log of changes with reasons), and Ideal State Criteria (atomic, testable, each with its own eval).

The eval ladder the article gives, in order: "code → assert → System 1 question set → Rubric / Tournament / LLM as a Judge", with cost rising from "$" to "$$$". The meal-planner example maps peanut-free, grocery list, and 40-minute criteria to code asserts, kid appeal to a fast-model question set, and variety to a stronger-model judge.

Worked examples: a family meal planner, an owl drawing (later drafts are checked against the ISA, not the last drawing), a yoga studio booking app (a login wall and wrong capacity fail two ISCs and are removed; the code is disposable and can be rebuilt against the same ISA), and a kitchen remodel (the contractor's plan fails the cook-faces-the-room check on paper, before construction).

Positioning: legacy spec-driven development (static requirement lists, separate from tests, rarely updated) is not what he means. The ISA is a living spec with evals built in. TDD and spec-driven development are framed as foundations, not mistakes.

## What the article does not specify

No file name, location, field names, status values, or Discuss-skill questions are given. Those are design choices made in [[Craft/Ideal State Method/Method|Method]] for this vault.

## Pocock's counterpoint

Pocock's framing, cited in the article's notes: "Code is executable, spec is not." His grill-me skill is the model for the Discuss skill. Its procedure: interview in rounds over a design tree, ask the whole frontier at once, number each question with a recommended answer, word questions so "yes" accepts the recommendation, look up facts rather than asking for them, stop when the frontier is empty. `/isa-discuss` adopts that procedure and points it at the Ideal State.

## Sources

- https://danielmiessler.com/blog/writing-is-closer-to-thought-than-code (fetched 2026-10-26)
- https://github.com/mattpocock/skills, `skills/productivity/grilling/SKILL.md` and `skills/productivity/grill-me/SKILL.md` (fetched 2026-10-26)

## Relevant To

- [[Craft/Ideal State Method/Method|Method]]
- [[Craft/Ideal State Method/Adoption Plan|Adoption Plan]]
