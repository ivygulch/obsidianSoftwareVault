---
type: research
confidence: verified
tags: [pool, spa, water-chemistry, utilities, indie-scan]
created: 2026-10-02
updated: 2026-10-02
---

# Pool & Spa Water Chemistry Apps — Landscape

> Deep dive from the [[Indie App Opportunity Scan — 2026-10-02]]. Store figures were fetched on 2026-10-02; every revenue figure is an estimate resting on an assumed ratings-to-downloads ratio. Keyword scores come from the appstore MCP's heuristic tool because the astro MCP was not connected.

Scope, date, method: deep dive on a pool/spa chemistry calculator and test log as a solo-developer portfolio app, run 2026-10-02. Store data came from the iTunes Search/Lookup API (US, FR, DE, AU, GB), the reviews RSS (100 most recent US reviews per app), App Store product pages (in-app purchase lists), Google Play pages (install bands) and the appstore MCP (Android search/details, keyword scores). The astro MCP failed to connect (ECONNREFUSED), so keyword figures are the appstore MCP's heuristic scores. Web figures come from search-result summaries unless marked "fetched". Builds on p2-b.md and p1-niches.md. Rating counts are a size proxy, not revenue.

## 1. Market table

US storefront, fetched 2026-10-02.

|Class|App (publisher)|Model / price|Avg|US ratings|Released / updated|
|---|---|---|---|---|---|
|Independent|Pool-Calculator (Pool and Spa Resources)|Paid $4.99|4.15|630|2011-01 / 2025-10|
|Independent|Pooli (Pooli, Inc.)|Free; Club Plus $13/mo, $33/qtr, $109/yr; Club Max $139/yr with strips (sold on pooli.app)|4.59|370|2020-01 / 2026-09|
|Independent|Pool Math (TroubleFreePool, a 501(c)(3))|Free + $7.99/yr|3.63|287|2017-06 / 2026-05|
|Independent|Pool Care by Swim University (Gazzini Ventures)|$49.99/yr, 7-day trial|4.60|224|2024-05 / 2026-09|
|Independent|Pool Math Calculator (S. Nesterenko)|Free + $12.99 unlock|4.79|43|2025-05 / 2026-07|
|Independent|Poolistry (Yonah Systems)|$1.99/mo, $9.99/yr, $59.99 lifetime|4.88|25|2025-10 / 2026-09|
|Independent|Simple Pool (Grey Park)|Free + $9.99 lifetime|4.95|20|2025-04 / 2026-09|
|Vendor|Clorox Pool, strip photo reader (BioLab)|Free|4.59|29,019|2015-02 / 2025-01|
|Vendor|Leslie's Pool Care, AccuBlue tester (Leslie's)|Free|4.62|14,176|2018-06 / 2026-08|
|Vendor|FROG Water Care, spa (King Technology)|Free|4.55|4,872|2018-08 / 2026-07|
|Vendor|HTH Test to Swim, strip reader (Solenis)|Free|4.68|3,974|2013-05 / 2026-07|
|Vendor|Orenda, LSI calculator (HASA)|Free|4.72|476|2016-12 / 2026-09|
|Monitor|WaterGuru|Free with hardware|4.09|237|2018-11 / 2026-09|
|Monitor|Sutro|Free with hardware|3.85|175|2020-02 / 2025-11|
|Service|Skimmer Pro|$1–$2 per serviced location/mo, $49 minimum|4.62|3,598|2017-07 / 2026-09|
|Service|Pool Brain|about $55–65 per technician/mo|4.00|259|2019-08 / 2026-09|

Also: Pool Time ClearPool Expert (BioLab, 5,634, last updated 2023-08); AquaChek Connect (strip reader, 1,235 at 3.21); Pool Water Calculator ($4.99, 94); iopool (95) and Crystal (5) monitors; PoolFu ($5.99/mo, $53.99/yr, Pro $29.99/mo; 4 ratings). Strip readers are all vendor apps plus Pooli's paid scan. pHin (Hayward) shut down 2021-12-20. Equipment-control apps are a separate, larger class (iAquaLink 100,277; Pentair Pool 24,141).

