---
type: research
confidence: verified
tags: [vehicle, fuel-log, maintenance, utilities, indie-scan]
created: 2026-10-02
updated: 2026-10-02
---

# Vehicle Fuel & Service Log Apps — Landscape

> Deep dive from the [[Indie App Opportunity Scan — 2026-10-02]]. Store figures were fetched on 2026-10-02; every revenue figure is an estimate resting on an assumed ratings-to-downloads ratio. Keyword scores come from the appstore MCP's heuristic tool because the astro MCP was not connected.

Scope: consumer iOS apps that log fill-ups, fuel economy, service history and reminders per vehicle; fetched 2026-10-02. Method: iTunes Search/Lookup API (US, DE, FR, GB, JP); App Store pages for in-app prices; reviews RSS (latest 100 where that many exist); appstore MCP for keyword scores and Google Play details (the astro MCP is configured but refused the connection, so there are no Astro figures); Wayback Machine copies of Fuelly forum threads (the live forum returns a Cloudflare 403); Apple's CarPlay Developer Guide (June 2026). Builds on p2-a.md and p1-stale.md. Rating count is a size proxy, not revenue. Figures not directly fetched are marked (estimate) or (unverified).

## 1. Market table

US storefront:

| App | Publisher | Model and price | Avg | US ratings | Released | Updated |
|---|---|---|---|---|---|---|
| Fuelly: MPG & Service Tracker | Fuelly, LLC | Sub: $0.99/mo, $7.99/yr | 4.74 | 29,557 | 2008-11 | 2024-06-03 |
| Vehicle Maintenance Tracker (VMT) | Hai Nguyen | Free; reviewers cite a paid "Pro" on annual subscription (price not found) | 4.30 | 2,927 | 2017-11 | 2026-06-27 |
| My Car – Vehicle Manager | KineApps Oy | Sub: $1.49/mo, $10.99/yr; Basic $2.99 | 4.70 | 1,168 | 2018-03 | 2026-09-22 |
| Drivvo | Cristian Cardoso | Ads + sub: $5.99–$49.90/yr listed | 4.68 | 967 | 2017-03 | 2026-09-30 |
| Road Trip MPG | Darren Stone | $6.99 paid, no IAP | 4.90 | 627 | 2008-12 | 2026-09-17 |
| Car Cave | Filemon Salas | Free + $4.99 one-time Premium | 4.67 | 370 | 2022-02 | 2026-09-30 |

Also: Simply Auto (867, $29.99 one-time or $1.49/mo, stale since 2022-03) and Fuel Monitor Pro (836, $1.99 paid). Adjacent: CARFAX Car Care (free, 127,591, 4.84, updated 2026-09-24) fills service history from shop reports and has no fuel log. GasBuddy (447,883) is a price finder; a Road Trip reviewer (2026-05-21) says its log's "editing features disappeared". AUTOsist (345) is now titled fleet management.

New entrants: eleven fuel or maintenance logs released since 2025 appear in the same searches, all at 76 ratings or fewer (MyAutoLog 76 since 2025-07; Gearboxe 4; ServiceLog Pro 4; Vehix 3; seven others at 0–2).

Regional (ratings in each storefront):

| App | DE | FR | GB | JP |
|---|---|---|---|---|
| Spritmonitor (free, remove ads $1.99) | 5,482 | 291 | 70 | 0 |
| 燃費記録簿 (no-ads $11.49/yr, cloud backup $19.99/yr) | — | — | 26 | 10,525 |
| Fuelly | 31 | 35 | 1,077 | 26 |
| My Car | 530 | 264 | 179 | 5 |
| Drivvo | 165 | 246 | 112 | 476 |
| Road Trip MPG (paid) | 141 | 43 | 121 | 15 |

Germany and Japan each have a healthy, current local leader (Spritmonitor: 39 of its latest 50 DE reviews at 4–5★; 燃費記録簿: 47 of 50 within five months). Germany also has FuelMe – Tankbuch (1,632) and HB-FahrzeugLog (1,347, $6.99 unlock), both current. France has no app above 300 ratings. The UK's largest is Fuelly at 1,077, with 24 of its latest 50 GB reviews at 1–2★.

