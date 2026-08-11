---
type: research
confidence: verified
tags: [licensed-ip, board-games, puzzle-brands, games, step-0]
created: 2026-08-05
updated: 2026-08-08
---

# Licensed IP Game Adaptations — Landscape

Step 0 of the licensed-IP research plan (2026-08-05): is the "license existing IP, build the mobile game" model alive on iOS in 2026? Probed the canonical mid-tier licensed adaptations plus a licensed puzzle brand via store data.

## Summary

**The model is alive, and its texture maps exactly onto the portfolio-income framing.** Professional mid-size studios (Dire Wolf) run it profitably at scale; genuinely small studios (Handelabra) sustain modest niche businesses on it; and the long tail demonstrates the most interesting property — licensed adaptations keep selling at $7–10 for *years after their developers stop maintaining them*, which both proves durable demand and creates the wedge: IP owners whose digital partner went stale, or whose game never got adapted. Counter-signal: content brands with volume (Penny/Dell, CGE) tend to build digital in-house rather than license out.

## Probes

| App | Studio | Price / model | Ratings | Score | Last updated | Read |
|---|---|---|---|---|---|---|
| Root | Dire Wolf Digital (licensing Leder Games) | $9.99 paid | 5,457 | 4.87 | 2026-03 | Model thriving at pro-studio tier |
| Spirit Island | Handelabra (small studio) | Free + IAP unlocks + $2.99/mo sub | 198 | 4.21 | **2026-07** | Small studio actively sustaining a niche title |
| Race for the Galaxy | Temple Gates (w/ Rio Grande) | $6.99 paid | 178 | 4.14 | **2018-10** | Abandoned yet still selling — 8-year long tail |
| Roll for the Galaxy | Temple Gates | $9.99 paid | 501 | 4.89 | **2020-09** | Same: beloved (4.89), unmaintained, still charging |
| Penny Dell Daily Crossword | PuzzleNation (= Penny Publications in-house) | F2P + puzzle-set IAP | 8,896 | 4.59 | 2026-07 | Brand went in-house, not licensed out |
| Galaxy Trucker | CGE Digital (publisher in-house) | $4.99 paid | — | 4.64 | — | Same in-house pattern for stronger publishers |

## Findings

1. **Viable at portfolio scale, not salary scale, for a small team.** Handelabra is the realistic comp: a small studio, actively shipping (July 2026 update), on a title with only ~200 iOS ratings — a modest durable stream, not a rocket. Fits the portfolio-income model precisely; would fail a "this must replace a salary" test.
2. **The long tail is commercially durable.** Temple Gates' two adaptations haven't been touched since 2018/2020 and still sell at $6.99/$9.99 with 4.1–4.9 stars. Ship-once revenue persisting 6–8 years is real in this category — board-game fans buy the adaptation whenever they discover the hobby, not at launch.
3. **The staleness dynamic is the wedge.** Abandoned adaptations (Temple Gates tier) mean IP owners with a dead digital channel. And if iOS 27's reported hard requirement for scene-based lifecycle is accurate ([[WWDC 2026 Platform Shifts]]), apps of that vintage may literally stop launching this fall — forcing re-license or re-build conversations across the whole stale tier. (Confidence on the breakage claim: cited from one developer writeup, not verified against Apple docs — verify before using it in outreach.)
4. **In-house is the competing pattern.** Brands with content volume and cash (Penny Publications → PuzzleNation; CGE) build their own digital arms. Target IP owners *below* that threshold: too small to staff a digital team, big enough to have a fanbase.
5. **Paid-up-front works here.** $5–10 paid, no ads, expansion IAP — exactly the monetization the fan-niche supports and the ad-volume model doesn't. Consistent with the [[Indie iOS Market Calibration 2026]] pricing findings.

## Lane 1 — Gap query results (2026-08-05)

Method note: BGG's XML API began requiring authentication in 2026 and its HTML is Cloudflare-walled, so the systematic API pull wasn't possible. Candidates were seeded from domain knowledge of the BGG top tiers and mass-market sellers, then verified against the App Store — the store check is the decision-relevant half. BGG rating-count figures below are therefore approximate/unverified.

| Game (owner) | Physical stature | iOS status | Read |
|---|---|---|---|
| **Skyjo** (Magilano, small German publisher) | One of the world's best-selling casual card games | **No official app.** Clones only — the lead clone has 3,159 ratings, F2P, actively updated | **Flagship find.** Massive proven demand (clone traction is the receipt), tiny owner below the in-house threshold, perfect mobile fit |
| **The Crew** (Kosmos) | Kennerspiel winner, huge co-op trick-taking hit | **No official app at all** | Strong gap; ideal async-co-op mobile fit. Kosmos is mid-large — harder counterparty than Magilano |
| **Azul** (Next Move/Plan B → Asmodee family) | BGG top-tier, mass market | Official app discontinued; a clone ("Tiles Mosaic") monetizes the gap | Real gap, but rights run through Asmodee — bad counterparty for a small shop |
| **Splendor** (Space Cowboys → Asmodee) | Mass-market gateway staple | Official app sunset by Asmodee; clones only | Same: proven orphaned demand, Asmodee-locked |
| Castles of Burgundy (Ravensburger/alea) | BGG top-20 | DIGIDICED app alive but **3.55★** at $8.99 | "Bad incumbent" tier — a beloved game with a resented adaptation |
| Patchwork (Lookout) | Modern classic 2p | Twin Sails (Asmodee mobile arm) app, 4.21★, updated Jan 2026 | Covered, mediocre; not a gap |
| Codenames (CGE) | Party mega-hit | CGE in-house app, $4.99, 4.74★ | Covered — confirms the in-house pattern for strong publishers |

