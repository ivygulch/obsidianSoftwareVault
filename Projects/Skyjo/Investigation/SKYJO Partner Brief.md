---
type: reference
created: 2026-08-10
updated: 2026-08-10
tags: [skyjo, magilano, partnership, executive-summary]
---

# SKYJO Venture — Executive Summary for Partner Conversation

Prepared 2026-08-10 for Doug's call with a prospective German-speaking partner (formerly based in Germany near the Swiss border; now living in northern Italy and still working in Switzerland). This entire thread is one week old: the licensing research, App Store market data, review mining, and the gameplay prototype were all produced August 5–10, 2026. Working prototype lives in the Demo1 repo.

## The opportunity in one paragraph

SKYJO — one of the world's best-selling casual card games, from Magilano, a small German publisher — has **no official digital version**. The demand is measurable and large: the leading unofficial clone has accumulated over 3,100 App Store ratings in the US alone — with as many again in France — despite abusive ads and collapsing reviews, and every rating represents someone who searched for SKYJO by name and settled for an imitation. That demand is currently captured by unofficial clones, and the leading one is actively collapsing under its own monetization. The plan: license the digital rights from Magilano and ship the official app — premium quality, no ads, in German, French, and English — with a German partner as a principal in the venture.

## The evidence

**Demand.** The lead clone ("Sky-jo: Golf Card Game," anonymous solo developer) holds 3,167 US ratings — and, remarkably, **3,163 in France (essentially equal to the US)** and 2,043 in Germany. The non-English market for this game plausibly exceeds the US one, matching the physical game's history: a German-born phenomenon that conquered France before American social media found it. The two smaller playable clones are both French-origin (334 and 283 French ratings vs 28 and 67 US).

**The incumbent is beatable — and beating itself.** The lead clone's lifetime 4.4★ hides a collapse: across its 200 newest US reviews the distribution is inverted (76 one-star vs 16 five-star, ≈2.3★ recent average). The dominant complaints: banner ads that hijack the screen mid-multiplayer game with no tap ("2 to 5 times a game"), freezes that eat wagered coins, senseless computer opponents, wrong card colors, and zero developer responses. Multiple reviewers state a price out loud: *"I'd gladly pay $5 or even $10 to have a decent mobile version of this game without any ads."*

**Why licensing (not just cloning).** SKYJO's mechanics are a folk game ("Golf") and can't be owned — what Magilano owns is the trademark, the trade dress, and enormous brand mindshare. The license buys: the exclusive right to the name in title/subtitle/keywords, Apple's trademark-dispute process to strip the mark from clone metadata (a web form, not litigation), eligibility for Apple editorial featuring and board-game press (official adaptations only), the physical-to-digital funnel (a QR code in every printed rulebook), and the price power that lets a polished official app charge real money against free clones. Comparable licensed adaptations (Root at $9.99, 5,457 ratings; Handelabra's Spirit Island sustaining a small studio) show the model works at both the pro and small-studio tiers — and adaptations keep selling for years after launch.

## The product approach

- **Official SKYJO for iOS and Android** (Android is non-optional — family play means mixed households). Web presence later if warranted.
- **v1 modes**: solo vs. computer opponents, pass-and-play, and async online play — "your move" notifications, designed for families playing across distance (a grandmother in Ohio playing grandkids in Texas is the killer use case). No real-time mode in v1.
- **Daily challenge**: a seeded daily deal with a leaderboard — procedurally generated retention with zero content treadmill; no clone has bothered.
- **Faithful and family-grade**: official card colors and rules, unhurried/untimed play, accessibility (Dynamic Type and beyond) — every item drawn directly from what players complain the clones lack.
- **Monetization**: free-to-try, one-time unlock (~$4.99–6.99), official expansions (e.g., SKYJO Action) as add-on purchases, house-rule variations as a feature. **No advertising, ever.**
- **Languages**: German, French, and English at launch, as equals; NL/IT/ES/PL as fast follows. Rules text comes from Magilano's own official rulebook translations under the license.

## Status: a working prototype — built in two days, honestly far from a product

The gameplay prototype was built in roughly **two days** (August 2026) using AI-assisted development, which is itself a data point about build economics for the venture. What exists today:

- A complete, rules-faithful SKYJO game engine — deterministic, fully tested (deck composition, the column rule, the doubling penalty with its positive-scores-only restriction, endgame sequencing), with the official rulebook ambiguities resolved and documented.
- **Trained computer opponents**: a parameterized strategy system (card counting, risk, endgame caution, mimicry, personality) plus an automated training pipeline — seeded tournaments and an evolution loop — that has already produced three distinct machine-trained "champion" personas alongside six handcrafted ones, selectable by difficulty tier.
- A playable iOS app (SwiftUI, modern stack) with opponent selection.

