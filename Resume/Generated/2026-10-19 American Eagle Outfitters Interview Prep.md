# American Eagle Outfitters — Interview Prep: AI Workflows

- **Created**: 2026-10-19
- **Company**: American Eagle Outfitters
- **Job title**: Staff iOS Engineer / iOS Architect (long-term contract, remote US, Eastern hours, India coordination)
- **Interview**: initial 60-minute call
- **Focus**: section 5 of the recruiter prep list, "AI workflows — a major interview priority"
- **Related**: [[2026-10-07 2144 American Eagle Outfitters]] (generated resume), [[CLEAR - Senior iOS Subcontract 2026-present]], [[Jason Poremba - FirefighterSpot 2026-present]], [[Walmart - Checkout Platform 2021-2026]]

## What the section asks for

One concrete example in six parts (problem, implementation, context and tooling, custom skills and MCP, validation, impact), told so that it separates "I use an assistant personally" from "I built a repeatable workflow a team runs." Distinguish production from experiments. The team uses Cursor and Gemini.

## Honest inventory

| Item | Column | Notes |
|---|---|---|
| FirefighterSpot | Production | Solo, hands-on, Spec Kit + Claude Code, shipped v1.0 Feb–May 2026, Swift Testing, Supabase, local-first sync. Primary example. |
| CLEAR | Production | Six-engineer team using Claude Code and Codex daily; codebase analysis behind the Swift 6.2 migration plan. Use "worked with," not "mentored." |
| Shared build/test/run scripts + per-project slash commands + CLAUDE.md rules | Production (own projects, carried into client work) | The strongest "repeatable workflow" artifact. Scoped `allowed-tools`, exit-code passthrough, filtered diagnostics, `--shot` screenshots. |
| Walmart Builder.io | Production, not agents | Evaluation criteria and working groups for a 120+ engineer org; trained 80+ on Builder.io specifically. Mandated adoption. |
| Routy (flighty-routes) | Experiment | Agent-only delivery experiment. Doug managed agents, never touched the code. Deployed to Fly.io as part of the experiment. Review found real defects (blocking I/O on the event loop, double-fetch race, N+1, untested lazy-fetch path). Use as the validation story, never as production. |
| Walmart Copilot, Xcode plugins | Experiment | Late 2024; plugins found deficient for iOS. |
| MCP servers | Configured and extended | XcodeBuildMCP, cupertino, Linear, scrivener, spec-kit, Apple Search Ads, a local fork of the appreply App Store server. Not authored from scratch. |
| Authored skills | Production (personal) | resume-generate with generate_docx.py, next-scene-prep, transcribe-dictation. Proof of ability to write skills. |

## The six-part example, built on FirefighterSpot

1. **Problem.** Solo engagement from non-technical requirements to a shipped local-first sync app, with no team to absorb spec drift or test gaps.
2. **Implementation.** Spec Kit for spec, plan, and task generation; Claude Code for implementation against those specs; the shared build and test scripts so the agent could verify its own work without hand-composed xcodebuild pipelines.
3. **Context and tooling.** Project CLAUDE.md for conventions; Spec Kit constitution and memory; XcodeBuildMCP and swift-lsp for navigation; Apple docs through an MCP server; Point-Free skills for library-correct code.
4. **Custom skills and MCP.** Spec Kit slash commands; scoped `allowed-tools` project commands wrapping the shared scripts; the configured MCP inventory; own authored skills as evidence.
5. **Validation.** Swift Testing coverage; human review of every change; the scripts fail the build, not the filter; Routy as the controlled experiment showing what unsupervised agent output gets wrong.
6. **Impact.** Shipped v1.0 in the February–May window as a solo engineer, with user and admin guides delivered. No ratio claims (the 5x framing was retired).

Attach the scale stories as one sentence each: CLEAR (team daily use plus migration analysis), Walmart (evaluation criteria, working groups, 80+ trained on Builder.io).

## Follow-ups to have ready

- **Personal vs team.** A team workflow is versioned in the repo, scoped by permissions, documented in CLAUDE.md, and survives you leaving. A personal workflow lives in chat history. Artifacts exist for both halves.
- **Cursor and Gemini.** Spend an hour in Cursor before the call. CLAUDE.md maps to `.cursor/rules`; slash commands map to Cursor commands; MCP is the same protocol and JSON; Gemini CLI uses GEMINI.md and MCP the same way. Say plainly that you have not run a team on Cursor, then show where each piece lands.
- **Production vs experiment.** Volunteer the split from the inventory table before they ask.
- **The resume line "trained engineering teams on those workflows."** Correct it yourself: the 80+ sessions were on Builder.io.

## Do not say

- Routy as shipped, production, or hands-on Kotlin or TCA work.
- "Built MCP servers." Say "configured and extended."
- "Mentored" at CLEAR.
- Any time-to-market ratio.

## Physical prep

- Have the scripts directory, one project's `.claude/commands` folder, and a project CLAUDE.md open in case they ask to see it.
- Write the six parts as six lines on a card. Keep the order, do not read it.
- Ask the section 10 question "How are Cursor and Gemini used today, and what would you like this person to improve?" early. The answer decides which pieces to emphasize in the second half.
