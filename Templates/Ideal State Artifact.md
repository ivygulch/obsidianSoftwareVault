---
type: isa
project: {{title}}
status: drafting
criteria_open: 0
criteria_done: 0
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# {{title}} — Ideal State

> This document is the source of truth for what the project is for. Code is one implementation of it. When code and this document disagree, this document wins: fix the code, or change this document and record why under Decisions. Method: [[Craft/Ideal State Method/Method|Ideal State Method]].
>
> **status** values: `drafting` (Ideal State still being written) · `building` (criteria exist, code in progress) · `checking` (a build exists, evals running) · `shipped` · `shelved`.

## Ideal State

_Prose, written as if the thing already exists and is working. Who is using it, in what moment, what they do, what happens, what it never makes them do. Write what you mean, not what is easy to build. A few paragraphs is the floor; thousands of words is fine. Built up with `/isa-discuss`._

## Constraints

_What must hold, and what must not be built. Each one should be recognizable when violated. Platform floors, data rules, things permanently out, cost ceilings, lines not to cross._

- 

## Decisions

_Dated log, newest first. Every change to the Ideal State or the Criteria goes here with the reason. Iteration lives in this list, not in the code history._

- <% tp.date.now("YYYY-MM-DD") %> — Document created.

## Criteria

_Ideal State Criteria (ISCs): atomic, testable, each with its own eval. Together they are the build target and the test harness. Numbered in order of creation; never renumbered; dropped ones stay in place with status `dropped`. Derived with `/isa-criteria`, checked with `/isa-check`._

_**Eval level**, cheapest first: `assert` (a unit or UI test in the code) · `check` (a scripted multi-step: build, run, capture, compare) · `questions` (a fixed yes/no set answered by a fast model or by eye against a screenshot or output; all must be yes) · `judge` (a written rubric with a pass bar, graded by a stronger model or by Doug). Use the cheapest level that can actually fail._

_**Status** values: `open` · `done` · `dropped`. **Scope** is optional: `v1`, `later`, or a version tag._

### ISC-1 — <short name>
- **Criterion:** 
- **Scope:** v1
- **Eval level:** assert
- **Eval:** _test name and what it asserts, the check steps, the question list, or the rubric and pass bar_
- **Status:** open
- **Last checked:** —
