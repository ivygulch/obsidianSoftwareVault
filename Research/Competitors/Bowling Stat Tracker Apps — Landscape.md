---
type: research
confidence: verified
tags: [bowling, sports, stat-tracking, indie-scan]
created: 2026-10-02
updated: 2026-10-02
---

# Bowling Stat Tracker Apps — Landscape

> Deep dive from the [[Indie App Opportunity Scan — 2026-10-02]]. Store figures were fetched on 2026-10-02; every revenue figure is an estimate resting on an assumed ratings-to-downloads ratio. Keyword scores come from the appstore MCP's heuristic tool because the astro MCP was not connected.

Scope: bowling score and stat trackers on the iOS App Store, assessed as a portfolio-member opportunity for one indie iOS developer. Data pulled 2026-10-02 from the iTunes Search/Lookup API, App Store product pages (in-app purchase lists), the customer-reviews RSS (100 most recent US reviews where that many exist), the appstore MCP keyword tool, lanetalk.com, bowl.com and the USBC 2025 annual report PDF. Builds on p2-a.md, p1-stale.md and p1-revenue.md. Figures not directly fetched are marked (estimate) or (unverified). Rating count is a size proxy, not revenue.

## 1. Market table

US storefront. Games excluded (Lets Bowl 2, My Bowling 3D, PBA Bowling Challenge and similar).

| App | Publisher | Model | Price | Rating | US ratings | Released | Updated |
|---|---|---|---|---|---|---|---|
| PinPal | Jeff Stuart | paid | $8.99, no IAP | 4.90 | 5,016 | 2009-07-25 | 2023-03-29 |
| Lanetalk Bowling | Lanetalk AB (Sweden) | subscription | $7.99/mo; $24.99/yr Basic; $29.99–$39.99/yr Pro USBC; $49.99/yr Pro | 3.84 | 2,296 | 2012-05-30 | 2026-09-21 |
| League Secretary | Nabso | free | standings lookup, not a tracker | 4.85 | 2,313 | 2022-09-05 | 2026-09-24 |
| Tenpin Toolkit | Tenpin Toolkit | one-time | $9.99 unlock, $39.99 lifetime; targeting/pattern tools, not score history | 4.92 | 851 | 2018-06-30 | 2026-07-21 |
| LaneTrax | LaneTrax Inc. | subscription | $9.99/mo, $89.99/yr; camera shot tracking | 4.78 | 594 | 2025-07-18 | 2026-09-17 |
| Bosc | Sho Nakazato (Japan) | freemium sub | $4.99/mo, $39.99/yr | 4.84 | 492 | 2023-11-30 | 2026-09-29 |
| BowlSheet | Edibu LLC | paid | $29.99 | 4.37 | 172 | 2011-12-21 | 2026-01-15 |
| Best Bowling LT | Tatsuhiko Koyama (Japan) | free | paid sibling ¥600 in Japan | 4.50 | 165 | 2010-07-31 | 2026-08-19 |
| Bowlski | Aidan Phi Twamley | freemium sub | $6.99/mo, $59.99/yr | 4.95 | 64 | 2026-06-25 | 2026-08-21 |
| StrikeMaster | Andrew Hill | freemium sub | $2.99/mo, $24.99/yr; PinPal Migration Add-on $5.99; AI scan packs $2.99–$4.99 | 4.90 | 63 | 2025-09-24 | 2026-09-17 |
| WeBowl | Chris Wolf | freemium | $19.99–$24.99/yr, lifetime $53.99–$59.99 | 4.84 | 32 | 2026-04-24 | 2026-09-27 |

Also: Bowlr (80 ratings, $9.99/yr). USBC's own apps are not trackers: BOWL.com (14 ratings, 2.50), BowlTV (66, 1.79). Center-chain apps were not checked.

Entrant count is higher than Phase 2 found: 14 manual trackers released since 2025-08, eleven in 2026. US ratings: Bowling XP 29, StrikeMaster 63, BowlingBoard 0, PinTracker 3, Advanced Bowling Tracker 15 ($9.99/yr), Score – Bowling Tracker 0, WeBowl 32, LaneMate 0, Bowlin 7, Lanebook 0, Panda Taps 12 ($14.99/yr, $24.99 lifetime), Bowlski 64, Lane 12 ($19.99/yr, $49.99 lifetime), Strikee 2 ($89.99/yr).

Other storefronts (ratings in that storefront):

