---
type: research
confidence: verified
tags: [card-games, mobile, competitors, ux, polish, reviews, skyjo]
created: 2026-09-10
updated: 2026-09-10
---

# Mobile Card Games — Landscape

Cross-tier sweep of mobile card games (single and multiplayer) on five questions: which titles are doing well, what their core play UI/UX looks like, what users say for and against, what below-notice polish makes them feel good, and what else matters. Twenty-plus apps across six tiers, ~80 reviews mined per app, plus designer talks and analyst data. US App Store, 2026-09-10. Point-in-time store numbers; revenue figures are tracker estimates and marked as such in the pillar notes.

Pillar notes (full detail, tables, quotes, sources):

- [[Mobile Card Games — Market|Market]] — six tier tables, trends, ten observations
- [[Mobile Card Games — Reviews|Reviews]] — 20 per-app sections, verbatim quotes, ranked cross-app complaint and praise lists, pay signals, 1-star triggers
- [[Mobile Card Games — UI & Polish|UI & Polish]] — gameplay conventions, async patterns, 25-row juice catalog, accessibility
- [[Mobile Card Games — Other Areas|Other Areas]] — monetization, retention, AI fairness, multiplayer infra, localization, IP, platform features (incl. tvOS presence), session design
- [[Mobile Card Games — Unlicensed Games|Unlicensed Games]] — traditional/public-domain and original-IP games that need no licensor, US and regional storefronts, ranked by size
- [[Mobile Card Games — UX Praise|UX Praise]] — which games have UI/UX praised for a specific interaction (user quotes, critics, awards), and which draw UI criticism
- [[Mobile Card Games — Feature Priorities|Feature Priorities]] — 20 features that stand out, ranked in five tiers by evidence weight, each with pillar pointers

## Summary

