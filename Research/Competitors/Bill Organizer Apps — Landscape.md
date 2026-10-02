---
type: research
confidence: verified
tags: [bills, reminders, personal-finance, utilities, indie-scan]
created: 2026-10-02
updated: 2026-10-02
---

# Bill Organizer Apps — Landscape

> Deep dive from the [[Indie App Opportunity Scan — 2026-10-02]]. Store figures were fetched on 2026-10-02; every revenue figure is an estimate resting on an assumed ratings-to-downloads ratio. Keyword scores come from the appstore MCP's heuristic tool because the astro MCP was not connected.

Scope: manual-entry bill due-date organizers and reminders on iOS (no bank login), US storefront, scanned 2026-10-02, building on `p1-stale.md` and `p2-a.md`. Method: iTunes Search and Lookup APIs (metadata, rating counts, five storefronts); App Store product pages (in-app prices, version history); the customer-reviews RSS feed (100 most recent US reviews per app); Apple's search-suggestion endpoint; web fetches for platform changes. Rating counts are all-time and a size proxy, not revenue; every revenue figure is an estimate. Four points in the inherited framing changed and are flagged where they occur: the incumbent is degraded rather than dead, its review flow is inflated by daily rating prompts, Chronicle Pro is a subscription rather than a one-time unlock, and the keyword-score tool proved unusable.

## 1. Market table

| App | Publisher | Model | Price | Avg | US ratings | Released | Last update |
|---|---|---|---|---|---|---|---|
| Bills Organizer & Reminder | Dennis Kruta (KDV Solutions) | free, 5-bill limit (per reviews), one-time unlocks | Unlimited Accounts $5.99; No Ads $3.99 | 4.69 | 24,715 | 2018-05-18 | 2024-04-10 |
| Bills Manager | Jose Fabian Pena | free with ads, one-time | Remove ads $5.99 | 4.77 | 8,079 | 2014-03-12 | 2026-08-11 |
| Bill Tracker Pro | Bill Tracker Pro, Inc. | subscription (was paid; now adds bank linking and a web app per reviews) | monthly $5.99–$11.99; annual $17.99–$49.99; Unlimited Bill Alerts $9.99 | 4.60 | 5,014 | 2015-11-24 | 2026-09-24 |
| Bill Organizer | Space-O Digicom | subscription + IAP | weekly $6.99; yearly $49.99; GoPRO $59.99; Unlock all bills $3.99 | 4.35 | 4,896 | 2012-04-13 | 2026-02-05 |
| Chronicle – Bill Organizer | LittleFin LLC | free + auto-renewing subscription (period not shown; reviews call it annual) | Chronicle Pro $14.99 | 4.83 | 3,788 | 2012-11-14 | 2026-09-25 |
| Bills Monitor Pro | 倩 赵 | paid + subscription | $0.99; Premium $0.99/mo, $9.99/yr | 4.63 | 1,699 | 2011-10-05 | 2026-08-18 |
| Bill Organizer + Reminders | Anastasia Kovba | freemium | Pro $0.99/3 mo; $2.99/yr; $9.99 lifetime | 4.84 | 319 | 2024-12-19 | 2026-08-20 |
| What's Due: Bill Tracker | Semper Phoenix LLC | freemium | $4.99/mo; $19.99/yr; $59.99 lifetime | 4.84 | 318 | 2023-05-15 | 2026-09-08 |

Also present: BillOut (284 ratings, $7.99 lifetime). Correction to `p2-a.md`: Chronicle Pro is described on its product page as an auto-renewing subscription, not a one-time purchase.

Other storefronts: the niche is a US one. The incumbent has 409 ratings in the UK, 9 in Germany, 0 in France, 3 in Japan; no bill-specific rival exceeds 81 in any of the four. The cause was not investigated.

