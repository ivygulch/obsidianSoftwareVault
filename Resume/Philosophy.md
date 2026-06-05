---
type: reference
updated: 2026-04-23
---

# Philosophy

Load-bearing principles, conventions, and process for this Resume vault. Read this before making significant structural changes or starting a new resume-generation pass. Update when a principle is adopted or overturned — not for tactical edits.

## Purpose

This vault is a queryable career database. The goal is to produce targeted resumes and cover letters on demand for different audiences — ATS filters at large employers, direct outreach to clients, contracting leads, referral intros. Source of truth lives in this folder, not in any single resume artifact.

The database is designed to be queried by Dataview across multiple axes — industry, employment type, technology, theme, date — so a targeted resume can be assembled from facts rather than copy-edited from a single master document.

## Target output

The end state this vault is designed for: a Claude session that takes two inputs —

1. The contents of this Resume folder (the queryable career database).
2. A job posting or contract description (the target).

— and produces three **markdown** outputs that I paste manually into existing `.docx` resume templates:

1. **ATS resume content** — reverse-chronological experience selected from engagements matching the target's requirements, with keyword matches and skills consolidated from frontmatter. Plain markdown bullets grouped by company / engagement.
2. **Focused resume content** — pillar-forward narrative drawn from `Framing/`, with pillars and engagement bullets curated to address the target's emphasis areas.
3. **Cover letter** addressing the specific needs, requirements, and questions stated in the posting — grounded in concrete engagements and bullets drawn from the database.

No custom tool is needed — a Claude session with access to the vault and the posting is sufficient. Output is markdown; docx formatting is the template's job.

The schema and structure of this vault are designed to make that generation reliable. **Conventions** (ATS-canonical casing in `tech` / `industry` / `practices`; atomic tagged bullets; engagement-level `concurrent_with` edges; pillar `pull_bullet_tags`; specific frontmatter field names) are tactical choices that serve generation — they can be revisited if they get in the way.

**Core principles** — Engagement facts separated from Framing editorial; Private Notes never output; Record once, Link everywhere — are not overridden by generation needs. If a principle genuinely blocks generation, the generation approach is wrong, not the principle.

Editorial policies (sourcing discipline, company About scope, Summary length) are between the two: more negotiable than principles, more deliberate than conventions.

## Core principles

**Record once. Link everywhere.** Engagements hold all substantive content — bullets, scope, metrics, tech. Companies are navigation layers with entity-level metadata, nothing more. No narrative fact should live in two files.

**The engagement is the unit of resume output.** Every resume bullet comes from an engagement file. Company files don't own bullets; Framing files don't own bullets. Framing files reference engagements by link; they don't duplicate engagement content.

**Framing is editorial; Engagements are factual.** `Framing/` holds narrative pieces — Summary, pillars (Core Focus Areas), Conference Talks, Earlier Career condensed narrative. These are editorial prose that doesn't map to a single engagement.

**Two output modes, one source.**
- **ATS resume**: reverse-chronological, keyword-dense, no tables. Pulls Summary + reverse-chron Experience from `Engagements/` + Skills consolidated from frontmatter + Education. Ignores most of `Framing/`.
- **Focused resume**: pillar-forward. Pulls Summary + Pillars + Conference Talks + Earlier Career from `Framing/`, alongside curated engagement bullets selected by pillar tags.

**Title-agnostic summary.** Role content matters, titles don't. The Summary never leads with a level qualifier (not "Principal iOS engineer" or "Senior iOS engineer" at the opening). Level or contract-structure preferences — if they exist — are negotiated in cover letters and recruiter conversations per `Career Preferences.md`, not in summary framing.

**Group small clients; extract significant ones.** Independent clients with short single-deliverable engagements live in grouped files (`Independent iOS Clients 2010-2014.md`, `Independent Java Consulting 2002-2012.md`). Promote to standalone engagement files when an engagement has multi-year duration, distinct client identity, or specific target-resume relevance.

**Private Notes never output.** Every engagement has a Private Notes section for information that informs future decisions but never goes on a resume — client contact details, data gaps, verification flags, honest caveats on claims. These are intentionally separated from the Achievements section so generators can safely ignore them.

**Archive is read-only.** Historical resume versions (1997–present) in `Archive/` are reference material for reconstructing dates, client names, and claims. They don't get edited.

## Folder structure

```
Resume/
├── _Resume MOC.md         — top-level navigation with Dataview rollups
├── Philosophy.md          — this file
├── Career Preferences.md  — targeting policy (role content, contract shape)
├── Education.md           — degree entries
├── scpResume.sh           — legacy tooling
├── Companies/             — entity metadata only, no substantive content
├── Engagements/           — source of truth for all resume bullets
├── Framing/               — editorial narrative pieces
│   ├── _Framing MOC.md
│   ├── Summary - iOS.md
│   ├── Pillar - *.md      — Core Focus Areas
│   ├── Conference Talks and Teaching.md
│   └── Earlier Career Summary.md
├── Templates/             — Templater templates for new entries
├── Archive/               — historical resumes, read-only reference
├── coverletters/          — outbound cover letters (not yet migrated)
└── portfolio/             — portfolio assets
```

