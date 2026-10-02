---
type: research
confidence: verified
tags: [indie-scan, app-ideas, market-validation, opportunity-scan]
created: 2026-10-02
updated: 2026-10-02
---

# Indie App Opportunity Scan — 2026-10-02

A wide scan for app ideas that one indie iOS developer could build well and that have a market large enough to matter as a portfolio member. Unlike the earlier idea research in this vault, this scan did not weight ideas toward personal background; the only tests were market viability for an indie and solo buildability. Run from the prompt in `appIdeaResearchPrompt.txt`.

> **confidence** is `verified` for store figures (fetched 2026-10-02 from the iTunes Search and Lookup APIs, the App Store review feed, and App Store product pages). Every revenue figure in this note is an **estimate** that rests on an assumed ratings-to-downloads ratio; no download or revenue data was available for any app. Keyword scores are not reported as evidence (see Gaps).

## Summary

About 70 candidates were surfaced from six evidence sources, 18 were store-checked, 12 survived the screen, and five were taken to deep dives. The five finalists, ranked: pool and spa water chemistry, pipe trades calculator, bowling stat tracker, vehicle fuel and service log, bill organizer.

Three findings cut across all five:

1. **Every finalist niche is filling with new entrants.** Eleven new pool apps since April 2025, 23 pipe-trade apps in 2026, 14 bowling trackers since August 2025, eleven vehicle logs since 2025, and 60 bill apps in 2025–2026. Almost none has passed 100 ratings. An opening visible in rating counts and stale update dates is visible to everyone, and being a competent entrant has not been sufficient for any of them.
2. **Mid-case revenue estimates land between about $450 and $1,400 a month for all five.** That matches the pay-once floor seen in the indie revenue disclosures ($300–$850 a month, no example above $1K). None of the mid cases reaches the $10K-a-month bar the [[Indie iOS Market Calibration 2026]] note sets for a niche worth a solo year; all five fit the portfolio-member framing of modest revenue at low upkeep. Only the high cases for pipe trades and bowling approach the calibration bar.
3. **The strongest revenue proof in the scan belongs to patterns that did not produce a finalist.** Coach and instructor session planners (two unrelated solo apps at about $10K a month), sport-specific player tools (one past $500K a year), and condition-specific health logs (the most independent examples) all showed solo developers earning well. The specific targets found for those patterns had thin target-level evidence, so they rank as runners-up, not finalists.

## Method

- **Phase 1, wide scan.** Six parallel scanners, one per source: App Store paid and grossing charts for 16 smaller categories (about 280 apps verified); stale or decaying incumbents (365 search terms, 4,617 apps, 145 flagged, 22 review-checked); indie revenue disclosures (50 rows, mostly payment-provider-verified leaderboard entries and self-reports); unmet-demand language (Bluesky and forums); new platform surface in iOS 26 and 27; and spending niches (about 80 hobbies, trades, and professions).
- **Phase 2, screen.** 18 candidates store-checked: top apps with model, price, rating, rating count, and last update, plus the star split of each leader's 50 most recent reviews.
- **Phase 3, deep dive.** Five finalists: market tables, the 100 most recent reviews beside lifetime scores, monetization evidence with a low, mid, and high revenue estimate, build scope, risks, and reach. Each is filed as a landscape note under Research/Competitors.
- **Already covered and excluded:** expense capture, family story capture, writer tools, licensed-IP adaptations, card and IP games, TCG companions, mobile card games, volunteer fire department scheduling, flight-route visualization, and anything whose core value is dictation.

## Scorecard