Android: Fuelio has 135,748 Play ratings and Drivvo 115,316 (appstore MCP; US or global unverified), against 159 (Fuelio, Sygic) and 967 on the US App Store. Fuelly's Android app (aCar) has 21,084 at 1.87, last updated 2025-01. The category's large audiences are on Android.

## 2. Review mining

| App | Lifetime avg | Latest 100: 1★ / 2★ / 3★ / 4★ / 5★ | Mean of latest | Span to 2026-09 |
|---|---|---|---|---|
| Fuelly | 4.74 | 18 / 7 / 14 / 16 / 45 | 3.63 | 26 months |
| VMT | 4.30 | 46 / 33 / 12 / 6 / 3 | 1.87 | 3 months |
| Road Trip MPG | 4.90 | 2 / 2 / 1 / 5 / 90 | 4.79 | 62 months |
| CARFAX Car Care | 4.84 | 28 / 14 / 10 / 6 / 42 | 3.20 | 5 months |

For My Car and Drivvo the feed returned 50 US reviews each; 18 of 50 are 1–2★ for both.

**Fuelly.** The stream is slow (about 46 written reviews a year) and still 61% at 4–5★; 25% are 1–2★. Thirty of the 100 cite years of use. Regex theme counts: gas-station lookup failing 12; subscription or price objection 10; odometer, edit and backdating bugs 10; data loss or sync 9; login or database errors 8; "not updated" 8; reminders not firing 6; Android parity 6; EV/PHEV 2; CarPlay or widgets 1; backup 1; community MPG comparison 0.

- "App / website dead??? Getting login / DB errors. No warning to backup data" (1★, 2026-08-10)
- "the app does not generate push or badge notifications to let you know when maintenance is due" (2★, 2026-08-26)
- "The app does not automatically sync across devices or users... We have been unable to find a similar iPhone/iPad app. If we did, we would give serious consideration to switching." (3★, 2026-01-01)
- "Desperately needs full app widget support as well as full carplay support..." (3★, 2025-09-18)
- Praise: "Been using this app for 12+ years - incredible history" (5★, 2026-08-10).

Stranded users ask, in order of frequency, for working login and sync, reliable reminders, editable history, station lookup, a one-time price and Android-app parity. Export/import, CarPlay and EV support get one or two reviews each; community comparison gets none.

**VMT.** 100 reviews in three months, 79 at 1–2★, nearly all one bug: "ALL of my service dates were changed to Jan 1, 1900" (1★, 2026-07-14). "The developer has no fix and blames you for not paying for the premium version... I have now moved onto using Google Sheets." (1★, 2026-07-07). Reviewers track equipment too ("10-15 different vehicles, mowers, tillers, boats", 1★, 2026-08-29).

**Road Trip MPG.** The healthy rival. Praise: one-time price, longevity, developer support, iCloud/Dropbox sync, export, EV support. "runs locally - backup to icloud - data is easily exportable" (5★, 2025-08-20); "I had issues moving my history (10 years of it) from Fuelly. I emailed the files directly to the developer and he responded within the hour" (5★, 2022-04-26). Complaints: sync between two phones failing (2★, 2025-02-23); "Apple CarPlay would be nice" (5★, 2025-07-05).

**Price statements, all apps:**

- Fuelly: "Should have one time purchase... It's a simple app." (2★, 2026-08-03); "Sure it's under 10 bucks a year but why should I pay again (and again) for something I already own." (1★, 2025-02-16); "I pay for premium and can't share it with my wife" (5★, 2025-04-07)
- VMT: "certainly one worth paying for" (1★, 2026-07-25); "I would gladly upgrade to Pro but am afraid the same thing would happen." (2★, 2026-09-24)
- My Car: "Worth supporting for less than a buck a month." (5★, 2026-05-25); "I have no problems paying for software like this once." (2★, 2024-06-02)
- Drivvo: "to export the data that I enter into your app it cost me a membership of no less than $25 per year" (1★, 2026-05-30)
- Car Cave: "Very reasonable price, so I paid for the iCloud back up feature." (5★, 2026-06-30)

## 3. Search demand

