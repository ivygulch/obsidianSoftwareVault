---
type: research
confidence: verified
tags: [writers, landscape, lane-2, app-store-screen, suite-thesis]
created: 2026-08-05
updated: 2026-08-05
---

# Writer Tools — Landscape

Lane 2 App Store screen of the writer market, run 2026-08-05 against the suite-of-small-apps thesis (unix-philosophy apps composed via App Intents, shared Story/Character/Location/Scene entities). Data from App Store search, app details, review analysis (recent-review mining), and ASO keyword scores via the appstore MCP tools. Install counts and difficulty scores are tool estimates, not ground truth.

## Summary

The screen supports the thesis. The category's flagship monolith (Scrivener iOS) is a confirmed stale incumbent: no update since September 2023, $23.99 paid, and recent reviews running majority-negative on a sync architecture (Dropbox-only) that Apple-ecosystem users hate. The big suite player (Campfire) validates demand for interconnected writer tools but executes mobile badly (3.4★). The most instructive competitor is Story Planner — a two-person team sustaining an $8.99 one-time app at 4.74★ for eleven years, which has just begun spinning out its own second small app. The suite slot on iOS is not yet occupied by anyone executing well natively; Fortelling is the closest and is a single freemium app, not a composable suite. Character tooling is the most-demanded capability in review text. All entry keywords show high traffic with difficulty ~7; "writing tracker" stands out: high traffic with only one exact-title match.

## Incumbents — weakness confirmed

### Scrivener (iOS) — stale monolith, still charging
- $23.99 one-time, 2,597 lifetime ratings at 4.18. **Last updated 2023-09-29** (~3 years). Released 2016.
- Recent-200 review distribution: **63×1★ / 23×2★ / 40×3★ / 22×4★ / 52×5★** — the recent average (~2.9) is far below the lifetime score; the brand is coasting on desktop reputation.
- Complaint mass centers on sync: "dropbox" 89 mentions, "sync/syncing" 114, "icloud" 40 — Dropbox-only sync, no iCloud, in an Apple-ecosystem audience. Stability complaints on modern iOS also present.
- Read: the category's biggest name has effectively abandoned mobile. Its users are the acquisition pool — any new tool should import/export Scrivener format (Story Planner already exports *to* it as a selling point).

### Campfire — suite demand proven, mobile execution weak
- Web/desktop monolith with 15+ "modules" (characters, worldbuilding, timelines, maps, magic systems); claims 100K+ writers. iOS app: **3.45★, only 69 ratings**, actively updated but clearly an afterthought.
- Recent reviews skew mid-to-low (12×1★ / 16×2★ / 30×3★ vs 13×5★); complaint keywords cluster on mobile parity with desktop, screen/UI behavior.
- Read: validates that writers want interconnected modular tools — and that a web-first company can't deliver the native iOS experience. The suite thesis executed natively attacks exactly this gap.

## Active competitors

### Fortelling — closest analog, single-app version of the idea
- Free + subscription, 988 ratings at 4.49, **actively developed** (v5.0.0 shipped 2026-08-02: family tree, writing sprints, statistics rework, widgets).
- Review text is character-dominated: "character/characters" 86 mentions — character tooling is what this audience loves and asks for more of. Recent grievance: family tree gated behind premium ("that's literally part of character development").
- Read: the serious competitor to watch. It is one monolithic freemium app; its paywall resentment and its single-app shape are both openings for a buy-once-per-tool suite.

### Werdsmith — owns the ritual/goals slice
- 7,935 ratings at 4.67, active since 2011, subscription; iPhone/iPad/Mac/Watch/Vision Pro. Focus: writing ritual, goals, projects, AI next-line suggestions.
- Read: strong and healthy, but its territory is the *writing habit*, not the story bible. A suite's tracker app competes here; its entity apps don't.