- Japan: local trackers lead. Best Bowling (paid, ¥600) 537 at 4.49; Bosc 415 at 4.57; Best Bowling LT 368. PinPal (¥1,500) has 3 ratings, Lanetalk 1. Best Bowling's 50 most recent JP reviews: 11 at 1–2★.
- Korea: 칠텐 (Stat&Co.) 2,069 at 4.79, free; 15 of its 50 most recent reviews at 1–2★. Lanetalk 3 ratings.
- UK, Germany, France: no local tracker found; no app exceeds 28 ratings (Lanetalk 19 / 27 / 5, PinPal 19 / 14 / 17).
- Sweden: Lanetalk 182. Canada: PinPal 133. Australia: PinPal 90.

**Lanetalk's position.** Lanetalk pulls each frame directly from the scoring system at connected centers, so the bowler enters nothing. lanetalk.com/centers states 1,599 connected centers and 990,000,000 games tracked, with integrations for ten scoring vendors including Brunswick, QubicaAMF and Steltronic; a center activates it "in a few clicks" with no extra hardware. Its App Store description claims "500,000+ bowlers" (self-reported). A search summary puts 450 of those centers in the US (unverified); USBC's 2026 State of the Association says it measured "more than 3,400 centers" in the US, so on those two figures roughly 13% of US centers are connected (estimate). This is a partner network effect a solo developer cannot replicate. What a manual tracker offers: it works at every center; it needs no account (14 of Lanetalk's 100 recent reviews cite login failures); Lanetalk's own manual entry is behind the $7.99/mo paywall and two reviewers report it deleting entered games; and data can be exported (a Lanetalk 3★ of 2026-03-01 objects to "the lack of ability to export my raw data").

## 2. Review mining

| App | Lifetime | Recent written reviews | 1★ | 2★ | 3★ | 4★ | 5★ | Recent mean |
|---|---|---|---|---|---|---|---|---|
| PinPal | 4.90 (5,016) | 100, spanning 2017-02 to 2026-09 | 1 | 3 | 6 | 18 | 72 | 4.57 |
| Lanetalk | 3.84 (2,296) | 100, spanning 2025-12-17 to 2026-09-30 | 38 | 9 | 9 | 19 | 25 | 2.84 |
| Bosc | 4.84 (492) | 22 (all it has), 2024-04 to 2026-05 | 1 | 1 | 0 | 6 | 14 | 4.41 |
| StrikeMaster | 4.90 (63) | 7 (all it has) | 0 | 0 | 0 | 0 | 7 | 5.00 |
| Bowlski | 4.95 (64) | 18 (all it has); 6 dated 2026-07-10/11 | 0 | 0 | 1 | 0 | 17 | 4.89 |
| LaneTrax | 4.78 (594) | 28 (all it has) | 4 | 3 | 4 | 5 | 12 | 3.64 |

Review velocity is the sharpest contrast: Lanetalk drew 100 written US reviews in 9.5 months; PinPal drew 7 in 2026, 7 in 2025, 8 in 2024, against 11–16 a year in 2017–2019.

**PinPal.** Praise: league / tournament / open-play separation (34 of 100 mention leagues or tournaments, 30 of them 4–5★), spare, leave and split statistics (13), ball tracking (16), reliability over years. Complaints: abandonment (7 mention updates or outdatedness), two reports of wrong statistics, single-line ball list.

- "it seems the developer has given up working on it. You can't sort your bowling balls" (3★, 2025-05-12)
- "Bowled 8 strikes in a row, but it only said I had 2 in a row. Now I'm questioning all of the stats" (2★, 2024-12-19)
- "would love to see is an integration with the Apple Watch ... to quickly mark the pins" (4★, 2025-07-09)
- "nice to see the developer updating the app after a few year hiatus" (4★, 2019-02-15) — PinPal has gone dormant and returned before.

**Lanetalk.** 47 of 100 at 1–2★. 44 mention price or subscription, 34 of those at 1–2★. Other complaint themes: login and account failures (14), ads shown to paying users (5), bugs and lost manual games (9). Praise (44 at 4–5★): automatic tracking and leave-conversion stats (19 of the 44).

- "Why would I pay $8/month to manually track my scores when so many other apps do it for free?" (1★, 2026-05-18)
- "I live in a city that doesn't have any automatic scoring centers ... it erased all of my scores" (2★, 2026-03-17)
- "The fact that I can look at my leaves and see my conversion rate is a GAMECHANGER" (5★, 2026-08-21)

**Bosc.** Praise: clean entry, calendar view. Complaints: cannot delete a session (2★, 2026-01-15), asks for card details (1★, 2025-01-25).

**StrikeMaster.** "the best manual bowling tracking app I've used ... tracks lots of stats from pin leaves to Brooklyn strikes. They update it frequently" (5★, 2026-01-21). One crash report on iOS 26 (5★, 2025-12-14).

**Price statements, every one found:**

- PinPal: "I'd pay double the cost for a few more clicks into the stats categories" (5★, 2025-05-07); "well worth the one time payment" (5★, 2026-05-03); "especially with the high price" while asking for Apple Watch (5★, 2021-12-05); "Not worth $9" — no iPad, one bowler only (2★, 2021-04-10).
- Lanetalk: "$39 is a lot ... What are we really getting from the app that I can get from other cheaper apps such as pinpal" (3★, 2026-08-13); "For $40 bucks a year for a USBC member it's a steal" (5★, 2026-05-02); "worth the annual subscription if you are an avid bowler" (5★, 2026-08-21); "I thoroughly despise monthly payments for software" (2★, 2026-06-11); "charge 20$ before I even opened the app" (1★, 2026-02-25).
- LaneTrax: "there needs to be a one time purchase option" (2★, 2026-07-10).
- Bowlski: "I would put more bag spots for the free version" (3★, 2026-07-20). Bosc: "Totally worth it to buy" (5★, 2024-11-24).

**Stats and features asked for** (PinPal mentions per 100 in brackets): drill from a stat to the games behind it; ball per shot, including spare balls; ball list with sort, photos, layout notes; multiple bowlers / family [8]; device sync and phone transfer [6]; export [5]; Apple Watch entry [4]; handicap [4]; no-tap leagues [3]; lane pair comparison [3]; ball speed [2]; month-by-month average; iPad. Lanetalk reviewers add raw data export, custom game ranges, multiple profiles, condition tags. Bosc reviewers add single-pin spare rate, spare rate excluding splits, a ball database. Rarely asked for: first-ball average (0 PinPal, 1 Lanetalk) and oil pattern (1 each).

## 3. Search demand

Tool: appstore MCP `get_keyword_scores` (US, iOS). The astro MCP failed to connect (ECONNREFUSED), so there are no Apple Search Ads popularity figures. These are 0–10 heuristic scores, not measured search volume. "What ranks" is iTunes Search API order, an approximation of the live store ranking.

| Term | Traffic | Difficulty | Top results | Games in results |
|---|---|---|---|---|
| bowling score | 8.3 | 8.17 | BowlingScore – Easy Record (57 ratings), Bosc, Lanetalk; PinPal 12th | 2 of 15 |
| bowling tracker | 6.03 | 8.48 | LaneTrax, Bosc, Lanetalk, StrikeMaster, Bowlski; PinPal 11th | 0 of 14 |
| bowling stats | 7.3 | 7.3 | Lanetalk, LaneTrax, Bosc, PinPal | 0 of 14 |
| bowling scorekeeper | 5.65 | 7.76 | BowlingScore – Easy Record, Bosc, Lanetalk | 0 of 10 |
| bowling league | 7.26 | 6.94 | League Secretary, LeaguePals, Lanebook, Lanetalk | 4 of 10 |
| pinpal | 8.61 | 7.13 | PinPal first; four unrelated pin-trading and note apps | 0 of 10 |
| lanetalk | 7.52 | 6.66 | Lanetalk, LaneTrax, Bosc, Tenpin Toolkit, StrikeMaster | 1 of 10 |
| bowling (context) | not scored | not scored | all games | 14 of 14 |

Apps with 57–64 ratings hold top-five positions for "bowling score" and "bowling tracker", and PinPal sits 11th–12th for both.

## 4. Size outside the store

- USBC membership, verified from the 2025 annual report PDF: "During the 2024-2025 season, USBC had 1,075,194 members, 10,280 certified tournaments and certified 29,026 leagues."
- Season series from bowl.com's 2026 State of the Association (fetched): 2021–22 1,053,129; 2022–23 1,093,909; 2023–24 1,093,000; 2024–25 1,075,194; 2025–26 forecast "down less than 1%". 2020–21 was 850,669 (search summary, unverified).
- Long-run: about 9.8 million league bowlers at the end of the 1970s, an 89% decline to 2022–23; US centers from about 12,000 in the mid-1960s to about 3,800 in 2023 (Wikipedia via search summary, unverified).
- r/Bowling: 114,102 members (reddapi.dev via search summary, unverified; Reddit itself could not be fetched).
- Spend (search summaries, unverified): league fees $15–$25 a week over a 32-week season, about $480–$800; reactive-resin balls $130–$250+ plus $40–$70 drilling.

## 5. Monetization evidence

What is charged: one-time $8.99 (PinPal), $29.99 (BowlSheet), $9.99/$39.99 (Tenpin Toolkit); subscriptions from $9.99/yr (Bowlr, Advanced Bowling Tracker) through $19.99–$24.99/yr (WeBowl, Lane, StrikeMaster), $39.99/yr (Bosc), $25–$50/yr (Lanetalk), $59.99/yr (Bowlski), $89.99/yr (LaneTrax, Strikee). Four of the newer entrants also sell a lifetime tier at $24.99–$59.99.

How users react: see the price statements above. The objection is to paying monthly for manual entry and to losing a free tier, not to paying at all.

Demand proxies (fetched): US rating accrual per month since release — LaneTrax 41, Bowlski 19, Bosc 14.5, Tenpin Toolkit 8.6, WeBowl 6, StrikeMaster 5. PinPal: 5,016 US ratings, every rater a payer.

PinPal cross-check (estimate): if 2–5% of buyers rated, 100,000–250,000 US sales over 17 years × $8.99 × 0.70 = $0.63M–$1.57M lifetime, or $37K–$92K a year averaged; current sales are lower, since its written-review rate is about half the 2017–2019 rate.

Entrant revenue range (estimate, net of Apple's 15%, steady state after the first year). Assumptions: ratings are 1–2% of downloads (estimate), which turns the accrual figures above into roughly 250–500 downloads a month for StrikeMaster, 700–1,450 for Bosc and 2,000–4,000 for LaneTrax; blended first-year price $25 (mix of $19.99/yr and $34.99 lifetime); conversion bounds from the calibration note (2.1% freemium median; 10.7% hard-paywall median).

| Case | Downloads/mo | Conversion | New payers/yr | New-payer revenue | Renewals | Total/yr | Per month |
|---|---|---|---|---|---|---|---|
| Low | 400 | 2.1% | 101 | 101 × $25 × 0.85 = $2.1K | about $0.4K | about $2.5K | about $200 |
| Mid | 1,000 | 5% | 600 | 600 × $25 × 0.85 = $12.8K | 180 × $17 = $3.1K | about $16K | about $1.3K |
| High | 3,000 | 8% | 2,880 | 2,880 × $25 × 0.85 = $61.2K | 864 × $17 = $14.7K | about $76K | about $6.3K |

Renewals assume half of payers choose annual and 60% of those renew. Checks: the calibration note puts $1K MRR within a year as a top-quintile outcome (17.3% of new apps reach it within two years), so the mid case already assumes a top-quintile result. The high case needs LaneTrax-level download flow, which no manual tracker has shown. Top-down: 1,075,194 members × about 57% iPhone (estimate) × 5% who keep frame-level stats in an app (estimate) is about 31,000 people; the mid case takes 2% of that pool a year, the high case 9%. Shot Pattern's $500K ARR rests on paid acquisition and a golf base far larger than bowling's (unverified); it supports the pattern, not the magnitude.

## 6. Build scope

Smallest version that beats incumbents on their top complaints:

- Pin-by-pin frame entry with league / tournament / open-play separation, no account, no ads — answers Lanetalk's paywall, login and ad complaints.
- Strike %, spare % by exact leave, single-pin, multi-pin and splits, with drill-down from any stat to its games and a month-by-month average — the PinPal "pay double" request.
- Ball arsenal with photos, layout notes, sort, and ball-per-shot; lane pair, oil pattern and notes fields per session.
- iCloud sync and CSV export; no-tap and handicap options.
- Apple Watch pin entry. None of PinPal, Lanetalk, Bosc, StrikeMaster, Bowlski or WeBowl mentions Apple Watch in its store description.
- One-time or lifetime tier beside an annual price.

Frameworks: SwiftData with a CloudKit private database (no server), Swift Charts, WidgetKit, a watchOS companion. All standard. PinPal import is the uncertain piece: StrikeMaster sells one for $5.99, so it is possible, but PinPal's backup format was not examined.

Camera scoreboard capture: moderately hard and no longer a differentiator. StrikeMaster and Bowlski both ship AI scoreboard scanning; StrikeMaster sells scans in packs, which suggests a per-scan server cost (estimate). On-device Vision text recognition must handle glare, oblique angles and vendor-specific layouts (estimate, untested), and a scoreboard photo yields frame scores, not pin leaves.

Yearly upkeep (estimate): iOS and watchOS SDK updates, bug fixes and support email, about 40–80 hours. No content if balls and oil patterns stay as free-text fields.

## 7. Risks and strikes

- **Crowding by new entrants — applies, materially.** Fourteen manual trackers since 2025-08; none has passed 64 US ratings. Bowlski is accruing fastest (64 ratings in about 3 months, though 6 of its 18 written reviews landed in two days). StrikeMaster targets PinPal's base with a paid migration add-on, is at version 7.6 after twelve months, and ships on Android. Bosc is strong in Japan.
- **Network effect — applies to automatic import only.** Lanetalk's 1,599 centers are not contestable. If Lanetalk restores a free tier, the push driving its 1–2★ reviews stops.
- **PinPal is not broken.** 90 of its 100 recent reviews are 4–5★, it has returned from a hiatus before, and its users owe nothing further.
- **Shrinking participant base — applies long-term, flat short-term.** Down 89% from the 1970s peak (unverified); 1.05M–1.09M across the last four seasons (verified).
- **Content treadmill — avoidable.** Applies only if a ball database or oil-pattern library is included.
- **Backend / support — low** with CloudKit; rises if AI scanning is server-side.
- **License / partner / hardware — none** for manual entry.
- **Regulated liability — none.**
- **Apple or AI absorption — low** for longitudinal leave stats; scoreboard-photo scoring is already commoditized.
- **Thin non-US demand** in the UK, Germany and France; Japan and Korea have local leaders. League play is seasonal (32-week seasons cited above).

## 8. Reach

- App Store search: apps with under 100 ratings reach the top five for "bowling score" and "bowling tracker".
- r/Bowling (114,102 members, unverified): rules on self-promotion not checked.
- Forums: bowlingchat.net and mrbowling300.net surfaced in search; sizes not checked.
- League secretaries: 29,026 certified leagues (verified); League Secretary's 2,313 ratings show bowlers already install an app for standings.
- Pro shops and bowling YouTube: not investigated.
- Editorial round-ups: gobowling.com's 2026 guide lists only Lanetalk, Bosc, PinPal and BowlSheet.

## 9. Gaps

- Download and revenue figures for every app; all revenue numbers rest on an assumed ratings-to-downloads ratio.
- Apple Search Ads popularity (astro MCP unavailable).
- Lanetalk's US center count (450 is from a search summary), its paying-subscriber count, and the date its free tier was removed.
- Whether any tracker ships an Apple Watch app (store descriptions only were checked).
- PinPal's backup format; whether its price has changed over its life.
- r/Bowling size and rules from Reddit directly; forum sizes; pro shop and YouTube channels.
- USBC age demographics; the long-run decline figures.
- Android install counts (Bosc, StrikeMaster and WeBowl are on Google Play); center-chain apps.

## Sources

- iTunes Search and Lookup API: https://itunes.apple.com/search , https://itunes.apple.com/lookup (storefronts us, jp, kr, gb, de, fr, se, ca, au)
- Reviews RSS: https://itunes.apple.com/us/rss/customerreviews/page=1/id=321817464/sortby=mostrecent/json (and ids 493763132, 6472614518, 6742661765, 6773135805, 6475736816, 1390556454; jp 1318643593; kr 1498707344)
- App Store pages (IAP lists): https://apps.apple.com/us/app/id321817464 (PinPal); same pattern for ids 493763132 Lanetalk, 6472614518 Bosc, 6742661765 StrikeMaster, 6773135805 Bowlski, 6759236761 WeBowl, 411894855 BowlSheet, 1390556454 Tenpin Toolkit, 6475736816 LaneTrax
- Lanetalk centers: https://lanetalk.com/centers/
- USBC 2025 annual report: https://images.bowl.com/bowl/media/assets/usbc/about/051826_2025-annual-report_final_1.pdf
- USBC State of the Association: https://bowl.com/a-future-for-the-sport/2026-state-of-the-association , https://bowl.com/a-future-for-the-sport/2025-state-of-the-association
- Long-run decline: https://en.wikipedia.org/wiki/Bowling_league
- r/Bowling size: https://reddapi.dev/subreddits/bowling/insights
- Tracker round-up: https://gobowling.com/blog/guides-tips/the-best-bowling-tracking-apps/
- Costs: https://www.flyingbowling.com/blog/how-much-does-a-bowling-ball-cost.html , https://www.bowlero.com/league-faqs
- Calibration: /Users/dwsjoquist/ivygulch/vault/Research/Trends/Indie iOS Market Calibration 2026.md
- Prior phases: p2-a.md, p1-stale.md, p1-revenue.md (same folder); raw pulls in p3bowl/

## Relevant To

- [[Bowling Stat Tracker]] — the seed idea this landscape supports
- [[Indie App Opportunity Scan — 2026-10-02]] — scorecard and ranking across the five finalists
- [[Indie iOS Market Calibration 2026]] — conversion and renewal figures used in the revenue estimates