Pattern confirmed: the **Asmodee purge** orphaned demand for several mass-market titles (Azul, Splendor) but locked the rights behind the worst counterparty; the *actionable* gaps are titles owned by publishers below the in-house threshold — **Skyjo/Magilano is the archetype** (huge fanbase, tiny owner, zero digital, clones proving willingness to play). Unchecked candidates for a second pass: Cascadia, Kingdomino, Concordia, Great Western Trail, Quacks of Quedlenburg, Hive, Lost Cities, NSV titles (Qwixx, The Game).

## Public-domain IP variant (assessed 2026-08-05)

PD inverts the licensing trade: zero royalty and zero counterparty risk, but **zero exclusivity — the IP provides no moat**, and the brand-search advantage that justifies licensing only exists for terms not already occupied.

- **US PD now covers works published through 1930** (95-year rule; 1930 works entered Jan 2026). But PD is jurisdiction-specific: Agatha Christie (d. 1976) is copyrighted in the UK/EU until 2046, so only her pre-1931 works are usable and only in the US — a worldwide App Store release needs region handling. Early Poirot and the first Marple novel (Murder at the Vicarage, 1930) are US-PD; **Agatha Christie Ltd actively enforces POIROT/MARPLE trademarks**.
- **Sherlock Holmes**: fully US-PD since 2023 — and the store probe shows why that doesn't help: the search term is walled by G5-style F2P hidden-object shovelware with UA budgets. PD whose search term is occupied delivers no acquisition advantage.
- **Winnie-the-Pooh**: 1926/1928 texts PD, but Disney's visual designs and trademarks remain; the post-2022 horror-film gold rush demonstrates the commodity-flood dynamic on newly-PD brands.
- **Conan**: the trap example — Howard's Conan stories are 1932+ (95-year expiry from 2028 onward), renewal status contested, and Heroic Signatures asserts trademarks aggressively. Not cleanly usable now.
- **Where PD does work**: when execution is the moat — adapting the actual *texts* (e.g., a faithful 1920s Poirot novel as a narrative deduction game, where writing and design quality carry it) rather than attaching a famous name to generic mechanics. That path leans on the writing leg of the portfolio and competes on craft, not brand search. Also viable: estate partnerships layering "official" branding over PD-adjacent material — which is just licensing with a cheaper entry.

Net: PD is a content strategy, not an acquisition strategy. For acquisition-by-fanbase, exclusive licensing of living niche IP (Skyjo tier) remains the stronger play.

## Skyjo keyword + SERP snapshot (2026-08-08)

Fresh pull of the "skyjo" US iPhone search term via the appstore MCP keyword scorer and Astro's live store search.