Tool: appstore MCP `get_keyword_scores`, iOS, US. These are the tool's 0–10 heuristic scores, not search volumes. "Ranks" is iTunes Search API order, an approximation of store ranking.

| Term | Traffic score | Difficulty score | What ranks (top results) |
|---|---|---|---|
| fuel log | 7.76 | 7.46 | Fuel and Mileage Log (0 ratings), Fuelly, Fuel Log Tracker (2), Gas Log (0) |
| mpg tracker | 6.96 | 8.11 | Fuelly, MPG Tracker (3), Road Trip Lite |
| gas mileage | 8.09 | 7.82 | Fuelly, Road Trip Lite, GasBuddy, MileIQ |
| car maintenance log | 5.48 | 7.15 | CARFAX, VMT, Car Cave, AutoLog (0) |
| vehicle maintenance | 6.56 | 8.43 | CARFAX, VMT, Vehicle Service Manager (29) |
| service log | 8.60 | 6.84 | ServiceLog (49), VMT, Car Cave |
| fuelly | 9.29 | 5.92 | Fuelly, GasBuddy, Fuel Tracker (686) |

Apps with zero to three ratings sit in the first results for "fuel log" and "mpg tracker".

## 4. Monetization evidence

Charged: subscriptions of $7.99–$10.99/yr (Fuelly, My Car), $17.99/yr (Fuelio), $19.99/yr (燃費記録簿 backup), $24.90–$49.90/yr (Drivvo); one-time $4.99 (Car Cave), $6.99 (Road Trip), $29.99 (Simply Auto). Reaction: subscription objections are 10 of Fuelly's latest 100 even at $7.99/yr; one-time pricing is praised (Road Trip, Car Cave); paywalled export and ads draw 1★ reviews (Drivvo).

Revenue range for a competent entrant — estimate, US only, steady state:

- Demand proxy: US rating accrual of current apps — MyAutoLog 76 in 14 months (about 65/yr), Car Cave 370 in 55 months (about 80/yr), Drivvo 967 in 115 months (about 100/yr), My Car 1,168 in 102 months (about 137/yr).
- Assumption: one rating per 40–100 downloads (estimate, not fetched).
- Conversion: 2.1% freemium median, 10.7% hard-paywall median (RevenueCat, per the calibration note); a log people enter data into before paying behaves like freemium.
- Retention: 55% annual renewal assumed (the note gives 23–40% at first renewal, 56–70% by the third), so steady-state subscribers are new payers × 2.2. Net of 15% commission.

| Case | Downloads/yr | Conversion | Subscribers (new × 2.2) | Price/yr | Net/yr | Net/mo |
|---|---|---|---|---|---|---|
| Low | 3,000 | 2% | 132 | $9.99 | $1,120 | $95 |
| Mid | 8,000 | 3.5% | 616 | $12.99 | $6,800 | $570 |
| High | 20,000 | 5% | 2,200 | $14.99 | $28,000 | $2,300 |

Low is MyAutoLog's rating rate at the niche's common price; mid is My Car's rate; high is about 300 ratings a year, which no post-2017 entrant here has reached on iOS; it requires top ranking for "fuelly", "mpg tracker" and "gas mileage" while Fuelly stays broken.

Cross-check (estimate): Road Trip MPG, $6.99, 627 US ratings over about 17 years. If 2–5% of buyers rated, that is 12,500–31,000 US buyers and $74K–$186K net lifetime, or $4.4K–$11K a year. Road Trip's DE+FR+GB+JP ratings are 51% of its US count, a rough ceiling on non-US uplift. p1-revenue.md has no vehicle-log disclosure; its one car-related entry, Speedster (speed-camera alerts, $6.8K MRR, 2,460 subscriptions), does a different job.

## 5. Build scope

Smallest version that beats the incumbents on their top complaints:

