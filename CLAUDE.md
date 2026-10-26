# App Dev Vault — CLAUDE.md

## Overview
This is an Obsidian vault for planning and organizing app development projects. Code lives in Xcode projects (accessible via the xcode mcp server), not in this vault. The vault handles app idea brainstorming, active project planning, research, marketing, newsletter, website, branding, and business development.

## Structure

```
00_Dashboard/                    — Central hub (_Dashboard.md)

App Ideas/                       — Brainstorming space, organized by area
  _App Ideas MOC.md
  Writing/                       — Apps for authors and readers
    _Writing MOC.md
    StoryRiffs/                  — Collaborative turn-based storytelling app
  Shelved/                       — Killed/parked ideas, frozen record with Why Shelved

Projects/                        — Ideas promoted to active work
  _Projects MOC.md
  <Project Name>/
    _<Project Name> MOC.md
    Brief.md, Design.md, Research.md, Development Log.md, Marketing.md, Notes.md
    Ideal State.md               — ISA: intent, constraints, decisions, criteria with evals (source of truth for the build)
    Evals/                       — per-date Eval Run notes from /isa-check

App Platform/                    — Cross-project business + presence layer
  _App Platform MOC.md
  Marketing/
    Strategy.md, Positioning.md, Launch Playbook.md, Channels.md
  Newsletter/
    Preconditions.md             — Audience + monetization answers; blocks Strategy work until filled
    Strategy.md, Production Checklist.md, Welcome Sequence.md, Content Calendar.md, List Building.md
    Ideas/                       — recurring content types
    Issues/                      — per-date folders (Summary + Draft/Final)
  Website/
    Structure.md, Copy.md, SEO.md
  Branding/
    Positioning.md               — Top-level; Voice and Visual Identity derive from this
    Voice.md, Visual Identity.md
  Business Development/
    Revenue Models/, Partnerships/, Market Research/
  Analytics.md
  Pricing & Monetization.md

Craft/                           — Skill development and study notes
  Point Free/                    — pointfree.co episode notes
  Ideal State Method/            — writing-first development method, adoption plan, article notes

Research/                        — Cross-cutting research
  _Research MOC.md
  Tech/                          — frameworks, libraries, APIs worth evaluating
  Competitors/                   — competitor teardowns
  Trends/                        — market + technology trends

Templates/                       — Templater templates
  App Idea.md, Project Brief.md, Research Note.md, Competitor.md, Newsletter Issue.md, Ideal State Artifact.md, Eval Run.md
```

## Conventions

### MOC Files
- MOC (Map of Content) files serve as navigation indexes for each folder
- File names use `_` prefix + ` MOC` suffix (e.g., `_App Ideas MOC.md`) so they sort to top of folders
- MOC pages are navigation only — content belongs in dedicated pages

### Idea Pipeline
- New concepts start in `App Ideas/<area>/` using the [[App Idea]] template
- `status:` frontmatter tracks state: `seed` → `exploring` → `promoted` or `shelved`
- Promoted ideas move to `Projects/<Project Name>/` with their own project folder and MOC
- The Dashboard uses Dataview to roll up the pipeline across areas

### Projects
- Each active project gets its own folder with `Brief.md`, `Design.md`, `Research.md`, `Development Log.md`, `Marketing.md`, `Notes.md`
- The vault tracks planning and analysis; Xcode holds the code
- `Brief.md` is the canonical project overview — other pages drill into specifics

### Ideal State Artifacts
- A project may carry `Ideal State.md` (the ISA): Ideal State prose, Constraints, a dated Decisions log, and Criteria (ISCs) each with its own eval. It is the source of truth for build intent; `Brief.md` stays the business overview.
- When code and the ISA disagree, the ISA wins: fix the code, or change the ISA and log a dated Decision.
- Skills: `/isa-discuss` builds the Ideal State and Constraints by interview; `/isa-criteria` derives ISCs with evals; `/isa-check` evaluates a build and writes `Projects/<Project>/Evals/<date> Eval Run.md`.
- Method, adoption plan, and article notes: `Craft/Ideal State Method/`.

### Templates
- Templates use `{{title}}` placeholder (Templater syntax)
- `App Idea.md` — one-liner, target user, problem, differentiator, status frontmatter
- `Project Brief.md` — concept, scope, out-of-scope, success criteria, risks
- `Competitor.md` — includes Dataview "Mentioned In" backlink query
- `Ideal State Artifact.md` — ISA: Ideal State, Constraints, Decisions, Criteria with eval levels
- `Eval Run.md` — one check of a build against the ISA; results table, failures, gaps, proposed decisions

### Linking
- Wikilinks (`[[Note Name]]`) for cross-referencing
- Dataview queries for automatic rollups on the Dashboard and MOCs

## Plugins
- **Dataview** — Querying notes (pipeline rollups, cross-reference lists)
- **Templater** — Template processing
- **Kanban** — Task management

## Development Tool
- **Xcode** — use the xcode mcp server for project/code inspection