New independent entrants since 2025-04: Simple Pool, Pool Math Calculator, Poolistry, Hot Tub Buddy, Loopym ("AI powered"), PoolFu, Aquavail, Soak, My Pool, PLOO (FR, 2026-09-22), Pool Guru (DE, 2026-09-24) — at least eleven in eighteen months.

Android (Play pages fetched; installs, ratings, average): Pool Math 100K+, 392, 3.0; Pooli 50K+, 333, 4.4; Orenda 50K+, 446, 4.6; Pool-Calculator 10K+, 220, 4.4 (free); Clorox Pool Care 500K+, 2.46K, 1.9; HTH 100K+, 1.05K, 4.6; WaterGuru 10K+, 153, 3.9. Roughly one rating per 100–250 installs for the independents.

Other storefronts:

- France (3.7M private pools in 2025, FPP via search summary): leaders are hardware and vendor apps — Flipr 7,837, Joey by Irrijardin 2,545, ICO by Ondilo 1,176, My Pool Expert by BAYROL 756, iopool 192. Pool Math has 0 French ratings, Pool-Calculator 1; Piscine Facile 10.
- Germany (832,600 private pools, bsw 2021, via search summary): ICO 623, My Pool Expert by BAYROL 597, Steinbach Pool Control 95 (1.92). No independent calculator above 2 ratings.
- Australia (pool count not found): Orenda 16, ICO 14, Pool-Calculator 13 (A$7.99, 2.77), Loopym 11, Pooli 10, Pool Math 7. No local leader surfaced; two AU searches failed (API throttling), so this is incomplete.
- UK (330,000+ hot tubs plus 800,000+ inflatables, BISHTA 2022, via search summary): a hot-tub market. Lay-Z-Spa WiFi 1,559, Smart Water Care 104, ControlMySpa 63, Pool-Calculator 21.

Units and practice (general knowledge, unverified here): metric outside the US; hardness in °f in France and °dH in Germany; salt chlorinators dominant in Australia; chlorine tablets, salt electrolysis, bromine, PHMB and active oxygen in France and Germany; bromine or chlorine granules for UK tubs. Pool Math, Pool-Calculator, Pooli, Orenda and Clorox Pool each list one language; Simple Pool and Poolistry list seven.

## 2. Review mining

Stars are 5/4/3/2/1 counts over the 100 most recent US reviews.

|App|Lifetime|Last 100|Span|
|---|---|---|---|
|Pool Math|3.63 (287)|34/17/11/14/24|2020-06 to 2026-09; last 50 are 12/9/3/9/17|
|Pool-Calculator|4.15 (630)|12/6/17/10/55|2019-05 to 2026-09; the 25 since 2023 are 3/2/5/3/12|
|Pooli|4.59 (370)|83/5/2/3/7|2021-12 to 2026-09|
|Clorox Pool|4.59 (29,019)|1/3/11/13/72|2024-06 to 2026-08|

Written reviews per year are few: Pool Math 12 (2025), 14 (2026 to date); Pooli 19, 10; Pool-Calculator 3, 4.

**Pool Math.** Praise: dosing for the owner's volume, "Effects of Adding", CSI, the timeline, the forum. Complaints since 2024: free tier locks after one log (6 reviews), lost history or failed sync (7), crashes and freezes (7), dislike of the 2024 redesign (6).

- 1★ 2026-09-20: "It should have just be a paid app ... You get exactly one test and then after that you cannot change."
- 1★ 2025-09-25: "Upgraded to a new phone and lost ALL my historical data"
- 1★ 2026-07-10: "Desktop app said 56oz of [muriatic] acid. The app said 8 oz"
- 1★ 2024-09-25: "My pool is a bromine pool. That's not an option in this app."
- 4★ 2022-11-21: "Why isn't bromine a sanitizer option? ... A hot tub is not a small pool."
- 2★ 2022-05-14: "I would be happy if the app let me customize these ranges"
- 4★ 2026-06-30: "Please add limited account sharing between (at least) two people."