Adjacent category (bank-linked): Rocket Money 395,467 ratings (Premium $2.99–$11.99), Monarch 112,190 ($99.99/yr), YNAB 61,705 ($109/yr), Copilot 30,456 ($95/yr), Quicken Simplifi 11,811. Is manual, no-login a distinct need? Partly. For: reviewers name it ("Good reminder easy to use. Don't have to give out information", 5★, 2026-09-11; "My old bill tracker was discontinued/swallowed up by a big name company", 5★, 2026-07-09); the price gap is $6 once against $95–$109 a year. Against: one reviewer scores manual entry as the defect ("Everything must be input manually and don't link to accounts", 1★, 2026-05-08); Bill Tracker Pro has moved toward bank linking; a competitor's blog reports Prism closed on 2024-02-20 alongside MyCheckFree and SilverBills and attributes it to autopay. Users on autopay still use the app as a ledger ("Check on the auto pays", 5★, 2026-04-17).

## 2. Review mining

| App | Lifetime avg | Recent-100 window | 1★ | 2★ | 3★ | 4★ | 5★ | Recent mean |
|---|---|---|---|---|---|---|---|---|
| Bills Organizer & Reminder | 4.69 | 2026-04-09 to 2026-09-28 | 20 | 6 | 11 | 4 | 59 | 3.76 |
| Bills Manager | 4.77 | 2024-07-01 to 2026-09-27 | 8 | 3 | 5 | 12 | 72 | 4.37 |
| Bill Tracker Pro | 4.60 | 2025-07-29 to 2026-09-30 | 31 | 9 | 8 | 11 | 41 | 3.22 |
| Chronicle | 4.83 | 2024-07-10 to 2026-09-30 | 16 | 2 | 9 | 13 | 60 | 3.99 |

The incumbent's page 1 feed returned empty during this run; its 100 combine page 2 fetched now with the page 1 cached by `p2-a` earlier the same day. Space-O's Bill Organizer (56 one-star of 100) is omitted because its 100 reach back to 2020.

**Bills Organizer & Reminder (incumbent).** Review rate about 17 a month, against 3.7 for Bills Manager, 7 for Bill Tracker Pro, 3.7 for Chronicle. That gap overstates relative demand: reviewers say the app prompts for a rating constantly ("asks me to give a review EVERY SINGLE DAY", 1★, 2026-05-09; "Stop asking for a review", 5★, 2026-08-11).

The fault is intermittent launch failure, not a hard stop, and it predates iOS 27. "since I've been to ios26, I'll open the app and it'll hang on loading the app and then it self shut down" (3★, 2026-04-28); "over the last six months it routinely crashes, or just stays on the blue loading screen" (3★, 2026-06-16); "Upgraded to iOS 27 with a new iPhone 18 Pro Max... it just sits at the main splash screen and doesn't load" (2★, 2026-09-19). 13 of the 26 one- and two-star reviews match launch/crash keywords (keyword match, not hand-coded). 59 of the 100 are still five-star, several noting the same fault.

- Praise: a glance view of what is due ("I just pop it open. See what's coming up.", 5★, 2026-04-17); avoided late fees ("saved me a lot of money in late fee charges", 5★, 2026-05-20); long tenure.
- Complaints: launch failure; the 5-bill free limit revealed after data entry ("Who has only 5 bills??", 3★, 2026-08-24; "waited to tell me until I'd spent all this time", 1★, 2026-04-29); data loss ("suddenly it just didn't work and everything was gone", 1★, 2026-05-16); unanswered support ("emailed the creators for support 5 times", 1★, 2026-08-13); ad content (2★, 2026-08-18).
- Requests: partner access ("I can't add my wife's access", 4★, 2026-07-31; also 2026-09-05); income against bills (4★ 2026-09-10; 3★ 2026-05-28).
- Price statements: "purchasing the unlimited accounts was worth every penny" (5★, 2026-08-08); "I would gladly pay a fee for this" (sync, 5★, 2026-04-09); "The published price is only 5.99 but i was charged 15.93. Such a scam!" (1★, 2026-09-04); "Bills Manager is better for those of you that want unlimited accounts for free!!!" (1★, 2026-04-24).

