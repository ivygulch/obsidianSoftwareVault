---
area: Games Activities & Utilities
status: seed
tags: [app-idea, indie-scan, pool, spa, utilities]
created: 2026-10-02
updated: 2026-10-02
---

# Pool & Spa Chemistry Log

**One-liner:** Enter test readings, get exact doses for your own chemicals and water volume, and keep a history that never gets lost.
**Target user:** Residential pool and hot-tub owners who maintain their own water; one-truck service techs as a later second audience.
**Problem:** The independent calculators are failing their users. In the 100 most recent reviews, Pool Math has 38 at 1–2 stars and Pool-Calculator 65; the free vendor app from Clorox has 85. Complaints are specific: a paywall after one log, lost history, no bromine or spa ranges, targets that do not save, spas under 1,000 gallons refused, and doses that contradict themselves.
**Differentiator:** Unlimited log with iCloud sync and no account; chlorine, salt, and bromine modes; a real spa profile; saved targets; a pH and alkalinity model that is consistent; metric units and localization for France and Germany, where no independent calculator has more than 10 ratings.

## The Three Questions

**Who pays, how often, how much?**
A pool or spa owner, once at season opening or annually. Reviewers anchor at $5 once or $8 a year and object at $50 a year. The scan's mid case assumed $14.99, one-time or annual, and that price is untested. Estimated range, net: about $45 a month (low), $600–$1,400 (mid), about $3,200 (high). All estimates.

**Year-2 maintenance cost:**
About 40–80 hours a year (estimate): one pass per iOS release, chemical product list changes, and support mail about dose disagreements. No server, no content feed.

**Kill criteria:**
- TroubleFreePool ships a Pool Math release that fixes the logging paywall, lost history, and saved targets.
- One of the eleven entrants since April 2025 passes about 500 ratings before this ships.
- A prototype's pH and alkalinity doses cannot be made to agree with a trusted reference across the cases where incumbents disagree.
- The formula lineage or the "PoolMath" naming turns out to carry a licence restriction that blocks an independent implementation.

## Concept

A calculator and log for one or more bodies of water. Readings in, doses out for the owner's actual products and strengths, with the side effects of each addition shown. Saturation index (CSI or LSI, user's choice), charts, reminders, CSV export. Later: household sharing, widgets, Watch, weather input, a multi-pool tier with a customer report for service techs.

## Prior Art

- **Pool Math (TroubleFreePool)** — $7.99/yr, 287 iOS ratings at 3.63. Backed by the largest pool forum and a nonprofit that reported $269K revenue in 2025, mostly from this app. Gets the chemistry method right for its community; fails on logging paywall, saved targets, and non-chlorine methods.
- **Pool-Calculator** — $4.99, 630 ratings. The original web calculator's app; 65 of its recent 100 reviews are 1–2 stars and it is reported broken.
- **Pooli** — 370 ratings, healthy (83 of recent 100 are five-star). Ships a test-strip reference card and an assistant; one reviewer marked it down for the assistant changing a dose mid-conversation.
- **Clorox Pool, Leslie's, HTH** — free vendor apps with large rating counts, tied to their own chemicals; Clorox refuses volumes under 1,000 gallons.

## Why It Could Work

- The paying base is larger than iOS rating counts show: the rival's revenue implies 17,000–40,000 subscribers (estimate).
- The complaints are concrete and fixable, and three incumbents share them.
- Hot tubs are a year-round segment with no water-care app above one rating on the head term.
- France and Germany are open.

## Why It Might Not

- Eleven new independent apps since April 2025; two already sell at $9.99 in seven languages.
- The main community channel belongs to the rival, which is a nonprofit funded by its app.
- Use is seasonal: 83 of Pool Math's recent 100 reviews fall in May–September.
- A chat assistant does one-off dosing math for free.
- Dosing advice for acid and chlorine is safety-relevant.

## Open Questions

- What share of TroubleFreePool's revenue is Pool Math, and on which platform?
- Do r/pools and r/hottub allow an independent developer to post?
- Does current SwiftData support CloudKit shared zones for household sharing?
- How accurate can camera strip reading be without a reference card?

## Related

- [[Pool & Spa Water Chemistry Apps — Landscape]]
- [[Indie App Opportunity Scan — 2026-10-02]]
- [[Indie iOS Market Calibration 2026]]
