---
type: reference
updated: 2026-09-12
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

**Title-agnostic summary.** Role content matters, titles don't. The Summary framing file never leads with a level qualifier (not "Principal iOS engineer" or "Senior iOS engineer" at the opening). Level or contract-structure preferences — if they exist — are negotiated in cover letters and recruiter conversations per `Career Preferences.md`, not in summary framing. Exception (2026-08-12): on a generated ATS resume, the summary opener may mirror the target JD's stated level — e.g., "Principal-level iOS engineer" for a Principal or Senior Principal posting. The framing file itself stays title-agnostic; the level lead is applied per target at generation time, only when the JD is explicitly leveled.

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

**Reference resume (2026-09-12).** `Archive/Resume2026_09_12_pinterest.docx` — produced by the skill's `generate_docx.py` from the Pinterest Sr. Staff generation and then hand-edited by Doug — is the reference ATS resume as is, superseding the 2026-08-25 Superhuman docx. `Framing/Reference Resume.md` is its verbatim transcription. Future ATS output starts from the reference (section order, role order, bullet order, wording, Skills lines) and adapts per JD; it does not regenerate wholesale from engagement files. Where a rule below conflicts with the reference, the reference wins. Specifics the reference settles: the summary is four sentences and carries no scale numbers (the DAU, 120+, and 80+ figures live in bullets, not the summary); the opener is "Principal-level iOS engineer with 15+ years designing and shipping mobile systems, from solo products to Walmart's flagship app." — the "Principal-level" lead was applied for the Pinterest Sr. Staff posting under the leveled-JD exception, so substitute "iOS engineer" for unleveled targets; the "Most recent full-time role" closing sentence is gone and "(full-time)" rides on the Walmart title instead; title parentheticals are lowercase — "(contractor)", "(independent, concurrent project)", "(contractor, concurrent with Walmart)"; McGraw-Hill is "iOS Developer (contractor, concurrent with Walmart)" with no "& Data Engineer"; the earlier-career block is "Independent Java / J2EE Architect & iOS Developer / Sunetos Inc. | 1998 – 2014" (with the period); the Walmart Principal bullet order is strategy → reactive systems → GraphQL collaboration → performance/reliability → testing discipline → feature flags + analytics (one bullet) → multi-team delivery → standards → mentoring → AI working groups/training; the Builder.io, App Store rating, and accessibility-teaching bullets are cut from Walmart (accessibility survives as "accessibility training" on the Skills Leadership line) — reintroduce per JD when a target calls for them.