**Bills Manager.** Praise: complete free tier, developer answers email (5★, 2026-09-27). Complaints: no device sync, so a phone change wipes data ("I had to change phones and my data was completely erased!!!", 1★, 2026-09-04; backup is Dropbox-only per the product page); ads (2★, 2025-07-26); notifications ("their notifications simply don't work", 3★, 2025-03-04); no CSV export (3★, 2025-09-20); missing recurrence types (semi-monthly, every 30 days). Price statements: "love one time fee vs monthly" (5★, 2025-01-24); "more than happy to pay the one time fee to remove ads" (4★, 2025-02-19); "I can do all the things I need without paying into the app" (5★, 2026-05-07); "I'm not paying and I'm not going to be fed ads constantly" (2★, 2026-05-01).

**Bill Tracker Pro.** A redesign and the move to subscription drew 22 one- and two-star reviews from November 2025 through January 2026. "They have changed to a subscription and have not honored my original purchase." (1★, 2026-03-08); "Why did I get charged $40 for this app when I literally just paid $3.99 for the month of December?" (1★, 2025-12-30); "I don't need all the bells and whistles and just needed it to keep track of my bills like it did when it was free." (1★, 2026-01-05). For the model: "the annual fee is very reasonable" (5★, 2026-03-30); "Just wish it had a lifetime payment option. Also needs family sharing support." (5★, 2025-11-01).

**Chronicle.** Praise: 15-year tenure, responsive developer, partner sync ("me and my husband can sync to the same calendar", 4★, 2026-08-02). Complaints: sync faults ("One is always outdated", 3★, 2026-02-13), no export (1★, 2025-11-30), entitlement errors after renewal (1★, 2026-04-21). Price statements: "Competitors charge way too much but this is either free or low cost" (4★, 2026-08-02); "I know it's only $11.99, but I definitely feel ripped off!!!!" (1★, 2025-12-05); "why would I commit to spending money on an app that doesn't let you at least demo the features or have a trial period" (1★, 2026-08-14).

## 3. Search demand

Tool used: the astro MCP keyword tool was configured but failed to connect (ECONNREFUSED). The appstore MCP `get_keyword_scores` was used instead and its output is **not reported as evidence**: two identical calls minutes apart for "bill reminder" returned 5 then 2 exact title matches, 23 then 54 competitors, and "Moderately difficult" then "Difficult"; "budget" scored as easier to rank for than "bill reminder". Only the string-length component was stable. No popularity or difficulty figure is available from this run.

What was measured instead:

- Apple's own search suggestions (ordered, no volume). "bill" yields "bill organizer" second and "bill tracker" eighth; "bills" yields "bills organizer", "bills: organizer & reminder", "bills manager", "bills calendar", "bills tracker", "bills monitor". Apple suggests the incumbent by name, and suggests the query **"bill tracking apps similar to bills organizer &"**. "Free" variants are suggested for every head term: "free bill reminder", "bill tracker free", "bill organizer free app", "bill calendar free".
- What ranks (iTunes Search API order, which may differ from in-app search ranking). The incumbent is first for bill reminder, bill organizer, bill tracker, bill calendar, payment reminder and bill pay reminder, and second for bills due (behind Bills Manager) and bill planner. Behind it, positions 2–6 hold a mix of the established apps, budget apps (Fleur 12,951; Buddy 9,513; Rocket Money) and apps with 0–25 ratings.
- Entrant flood. Across the top 50 results for five terms, 104 distinct apps carry bill/due/payment in the name: 36 released before 2023, 5 in 2023, 3 in 2024, 18 in 2025, 42 in 2026. None of the 60 from 2025–2026 has reached 100 ratings (highest 78; median 1–3).

## 4. Monetization evidence