Other asks: reminders that actually notify (2★ 2025-11-16); Apple Watch (4★ 2023-02-20); choice of LSI or CSI and custom tracked parameters (5★ 2021-05-26); non-chlorine oxidizer and spa options (4★ 2022-04-21); phosphate (3★ 2022-07-19); volumes as well as weights (4★ 2021-06-20); tablet counts (5★ 2024-07-04); health-department ranges (4★ 2024-06-01); no login (1★ 2020-10-26).

**Pool-Calculator.** Praise is old (2019–2020). Since 2023: blank screens, load errors, lost data, no support contact.

- 1★ 2026-04-01: "Just bought this app. Doesn't work. Just get Error: Pool failed to load"
- 3★ 2026-03-01: "the muriatic acid calculation when you add borate is way off"
- 1★ 2022-02-05: iPhone and iPad versions gave 0.9 oz and 1.4 oz of acid for the same inputs.

**Pooli.** Praise: customizable parameters and ranges per pool or spa, chemical inventory, reminders, hot tub use, responsive developer. Complaints: strip-scan price, inconsistent scans, upselling, its AI assistant.

- 1★ 2024-08-02: "if you do multiple scans, you will get huge swings in between each scan"
- 2★ 2026-07-11 (AI assistant): "the chlorine recommendation changed from buying 12 gallons, to adding 2 gallons, then none"

**Clorox Pool.** 85 of the last 100 are 1–2★: login failures, freezes, inconsistent strip photos, product pushing, no spa support.

- 1★ 2026-08-02: "I can take multiple pics of the same strip and the numbers are all over the place."
- 1★ 2026-07-11: "No option for spa — Requires pools to be at least 1000 gallons" (also 2026-07-15, 06-16, 05-06)
- 1★ 2026-06-28: "Just use Gemini. It's AI can keep track of everything for you"

**Price statements.**

- Pool Math 5★ 2021-03-06: "$8 a year is a bargain"; 5★ 2021-03-29: "I'd pay way more for this app".
- Pool Math 5★ 2021-03-14: "not a huge fan of the $7.99 subscription ... Should be a single purchase"; 3★ 2024-02-24: "not paying a subscription fee for an abandoned app".
- Pool-Calculator 2★ 2022-05-08: "Wasted 5.00. You can pay 9.99 a year ... on web version which is a lot."
- Pooli 1★ 2023-08-23: "$13/month is insane."; 3★ 2021-12-31: "$10.00 per month is insane ... I'd probably pay $3.00 per month"; 1★ 2024-08-02 cancelled "because of wintertime coming up".
- Swim University 1★ 2026-07-07: "$50 a year is overpriced. Pool Math app does the same thing for $7.99 a year."

Stated willingness sits at $5 once to $8–10/yr, with one reviewer naming $36/yr for scanning; $50/yr and above draws objections.

## 3. Search demand

Tool: appstore MCP `get_keyword_scores`, US iOS (astro unavailable). Heuristic 0–10 scores built from suggest position and the installs of whatever ranks; billiards games and social apps inflate them. Not Apple Search Ads popularity.

|Term|Traffic|Difficulty|Top 5 (iTunes Search API order)|Vendor apps in top 8|
|---|---|---|---|---|
|pool calculator|7.59|7.67|Orenda, Poolistry, Clorox, Pool Math, Pool-Calculator|4|
|pool chemistry|8.05|7.68|Pooli, Orenda, Clorox, Leslie's, Pool Time|5|
|pool math|8.41|7.54|Pool Math, Pool Math Calculator, Orenda, Clorox, Leslie's|4|
|pool care|8.30|6.64|Swim University, Leslie's, Clorox, Pool Time, Pooli|4|
|pool maintenance|6.50|7.76|Clorox, Leslie's, Skimmer Pro, Pool Time, Pool Math|4, plus Skimmer|
|hot tub|9.44|7.05|X Browser, X, SmartTub, Hot Tub Buddy (1 rating), Telegram|1; no water-care app above 1 rating|
|spa chemistry|6.67|7.45|PoolFu (4 ratings), HTH, Pool-Calculator, then games|1 of 3 relevant|
|pool test|8.94|6.03|Clorox, HTH, Pool Time, Swim University, Pool Math|5|