- Fill-up entry with partial and missed fills, fully editable and backdatable history (Fuelly's edit bugs).
- Service records with photo/PDF attachments; reminders by date and by mileage or hours, delivered as local notifications (Fuelly's reminders do not fire).
- Per-vehicle units, kWh entries for EV and PHEV, hour-meter equipment.
- No account: local store with iCloud sync, plus sharing with a spouse (Fuelly: no sync across users, Premium not shareable).
- CSV export in the free tier; import of Fuelly's CSV. Fuelly's web export exists, per vehicle, with odometer, miles, gallons, price, date, tags and notes (Fuelly FAQ, search summary). Road Trip already publishes a Fuelly import guide. Fuelly service-record export and any VMT export were not checked.
- Home and Lock Screen widgets; a "log fill-up" App Intent (Siri, Shortcuts, Action Button).

Frameworks: SwiftData with CloudKit for the private store; household sharing needs CloudKit shared zones, which SwiftData does not provide directly (platform knowledge, not re-checked; Core Data's NSPersistentCloudKitContainer or SQLiteData's SyncEngine instead). WidgetKit, App Intents, UserNotifications, Swift Charts, StoreKit 2, MapKit search for station names. VisionKit for receipt or pump photos is optional. Live Activities have no obvious use.

CarPlay: entitlement categories are audio, communication, driving task, EV charging, fueling, navigation, parking, public safety, quick food ordering, video and voice-based conversational. Driving task apps "must enable tasks people need to do while driving. Tasks must actually help with the drive"; fueling apps "must provide meaningful functionality relevant to driving". A log filled in while parked fits neither on a plain reading (my reading; not tested). The guide also says "Your app does not need to be a CarPlay app to support widgets and Live Activities in CarPlay" (iOS 26 and later), but a widget "can only launch your app in CarPlay if your app is also a CarPlay app". So a glanceable CarPlay widget (last MPG, next service due) needs no entitlement; data entry in the car is not available.

Yearly upkeep (estimate): one pass per iOS release, import-format fixes and migration support email, roughly 40–80 hours. A make/model list would add a yearly content update (a Fuelly complaint, 1★ 2026-01-20); free-text vehicle names avoid it.

## 6. Risks and strikes

- **Fuelly rewrite: real, staff-confirmed, repeatedly slipped.** Site Team account EMY92, 2025-05-20: "Fuelly is supported. We are currently working on a completely new Android & iOS app to replace the existing apps... Hopefully, the app will be ready for release later this year." 2025-09-12: screenshots posted. 2025-10-22: "All of the feature work is done... we should have a beta version available around the beginning of the year." 2025-11-20: beta set for 2025-12-15, then missed. 2026-01-05: "Not yet... but we're very close." The beta thread's last post was 2026-05-17 (not read). The App Store still serves v3.3.7 from 2024-06. If it ships, the incumbent that holds users' accounts and data stops being stale.
- **A healthy rival already covers the feature list.** Road Trip MPG has EV support, iCloud and Dropbox sync, export, Fuelly import, a one-time price and 95 of 100 recent reviews at 4–5★. Its small count (627) reflects paid-up-front distribution, not product weakness.
- **Free absorber of the service half.** CARFAX Car Care is about 44 times VMT's size and free; 42 of its latest 100 reviews are 1–2★ (forced logouts and deleted vehicles after a July 2026 update, no custom service types), which may be temporary.
- **Crowding.** Eleven new entrants since 2025, none above 76 ratings: others see the opening and none has converted it.
- **Network effect.** Fuelly's community MPG database is one; zero of 100 recent reviewers mention it. Applies weakly.
- **Backend/support.** No backend with CloudKit. Support leans toward data migration; a VMT-style corruption bug is fatal here.
- **Content treadmill, license, hardware, regulated liability.** None, provided no vehicle database is shipped and OBD dongles stay out of scope.
- **Apple or AI absorption.** No Apple fuel or service log surfaced in iOS 26/27 coverage (search summaries, unverified). Low today.
- **EVs and connected cars.** EVs are about 2.6% of US light vehicles in operation and 5.8% (Cox) to 7.9% (Alliance for Automotive Innovation) of Q2 2026 new sales (search summaries). The fuel half erodes slowly. Manufacturer-app automatic logging was not assessed.
- **Platform split.** Fuelly reviewers in mixed iPhone/Android households rely on cross-platform sync.
- **Price ceiling.** Subscription resistance at $7.99/yr; the best-liked apps are one-time purchases.

## 7. Reach

- Search: "fuelly" (traffic score 9.29, lowest difficulty of the set), "fuel log", "mpg tracker", "service log".
- Migration: "Fuelly import" and "Fuelly alternative" pages for web search (App Store search for "fuelly alternative" returns no fuel log but Fuelly); alternativeto.net's Fuelly page; Simply Auto already runs such a blog page.
- Fuelly's own forum has a thread titled "Fuelly gone - what to use next" and a post "Wondering what everyone is moving too??" (2025-04-30).
- Car-enthusiast forums and subreddits; not surveyed.
- Equipment owners (mowers, generators, boats), visible in VMT and Road Trip reviews.
- Mileage-deduction audience: MileIQ (113,761), Stride (97,404) and Driversnote (38,965) hold those search results.

## 8. Gaps

- Astro keyword popularity and difficulty: the astro MCP did not connect.
- Fuelly beta status after 2026-01: live forum blocked.
- Downloads, subscribers and revenue for every app: none disclosed; the ratings-to-downloads ratio and Road Trip's buyer-rating share are assumptions.
- VMT's Pro price and export capability; Fuelly's service-record export.
- CarPlay entitlement outcome: read from the guide, not tested.
- Road Trip's current UI and widget support; Reddit and car-forum demand; manufacturer-app automatic logging.

## Sources

- iTunes Search and Lookup API: https://itunes.apple.com/search , https://itunes.apple.com/lookup (storefronts us, de, fr, gb, jp)
- Reviews RSS: https://itunes.apple.com/us/rss/customerreviews/page=1/id=295905460/sortby=mostrecent/json (same pattern for the other app ids and storefronts)
- App Store pages for IAP lists: https://apps.apple.com/us/app/id295905460 (same pattern)
- Google Play via appstore MCP: com.kajda.fuelio, br.com.ctncardoso.ctncar, com.zonewalker.acar
- Fuelly forum (Wayback): http://web.archive.org/web/20250523103443/https://www.fuelly.com/forums/f2/is-fuelly-no-longer-supported-23277.html ; http://web.archive.org/web/20251114021133/https://www.fuelly.com/forums/f41/sneak-peek-of-the-new-fuelly-ios-and-android-app-23363.html ; http://web.archive.org/web/20260118131739/https://www.fuelly.com/forums/f41/fuelly-v2-mobile-app-beta-invitation-23438-2.html ; http://web.archive.org/web/20260123194506/https://www.fuelly.com/forums/f42/fuelly-android-app-beta-testing-look-if-interested-23439.html ; http://web.archive.org/web/20260531144720/https://www.fuelly.com/forums/
- Fuelly export FAQ: https://www.fuelly.com/index.php/faq/9/Can-I-export-my-fuelup-data (search summary)
- Road Trip Fuelly import: https://darrensoft.ca/roadtrip/manual/csv-import/import-fuelly/ (search result, not opened)
- CarPlay Developer Guide, June 2026: https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf
- iOS 27 CarPlay coverage: https://www.macrumors.com/2026/08/17/ios-27-biggest-new-carplay-feature-in-years/ ; https://9to5mac.com/2026/09/21/heres-everything-new-for-carplay-in-ios-27/ (search summaries)
- EV share: https://www.coxautoinc.com/insights/q2-2026-ev-sales-report-commentary/ ; https://www.autosinnovate.org/posts/press-release/2026-q2-get-connected-press-release (search summaries)
- Fuelly alternatives: https://alternativeto.net/software/fuelly ; https://simplyauto.app/blog/fuelly-alternative.html
- Conversion and renewal figures: /Users/dwsjoquist/ivygulch/vault/Research/Trends/Indie iOS Market Calibration 2026.md
- Raw data and scripts: /private/tmp/claude-501/-Users-dwsjoquist-ivygulch-vault/86a81cea-4349-422b-8c6e-249d7c4427a0/scratchpad/ideas/p3v/

## Relevant To

- [[Vehicle Fuel & Service Log]] — the seed idea this landscape supports
- [[Indie App Opportunity Scan — 2026-10-02]] — scorecard and ranking across the five finalists
- [[Indie iOS Market Calibration 2026]] — conversion and renewal figures used in the revenue estimates