### Story Planner (Literautas) — proof the model works at solo scale
- **$8.99 one-time, 4.74★ across 1,173 ratings, sustained for 11 years by a two-person team (a writer + an indie dev).** iCloud sync, privacy-first, exports to Word/Scrivener/Final Draft/Ulysses, widgets and Shortcuts support.
- The same developer just launched a separate **Writing Tracker** app (5★, new) — the small-apps-portfolio move is beginning in this exact market.
- Read: existence proof for every load-bearing assumption — willingness to pay one-time prices, solo-scale sustainability, interop-as-feature, and now multi-app portfolio. Also the most likely convergent competitor to the suite thesis. Worth a full [[Competitor]] teardown in Phase 3.

### Others noted
- Novelist (free/indie, 4.39), Werdsmith-adjacent small writing apps, Writer's Companion (4.41), Sci-Fi/Fantasy Writer's Companion (Alexander Winn — niche-genre companion pattern, mixed ratings), Lorebind (new worldbuilding-notes entrant, unrated) — steady flow of new small entrants confirms the niche is alive; none are executing a composable multi-app suite.
- Sudowrite iOS (4.45) occupies AI prose generation — commodity-AI territory per the sherlock rule; stay in the structure/data layer, not the prose-generation layer.

## Keyword screen (US iOS; difficulty ~7 across the board)

| Keyword | Traffic | Difficulty | Notable |
|---|---|---|---|
| writing tracker | 7.74 (high) | 7.31 | **Only 1 exact-title match** — best traffic-to-title-competition ratio found |
| novel planner | 7.15 (high) | 7.66 | Suggest-index 2 — strong autocomplete presence |
| story bible | 7.0 (high) | 7.62 | 7 exact-title matches already |
| worldbuilding | 6.73 (moderate) | 7.33 | Top-ranked apps include non-writer games — intent is split |
| character keeper writer | 5.71 (moderate) | 7.01 | Low competition count (19) |

Read: no free lunch, but "writing tracker" and long-tail character/worldbuilding phrases are the softest entries. Suite apps each get their own keyword surface — one ASO advantage of the multi-app model over a monolith.

## Fit against the suite thesis

- Entity model confirmed by what users discuss: Character (dominant), World/Location, Plot/Scene, Draft, plus the habit layer (goals, sprints, streaks).
- Interop sells in this market: Story Planner advertises Scrivener/Ulysses/Final Draft export; Scrivener refugees need import. App Intents composition + file-format interop = the suite's moat and its migration path.
- Sherlock risk low: story bibles, plot structure, and series continuity are domain data, not OS features. Avoid the prose-generation layer (Sudowrite, commodity AI).
- Monetization read, combining with [[Indie iOS Market Calibration 2026]]: this audience demonstrably pays one-time ($8.99–$23.99) and resents subscription gating of core tools (Fortelling family-tree complaint). Suits per-app buy-once with a suite unlock via web — decide before app #1.

## Gaps in this screen (follow-ups)

- Submission/query tracking was not searched — likely thin on iOS (QueryTracker is web-only); could be an underserved suite member. Same for revision/edit-pass tracking and beta-reader feedback management.
- Ulysses reviews not mined (general prose app, less suite-relevant) — revisit if the suite grows a drafting member.
- No Android-side scan; no download/revenue estimates beyond tool proxies.
- Fortelling and Story Planner deserve full Phase 3 teardowns with 1–2★ review pulls before any build commitment.

## Sources

- App Store data via appstore MCP tools, 2026-08-05: search ("novel writing", "story planner character", "writing tracker word count", "worldbuilding writer"), app details (Scrivener 972387337, Campfire 1626123915, Fortelling 1503524513, Werdsmith 489746330, Story Planner 860024390), review analysis (recent 100–200 per app), keyword scores (5 terms).

## Relevant To

- Suite-of-small-apps thesis (App Intents composition) — conversation of 2026-08-05
- [[WWDC 2026 Platform Shifts]] — App Intents 2.0 mechanics the suite would build on
- [[Indie iOS Market Calibration 2026]] — pricing/monetization calibration applied above
- StoryRiffs (App Ideas/Writing) — adjacent audience