Apps with 20–43 ratings (Poolistry, Simple Pool, Pool Math Calculator) already sit in the top 8 for head terms. "hot tub chemistry" returns FROG (4,872), then Soak (2) and Aquavail (1).

## 4. Size outside the store

- Pools: about 10.7M US pools, about 10.4M residential (PHTA as repeated by secondary sites; PHTA's page not fetched).
- Hot tubs: 7.3M (ConsumerAffairs, via search summary); a PHTA document says "more than 5.5 million". Range 5.5–7.3M.
- TroubleFreePool: "over 400,000 members" (search summary, unverified). TFP's PoolMath page (fetched): "75k+ pools managed", "1M+ tests logged", "PoolMath is now the primary source of funding for Trouble Free Pool."
- TFP Form 990 data (ProPublica, fetched): revenue $209,437 (2022), $197,028 (2023), $237,412 (2024), $268,999 (2025), 100% program services.
- Reddit: r/pools 171K (2026-07-21), r/hottub 81K (GummySearch via search summary; Reddit blocked).
- Chemical spend per pool: not found. Search summaries gave $15–25/month for a spa chlorine program (unverified).
- Seasonality, from review dates: Pool Math 83 of 100 reviews in May–September; Pooli 76 of 100 in April–August; Clorox Pool 44 of 100 in June alone. Regional split (Sunbelt year-round, north late May to early September) is general knowledge, unverified. Hot tubs run year-round.

Three searches were used here, one over budget.

## 5. Monetization evidence

Disclosed comparable: TFP's $269K in 2025. If PoolMath is half to all of it, that is $135K–$269K a year (estimate; no breakdown, and gross versus net of store fees is unknown), or roughly 17,000–40,000 subscribers at $7.99 across iOS, Android and web (estimate) — from an app with 287 iOS ratings. Rating counts understate this niche's paying base. That base took nine years and sits on TFP's forum.

Entrant accrual without a community: Poolistry 25 ratings in 11 months, Simple Pool 20 in 17, Pool Math Calculator 43 in 16, Pooli about 55 a year. At 100–250 installs per rating that is 2,000–14,000 installs a year (estimate).

Revenue range for a competent entrant — estimate, net of a 15% store fee:

- Low: 3,000 installs/yr × 2.1% (freemium median, calibration note) = 63 buyers × $9.99 × 0.85 = about $535/yr, $45/month. Performs like the 2025 entrants.
- Mid: 10,000 installs/yr × 6% (hard paywall after a trial; calibration median 10.7%, discounted for the $8 anchor and free vendor apps) = 600 buyers/yr. One-time at $14.99: 600 × $12.74 = $7.6K/yr, about $640/month. Annual at $14.99 with 55% renewal (assumed): 600 ÷ 0.45 = 1,330 subscribers × $12.74 = $17K/yr, about $1,400/month. Mid: $600–1,400/month.
- High: about 10% of PoolMath's implied base plus spa owners: 3,000 subscribers × $14.99 × 0.85 = $38K/yr, about $3,200/month. Assumes top-3 rank on head terms and a channel into dissatisfied Pool Math users. (Calibration note: $1K MRR within a year is a top-quintile outcome.)

Seasonality and model: installs cluster in April–July, so monthly plans get cancelled for winter. An annual plan bought at opening renews at the next opening. A one-time price removes seasonal churn and matches reviewer requests, but revenue then tracks each spring's new installs only. Spa owners are the year-round segment.

## 6. Build scope

Smallest version aimed at the top complaints:

1. Unlimited test log and calculator, no account, automatic iCloud sync.
2. Chlorine, salt-generator and bromine modes; a spa profile with its own ranges and volumes below 1,000 gallons; US and metric units.
3. Editable targets that persist, with presets (FC-by-CYA rule, conventional industry ranges, custom).
4. Doses for the owner's product and strength, by weight and volume, with side effects shown: bleach, cal-hypo, dichlor, trichlor, muriatic acid, dry acid, baking soda, soda ash, borax, calcium chloride, CYA, salt, MPS.
5. CSI and LSI, user's choice.
6. Charts, reminders that fire, multiple bodies of water, CSV export. Later: household sharing, widgets, Watch, weather, localization.

Chemistry model: chlorine, salt, calcium and CYA doses are stoichiometry plus product strength. pH and alkalinity doses need a carbonate-equilibrium model covering TA, CYA and borates; this is where incumbents disagree with themselves (8 oz vs 56 oz; 0.9 vs 1.4 oz; borate case "way off"). LSI is Langelier's published index; CSI follows Wojtowicz's published refinements as implemented in Richard Falk's ("chem geek") PoolEquations spreadsheet (attribution from memory, unverified). Lineage per forum threads (search summary): Falk's spreadsheet → Jason Lion's Pool Calculator → sold to poolcalculator.com ("© 2009–2026 ... All rights reserved") → TFP's PoolMath. No open licence was found for the spreadsheet or either codebase, so the path is implementing from published chemistry, not porting code or tables. No USPTO result surfaced for "PoolMath", "TFP" or "TFPC" (unverified); they are TFP's names. To be learned: carbonate equilibrium, chlorine–CYA equilibrium, ionic-strength corrections, bromine chemistry, generator output math.

Frameworks: SwiftData with CloudKit private database (no server); Swift Charts; WidgetKit; local notifications; WeatherKit optional. Household sharing needs CloudKit shared zones, which SwiftData did not support natively as of my knowledge (unverified for the current SDK). Camera strip reading is hard: colour under uncontrolled light needs a reference card (Pooli ships one), and reviewers of both Clorox and Pooli report repeat scans that disagree.

Yearly upkeep (estimate): OS-release pass, product list changes (a reviewer asked for 7.5% bleach), support mail about dose disagreements — 40–80 hours.

## 7. Risks and strikes

- Content treadmill: does not apply.
- Network effect: none in the product.
- Backend or support: no backend. Support is moderate; dose disputes are the load.
- License or partner dependence: none required; naming and formula provenance need care (section 6).
- Hardware: small in the US. WaterGuru claims "50,000+" customers (vendor claim, search summary), about 0.5% of residential pools; pHin is dead; Sutro reportedly ceased operations in October 2025 (search summary). In France connected devices lead the store (Flipr 7,837).
- Regulated liability: applies moderately; acid and chlorine doses are safety-relevant. Clorox's store text says "you use this information at your own risk"; Pool Math, Pooli and Orenda carry no disclaimer in store text (terms pages not checked).
- Absorption by a general AI assistant: applies, with review evidence ("Just use Gemini"). One-off dosing math is free in a chat. What an app adds: deterministic math (Pooli's assistant drew a 2★ for changing its dose mid-conversation), a persistent log and charts, reminders, widgets, offline use.
- Community: applies heavily. TFP is a nonprofit with the largest forum, sends newcomers to Pool Math, prices at $7.99 and is funded by it. Its users write the 1–2★ reviews, but the channel to them is TFP's.
- Free vendor apps: hold 4–5 of the top 8 on most head terms. Recent reviews are poor (Clorox 85 of 100 at 1–2★) and Clorox refuses volumes under 1,000 gallons.
- Crowding: at least eleven new independent apps since 2025-04, two already offering seven languages at $9.99 lifetime or $9.99/yr, one with bromine. The Phase 2 gap is being filled now.
- Price ceiling: reviewers anchor at $5 once or $8 a year.

## 8. Reach

- Search: reachable; 20-rating apps rank in the top 8. The same holds for every other entrant.
- r/pools (171K), r/hottub (81K): self-promotion rules not checked.
- TroubleFreePool forum: realistically closed to a rival app.
- Facebook owner groups and pool YouTube: not sized; Swim University sells its own app.
- Pool stores sell chemicals and in-store testing; misaligned. Independent hot-tub dealers are a possible outlet (unverified).
- One-truck service techs: served by Skimmer ($49/month minimum), Pool Brain, PoolFu Pro ($29.99/month), Pooli Pro. They need routing and billing; a multi-pool log with a customer report is a later tier.
- France and Germany: no independent calculator above 10 ratings; metric and local hardness units are the entry requirement.

## 9. Gaps

- PoolMath's share of TFP's $269K and its subscriber count are not disclosed; 17,000–40,000 is derived.
- No download or revenue figure for any independent iOS app; install bands are Android only.
- Keyword popularity is heuristic; no Apple Search Ads popularity or rank tracking.
- PHTA counts, TFP membership, subreddit sizes, Sutro's shutdown and WaterGuru's customer count were read through secondary or single sources.
- Chemical spend per pool: not found.
- Australia: pool count, local leader and salt-chlorinator share not found.
- Trademark status of "PoolMath"/"TFP", licence terms of PoolEquations and incumbents' terms-of-service disclaimers not checked at source.
- Strip-reading accuracy is from reviews only; community promotion rules and dealer interest not checked.

## Sources

- iTunes Search/Lookup API and reviews RSS: https://itunes.apple.com/search , https://itunes.apple.com/lookup , https://itunes.apple.com/us/rss/customerreviews/page=1/id=1228819359/sortby=mostrecent/json (also ids 412876581, 1491565847, 957130735, 1376878954, 6479329322, 1171005221)
- App Store pages (IAP lists): https://apps.apple.com/us/app/id1228819359 and the same path for ids 6479329322, 6748267875, 6744664712, 6746519942, 6756633198
- Google Play: https://play.google.com/store/apps/details?id=com.troublefreepool.poolmath and the same path for app.Pooli, com.psiflow.poolcalculator, com.elitecrest.orenda, com.kikcorp.cloroxpool, com.hthpools.tester.release, com.waterguru.android
- TFP: https://www.troublefreepool.com/blog/poolmath/ , https://projects.propublica.org/nonprofits/organizations/810726521 , https://www.troublefreepool.com/blog/2019/01/18/what-is-tfpc/
- Calculator lineage: https://www.troublefreepool.com/threads/pool-calculator-app.119559/ , http://www.poolforum.com/pf2/showthread.php/13364-The-Pool-Calculator , https://www.poolcalculator.com/
- Pooli pricing: https://pooli.app/lite-offering/ , https://pooli.app/pro-offering/
- Pool and hot tub counts: https://poolguardusa.com/swimming-pool-statistics/ , https://www.poolfounder.com/pool-ownership-statistics-us , https://www.consumeraffairs.com/homeowners/hot-tub-statistics.html , https://www.sundancespas.com/en-us/Hot-Tub-Chemical-Cost-Per-Month.html
- Reddit sizes: https://gummysearch.com/r/pools/
- Hardware: https://waterguru.com/ , https://iopool.com/blogs/connected-objects/phin-alternative , https://theygotacquired.com/product/sutro-acquired-by-sani-marc/
- International: https://www.connexionfrance.com/news/swimming-pool-boom-in-france-helped-by-fuel-crisis/789743 , https://www.fairland.com.cn/allnews/german-private-swimming-pool-market-grows-with-potential.html , http://www.poolandspascene.com/news/one-in-ten-households-own-hot-tub
- Service software: https://www.getskimmer.com/pricing , https://www.poolfounder.com/skimmer-vs-poolbrain
- Calibration: /Users/dwsjoquist/ivygulch/vault/Research/Trends/Indie iOS Market Calibration 2026.md ; prior phases: p2-b.md, p1-niches.md, p1-revenue.md

## Relevant To

- [[Pool & Spa Chemistry Log]] — the seed idea this landscape supports
- [[Indie App Opportunity Scan — 2026-10-02]] — scorecard and ranking across the five finalists
- [[Indie iOS Market Calibration 2026]] — conversion and renewal figures used in the revenue estimates