**Copy style additions from the 2026-08-25 hand edits** (apply to all future resume output; the reference transcription is authoritative where a case isn't listed; superseded items struck by the 2026-09-04 list below):

- ~~Summary verbs read as first-person-implied: "Partner with product management…"~~ — overturned 2026-09-04: third person restored ("Partners with product management…"), and "Fluent in" became "Proficient in AI coding tools".
- "feature flag rollouts" unhyphenated in summary prose; the Skills line stays "feature flags."
- Restate the object after a semicolon: "; implemented *the migration* incrementally," not "; implemented incrementally."
- Include natural articles: "Led *a* refactor of checkout to *a* unidirectional, reactive architecture"; "owning *the* client, backend, and rollout"; "adopted *the tooling* as the standard."
- "added test coverage" (not "wrote new test coverage"); "maintained *a* 99.9%+ crash-free session *rate*."
- The App Store rating rides in parentheses on the checkout-UI bullet: "…in the Walmart iOS app (rated 4.8 stars on the App Store from millions of ratings)."
- Accessibility bullet tightened: "Taught sessions across the iOS engineering organization on accessibility principles and implementation techniques…" — drop "entire" and "the reasoning behind."
- Drop engagement-emphasis asides like "(the primary focus of the engagement)."
- Spell out "daily active users" in bullets (not "DAU").
- Skills Leadership line says "interview bar-raiser" (noun), not "interview bar-raising."

**Copy style additions from the 2026-09-04 hand edits** (to `Archive/Resume2026_09_04_actai.docx`; where these differ from the 2026-08-25 reference wording, the newer wording wins):

- Summary opener: "15+ years of mobile *app* design and architecture."
- Summary second sentence: "Shipped iOS applications ranging from solo *proofs of concept* to *Walmart's flagship app* serving 5M+ daily active users, *in an* iOS organization of 120+ engineers." — spell out "proofs of concept" (no "POCs" abbreviation), name the flagship app instead of "large-scale applications," and ", in an" replaces "within Walmart's".
- "Proficient in AI coding tools…" (not "Fluent in/with"); "Partners with product management…" (third person restored).
- CLEAR title is "Senior iOS Engineer (Contractor)" — matching the WalmartLabs "(Contractor)" pattern — not "Senior iOS Subcontractor."
- Fire-department title carries "(Independent, Concurrent project)".
- "with agentic tooling *to assist* research and drafting" (infinitive, not "assisting").
- Accessibility bullet ends at "…implementation techniques." — drop "for building accessible apps."
- Feature-flag bullet: comma, not semicolon — "behind feature flags, with more than half run as A/B experiments…".

**Copy style additions from the 2026-09-12 hand edits** (to `Archive/Resume2026_09_12_pinterest.docx`; where these differ from the earlier lists, the newer wording wins):

- Summary compressed to four sentences: "Principal-level iOS engineer with 15+ years designing and shipping mobile systems, from solo products to Walmart's flagship app." replaces the two-sentence opener — drop "proofs of concept," the DAU figure, and the 120+ figure from the summary (they stay in bullets).
- Summary second sentence: "Deep expertise in Swift, SwiftUI, UIKit, Combine, and Swift 6.2 concurrency; strong in platform architecture, SPM modularization, automated testing, and reliability at consumer scale." — "SPM" abbreviation is fine in summary prose; the Skills line keeps "Swift Package Manager modularization."
- Summary AI sentence: "Applies AI coding tools (Claude Code, Codex, GitHub Spec Kit) across planning, implementation, testing, and deployment, and has trained engineering teams on those workflows." — no "Proficient in," no "80+" count in the summary.
- Summary closing sentence: "Partners with product, design, and backend on scope and architectural trade-offs; experienced in GraphQL collaboration, feature-flag rollouts, A/B experimentation, and analytics instrumentation." — drop "management" and "teams" here; the Skills Leadership line keeps "product management, design, and backend teams."
- "feature-flag rollouts" is hyphenated in summary prose — overturns the 2026-08-25 unhyphenated rule. The Skills line stays "feature flags."
- No "Most recent full-time role" closing sentence, even on a leveled posting; the Walmart Principal title carries "(full-time)" instead.
- Title parentheticals are lowercase: "(contractor)", "(independent, concurrent project)", "(contractor, concurrent with Walmart)".
- McGraw-Hill title is "iOS Developer (contractor, concurrent with Walmart)" — "& Data Engineer" dropped.
- CLEAR block is four bullets: codebase analysis, migration plan, Fastlane, team collaboration. The UX bullet and the SwiftUI/Swift Testing bullet are cut. The analysis bullet ends at "…and improvement opportunities." (architectural-proposals clause dropped). The migration bullet ends at "…to Swift 6.2 concurrency." (no enumeration, no "implemented incrementally" clause).
- Fire-department block is three bullets. "Built a local-first SwiftUI client with Swift 6.2 concurrency and a Supabase backend; covered the client with Swift Testing." replaces the requirements-translation bullet and the backend/validation bullet. "with" attaches the concurrency here; "covered … with Swift Testing," not "validated."
- Walmart feature-flag and analytics bullets merged into one two-sentence bullet: "Launched all new checkout features behind feature flags, running most as A/B experiments measuring customer and business impact. Owned checkout analytics: instrumentation, dashboards, and monitoring through production rollout." — "most" replaces "more than half."
- McGraw-Hill internal-tools bullet ends "…and push notifications for mobile applications."
- ASDA: "Converted the ASDA UK iOS app's architecture to reactive programming…" (drop "grocery" and "internal"); the second bullet drops "over three years."
- "Sunetos Inc." with the period on the company line.
- Skills Leadership line adds "accessibility training" after "technical training."
- **Cover letters** (from the hand-edited `coverletters/CoverLetter_2026-09-12_pinterest.txt`): sign off "Doug Sjoquist" with no contact block beneath the signature (the .txt is pasted into an application form; the resume header still reads "Douglas W. Sjoquist"). Drop interview-flattery closers ("which I gather is exactly what your interviews ask"); state plainly what he can walk through — "how I used the tools for research and development as well as what I accepted and what I rejected or modified." When a gap statement has real adjacent experience, say both: "I did not lead or design a search or discovery system, but I worked regularly with those teams at Walmart" — not a bare "I have not." Use the A/B share the resume uses ("most"). For hybrid postings outside commuting distance: "I am not within commuting distance, but am open to periodic visits." Lead the Walmart fit sentence with the concrete scope ("responsible for the checkout flow in the flagship iOS app") rather than a metaphor ("the flow where intent becomes a purchase").

**Copy style** (from hand edits to the 2026-08-08 Eleos and CVS docx files; apply to all future resume output):

- Prefer plain connectors: "from solo POCs *to* core-team work," not "*through*." (The 2026-08-22 reference summary uses "ranging from solo POCs to large-scale applications"; the no-"through" rule still holds.)
- Org scale: either form is fine — "Walmart's iOS organization of 120+ engineers" or "Walmart's 120+ engineer iOS organization" (noun-phrase preference dropped 2026-08-12).
- Prefer "incrementally" over "step by step."
- Name the object of validation explicitly when a bullet spans client and backend: "validated *the iOS client* with the Swift Testing framework," so the backend isn't implied to be Swift-tested.
- Lead tool bullets with the tool's role in the work: "Used GitHub Spec Kit to drive spec-first development and Claude Code for implementation," not "Built spec-first using GitHub Spec Kit for specification generation."
- Soften the App Store ratings figure — don't cite the exact count (it drifts and reads as overreach). Preferred phrasing: "rated 4.8 stars on the App Store from millions of ratings."
- The Skills "AI-Assisted Development" line lists only current, load-bearing tools (Claude Code, Codex, GitHub Spec Kit, plus practices). Legacy or peripheral tools — Builder.io, Figma, Microsoft Copilot — must never appear in Skills: listing them there is misleading, implying working proficiency rather than evaluation/integration exposure. They may appear in engagement bullets where the surrounding context makes the actual role clear (e.g., "assisted the platform team evaluating and integrating Builder.io").
- Drop "structured" when the concurrency enumeration follows: "Swift 6.2 concurrency — async/await, actors, Sendable, and strict concurrency checking." Standalone "structured-concurrency migration" (no enumeration) is fine.
- "Analyzed" (not "Researched") for codebase-investigation bullets.
- Attach technology with "using," not "on": "a SwiftUI client *using* Swift 6.2 concurrency."
- Drop "on-platform" — "iterated with stakeholders."
- Preferred ratings-bullet lead: "Key contributor to checkout UI development in the Walmart iOS app."
- Analytics bullet scope reads "for checkout features," not "for every feature I led."
- Micro-tightenings: "bar-raiser for dozens of prospective engineers" (no gerund), "with retry handling," "Equally effective *at* translating," "a large user base" (drop redundant "consumer"). The using-not-on rule extends to SDKs/platforms: "subscription experience *using* RevenueCat and StoreKit."
- Cover letters: when CLEAR and the fire-department app appear in the same paragraph, mark the latter as "a separate, solo app" so it doesn't read as CLEAR work (from the sent Square letter, 2026-08-09).
- Current preferred summary is the 2026-09-12 reference summary (see `Framing/Reference Resume.md`). `Framing/Summary - iOS.md` still carries the older "2M+ DAU" / "120+ iOS engineer organization" phrasing and the focused-resume voice; reconcile the framing file deliberately when ready.

**ATS docx style** (from hand edits to the 2026-08-12 Home Depot docx, superseded where noted by the 2026-08-22 reference; apply to ATS resume output, markdown and docx):

- Pipe separators on metadata lines: contact line as "email  |  phone  |  linkedin" (bare linkedin.com/in/… URL, no https://); title on its own line above "Company  |  Month Year – Month Year"; education collapsed to one line, "B.A. Business Administration  |  Cedarville College  |  June 1982", with no emphasis line beneath (the "Computer Information Systems emphasis" line was dropped in the 2026-08-22 reference).
- Keyword-dense summary in short sentences. May open with a level qualifier mirroring the JD (see Title-agnostic summary exception). Name the load-bearing keywords explicitly (e.g., Combine, GraphQL, modular architecture) rather than folding them into prose. Closing sentence "Most recent full-time role: <title>, <area>, <company> (years)." — rule wording set 2026-08-22; dropped again in the 2026-09-12 reference even on a leveled posting, with "(full-time)" on the Walmart title carrying the signal instead. Do not reintroduce unless a JD asks for it.
- Tighter bullets: prefer parentheses over em-dash appositive clauses ("(architecture evolution, modularization, long-term maintainability)"); cut trailing qualifier phrases that restate context ("before full rollout," "during the refactor"); "each year" → "annually"; "approximately" → "~"; "over 20" → "20+".
- Verb choices: "Launched" for feature-flag rollouts; "Created and executed" for migration plans that were both planned and implemented; "Collaborated with" for team enablement.
- Skills category names use ampersands: "Languages & Frameworks," "Platform & Architecture," "Delivery & DevOps," "Analytics & Monitoring," "Backend & Data," "AI-Assisted Development," "Testing," "Leadership."

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