**The market splits into three economies.** Solitaire live-ops F2P is the volume engine (348M downloads, $470M spend in 2024; Solitaire Grand Harvest alone $1.5B lifetime, 63% of genre spend). Collectible IP is one growing title (Pokémon TCG Pocket, ~$1B IAP in 2025) while Marvel Snap and Hearthstone decline. Premium buy-once is small but real: Balatro ($9.99, no IAP, 106K US ratings at 4.96, still #2 paid Card two years on) is an outlier two orders of magnitude above the next premium card title, but Marmalade's $4.99–$9.99 licensed adaptations doubled EBITDA in FY25 and premium title count grew 77% in 2025.

**Every licensed family card app is F2P with ads and coins.** UNO!, Phase 10, Skip-Bo, Rummikub, Monopoly Solitaire, Play Nine, Five Crowns: none has a premium ad-free entry. Mattel bought Mattel163 outright at a $318M valuation (Feb 2026); Bonfit self-publishes Play Nine and now Five Crowns. The golf-family tier tops out at Play Nine (38.9K US ratings); no official Skyjo app exists on either store, and the "skyjo" term is held by a 2021 ad-supported clone (3.3K ratings) plus score keepers.

**Lifetime ratings and recent ratings diverge everywhere.** Lifetime scores of 4.4–4.9 sit on recent-100 distributions that are bimodal or majority 1-star (UNO 60% recent 1-star, Hearthstone 61%, Euchre 3D 54%, Spades Plus 53%). Rating prompts buoy the headline number; the recent stream is where the actual product state shows.

**The complaint stack is the same across tiers.** Ranked by number of apps: rigged dealing / AI "gets exactly the card it needs" (14 of 20, including Balatro at $9.99); ads that are unclosable, mid-hand, or over silent mode (12); fee-equals-payout coin economies (8); bots masquerading as humans (7); dumb AI partner or opponent (7); crash-after-update (7); rule infidelity to the physical game (6); paid ad removal revoked or moved to subscription (6).

**The praise stack is emotional, not feature-driven.** Playing with distant family is the dominant praise theme in nine apps (an 85-year-old grandmother's daily 5pm Trickster game; a Euchre 3D player keeping their late father as the AI partner). Then: no ads / no IAP / one price; faithful to the box; quick rounds; offline play; daily ritual and "keeps the brain sharp" from older players, who are also the ones who pay.

**Users name their price.** One-time ad-free at "$5 or even $10" (Sky-jo clone), "$5–$10" (Play Nine), "up to $7.99" (MobilityWare), "a small fee" (Five Crowns). $9.99 is accepted for a complete premium game (Balatro, Slay the Spire; several bought twice across platforms). Subscriptions for ad removal are rejected outright, and paid-plus-IAP on a paid app (Exploding Kittens 2's $18 expansions) is the main negative in an otherwise liked title.

**Polish that matters is a small, consistent vocabulary.** The designer-talk canon (Hearthstone GDC UI and sound talks, Marvel Snap GDC, Juice It or Lose It, Vlambeer, WWDC18 Fluid Interfaces, the Balatro juice teardown) converges on: one motion vocabulary across every screen and never shrinking cards to fit; overshoot easing plus random per-card stagger on deals; interruptible springs with 1:1 drag tracking; feedback proportional to significance (a flipped 12 looks and sounds different from a flipped 1); digit roll on scores; layered sound as the cheapest way to sell contact; opponent turns authored to a fixed rhythm; one skippable celebration; animation-speed and Reduce Motion settings on day one. Screen shake is the one canonical technique the sources themselves warn against for this register.

**AI fairness is a perception problem as much as an engineering one.** The rigged accusation arrives regardless of implementation (Cribbage Pro documented it in 2010 with data showing the opposite). Shipped mitigations: published shuffle audits (Cribbage Pro), commit-reveal seeds with a SHA-256 hash shown before the deal plus a test proving the AI never reads hidden cards (Just Cribbage), per-persona win-rate stats, and AI turns paced with a visible "thinking" tell proportional to decision difficulty. Unreadable or strategy-less bots are the top gameplay complaint in every golf-family app.

**Async multiplayer fails in three specific ways in reviews.** Pushes that open a lobby instead of the match (Star Realms), abandoned opponents (Carcassonne lets the remaining player play their turns; ~1 in 4 matches break), and lost match state. Game Center turn-based is free and store-and-forward but Apple-only with a documented match-loss history; every cross-platform peer (Trickster, Play Nine) uses accounts plus short join codes on a custom backend. No shipped card game uses a "your turn" Live Activity.

**Session contract for the genre:** portrait, one thumb, a round in under two minutes, user-chosen round count (Play Nine 2–9 holes, Golf Card Game 3/6/9), offline solo as a headline feature in every listing. Balatro's landscape-only mobile spawned a community portrait mod with swipe-to-play and a left/right-hand toggle.

**Platform and region.** iOS 26 Games app Challenges are built on Game Center leaderboards, giving any seeded daily a free system-level competition surface. France has sold 3M+ physical Skyjo copies (number one at JouéClub 2023 and 2024); the clones already localize store titles per storefront (US/DE/FR), and the German store has a score-keeper ecosystem. SKYJO is a registered US word mark (Reg. 7536287, Bernhardt, 2024); Apple routes name disputes to the parties rather than adjudicating.

## Cross-pillar observations

1. The features users ask for in golf-family apps are a fidelity and honesty list, not a content list: official card colors, correct discard-stack rule, adjustable AI that actually tries to go out, no timer, pay-once ad-free, house-rule variants, stats.
2. Paying raises the fairness bar rather than lowering it. Users who bought ad removal and then met "rigged" dealing call the purchase a waste (Phase 10); Balatro's only 1-stars are a year-old cloud-save bug on a $9.99 app.
3. The loyal-user 1-star triggers are all trust breaks: ad removal revoked or made a subscription (Euchre 3D), an update that shrinks cards or removes options (MobilityWare), discovering opponents are bots (MobilityWare's fake chat), economy changes devaluing prior purchases (Marvel Snap), ads added after an ad-free launch (Five Crowns).
4. Five Crowns: Kingdom Quest (May 2026, Bonfit, single-player only at launch, ads added post-launch) is the live case of a physical-brand adaptation shipping on a smaller brand than Skyjo's; it reached #108 Family within four months and its top review request is multiplayer for family moving away.
5. The premium tier's ranking titles (Balatro, Exploding Kittens 2, Dawncaster) pair the upfront price with zero IAP or expansion/cosmetic DLC only; the folk tier (Euchre 3D, Spades+, Cribbage Pro) sustains 60K–180K ratings for 15 years on ads plus a single lifetime ad-removal SKU at $4.99–$19.99.
6. Nothing in the reviewed set documents a good pass-and-play handoff; the UI & Polish note marks that spec as inference.

## Gaps

- No per-title revenue for Phase 10, Skip-Bo, or Play Nine; Marvel Snap 2025 revenue conflicts between sources (both noted in Market).
- No public 2025 keyword-difficulty data for the Card category.
- No current-iOS reliability data on Game Center turn-based matches beyond older developer-forum threads.
- Apple HIG haptics page and the AppleVis Accessible Solitaire page were summarized from secondary coverage (fetch returned 403).
- Apple Arcade card-title list and Tinytouchtales lifetime revenue figures are from search summaries, marked unverified.

## Sources

Consolidated in each pillar note. Store data: appstore MCP, US storefront, 2026-09-10. Analyst data: Sensor Tower, AppMagic, PocketGamer.biz, mobilegamer.biz, Naavik, Deconstructor of Fun. Talks: Sakamoto GDC 2015, Dodds GDC 2014, Brode GDC 2023, Jonasson/Purho 2012, Nijman 2013, WWDC18 803, Crosley Balatro guide.

## Relevant To

- [[Projects/Skyjo/Design|Skyjo Design]] — fidelity list, monetization position, modes
- [[Projects/Skyjo/UI Explorations|Skyjo UI Explorations]] — the juice catalog and AI-legibility findings map onto Territories 1–4
- [[App Comps]] — earlier Skyjo-specific comp table; this note supersedes its market figures
- [[Card Game Construction Kit]] — the IP-agnostic engine idea; the UI conventions and session contract apply to any grid/hand card game
- [[Licensed IP Game Adaptations — Landscape]] — the licensing-model gate check this extends