| | Evidence of paying demand | Incumbent weakness | Search demand against difficulty | Solo build fit | Upkeep | Absorption risk | Reach |
|---|---|---|---|---|---|---|---|
| **1. Pool and spa water chemistry** | The rival nonprofit behind Pool Math reported $269K revenue in 2025, mostly from its $7.99/yr app (implies 17K–40K subscribers, estimate). Paid independents top out at 630 ratings. | Recent-100 reviews at 1–2 stars: Pool Math 38, Pool-Calculator 65, Clorox Pool 85. Pooli is healthy (83 five-star). | Apps with 20–43 ratings already sit in the top eight for head terms; vendor apps hold four or five of the top eight. | No backend. The hard part is the pH and alkalinity model, where incumbents contradict themselves. | 40–80 hours a year (estimate); support is dose disputes. | A chat assistant does one-off dosing math ("Just use Gemini" appears in reviews). Apple: none. | Search is open. The largest community belongs to the rival. France and Germany have no independent calculator above 10 ratings. |
| **2. Pipe trades calculator** | Pipe Trades Pro grew from 3,251 to 4,330 ratings in 20 months on a $39.99/yr subscription. QuickBend adds 622 ratings a year at $6.99. Reviewers name $25–$40 as a fair one-time price. | 36 of Pipe Trades Pro's 39 low reviews since 2022 are about the subscription, but it averages 4.81 and is accelerating. One-time apps are stale since 2015–2018. PipeBook ($12.99 one-time, August 2026) now holds the wedge. | Autocomplete confirms intent; results below the leader are thin. 23 new apps in 2026, 20 with zero to three ratings. | No backend. Calculators plus dimension tables; ASME requires permission to republish tables and no legal review was done. | One iOS pass a year plus table corrections. | The trigonometry is trivial for an assistant; offline use and trusted tables are not. | Job-site word of mouth. The incumbent owns the union training-center channel. Some plants ban phones. |
| **3. Bowling stat tracker** | PinPal has 5,016 ratings at $8.99 paid, every rater a payer. Lanetalk charges $25–$50/yr. A PinPal reviewer: "I'd pay double." | Lanetalk's recent 100 average 2.84 against 3.84 lifetime; 34 of 47 low reviews are about price. PinPal is unchanged since 2023 but 90 of its recent 100 are 4–5 stars. | Apps with 57–64 ratings reach the top five for "bowling score" and "bowling tracker". | Standard frameworks. Apple Watch entry is unclaimed. Scoreboard scanning is already shipped by two entrants. | 40–80 hours a year (estimate). | Low for longitudinal stats. Lanetalk's auto-import from 1,599 centers cannot be contested, and a restored free tier would end the push. | Search; 29,026 certified leagues; 1,075,194 USBC members, flat for four seasons. US-only market. |
| **4. Vehicle fuel and service log** | One-time prices of $4.99–$6.99 are praised; subscriptions are resisted even at $7.99/yr. | Vehicle Maintenance Tracker has 79 of its recent 100 at 1–2 stars (a date-wiping bug). Fuelly has had no release since June 2024. But Road Trip MPG ($6.99) has 95 of 100 at 4–5 stars and already imports Fuelly data, and Fuelly staff confirm a rewrite. | Apps with zero to three ratings appear in the first results for "fuel log" and "mpg tracker". | Standard frameworks. No CarPlay app category fits (a reading, not tested). | 40–80 hours a year (estimate); migration support. | Apple: none found. CARFAX Car Care (127,591 ratings, free) covers the service half. EVs are about 2.6% of the US fleet. | "Fuelly alternative" searches and Fuelly's own forum. The large audiences are on Android (Fuelio 135,748; Drivvo 115,316). |
| **5. Bill organizer** | One-time unlocks of $4–$10 are the norm; Bill Tracker Pro sells $18–$50/yr with 5,014 ratings. "Free" is a suggested modifier on every head term. | The incumbent (24,715 ratings) has had no release since April 2024 and its recent 100 average 3.76 against 4.69 lifetime. But 59 of those are five-star, and one compatibility release closes the gap. | Apple suggests "bill tracking apps similar to bills organizer &". The incumbent still ranks first on six of eight terms. 60 new apps in 2025–2026, none past 100 ratings. | The simplest build of the five; sync and partner sharing are the work. | One pass per iOS release; lost data or a missed reminder is unforgiving. | Moderate and rising: iOS 27 Reminders builds repeating reminders from a sentence, and Wallet gained a Recurring view. | Search and Search Ads on the incumbent's name. US only. |

