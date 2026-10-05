---
type: plan
status: proposed
tags: [proverbs, app-idea, plan, exploration]
created: 2026-10-04
updated: 2026-10-04
---

# Applying Proverbs — Exploration Plan

A plan for turning [[Applying Proverbs]] from a seed into a decision: a long-range vision and a V1 scope to commit to, or a reasoned shelving. Built on the research already filed in this folder and in [[Bible Text Licensing & APIs]], [[Proverbs & Situational Scripture Apps — Landscape]], and [[Indie iOS Market Calibration 2026]]. The plan is for one developer. Phases 1 and 2 can run at the same time; everything after Phase 2 depends on its result.

## The decision this plan serves

Two facts from the research frame everything. First, the competitor scan found nothing on either store that categorizes Proverbs on more than one axis, lets a user tag or link passages, or keeps context groups; the situation-to-verse job at scale belongs to AI chat apps selling weekly subscriptions whose one-star reviews are about price. Second, the licensing note found that the preferred ESV, and every other major copyrighted translation, needs a negotiated license for a complete book, while the Berean Standard Bible is CC0. So the open questions are not whether the product is possible but whether the categorization is good enough to be the product, whether an AI tier adds anything over a free chat assistant, and what the text path costs.

## Phase 1 — Text path (one to two weeks of elapsed time, a few hours of work)

**Goal:** know by the end of the exploration whether the ESV is available on acceptable terms, without letting that answer block anything else.

**Questions:** Will Crossway license a complete Proverbs to Ivy Gulch LLC for a free app with a paid AI tier, at what fee structure, with offline storage, and with text sent to a model at inference time? Is a licensed text worth more than the BSB to this app's users?

**Activities:**
- Submit Crossway's digital licensing form with a one-paragraph description: free app, complete Proverbs offline, optional subscription for an AI feature that sends a user's situation and candidate verses to a model, developer is an LLC. Ask the five questions above explicitly, including the AI clause, since Crossway publishes none.
- Optionally send the same inquiry to Lockman (NASB or LSB) as a second licensed candidate; its stated quotation ceiling is the most generous of the copyrighted versions.
- Build the BSB Proverbs data file now: fetch from berean.bible, verse-align, store as JSON keyed by chapter and verse, with the KJV alongside as a second version. Keep a log of the source and date.
- Read Proverbs 1, 10, and 31 in the BSB in one sitting and note any line that reads worse than the ESV. The [[Text Version Comparison]] sample is four passages; this is the fuller read.

**Produces:** a Text Decision section in the idea note; the BSB and KJV data files; the Crossway correspondence log.

**Ends the exploration early:** nothing in this phase does. The BSB exists, so the text path cannot kill the idea; it can only change its cost.

## Phase 2 — Scheme test on two chapters (two to three weeks)

**Goal:** prove or disprove that multi-axis categorization is both doable and useful before committing to 915 verses.

**Questions:** What is the unit (verse, saying, or both)? Do the seven axes in [[Categorization Scheme]] stay distinct when applied, or collapse into one topic list? Does the categorization find the right passages for real situations without any AI?

**Activities:**
- Categorize chapter 10 (32 two-line sayings) and chapter 3 (discourse) in full, on every axis in the draft scheme, in a spreadsheet or the Phase 3 schema. Record time per verse.
- Write 20 situations the way a user would describe them ("my brother keeps borrowing money and not paying it back," "I got praised for work I did not do," "I want to confront a coworker"). Ten should be answerable from these two chapters; ten should not, to test for false hits.
- Run the retrieval test by hand: for each situation, pick category values and see which passages come back. Score each: a satisfying passage in the top five, a weak one, or nothing.
- A week later, re-categorize ten verses without looking at the first pass and compare. If a second reader who knows the book is available, have them categorize the same ten blind.
- Count how many category values each axis produced and how many passages carry more than one axis.

**Produces:** scheme v1 with the unit decided; the two chapters as data; the 20-situation retrieval test with scores; a time estimate for the whole book.

