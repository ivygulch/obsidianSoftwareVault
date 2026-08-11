---
type: research
confidence: verified
tags: [tcg, companion-apps, scanners, deck-builders, landscape, deep-pass]
created: 2026-08-06
updated: 2026-08-06
---

# TCG Companion Apps — Landscape

Deep pass (2026-08-06) on the companion-utility niche flagged in [[Card & IP Games — Landscape]]: per-TCG coverage map, review-mining of official companions, and monetization check on third-party tools.

## Summary

The thesis survives contact with the data and gets sharper. Every recently launched physical TCG immediately spawns indie companion apps (Riftbound, months old, already has four), official publisher apps fail structurally and consistently (Bandai's TCG+ is at 2.19★ with 77 of its last 100 reviews one-star), and small indie tools outrate the officials in every single game checked. The niche runs on a repeatable playbook — one scan/catalog/price/deck engine, re-skinned per game, launched into each new TCG's wave. The main open question is monetization depth: the store's pricing API is too shallow to see IAP/subscription structure, and that needs a manual check on the leaders before committing.

## Coverage map (per TCG)

| TCG (launch) | Official companion | Third-party field | Opening |
|---|---|---|---|
| **Riftbound** (Riot, 2025) | None visible | 4+ indie apps within months: Runes Companion 4.77, Rift TCG Scanner 4.30, Riftbound Assistant 5.0 (new), second scanner (new) | Wave in progress; no official to compete with |
| **Gundam Card Game** (Bandai, 2025) | Teaching App 4.02; BANDAI TCG+ **2.19** | GNDM TCG Dex 4.77, Gundex 4.65 (brand-new indies) | Widest official-vs-indie quality gap observed |
| **One Piece / Digimon / DBS** (Bandai) | Same BANDAI TCG+ 2.19 serves all | Generic multi-TCG scanners (HoloDex 4.82, others) | Bandai family = one shared official failure across several huge fanbases |
| **Disney Lorcana** (Ravensburger, 2023) | TCG Companion 4.19 | InkcasteR 4.68, Lowly scanner 4.54, others | Official is mediocre-not-hated; opening is feature depth |
| **Star Wars Unlimited** (FFG, 2024) | None (Topps Card Trader is a separate collecting product) | S.W.U. DeckbuildeR 4.49, HoloScan 4.86 | No official; indie field thin |
| **Pokémon TCG** (mature) | None for collecting (TCG Live is the game, 4.26) | **Collectr 4.89** (category leader), TCG Companion 4.53, DittoDex 4.83 | Mature but still growing; Collectr is the bar |
| **MTG** (mature) | Wizards Companion 4.69 (narrow: events/life) | ManaBox 4.65, TopDecked 4.77, Dragon Shield scanner 4.63 | Crowded; multiple indies coexist — proof of market depth, not an entry point |
| **Sports cards** | PSA official 4.83 | CollX, Ludex, Card Ladder — VC-funded | **Avoid** — capitalized incumbents |

## Why officials fail (review mining)

- **BANDAI TCG+** (100 recent reviews: 77×1★): complaint mass is sign-in failures and event/tournament/store search — it's an *event registration* app serving publisher logistics, and it fails even at that. Publisher apps are built for publisher needs (event ops, rules teaching, sanctioned play); collector needs (what's my collection worth, scan a binder fast, iterate a deck) are structurally out of scope.
- **Lorcana Companion** (100 recent: mode is 4★, heavy "wish/would/could" language): liked as a basic tracker, walled by missing depth — deck-building limits, catalog gaps, account friction. The gap here is feature velocity, which an indie has and a board-game publisher's app vendor doesn't.
- Implication: third parties don't need to beat officials — officials aren't playing the same game. The real competition is other indies (Collectr tier) and the multi-TCG generics.

## Monetization (weak data — flag)

The pricing endpoint only sees base price + an IAP boolean, and it's demonstrably unreliable (it reports Collectr as "completely free," which contradicts its known premium subscription). Observed: all checked tools are free-to-download; Lowly's Lorcana scanner shows freemium IAP. **Follow-up before any commitment: manually check Collectr, ManaBox, and TopDecked store listings for subscription tiers and price points** — the working hypothesis is freemium + subscription gated on price-tracking/portfolio features, but it's unverified.

## Strategy read

- **The repeatable playbook**: one engine (scan → identify → catalog → price → deck-build), re-skinned per TCG, shipped early in each new TCG's launch wave. Vadym Pavlov (InkcasteR + S.W.U. DeckbuildeR) and HoloDex both run it; nobody visible owns it dominantly outside Pokémon.
- **Timing is the moat**: Riftbound shows the wave closes in months. The play is having the engine ready *before* the next major TCG announcement (Bandai and Universus pipelines, annual Gen Con reveals).
- **On-device scanning is the 2026 cost edge**: Foundation Models image input ([[WWDC 2026 Platform Shifts]]) means card identification without per-scan server-vision costs — a margin advantage over incumbent scanners built on cloud vision, and free at indie scale under the PCC tier.
- **Rights posture**: companions ride nominative use; the ecosystem's existence proves tolerance, but Disney/Ravensburger are the touchiest tier and Bandai enforces its marks. Keep game names out of app *titles* where possible (Gundex/InkcasteR-style coined names), full compliance on assets (no card imagery beyond user scans).
- **Data dependency is the hidden fragility**: card databases and price feeds (TCGplayer API et al.) are third-party dependencies with ToS/rate-limit risk — diligence them per game before building.
- Fits the portfolio model: each TCG's app is a modest stream; the engine compounds across launches; utility monetization, zero UA.

## Sources

- App Store data via appstore MCP tools, 2026-08-06: searches "One Piece card game scanner", "Riftbound TCG", "Gundam card game", "Collectr", "Magic the Gathering deck builder" (plus prior sweep's Lorcana/SWU searches); review analysis Lorcana Companion 6444333831 and BANDAI TCG+ 1599299476 (100 recent each); pricing probes Collectr/Runes/Lowly scanner (shallow — see monetization flag).

## Relevant To

- [[Card & IP Games — Landscape]] — parent sweep
- [[WWDC 2026 Platform Shifts]] — on-device vision cost edge
- [[Indie iOS Market Calibration 2026]] — freemium/subscription calibration
- [[Licensed IP Game Adaptations — Landscape]] — sibling thread (adaptation vs companion strategies)