**Revenue estimates (net of a 15% store fee, steady state; all rest on assumed ratings-to-downloads ratios)**

| | Low | Mid | High | What the high case requires |
|---|---|---|---|---|
| Pool and spa water chemistry | about $45/mo | $600–$1,400/mo | about $3,200/mo | Top-three rank on head terms and about 10% of Pool Math's implied base |
| Pipe trades calculator | under $100/mo | $570–$1,400/mo | $4,300–$8,500/mo | QuickBend-level adoption, which took QuickBend four years to begin |
| Bowling stat tracker | about $200/mo | about $1,300/mo | about $6,300/mo | A download flow no manual tracker has shown; the mid case already assumes a top-quintile outcome |
| Vehicle fuel and service log | about $95/mo | about $570/mo | about $2,300/mo | A rating rate no post-2017 iOS entrant here has reached, while Fuelly stays broken |
| Bill organizer | about $70/mo | about $450/mo | about $2,500/mo | The incumbent's search position and a firmer paywall than the niche norm |

## Ranked finalists

1. **Pool and spa water chemistry calculator and log** — [[Pool & Spa Water Chemistry Apps — Landscape]], seed [[Pool & Spa Chemistry Log]]. The only finalist with outside evidence of a large paying base: the nonprofit behind Pool Math reported $269K in 2025. Three incumbents are failing in their recent reviews on specific, fixable complaints (one-log paywall, lost history, no bromine or spa ranges, targets not saved). France and Germany are open. Against it: eleven new entrants, a $5-once or $8-a-year price anchor, heavy seasonality, and the main community channel belongs to the rival.
2. **Pipe trades field calculator** — [[Pipe Trades Calculator Apps — Landscape]], seed [[Pipe Trades Calculator]]. Demand is live and measured (ratings growth from archived snapshots), users name the one-time price they would pay, and there is no backend, content treadmill, or regulated liability. Against it: a solo developer shipped the one-time-price version two months ago, the subscription incumbent is growing faster, and republishing ASME tables needs permission that no one has confirmed holding.
3. **Bowling stat tracker** — [[Bowling Stat Tracker Apps — Landscape]], seed [[Bowling Stat Tracker]]. A forced subscription is pushing users away from the category leader, the paid incumbent is frozen, and Apple Watch entry is unclaimed. Against it: 14 entrants in 14 months, the frozen incumbent's users are satisfied, and the leader's automatic score import is a network effect a manual tracker cannot match.
4. **Vehicle fuel and service log** — [[Vehicle Fuel & Service Log Apps — Landscape]], seed [[Vehicle Fuel & Service Log]]. Two large incumbents are broken at once. Against it: an excellent paid rival already covers the feature list and imports Fuelly data, Fuelly's rewrite is staff-confirmed, the price ceiling is the lowest of the five, and the big audiences are on Android.
5. **Bill organizer** — [[Bill Organizer Apps — Landscape]], seed [[Bill Organizer]]. The largest stranded base by rating count and the simplest build. Against it: the incumbent is degraded, not dead; 60 new apps have not converted the opening; Apple is moving into the job; and the lowest revenue estimate of the five.

The ranking orders the evidence, and the gap between second and fourth is small. It rests on review streams and rating counts, not on downloads or revenue.

## Screened survivors not taken to deep dive

Seven of the twelve screening survivors were not deep-dived. They are the next candidates if a finalist falls through.