To be clear about the distance remaining: this is a prototype, not a product. No online multiplayer, no visual polish/art/sound, no localization, no daily challenge, no Android — the actual product build is the real work of the venture. What the prototype proves is that the rules engine and skillful opponents (the two things the clones' reviews complain about most) are solved, and that the team can move fast.

The demo is still the recruiting and licensing asset: fifteen minutes of the actual game playing, next to the incumbent's one-star avalanche, makes the pitch better than any deck.

## Business structure (current thinking)

- **US side**: Ivy Gulch LLC (Doug's Ohio LLC) as the initial licensing entity — cheapest, fastest, already exists.
- **Partner stake**: a real stake, not a favor-sized involvement — and per the colleague's stated preference (2026-08-11), he does not want to form a company of his own and prefers to work **as an individual through Ivy Gulch LLC**. That points squarely at the contractual revenue-share shape: a consulting/representation agreement between Ivy Gulch and him individually, with revenue share on the venture — which also happens to be the cleanest cross-border structure (an EU-resident individual holding units in a US pass-through entity would create tax friction on his side; a contractor relationship avoids it). His tax situation is his own — he is now an **Italian tax resident working in Switzerland**, so his agreement with Ivy Gulch runs under the US–Italy treaty (W-8BEN; services performed abroad are generally foreign-source with no US withholding — verify with the accountant when drafting). An agreed path to equity can stay in the agreement as an option if circumstances change.
- **Entity flexibility preserved**: the license would include an assignment clause allowing transfer to an affiliated EU entity later — though with the colleague preferring individual status, any future German entity would be Doug-owned with him as contractor, so this option matters less than before.
- **Known admin items** (all front-loaded, one-time): EU trader-status disclosure for the DSA (virtual business address planned), trilingual privacy/support pages, US–Germany royalty withholding paperwork (treaty-reduced to 0% with correct filings).

## What a German partner's role would consist of

1. **Named principal in the Magilano pitch, writing in German as Doug's representative.** The outreach changes from "a US developer" to "a team with a German-speaking partner" — for a family-scale publisher weighing its most valuable asset, native-language contact is the single biggest thing a partner adds on day one. Note: Magilano's named principal, Alexander Bernhardt, is SKYJO's *designer and artist* — the outreach goes to the creator personally, which raises the premium on fidelity, quality, and tone.
2. **The German-language relationship.** Native-language conversation and negotiation with Magilano; cultural ground truth on how SKYJO reads in its home market; in-person contact possible if it comes to that (Hachenburg from northern Italy is a day's travel, not a domestic hop).
3. **German market ownership at and after launch**: German App Store metadata and screenshots, German-language support, German board-game press and community outreach (spielbox, Brettspiel-News, local communities), the Apple Germany editorial-featuring pitch — plus the Switzerland storefront, which sits outside the EU regulatory umbrella and comes nearly free to a partner near the border.
4. **Translation quality**: review of the German app text against Magilano's official rulebook language, and licensor-approval workflow on brand usage.
5. **European presence**: an EU resident (Italy) who works in Switzerland — ground presence for European market matters, plus a natural connection to the Swiss storefront (a strong SKYJO market outside the EU regulatory umbrella). Note his move means the earlier "German address for trader status" idea no longer applies — the planned virtual business address covers that regardless.

## What we're asking in tomorrow's conversation

Not a commitment — a clean read on three things: interest in principle (yes/no/maybe), comfort with the stake shape (equity/rev-share as a real participant, not an advisor), and whether he'd take the lead on the Magilano contact — the plan, if he's in, is that **he sends the outreach to Herr Bernhardt in German, as Doug's representative**, with the prepared English draft as his source text. The rights may not even be available — the first Magilano email is precisely the question — so everything is contingent, and the plan is timeboxed: roughly two weeks to decide together, then the outreach goes (jointly or solo), while the incumbent's review collapse is still fresh evidence.

## Related

- [[Magilano Outreach]] — outreach email draft v2 (evidence-backed) + colleague messages
- [[Licensed IP Game Adaptations — Landscape]] — full research record: licensing model health check, Lane 1 gap query, keyword/SERP snapshot, review mining
- [[Ivy Gulch LLC]] — corporate record
