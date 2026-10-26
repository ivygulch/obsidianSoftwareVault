---
type: plan
status: active
created: 2026-10-26
updated: 2026-10-26
---

# Adoption Plan — Ideal State Method

Bring the [[Craft/Ideal State Method/Method|method]] into the active projects one at a time, starting with the project closest to shipping. Each phase has a done-condition. The method itself has kill criteria at the end.

## Phase 0 — Setup (done 2026-10-26)

- [x] Templates: [[Templates/Ideal State Artifact|Ideal State Artifact]], [[Templates/Eval Run|Eval Run]]
- [x] Skills: `/isa-discuss`, `/isa-criteria`, `/isa-check` in `.claude/skills/`
- [x] Method, article notes, this plan under `Craft/Ideal State Method/`
- [x] Vault `CLAUDE.md` convention, Project Brief template link, Dataview rollups on the Projects MOC and Dashboard

## Phase 1 — Pilot on FirefighterSpot v1.1

Why this one: it is live, scoped small (single org, sign-in, App Store release), and the [[Projects/FirefighterSpot v1.1/Spec Q&A|Spec Q&A]] already holds the raw material. Its questions Q25 to Q27 (continue Spec Kit, who drives, where the spec lives) are answered by adopting this method.

Steps:

1. Finish answering the Spec Q&A sections A to D as they stand. The answers are inputs, not the ISA.
2. Run `/isa-discuss FirefighterSpot v1.1`. The skill reads the Q&A answers and the 1.0.1 baseline, then interviews for what the Q&A does not cover: the scene of use (a chief creating an incident in the truck; a member joining by code), what sign-in must never get in the way of, what "done" looks like for the admin screen. It writes the Ideal State prose and Constraints (single org; custom accounts table; RLS "Allow all" accepted for 1.1; no Supabase Auth; and so on).
3. Run `/isa-criteria FirefighterSpot v1.1`. Expect roughly 10 to 15 ISCs: sign-in gate, request-account mail prefill, admin-only Manage Data, account create and deactivate, session behavior offline, App Store listing items, demo login for review. Most will be `assert` or `check`; the sign-in UX ones may be `questions`.
4. Answer Q25 to Q27 in the Q&A with a pointer to the ISA. Proposed answers: the ISA in the vault is canonical; the repo's `CLAUDE.md` points to it (snippet in Method); Spec Kit continues only if the per-feature specs cite ISC ids, otherwise retire it for this release.
5. Run `/isa-check FirefighterSpot v1.1` against the 1.0.1 baseline before any new code. Most ISCs should fail. That failure list is the work plan.
6. Build. Name `assert` tests after ISCs.
7. Run `/isa-check` after each meaningful build until every non-dropped ISC is `done`.
8. Write a short retrospective in the project's Development Log: was the ISA read during build sessions, which eval levels were used, what the Decisions log caught that would otherwise have been lost.

Done when: v1.1 is submitted with every non-dropped ISC at `done`, and the Decisions log has at least one entry made during the build (evidence the writing ↔ implementation loop ran).

## Phase 2 — Retrofit Skyjo (optional, after Phase 1)

Skyjo has a working prototype and no ISA. Writing the ISA for the product as it should be, not as the prototype is, tests the article's claim that drafts get checked against the ISA rather than against the last draft. It also produces a clean statement of the product for the Magilano conversation.

Steps: `/isa-discuss Skyjo` using Brief, Design, UI Explorations, and Game Flow Research and Plan as inputs; `/isa-criteria`; one `/isa-check` against the current prototype.

Done when: the ISA exists with criteria and one Eval Run is recorded. Whether the prototype is rebuilt against it is a separate decision.

## Phase 3 — Greenfield: Applying Proverbs

When [[App Ideas/Miscellaneous/Applying Proverbs/Applying Proverbs|Applying Proverbs]] is promoted, the ISA is written before any code. Its existing [[App Ideas/Miscellaneous/Applying Proverbs/Exploration Plan|Exploration Plan]] phases become ISC groups with `Scope` tags; the V1 candidate becomes the set of ISCs tagged `v1`. The text-licensing kill criterion becomes a Constraint.

Done when: the first build is checked against the ISCs, not against a feature list.

## Phase 4 — Make it the default

- Promotion from App Idea to Project creates `Ideal State.md` alongside `Brief.md`.
- Decide whether `Design.md` survives as a separate page or folds into the ISA. Keep both until Phase 1 shows which way the content leans.
- Add a "Last eval run" line to each project MOC.

## Kill criteria for the method

Evaluate after Phase 1. Any one of these means the method is not earning its keep and should be cut back to the ISA alone or dropped:

- The ISA was not opened during build sessions: Decisions log empty and ISC statuses stale after three or more builds.
- Evals exist only at the `judge` level because no `assert` tests were written, so the harness never ran as a harness.
- The ISA and the Spec Kit spec say the same things in different words. Then one of them goes.

## Open questions

- Spec Kit for FirefighterSpot v1.1: continue with ISC citations, or retire it for this release? (Spec Q&A Q25)
- Does the ISA replace `Design.md` for new projects, or does Design stay as the "how" page?
- Where do `questions` and `judge` evals run by default: a Claude Code session fed screenshots, or Doug by eye with the question set in hand?
- Should each code repo hold a read-only copy of its ISA (synced on commit) or only a pointer to the vault?
- Is one ISA per project with `Scope` tags enough, or will a major version (Skyjo v2) want its own document?