| Candidate | Evidence for | Why it ranked below the five |
|---|---|---|
| Swim practice planner for coaches | The coach-planner pattern is the best-proven solo earner in the scan: Elite Hoops (basketball) about $10K MRR and Floga (yoga) about $10K MRR, both self-reported. Commit Swimming sells on the web at $39/month (unverified); its iOS app has 18 ratings at 3.33. Wrestling is the second target: 11,526 boys' high school teams and no planner app with ratings. | The pattern is proven in other sports; the swim-specific evidence is one unverified web price and an app with 18 ratings. First runner-up. |
| Knitting pattern PDF and chart tracker | knitCompanion ($29.99, 6,875 ratings) has 18 of its last 50 reviews at 1–2 stars (no sync, per-device purchase). Loopsy (16,167) has 21 of 50 at 1 star after removing PDF import. | My Row Counter (3,715 ratings, $10–15/yr, 45 of 50 recent at 5 stars) already does PDF import with a highlighter. A healthy rival holds the opening. |
| Cross-stitch pattern markup | Markup R-XP (3,009 ratings) has 21 of its last 50 reviews at 1 star after an August 2026 redesign. Surfaced during the screen, not checked further. | Not screened in full: no price, rival, or size data gathered. |
| Lock-screen spaced-repetition tool for Arabic script and Quranic vocabulary | A one-person lock-screen kanji app shows $6.8K MRR (payment-provider verified). The same mechanic reached 327 ratings (Korean) and 665 (kana) in three months. Arabic study apps sit at 6,800 and 4,177 ratings; the only widget-first Arabic app has none. | One publisher shipped three CJK scripts in two weeks, so the mechanic is being rolled across scripts by an existing player. |
| Eczema log for parents | 31.6M US patients against a top app with 217 ratings (free, nonprofit, login failures). | No paying evidence exists for eczema logging. Ten of 22 conditions checked already have a loved or established app. |
| Machinist feeds-and-speeds calculator | CNC Machinist Calculator Pro at $14.99 has 678 ratings and no update since 2024-10; desktop G-Wizard is $79/yr; 299,500 machinists (BLS). | The leading seller is still active with a newer edition. Covered as a sub-niche in the pipe trades deep dive. |
| Delayed-video instant replay for coaches | Paid apps at $39.99 (225 ratings) and $7.99 (84) still chart; no strikes apply. | The whole niche totals under 1,000 ratings, and the incumbent's free version (535 ratings, $12.99/month) was updated 2026-09-29. |

## Cut at the screen (Phase 2)

| Candidate | Reason |
|---|---|
| Kids' allowance and chore ledger | iAllowance has two reviews in 2026; Chorsee (11,810, $39.99/yr) and Chores & Allowance Bot (10,929) already hold the users. |
| Radio-to-TV sports audio sync | The only dedicated app has 52 ratings at 1.48. No legal audio source without a stream partner or external radio, and streams usually trail the TV picture and cannot be advanced. |
| Quilt design on iPad | Desktop pay is real (EQ8 $239.95, PreQuilt $50/yr) but it is the largest build considered, the best iPad design app has 220 ratings in ten years, and two apps were updated in September 2026. |
| Beekeeping hive log | The category totals about 2,500 ratings; HiveTracks (1,119) has 38 of 50 recent reviews at 4–5 stars and HiveBloom holds the low-price slot at $17.99/yr. |
| Machine-embroidery design viewer | StitchBuddy HD has 295 ratings after 14 years and is still updated; stitch formats and machine transfer are proprietary; Brother's Artspira is disliked but locked to Brother machines. |
| Count-sheet builder for dance and cheer | The only count-sheet app has 10 ratings with a $1.99 unlock; cheer music vendors give count sheets away as PDFs; ArrangeUs (4,422 ratings) can add counts from the same free iOS 27 framework. |
| WBGT heat-stress monitor | Zelus has 18 of 32 written reviews at 1 star, nearly all about losing the free tier; Heat Safety (2,781) tops out at a $6.99 upgrade; app-estimated readings are reported off by up to 4°F (unverified). Counter-signal: Texas UIL mandated WBGT monitoring from 2026-08-01 and allows apps. |
| Sport-specific player tool (pickleball, disc golf, darts, billiards, archery, tennis) | UDisc has 67,048 ratings, SwingVision 4,910, darts scorers are free and loved, the pool-league scorekeeper is gated by league data, and pickleball's unfunded remainder is a $3–6 scoring utility. Bowling was the exception and became a finalist. |

