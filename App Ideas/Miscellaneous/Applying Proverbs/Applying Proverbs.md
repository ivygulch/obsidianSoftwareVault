---
area: Miscellaneous
status: seed
tags: [app-idea, proverbs, bible, wisdom, reference]
created: 2026-10-03
updated: 2026-10-03
---

# Applying Proverbs

**One-liner:** Find the proverbs that speak to a situation you are in, and keep them attached to the situations, people, and projects in your life.
**Target user:** Someone who reads Proverbs devotionally or practically and wants to reach the right passage at the moment a situation calls for it, not only in chapter order.
**Problem:** The 915 verses of Proverbs are arranged by collection, not by subject. Existing apps serve a daily verse or the chapter of the day; none that was found lets a person search by situation, build their own tagging and links between passages, or keep context groupings for ongoing situations.
**Differentiator:** A full categorization of the book by several category types at once (situations, attitudes, characteristics of a person, results), user tags, wiki-style links between passages, and user-defined context groups. An optional AI tier takes a described situation and returns candidate passages drawn from the categorized text.

## The Three Questions

**Who pays, how often, how much?**
The core app is free. The working idea for revenue is a low-cost subscription for the AI situation-matching feature. Who pays, at what price, and whether a one-time tier belongs beside it are open. (Context from the vault's [[Indie iOS Market Calibration 2026]]: scripture and devotional companions do earn for solo developers at the $1–6K-a-month level, and the 2026 scan's chart agent found a Reference paid chart populated by individual sellers of scripture-memory and devotional apps.)

**Year-2 maintenance cost:**
Depends on three decisions still open: which Bible text (licensed text may carry renewal terms and attribution upkeep), whether the AI tier calls a hosted model (per-call cost and a server or proxy to hold the key) or Apple's on-device Foundation Models (no cost, device floor), and whether the categorization is a fixed data set shipped with the app (no treadmill) or grows.

**Kill criteria:**
Not yet set. Candidates to decide on: the preferred text (ESV) cannot be licensed for a full offline Proverbs in a freemium app on acceptable terms, and no public-domain or open text reads well enough; or a categorization pass over the whole book produces groupings too thin to make situation search useful; or the AI tier adds nothing a free chat assistant does not already do when handed a situation.

## Concept

Three layers.

1. **The text.** All of Proverbs, offline, in one version. Text version and licensing are the first dependency; see [[Bible Text Licensing & APIs]].
2. **The structure.** Every passage (verse or short unit, since many proverbs span two or more verses) carries categories of several types, keywords, and links to related passages. Users add their own tags and links. Navigation is wiki-like: from any passage to its categories, from any category to its passages, and across links. Draft scheme in [[Categorization Scheme]].
3. **The person's context.** User-created context groups for an ongoing situation, a person they deal with, or a project, holding the passages and notes that belong to it. Delivery surfaces: flash cards, scheduled or random daily reminders, quick entry from the keyboard or microphone through App Intents, and the optional AI situation-matching tier.

The full set of raw ideas is in [[Idea Backlog]]; the sorting into a long-range plan and a V1 scope has not been done yet. The physical card deck that seeded part of the idea is described in [[Wisdom Deck Reference]].

## Prior Art

Store scan 2026-10-03, US storefront; n is the US rating count.

- **Proverb-A-Day: Bible Verses** (iDelata, free, n=514, 4.78, updated 2025-12) — a hand-picked daily verse with occasional commentary. Does the daily-delivery job; no search by situation, no tagging, no structure.
- **Proverbs & Psalms – King James** (Watchdis Group, free, n=1,101, 4.81, updated 2026-07) — the largest Proverbs-specific app found; a reader for two books in the public-domain KJV. Shows that a single-book app can reach four-figure ratings. Reading only.
- **Proverbs++** (Luke Thomas, free, n=3, 2025) and **EverydAI Proverbs** (Kosmaum, free, n=0, 2025) — new solo entrants: chapter-of-the-day reading habit, and read/listen/reflect with daily artwork. Neither offers categorization or context groups.
- **Bible (YouVersion)**, **Bible Gateway** — general Bible apps with topical verse lists and plans; the situation-to-passage job is served generically, across the whole Bible, without the user's own structure.
- **The Wisdom Deck** (Mark Matlock, 2008, physical cards) — one verse per card, with the traits of a wise person it exhibits marked on the back. The closest thing found to the "characteristics" category type; see [[Wisdom Deck Reference]].

The fuller scan in [[Proverbs & Situational Scripture Apps — Landscape]] (2026-10-03) adds: **Bible Topics and Quiz** (solo, 1 US rating, $0.99 Pro) is the nearest feature analog with topic links, per-verse journals, reminders, and spaced repetition over the whole Bible; the situation-to-verse job at scale is AI Bible chat (**Bible Chat** 364K ratings, **Haven** 149K, **Creed** 68K) at $2.99–$6.99 a week, with price-driven one-star streams; five more Proverbs-only solo apps shipped in 2025–2026, none above 14 ratings. Not found anywhere: multi-axis categorization of Proverbs, user tags or links on Proverbs passages, context groups for ongoing situations, App Intents capture, or a Proverbs-scoped AI matcher backed by a curated index. Public categorization schemes are all single-axis topic lists.

## Why It Could Work

- The book is small and fixed: 31 chapters, about 915 verses. A complete, high-quality categorization is a bounded one-time effort, not a content treadmill.
- Proverbs is the one book of the Bible people already read by the day of the month, so a daily habit exists to attach to.
- Scripture apps from individual sellers do chart and earn (see the 2026 indie scan's Reference-chart cluster: Fighter Verses $4.99 with 2,120 ratings, Universalis $9.99 with 9,561, e-Sword LT $3.99 with 7,055).
- The user-structure layer (tags, links, context groups) is personal data that a general Bible app or a chat assistant does not keep.

## Why It Might Not

- Text licensing may rule out the ESV for a full book in a freemium app, and the public-domain alternatives read differently.
- A general AI assistant already answers "which proverb applies to my situation" for free; the AI tier must be better than that by using the categorization, or it is a thin wrapper.
- Single-book apps are small: the largest found has 1,101 ratings after eight years.
- The categorization quality is the product, and it has to be done by a person who knows the book well.

## Open Questions

- Which text version, under what license, and does the license allow sending verses to an AI model? License-free candidates compared in [[Text Version Comparison]].
- Unit of categorization: verse, or sayings that span verses, or both?
- Fixed categories with user tags, or a single open tagging system with curated starter tags?
- On-device model or hosted model for the AI tier, and what does the tier add beyond a chat assistant?
- Which of the backlog items belong in V1?

## Related

- [[Idea Backlog]] — every idea so far, grouped
- [[Categorization Scheme]] — draft category types and starter taxonomy
- [[Wisdom Deck Reference]] — the physical deck
- [[Bible Text Licensing & APIs]] — version licensing research: no major copyrighted translation allows a complete book without a negotiated license; BSB (CC0), WEB, and KJV can ship whole
- [[Proverbs & Situational Scripture Apps — Landscape]] — competitor scan
- [[Text Version Comparison]] — KJV beside BSB on four passages, and an assessment of modernizing the KJV by rule
- [[Public-Domain Proverbs Commentaries]] — which commentaries are usable as-is (Henry, Clarke, JFB, Keil & Delitzsch, Wesley, TSK via SWORD modules), which need cleanup, and which are off the table
- [[Indie App Opportunity Scan — 2026-10-02]] — the scan whose Reference-chart findings are cited above