## Schema conventions

**ATS-canonical casing** in fields that feed ATS output:
- `industry` — `"E-Commerce"`, `"Healthcare"`, `"Mobile Applications"`
- `tech` — `"Swift"`, `"SwiftUI"`, `"Claude Code"`, `"Builder.io"`
- `practices` — `"Technical Leadership"`, `"AI-Assisted Development"`

**Internal kebab-case** in fields for Dataview grouping:
- `themes` — `architecture`, `testing`, `agentic-tooling`
- `deliverables` — `checkout-platform`, `asda-ios-releases`

The duplication of casing is deliberate. ATS output expects `"Swift"`; Dataview tag rollups work better with lowercase-kebab. Don't collapse to one casing.

**Required engagement frontmatter**:
- `type: engagement`
- `company: "[[Company File]]"` (empty for grouped-independent engagements)
- `brand:` — product/brand within the parent company (e.g., ASDA for Walmart)
- `role:` — title as held
- `employment:` — `employee` | `contractor` | `subcontractor` | `independent`
- `start:` / `end:` — `YYYY-MM`
- `concurrent_with:` — links to overlapping engagements
- `industry:`, `tech:`, `practices:`, `themes:`, `deliverables:`
- `status:` — `current` | `past` | `archive`

**Bullets are atomic and ATS-ready.** Fact + metric + tech keyword, single line, no narrative connective tissue. Tagged inline with hashtags for Dataview pull into pillars (e.g., `#agentic-tooling #training #scale-80`). The focused-resume generator matches these tags against each pillar's `pull_bullet_tags` frontmatter list.

## Editorial policies

**Sections of an engagement file**:

- **Context** — 1-3 sentences setting up what this engagement was. Must make sense cold to a reader who hasn't seen the company page.
- **Role** — title plus 1-2 sentences on scope.
- **Achievements** — the source of resume bullets. Atomic, ATS-ready, hashtag-tagged.
- **Tech Stack** — human-readable sentence denormalized from `tech:` frontmatter. For readers; generators pull from frontmatter.
- **Private Notes** — internal only. Never pulled into output.
- **Related** — manual cross-links: company, concurrent engagements, same-company siblings, skills.

**Company About sections describe the company, not the engagement.** If the About reads as "what I did here," rewrite it. Company facts: industry, HQ, size, URL, corporate history. Engagement facts: what I did, when, with whom, what shipped.

**Claims require sourcing discipline.** When a number appears on a bullet (`~85% coverage`, `120+ engineers`, `80+ trained`), it should either be verifiable or flagged in Private Notes as an older-resume claim that needs verification before being cited on an ATS resume.

**Keep Summary short** (3-4 sentences). It's the first thing any reader sees; it needs to work on its own.

## Iteration process

This vault was built iteratively through user-approved batches rather than a single migration. The pattern that worked:

1. Propose structure or content with open questions flagged.
2. User answers or redirects.
3. Execute a proof-of-shape batch (2-3 files) before committing to a full migration.
4. Execute the remainder in one or two larger batches once the shape is validated.
5. Fix cross-links and broken wikilinks after each batch.
6. Surface ambiguities and data gaps rather than guessing past them.

User overrides and linter reformatting are respected as intentional. If a field format was changed (e.g., single-line `[a, b]` to multi-line YAML list), subsequent edits follow the new format.

## Handling verification and uncertainty

**Archive-corroborated facts are strongest.** Dates and client names drawn from archived resume versions or Apple Mail correspondence are treated as verified. Claims that can't be corroborated are flagged in Private Notes.

**When a claim in the seed `resume.md` conflicted with the email archive**, the archive won. The seed resume was treated as input material, not ground truth. Examples: Walmart contractor-to-FTE transition dates came from email, not memory. TherexRx (Clinically Relevant) vs MyFactor (BioRx) identification came from email correspondence.

**Ambiguities are captured, not resolved.** Where a claim is imprecise (e.g., "<50% to >75% coverage" at Sam's Club), the bullet preserves the directional claim and Private Notes flag the numeric imprecision. A target resume decides whether to include specific numbers or soften them.

**When content is deleted by the user or a linter, it's intentional.** Don't restore it. If broken wikilinks result, clean up the references; don't re-add the deleted content.

## When to update this file

- A new load-bearing principle is adopted (new output mode, new required schema field, new folder).
- An existing principle is overturned (e.g., summary variants were created, then consolidated into one — that's when this file gets updated to reflect the single-summary policy).
- The folder structure changes materially.

Don't update for tactical edits. Philosophy stays at the level of decisions that apply across engagements and targets.