## Cut after the wide scan (Phase 1)

| Candidate | Source scan | Reason |
|---|---|---|
| Safari extensions | Charts | Fifteen chart entries from individuals prove the format, but no specific unmet job surfaced; Safari keeps absorbing the common ones and site-specific ones break when the site changes. |
| Co-parenting custody log | Charts | The indie incumbent Alimentor 2 ($6.99, 1,316 ratings, 4.85) is healthy; the subscription products need both parents to join. |
| Occupation-specific shift calendars and pension calculators | Charts, stale | Small market per occupation and yearly pay-table upkeep; Supershift and others hold the general shift-calendar users. |
| Youth-sports walk-up music and scorebooks | Charts | BallparkDJ (25,968 ratings) holds walk-up music; GameChanger absorbs scoring. |
| Photography light planners and film tools | Charts | Seven well-rated planners at $8–12; ephemeris math is a commodity. |
| RV boondocking and public-land finders | Charts | Point-of-interest data needs constant upkeep; user-submitted sites are a network effect. |
| GPS audio tours | Charts | The content is the product; each tour is a production. |
| Hobby collection logs (whiskey, board games, aquarium, dive) | Charts, niches | Catalog databases are a content burden; aquarium is crowded with 2026 entrants and controller hardware; dive logs depend on dive-computer sync. |
| EMS and fire pocket references | Charts | Protocol text belongs to agencies; dosing content carries liability; revisions are a treadmill. |
| Peptide and GLP-1 dose trackers | Charts, revenue | Dosing liability, App Review exposure, and fast-follower crowding with venture-funded leaders. |
| Niche single-purpose weather (drone, astronomy, rain totals) | Charts | Individuals do chart here, but each needs a data feed with uptime expectations; Apple Weather absorbs the generic cases. |
| Field paperwork for tradespeople | Revenue | Both verified earners run multi-user backends and sell country-specific tax compliance. |
| Single-behavior quit counters | Revenue | The earners are driven by short-video marketing, and success ends the need. |
| Creator capture utilities and teleprompters | Revenue, platform | Five maintained teleprompters with 15K–35K ratings; camera features are Apple's home turf; the foldable-iPhone angle has a tiny installed base. |
| Scripture and devotional companions | Revenue, charts | Modern translations are licensed; funded "Bible chat" apps dominate the grossing chart. |
| Local-first habit tracker | Revenue | Least open room of the revenue patterns; HabitKit took three years to pass $10K MRR. |
| App-gating focus blockers | Revenue | Rests on Apple's Screen Time entitlement; flooded category. |
| Phone-as-accessory utilities (TV remotes, speed cameras) | Revenue | Depend on device protocols or licensed data; overrun by weekly-subscription clones. |
| Song-structure practice player | Platform | About ten maintained rivals can add the same free iOS 27 analysis; no stems or chords; streaming tracks probably cannot be analyzed (unverified). |
| On-device team photo sorter | Platform | Delivery to other families needs a backend; biometric-privacy law applies to other people's children's faces. |
| Shift-pattern alarm clock | Platform | Supershift already sells shift alarms; two AlarmKit-native entrants have almost no ratings. |
| Handwritten-answer math facts | Platform | The largest incumbent already has handwriting recognition. |
| Seed-packet planting calendar | Platform | Seed to Spoon already handles packet photos; a chat assistant does the same from a photo. |
| As-needed medication interval timer; pay-once medication reminder | Platform, demand | Dosing guidance is a liability; the app would sit on top of Apple Health's own medication feature; the reminder store is crowded. |
| Teen driving log | Platform | Eight new entrants in 2026, most free; single-season use. |
| Offline baby monitor | Platform | Cloud Baby Monitor already works offline; reliability support load; needs an Android app for the cross-platform claim. |
| HVAC duct and psychrometric calculators; electrical and conduit calculators; concrete calculators | Niches, charts, stale | Healthy or free incumbents hold each (QuickBend for conduit, manufacturer apps for refrigerant, Concrete Calculator Plus still at 47 of 50 five-star). Pipefitting was the open sub-niche and became a finalist. |
| Cut-list optimizer | Niches | The top subscription app has 116 ratings; free web optimizers exist. |
| Homeschool planner | Niches | No iOS app shows meaningful paid ratings; the keyword filled with 2026 entrants; reporting rules differ by state. |
| Handweaving draft designer; small-livestock breeding records; yoga sequence builder | Niches | Very small base; breeders expect web sync and data migration; yoga is already held by Floga and Tummee. |
| Daily "I'm OK" check-in | Demand | Needs a server to detect a missed check-in and alert contacts, with safety liability; Snug leads. |
| Pantry-to-recipe matcher | Demand | Needs a licensed or maintained recipe database. |
| Storage bin tracker; physical media catalog; garden planner | Demand | Already served (Sortly, CLZ) or crowded and seasonal. |
| Pet seizure log; name-and-face flashcards; grocery price book; acreage marker | Demand | One or two asks each; no paying evidence. |
| Cocktail recipes; wine journal; speech-therapy word lists | Stale | Content-heavy; Vivino and CellarTracker hold the wine users. |
| Teacher grading slide chart; note-reading trainer; first-responder shift calendar | Stale | Users of the stale grading app are satisfied (50 of 50 five-star); healthy rivals hold the other two. |
| Menopause tracker; photo calorie logging | Platform | Apple shipped both in iOS 27. |