What is charged: one-time unlocks $3.99–$9.99 (incumbent, Bills Manager, BillOut, Bill Organizer + Reminders lifetime); annual plans $2.99–$19.99 at the small end (Chronicle $14.99, What's Due $19.99) and $17.99–$49.99 at Bill Tracker Pro and Space-O; lifetime up to $59.99. How users react: one-time is praised by name; subscriptions draw objections when imposed on an app that used to be paid or free, and when the charge surprises; a free tier with a low bill cap revealed after data entry is the single most repeated price complaint; "free" is an explicit search modifier and reviewers send each other to the free app.

Revenue range for a competent entrant (estimate). Demand proxy: the only two bill-specific entrants since 2023 to pass 100 ratings accrued 318 ratings in 40.6 months (7.8/month, What's Due) and 319 in 21.4 months (14.9/month, Bill Organizer + Reminders). Bills Manager averages 53.6/month over its life (8,079 ÷ 150.7); the incumbent 246/month (24,715 ÷ 100.5), inflated by its prompts. Converting ratings to downloads uses an assumed 2% of downloaders rating (unverified rule of thumb), giving roughly 400–750 downloads a month for the two entrants and about 2,700 for Bills Manager. Conversion anchors from the calibration note: freemium median 2.1% download-to-paid, hard paywall 10.7%, freemium Day-14 revenue per install $0.27, North America Day-60 $0.55. Net of 15% commission:

| Case | Downloads/mo | Conversion | Price | Arithmetic | Net |
|---|---|---|---|---|---|
| Low | 400 | 2.1% | $9.99 one-time | 400 × 0.021 × 9.99 × 0.85 | about $71/mo, $850/yr |
| Mid | 1,000 | 3.5% | $14.99 | 1,000 × 0.035 × 14.99 × 0.85 | about $446/mo, $5.4K/yr |
| High | 3,000 | 5% | $19.99 | 3,000 × 0.05 × 19.99 × 0.85 | about $2,549/mo, $30.6K/yr |

Low is what the two traction-getting entrants' volume implies at median conversion; most 2025–2026 entrants sit below it. Mid cross-checks against revenue per install (1,000 × $0.27–$0.55 = $270–$550 gross) and `p1-revenue.md`'s pay-once comparables at $300–$850 a month. High requires Bills Manager-level volume, meaning the incumbent's search position, and a firmer paywall than the niche norm. One-time pricing makes revenue track new downloads only; an annual plan adds renewals at an unknown retention rate. No bill app's actual revenue was found.

## 5. Build scope

Smallest version that beats incumbents on the top complaints:

- Opens reliably on the current OS; unlimited bills before any paywall prompt, or the limit stated up front.
- iCloud sync and survival of a phone change (Bills Manager's worst review theme; incumbent's data-loss theme).
- Recurrence done fully: weekly, biweekly, semi-monthly, monthly, every-N-days, quarterly, annual; edit one or all future.
- Reminders that fire, with mark-as-paid from the notification (the incumbent already has this).
- Upcoming list, calendar view, monthly total, paid history; optional income line for "left after bills".
- CSV export (requested on Bills Manager and Chronicle); partner sharing (requested on three of four apps).
- iPad layout, home/lock-screen widget, no ad network.

Frameworks: SwiftUI; SwiftData with a CloudKit private database for sync, or Core Data `NSPersistentCloudKitContainer` / SQLiteData `SyncEngine` if partner sharing is in scope, since SwiftData did not expose shared CloudKit zones as of iOS 26 (iOS 27 unverified); UserNotifications with actions, rescheduling around the 64 pending-notification cap; WidgetKit with interactive App Intents; App Intents for Siri (Chronicle shipped "new Siri AI" support on 2026-09-25); StoreKit 2. Not needed: Live Activities, AlarmKit, any server.

Upkeep per year: a compatibility pass on each iOS release (the task the incumbent skipped), StoreKit and widget API changes, and support mail on sync and lost data. No content, no server cost.

## 6. Risks and strikes

- Content treadmill, marketplace/network effect, hardware, license or partner dependence: none while manual.
- Backend or support: no backend. Support is moderate and unforgiving: users keep years of history, and a missed reminder or lost data produces one-star reviews in every app here.
- Regulated liability: none if it never moves money or links accounts.
- Absorption by Apple: moderate and rising. iOS 27 Reminders builds repeating reminders from a typed sentence. iOS 27 Wallet adds a Recurring view with calendar and list of upcoming charges, Apple Card only per the one source fetched. One incumbent reviewer already left for a system app: "I have moved all my bills to iPhone's Calendar" (3★, 2026-06-16). Not covered by Apple today: amounts and monthly totals for manually entered bills, paid history, non-card bills.
- General AI assistant: moderate; an assistant can set reminders, but the ledger, totals and history are the product.
- Commodity flood (not on the list, applies badly): 60 new bill apps in 2025–2026 in the top-50 results, none past 100 ratings. Being a competent entrant has not been sufficient for any of them.
- Price ceiling: strong free expectation in search suggestions and reviews.

Is the incumbent's audience reachable? Partly. For: Apple suggests "bill tracking apps similar to bills organizer &", and reviewers say they are leaving ("Looking for something else better", 1★, 2026-07-02). Against: the incumbent still ranks first on six of eight terms, so generic searches lead back to it; 59% of its recent reviews are five-star, so most of its users are inconvenienced rather than stranded; the "similar to" query returns Bill Tracker Pro, Space-O, Chronicle, Buddy and Bills Manager; one web search found only store pages, no forum threads about replacing it.

Is the gap about to close? No sign of an incumbent fix: last release 2024-04-10, developer site's last news post April 2024 and footer "2018 – 2024", no developer replies on the product page, reviewers report unanswered email. It cannot be ruled out, and a single compatibility release would remove the opening. Among rivals, Chronicle and Bills Manager both shipped within eight weeks; Bill Tracker Pro is moving upmarket and antagonizing simple-tracker users. Funding was not checked.

## 7. Reach

- App Store search: title and subtitle on "bill organizer", "bill reminder", "bill tracker"; the incumbent's own name as a keyword.
- Apple Search Ads on the incumbent's brand term and the "similar to" query (cost per tap unverified).
- Web comparison pages aimed at "alternative to" and "after Prism" queries; a competitor (Finny) already publishes these.
- Communities where manual tracking is the stated preference: personal-finance, budgeting, ADHD and caregiver forums. Reviewers self-describe as "a scatterbrain", "a senior citizen and also a caregiver", and recovering from a stroke. Receptiveness of specific communities was not tested.
- App Store editorial: a "Master Your Bills" story exists (contents not fetched).

## 8. Gaps

- No keyword popularity or difficulty: astro unavailable, appstore MCP scores unstable.
- No download or revenue figures for any bill app; every revenue number rests on an assumed 2% ratings-per-download ratio.
- iTunes Search API order stands in for in-app search ranking.
- Launch failure not reproduced on a device; breadth is inferred from reviews.
- Incumbent's backup format and importability not examined.
- Chronicle Pro's billing period and rivals' free-tier limits not confirmed in-app.
- Wallet Recurring coverage rests on one article.
- Incumbent review page 1 came from a same-day cache.
- Android demand not established (Play page did not load).
- Renewal retention for small annual plans not pulled.

## Sources

- iTunes Search API: https://itunes.apple.com/search?term=bill+reminder&country=us&entity=software
- iTunes Lookup API: https://itunes.apple.com/lookup?id=1352782733&country=us
- Reviews RSS: https://itunes.apple.com/us/rss/customerreviews/page=1/id=1352782733/sortby=mostrecent/json (also ids 834370671, 1059461492, 572561420, 514301848)
- Search suggestions: https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=bill
- Product pages: https://apps.apple.com/us/app/id1352782733 (incumbent); same pattern for ids 834370671, 1059461492, 572561420, 514301848, 468993411, 6447707197, 6737248419, 1561575664
- KDV Solutions news: https://kdvsolutions.com/news/
- iOS 27 Reminders: https://9to5mac.com/2026/09/29/heres-everything-new-for-reminders-in-ios-27/
- iOS 27 Wallet Recurring: https://www.theapplepost.com/2026/09/16/71418/how-to-see-recurring-apple-card-charges-in-ios-27/
- Prism shutdown (competitor blog): https://getfinny.app/blog/best-bill-tracker-apps-2026
- Calibration: /Users/dwsjoquist/ivygulch/vault/Research/Trends/Indie iOS Market Calibration 2026.md
- Prior phases: p1-stale.md, p2-a.md, p1-revenue.md in the same scratchpad folder; raw pulls in the p3bills subfolder

## Relevant To

- [[Bill Organizer]] — the seed idea this landscape supports
- [[Indie App Opportunity Scan — 2026-10-02]] — scorecard and ranking across the five finalists
- [[Indie iOS Market Calibration 2026]] — conversion and renewal figures used in the revenue estimates