**Ends the exploration early:** fewer than 12 of the 20 situations get a satisfying hit, or the axes beyond "topic" each end up with under five values, or re-categorization agreement on the ten verses is under about 70%. Any of those means the differentiator does not hold and the idea reduces to a topical reader, which the competitor scan shows already exists at small scale.

## Phase 3 — Data model and storage (one week, overlaps Phase 2)

**Goal:** a schema in which a later text-version change costs only the keyword layer, and in which user data and curated data never mix.

**Questions:** Bundled JSON or SQLite for the curated data? Fixed at release or able to grow? Where do user tags, links, notes, and context groups live?

**Activities:**
- Sketch the schema: `passage` (reference range, canonical order), `version_text` (version, reference, text), `category_type`, `category`, `passage_category`, `keyword` with `passage_keyword` carrying a version column, `link` (passage to passage, kind: automatic, editorial, user), `user_tag`, `user_note`, `context_group`, `context_group_passage`.
- Decide fixed versus growing: curated data ships in the bundle and changes only with app updates; user data lives in SwiftData with CloudKit sync. Growth, if any, is by app update, not by server.
- Choose storage. Bundled SQLite (SQLiteData is already in the vault's toolset) supports full-text search and category joins without loading everything; JSON is simpler if the whole book plus categories stays under a few megabytes, which it will.
- Load the Phase 2 chapters into the schema and run the 20 situations as queries.

**Produces:** a schema note and a working loader with the two chapters.

**Ends the exploration early:** no.

## Phase 4 — AI tier test (one week, after Phase 2)

**Goal:** find out cheaply whether retrieval over the curated index beats what a free chat assistant already does, before building a paid tier.

**Questions:** What does the tier do that ChatGPT or Claude does not when a user pastes a situation? On-device Foundation Models or a hosted model? Does the model ever cite a passage that is not in the index?

**Activities:**
- Take the 20 situations. Get answers three ways: a plain chat assistant asked "which proverbs apply"; an on-device Foundation Models session that classifies the situation into the scheme's category values, retrieves from the two-chapter index, and returns only indexed passages; the same pipeline with a hosted model.
- Score each answer on the same scale as Phase 2, plus hallucinated references and latency.
- Note the device floor for the on-device path (Apple Intelligence devices only) against the audience in the competitor reviews.

**Produces:** an AI Tier Test note with the three-way comparison.

**Ends the exploration early:** if the plain assistant matches the index-backed pipeline, the paid tier is a thin wrapper. That does not kill the app; it removes the working revenue model and sends the pricing phase to a one-time unlock instead.

## Phase 5 — Surfaces and the V1 cut (two to three weeks)

**Goal:** see the three core flows on a phone and decide what is V1.

**Activities:**
- SwiftUI prototype of: browse by category and search; passage detail with its categories, keywords, links, user tags, and notes; a context group holding passages and notes. Use the two categorized chapters.
- Add the second-tier surfaces only as far as a screen each: a flash-card review with per-card resurfacing controls (the Readwise pattern in [[UX Pattern Research]]); a daily reminder with the passage text in the notification and user-set hours; a home-screen widget.
- Decide the cut using the UX note's evidence. Candidates for later: App Intents capture (no sampled app parses voice into structure; Apple Journal is the entry-point model), the commentary layer (the SWORD-sourced works in [[Public-Domain Proverbs Commentaries]] are ready, but they are a reading feature, not a finding feature), Watch, StandBy, sharing of context groups.

**Produces:** a prototype and a V1 Scope note listing each surface as V1 or later with its reason.

**Ends the exploration early:** no.

## Phase 6 — Pricing and the free/paid line (a few hours, after Phase 4)

**Questions:** What is free, what is paid, and in what form?

**Activities:**
- Lay out three models against the calibration note: free core with an annual AI subscription; free core with a one-time unlock for context groups, flash cards, and commentary; both. The note's figures that bear on it: hard paywalls convert about five times better than freemium, annual plans renew at 83%, higher prices convert better than lower ones, and the competitor scan shows weekly pricing is the dominant complaint in this category.
- Set the free line so that the categorized book, browse, search, and one context group are free, since the core feature is free by position.
- Write the revenue arithmetic the way the opportunity scan did: an assumed install rate, a conversion from the calibration note, a price, net of the store fee, as low, mid, and high.

**Produces:** the "Who pays, how often, how much" answer in the idea note.

## Phase 7 — Decision gate

Fill the three questions in [[Applying Proverbs]] with the real answers from Phases 1 to 6, set the status to exploring or shelved, and write the Why Shelved paragraph if shelved. The idea note stays at seed until then; this plan does not itself justify the change.

## Kill criteria, as evidence collectable in these phases

- Phase 2 retrieval test: fewer than 12 of 20 situations get a satisfying passage.
- Phase 2 consistency: under 70% agreement on re-categorization, or the non-topic axes each hold under five values.
- Phase 2 time: the whole-book pass projects to more than about 80 hours and no second reader is available to check it.
- Phase 4: the index-backed pipeline is not better than a plain assistant, and no one-time unlock feature set survives Phase 5 as worth paying for.
- Phase 1: Crossway's terms are unacceptable and the BSB read test turns up lines that would embarrass the app. Both must be true; either alone is not a kill.

## Proposal: V1 candidate (for acceptance or editing)

**Text:** BSB, with KJV selectable; ESV added later only if Crossway's terms allow.
**Content:** all of Proverbs categorized on four axes (situation, attitude, characteristic, result) plus domain; keywords; editorial links for the repeated and paired sayings. Shipped as bundled data.
**Free:** browse by any axis, full-text search, passage detail with categories, keywords, and links; user tags and notes; one context group; a daily passage reminder with the text in the notification, planned or random, user-set hours; a home-screen widget.
**Paid, one-time or annual depending on Phase 6:** unlimited context groups; flash-card review with resurfacing controls; the AI situation matcher if Phase 4 earns it.
**Later:** App Intents and voice capture, commentary layer, Watch, StandBy, sharing a context group, ESV.
**Not in V1:** accounts, server, social features, other books.

## Proposal: long-range vision (for acceptance or editing)

A personal wisdom reference built on one fully categorized book, where the user's own structure (tags, links, context groups, notes) accumulates over years and stays on their devices. The categorization engine and user layer are book-independent, so Ecclesiastes, James, and the Sermon on the Mount could follow as bundled packs without changing the app. The AI tier, if it survives Phase 4, reads the user's context groups as background and answers only from the curated index, which is the one thing the AI chat apps cannot do. Commentary from the public-domain works in the survey sits one tap below each passage. Revenue is modest and recurring, and upkeep is an OS pass a year and occasional data corrections.

## Research still missing

| Gap | What it blocks |
|---|---|
| Crossway's actual terms for a complete book in a freemium app with an AI feature | The text decision; the "ESV" line in the long-range vision |
| Whether the BSB's footnotes and cross-references are under the same CC0 dedication as the text | Whether the BSB's own apparatus can ship |
| How many of the 915 verses belong to multi-verse sayings | The unit decision in Phase 2 |
| On-device Foundation Models availability by device, and App Review's current stance on AI features that produce scripture-adjacent advice | Phase 4's platform choice and the paid tier's risk |
| Which App Store category (Reference, Lifestyle, Education, Books) the Proverbs-specific apps sit in and chart in | Discoverability; the opportunity scan's keyword tooling was unusable, so this is still unmeasured |
| Whether pastors, youth leaders, and small-group leaders are a reachable channel, and what they would use a categorized Proverbs for | Reach beyond search |
| The Wisdom Deck's current rights holder and whether its seven marks' wording may be reused | Only if the Characteristic axis keeps the deck's phrasing verbatim; generic rewording avoids the question |

## Related

- [[Applying Proverbs]]
- [[Idea Backlog]]
- [[Categorization Scheme]]
- [[Text Version Comparison]]
- [[Public-Domain Proverbs Commentaries]]
- [[UX Pattern Research]]
- [[Bible Text Licensing & APIs]]
- [[Proverbs & Situational Scripture Apps — Landscape]]
- [[Indie iOS Market Calibration 2026]]
