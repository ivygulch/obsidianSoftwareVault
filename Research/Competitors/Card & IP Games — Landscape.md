---
type: research
confidence: verified
tags: [card-games, tcg, licensed-ip, games, landscape]
created: 2026-08-06
updated: 2026-08-06
---

# Card & IP Games — Landscape

App Store sweep (2026-08-06) of popular trading-card games and games built on real-world IP, plus the adjacent types surfaced by the data — assessed against the portfolio model (small team, AI-assisted, modest durable streams) and the licensed-IP research thread.

## Summary

The card-battler tier (Pokémon TCG Pocket, Marvel Snap, Yu-Gi-Oh) and the licensed F2P tier (MONOPOLY GO!) are IP-giant/UA-giant territory — observation targets only. But the sweep surfaced four adjacent types where small teams demonstrably win: **physical-TCG companion utilities** (an indie runs deck tools across multiple new TCGs; official companions are weak), **card-shop/pack-opening simulators** (an indie title with 41K ratings), **premium single-player card games** (Balatro at 4.96/$6.99), and **premium licensed adaptations of classic games** (Marmalade's $4.99 Monopoly — the model the Skyjo thread already targets). The strongest new finding is the companion-utility wave around newly launched physical TCGs.

## The observation tier (not buildable, but instructive)

- **Pokémon TCG Pocket** (4.79) — the collecting-first redesign (pack-opening ritual over competition) is the mechanic every adjacent indie type now borrows.
- **MARVEL SNAP** (4.69), **Yu-Gi-Oh Duel Links** (4.73), **Pokémon TCG Live** (4.26) — IP + live-ops + UA.
- **MONOPOLY GO!** (Scopely, 4.80) — licensed classic as multi-billion F2P; the maximal version of brand-search acquisition.
- **Topps BUNT / Star Wars Card Trader / Disney Collect** — digital *collecting* (no gameplay) on real-world IP. Instructive: IP holders license collecting rights separately from game rights — a cheaper rights slice.

## Adjacent types worth future exploration (ranked for fit)

### 1. Companion utilities for newly launched physical TCGs — best fit

- Every new physical TCG (Disney Lorcana, Star Wars Unlimited, One Piece, etc.) spawns demand for scanners, deck builders, and collection trackers. **Official companions are consistently weak** — Ravensburger's Lorcana Companion sits at 4.19 while third-party tools rate higher.
- Existence proof of the portfolio model: indie dev Vadym Pavlov runs companion apps across multiple TCGs (InkcasteR for Lorcana 4.68, S.W.U. DeckbuildeR 4.49); Lowly Apps' Lorcana scanner 4.54. One codebase (scan, catalog, price, deck-build), re-skinned per game — a unix-suite pattern with a launch wave every time a new TCG ships.
- Caution: the *sports-card* scanning corner (CollX, Ludex, Card Ladder, PSA official) is VC-funded and crowded — the opening is new-TCG niches, not sports.
- Trademark note: companion apps ride nominative use of the TCG name in metadata — survivable (the ecosystem exists) but each rights holder's tolerance varies; Ravensburger/Disney are the touchiest tier.
- On-device card scanning is exactly the Foundation Models image-input sweet spot ([[WWDC 2026 Platform Shifts]]).

### 2. Licensed premium adaptation of classic/casual games — already in motion

- Marmalade's MONOPOLY ($4.99 paid, 4.66, 5K+ ratings context) validates premium licensed adaptations at the top; the [[Licensed IP Game Adaptations — Landscape]] note covers the niche tier (Root, Skyjo thesis). This sweep adds nothing negative — the two-model split (Scopely F2P giant vs premium adaptation) is stable.

### 3. Card-shop / pack-opening simulators — proven, with a caveat

- **TCG Card Shop Tycoon Simulator: 40,956 ratings at 4.70, built by an indie** (OPNeon, with a sequel) around an invented card IP ("Tetramon") — no license needed. HOMA's Mini Monsters (4.82) and Rips by Triumph confirm the wave.
- The engine is the pack-opening dopamine loop — the same variable-reward mechanic as loot boxes. It monetizes extremely well and is gambling-adjacent by design; whether to build in that mechanic space is a values call as much as a business one.

### 4. Premium single-player card roguelikes — proven ceiling, lottery odds

- **Balatro: $6.99 paid, 4.96** (plus an Apple Arcade edition) — decisive proof that premium single-player card games thrive on mobile. But it's a design-lottery outcome; the de-risked version of "premium card game" is adapting a *proven* physical design under license (the Skyjo path), not inventing one.

### 5. Micro-companions for physical play — smallest tier

- Score keepers and rules helpers for specific games (Azul Score Tracker, Skyjo Score Keeper observed in earlier sweeps) — trivially small, suite-able, but trademark-in-title exposure without a license and tiny ceilings. Useful as license-relationship door-openers more than as products.

## Cross-cutting observations

- The Pokémon Pocket effect: collecting/ritual now outdraws competition across the whole space — favors collection-first products (types 1 and 3) over battlers.
- The "invented TCG" trick (Tetramon, Mini Monsters) sidesteps licensing entirely for sim-type games — IP costs zero when the cards are fictional.
- get_similar_apps on the tycoon title returned only generic top-chart games — the store's similarity graph is useless for niche clustering; keyword searches remain the tool.

## Follow-ups

- Deep pass on the new-TCG companion niche: per-TCG coverage map (Lorcana, SWU, One Piece, Riftbound, Gundam), review-mine the weak official companions, and check what the third-party tools monetize (sub vs one-time).
- Watch Balatro-likes for whether a licensed niche-card-game premium adaptation can borrow the daily-challenge/roguelike retention layer.

## Sources

- App Store data via appstore MCP tools, 2026-08-06: analyze_top_keywords "trading card game"; searches "Monopoly", "card collection tracker scanner", "Disney Lorcana", "Balatro", "Star Wars Unlimited deck"; details TCG Card Shop Tycoon 1605261462; similar-apps probe on same.

## Relevant To

- [[Licensed IP Game Adaptations — Landscape]] — same research thread; this note maps the adjacency space
- [[WWDC 2026 Platform Shifts]] — on-device vision for card scanning
- [[Indie iOS Market Calibration 2026]] — monetization calibration