## Gaps

- **No download or revenue data for any app.** Every revenue figure converts rating counts to downloads with an assumed ratio (1–5% depending on the report). The ratio is the single largest uncertainty in the scan.
- **No usable keyword measurement.** The astro MCP refused the connection in every agent. The appstore MCP's keyword scores changed between identical calls and are not reported as evidence. What is reported instead: Apple's search suggestions and which apps appear for each term in the iTunes Search API, which approximates but is not the live store ranking.
- **Reddit was unreachable** for fetch and for domain-filtered search. The unmet-demand scan relied on Bluesky and four forum pages, and it found nothing usable from trades and professions. That is a coverage gap, not evidence of no demand.
- **The three best-proven revenue patterns were screened only at pattern level.** Coach planners, sport-specific player tools, and condition logs each got one screening pass to pick a target. None got a deep dive.
- **Regional storefronts were checked only inside the deep dives.** The wide scan and the screen were US-only.
- **Launch failures and bugs were read from reviews, not reproduced on a device.**
- **Legal questions were identified, not resolved:** republishing ASME dimension tables, the lineage and licensing of the pool chemistry formulas, and the "PoolMath" and "TFP" names.
- **Per-finalist gaps** are listed at the end of each landscape note.

## Sources

Listed in each landscape note. Phase 1 and Phase 2 working files (chart pulls, the 365-term sweep, the revenue disclosure table, screening tables) were kept in the session scratchpad and are not filed in the vault.

## Relevant To

- [[Pool & Spa Chemistry Log]], [[Pipe Trades Calculator]], [[Bowling Stat Tracker]], [[Vehicle Fuel & Service Log]], [[Bill Organizer]] — the five seed ideas
- [[Indie iOS Market Calibration 2026]] — the viability bar and conversion figures
- [[WWDC 2026 Platform Shifts]] — the sherlock avoid-list, extended here by two iOS 27 absorptions (menopause tracking, photo calorie logging)