**Keyword scores** (heuristic, appstore MCP — not Apple's official popularity index): traffic **9.64/10** ("very high search traffic"), difficulty **6.8/10** ("moderately difficult"). ~37 apps rank for the term; 6 carry exact title matches. Apple Search Ads console popularity index still unchecked (free to look up; ASA MCP server setup pending).

**Correction (2026-08-10, on-device test by Doug):** an earlier version of this section claimed "skyjo" appears at position 2 in US App Store autocomplete after typing just "sk". That is false — the term does not appear until "skyj" is typed. The claim came from over-reading the tool's `suggest {length: 2, index: 2}` component, which is an opaque heuristic input, not a literal autocomplete position. Treat suggest metrics as scoring inputs only; the verifiable demand signals for this term are the clone ratings volumes and the storefront parity below.

**Ratings re-verified 2026-08-10** (Astro store search): lead clone US 3,168 / FR 3,160 / DE 2,043 — the France≈US parity and Germany-at-two-thirds figures cited in [[SKYJO Partner Brief]] and [[Magilano Outreach]] are current.

**Who commands the results** (top of 50):

| # | App | Dev | Ratings | Type |
|---|---|---|---|---|
| 1 | Sky-jo: Golf Card Game (4.4★) | "Anusha s t" | **3,167** | Playable clone — the lead clone from Lane 1 (3,159 on 2026-08-05, so still growing) |
| 2 | Skygo: The Card Game (4.6★) | Alexandre Morcos | 67 | Playable clone, recent |
| 3 | skyjo-o: flip your skyjoe (4.6★) | julien DOLAIS | 28 | Playable clone, recent |
| 4–11 | Score Keeper, Score Board, Companion, Gamepad, Score, Lumio, Sky-jo Companion, Scorekeeper | various solo devs | 0–42 each | Companion scorekeepers |
| 12+ | Sunset forecasts, skydiving logbooks, jet charter | — | — | Relevant results exhausted |

**Reads:**

1. **The #1 clone holds a 47× ratings moat** over the next app but remains a beatable incumbent: anonymous solo developer account, keyword-stuffed subtitle ("Euchre Inspired Multiplayer"), F2P. No official Magilano presence anywhere in the results — unchanged.
2. **The companion-scorekeeper angle is already a swarm**: eight scorekeepers in the top 11, nearly all with App Store IDs in the 674–677M range (shipped within roughly the last year), none above 42 ratings. Indie devs are noticing the same gap and all building the easy thing. The *playable game* tier still has exactly one serious occupant.
3. **The field is shallow for the traffic level** — relevant results run out by position ~11 on a 9.6/10-traffic term. High demand, thin supply, beatable leader: the licensing thesis's store-side conditions are all still present and slightly stronger than at the 2026-08-05 pull.

## Skyjo clone review mining (2026-08-08)

Read the App Store reviews for all three playable clones. The incumbent's lifetime 4.4★ is a mirage — **recent sentiment has collapsed**.

**#1 Sky-jo: Golf Card Game** (3,167 ratings, 4.4★ lifetime): across the 200 *newest* US reviews the distribution is inverted — 76×1★, 45×2★, 38×3★, 25×4★, 16×5★ (~2.3★ recent average). Complaint stack, by frequency:

1. **Ad hijacking** (dominant): SHEIN/TEMU banners auto-redirect to the browser mid-multiplayer with no tap, disconnecting the player while auto-play burns their turns — "2 to 5 times a game." At least 8 of the 40 newest reviews name SHEIN specifically.
2. **No paid ad-free option — users are naming their price**: "I'd gladly pay $5 or even $10 to have a decent mobile version of this game without any ads." Multiple similar. The market is pricing an official app in the incumbent's own reviews.
3. Freezes that eat wagered coins; multiplayer lockups; "works about 40% of the time."
4. Bot quality: "no logic to the moves they make"; house-cheating suspicion ("the computer cheats").
5. Rule fidelity: card colors don't match the physical deck (one reviewer spells out the exact official bands: -2/-1 purple, 0 blue, 1–4 green, 5–8 yellow, 9–12 red); no untimed mode "like the physical card game."
6. **Zero developer responses** on any review.

**#2 Skygo: The Card Game** (67 ratings, 4.6★): six US text reviews. AI "has no regard to zipping and does not care about going out even if there is no possible way for them to have the lowest score" (i.e., no doubling-penalty judgment); a 1★ for missing accessibility — visually impaired user cannot read or enlarge the cards; phone overheating; forced haptics; one scareware-ad report. No developer responses.

**#3 skyjo-o** (28 ratings, 4.6★): zero US text reviews — no US voice at all.

**Read**: demand is provably high (traffic 9.6/10), the only serious incumbent is monetizing abusively enough to generate a 1★ avalanche it never answers, users state a $5–10 willingness to pay, and the cited quality gaps — trustworthy smart bots, faithful rules/colors, untimed play, accessibility, no hijacking ads — are exactly the checklist an official licensed paid app clears. This is the strongest store-side evidence yet for the Magilano pitch; the incumbent's own reviews read as the outreach email's proof section.

## Gate decision

Step 0 **passes**; Lane 1 first pass complete (results above) with Skyjo/Magilano as the standout target profile. Remaining: Lane 1 second pass (unchecked candidates), Lanes 2–4 (authors, puzzle brands, other creatives) per the plan. Note: BGG XML API now requires authentication — register an API key if a systematic pull is wanted later.

## Sources

- App Store data via appstore MCP tools, 2026-08-05: Spirit Island 1501321205, Root 1439262206, Race for the Galaxy 1190675052, Roll for the Galaxy 1324815218, Penny Dell Daily Crossword 655645841; searches "Spirit Island", "Root board game", "Race for the Galaxy", "Penny Dell crossword".
- Keyword + SERP snapshot 2026-08-08: appstore MCP `get_keyword_scores` ("skyjo", ios/us) and Astro MCP `search_app_store` ("skyjo", us, top 50). Lead clone app ID 1567186753.
- Review mining 2026-08-08: appstore MCP `analyze_reviews` (1567186753, newest 200) and `fetch_reviews` (1567186753 ×40, 6758668944 ×6, 6744247458 ×0), US storefront. Review quotes verbatim from fetched texts.

## Relevant To

- Licensed-IP games research plan (chat, 2026-08-05) — Step 0 gate
- [[WWDC 2026 Platform Shifts]] — iOS 27 breaking changes as the stale-tier forcing function
- [[Indie iOS Market Calibration 2026]] — pricing model consistency
