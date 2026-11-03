---
type: design-doc
project: Proverbs
status: snapshot
created: 2026-11-02
updated: 2026-11-03
---

# Get Wisdom — Design Document

Snapshot of everything decided and still open about the Get Wisdom app as of 2026-11-02, assembled from the Proverbs project notes. Written to stand alone so it can be pasted into a chat and used as the basis for exploring design alternatives. The sections are marked **Decided** or **Open** so the exploration space is clear. The source of truth for intent remains the Ideal State Artifact in the vault; this document summarizes it and does not replace it.

## 1. The product in one paragraph

Get Wisdom (working title, from Proverbs 4:7; vault project name Proverbs) is an iPhone and iPad app that lets a person find what the book of Proverbs says about what is happening in their life by following the book's structure instead of reading it in chapter order. The whole book is categorized on several axes at once, passages are linked to each other with weighted links, and the user navigates from a cloud of tags to passages to related passages, keeping the path as a backtrackable tree. The user adds their own tags, notes, overrides, and context groups on top of the curated layer. The primary use case is a user with a particular scenario in mind, usually a combination of several tags, looking for guided counsel from the book on it; the tags act as a precomputed search index. The curated categorization is the product. The app never interprets, paraphrases, or generates scripture.

## 2. Who it is for

Someone who reads Proverbs devotionally or practically and wants to reach the right passage at the moment a situation calls for it. The first user the curated layer has to satisfy is Doug, in his own situations. Elevator version: "Proverbs linked up like a wiki: you start from whatever you are dealing with, follow the threads, and keep the trail."

## 3. The user experience (Ideal State, condensed)

**Primary use case (Decided 2026-11-02, recorded in the ISA as a Decision and ISC-44).** The user has a particular scenario in mind. That scenario is usually a combination of several tags, not one: a situation, an attitude, a role, a domain at once. The tags are a precomputed search index over the book, and the user is looking for guided counsel from Proverbs on that scenario. The cloud, the links, and the trail are the means; the outcome the user wants is the set of passages that speak to the scenario they came in with. Passages carrying every chosen tag come before passages carrying only some (ISC-44); ordering within those bands is open. Composing a query from several tags is the entry the app has to make easy. When a tag is selected, the app suggests related tags that may be pertinent, drawn from the curated index (tags sharing passages with it or linked to it), so the scenario can be widened or sharpened without hunting through the cloud. Suggestions are a setting the user can switch off; on by default (Decided 2026-11-02, ISC-45 and ISC-46).

**Finding.** The app opens to a cloud of tags: a word map of the categories and keywords the book has been given. The user picks the one closest to what they are dealing with and sees its passages. From any passage, links lead outward to other passages and other tags. Links are weighted so the ones that belong together in sense stand out from the ones that merely share a word. The user follows one, then another. The path is kept as a tree the user can see and move back along, so a detour is never lost: return to a fork and take the other branch.

**The passage is the focus.** A selected passage is shown in full, in the text's own words with its reference, with its connections arranged around it. Nothing on screen is written by the app. The words are the text, the tags, and the user's own notes. The app finds and arranges; it never interprets. Application notes and public-domain commentaries belong to a later layer, one deliberate step below the passage, never in the finding path.

**Clouds are the one document type.** The default cloud is the whole book. A named session is a cloud. A curated group is a cloud. A context group is a cloud. They differ in where they came from, not in what they are, and they all open in the same cloud view.

**Sessions and trails.** Every meander is kept automatically with its date and time. Returning within a short threshold resumes silently; between two thresholds the app asks whether to resume; beyond both, a new session starts at the default cloud and the old one stays findable. Naming a session keeps it as a trail that can be reopened and attached to a context group. Unnamed sessions appear in a list by date and time, each row showing the tags and passages it touched, and from there one can be named or attached. Unnamed sessions expire after a configurable age; named ones never do.

**Two kinds of groups, kept distinct.** Curated groups ship with the book, built by Doug across the whole book before launch. Context groups are the user's: a person, an ongoing situation, a project, holding the passages, notes, and trails that belong to it. A context group may reference a curated group but the two kinds never merge.

**The user's own marks.** The user tags passages with their own tags; writes notes on passages, on trails, and on the predefined tags themselves; and can override the curated tagging of a specific passage by removing a tag or adding a different predefined tag. A filter switches overrides off to see the book as shipped. All of it syncs across the user's iPhones and iPads through iCloud, and the app works in full when iCloud is unavailable. The entire finding experience works with no network.

**A second door.** The user can type or speak what is going on and the app suggests existing tags to start from. This runs on device, never writes a sentence back, and is a later feature than the cloud itself.

**Curated updates.** When the curated layer is revised, the new groups and tags take precedence; superseded groups are archived and reachable from a setting, never deleted. The user's tags, notes, and overrides survive untouched; an override on a tag that no longer exists simply stops applying.

**First run and reminders.** A short onboarding sequence walks through picking a tag and following a trail; every screen has a skip box and a setting resets the sequence. No notifications by default. A tag or a cloud can be asked to remind the user on a schedule; each notification carries a passage's verbatim text, and tapping it opens that passage inside that tag's or cloud's map.

**A year on.** The user has a handful of named trails and context groups they return to, a cloud shaped by a year of their own tags and notes, and the habit of reaching for the app when something is happening rather than searching the web. Clouds and notes can be shared with another person, who receives a copy they own, not a live link back.

## 4. Vocabulary

| Term | Meaning |
|---|---|
| Passage | The unit of categorization: a contiguous span of text, one verse or several, which may begin or end mid-verse. A verse belongs to one passage, except a split verse, which belongs to exactly two adjacent passages |
| Tag | A curated label on a passage. Tags have types (the category axes below). Users also make their own tags, in a flat per-user space |
| Category | A curated tag type and its values; "category" and "tag" are used loosely for the same curated vocabulary |
| Keyword | A free term per passage drawn from its own words or its sense; drives search and automatic links; not a category |
| Suggested tag | A related tag offered when a tag is selected, derived from the curated index; a setting switches suggestions off |
| Link | A weighted connection from a passage to another passage or to a tag; every passage has at least one, so no passage is a dead end |
| Cloud | The one document type: a set of tags and passages shown as a map. Default cloud, named session, curated group, and context group are all clouds |
| Session | One meander, kept automatically as a tree of navigation steps with date and time |
| Trail | A named session; persists and can be attached to a context group |
| Curated group | A shipped, read-only cloud built before launch |
| Context group | A user-made, user-named cloud for something ongoing in their life |
| Override | A user's removal of a curated tag from a passage, or addition of a different predefined tag to it; never alters curated data |
| Note | User text attached to a passage, a trail, or a predefined tag |
| Version-specific tag | A tag bound to one translation because translations and underlying texts differ; never shown against another version |

## 5. Constraints (Decided)

- No AI paraphrasing of the text, ever.
- No biblical text that is not in the shipped text. Nothing generated, nothing hallucinated.
- The app never interprets. Application notes and commentaries sit below the passage, never in the finding path.
- The finding experience works fully offline.
- Curated groups and the user's context groups are distinct kinds and never merge.
- User overrides of curated tagging never alter the curated data; they can always be switched off by a filter.
- Notifications exist only where the user asked for them on a tag or cloud. None by default.
- No book beyond Proverbs until the Proverbs cloud has shown what works for users.
- Suggesting tags from a described situation happens on device and never produces prose.
- Superseded curated groups are archived, never deleted.
- A curated update never alters or removes the user's tags, notes, or overrides.
- Sharing hands over a copy; nothing shared stays linked to the sender.
- A tag that depends on a translation is bound to that version and never shown against another.

## 6. The curated layer

### Unit of categorization (Decided 2026-10-26)

The passage, as defined above. Proverbs mixes one-verse sayings (most of chapters 10 to 29), multi-verse and numerical sayings (chapters 30 to 31, parts of 22 to 24), and extended discourses (chapters 1 to 9). Some verses are split awkwardly between sayings, so a passage may begin or end mid-verse.

### Category axes (Draft, Open)

Each axis is separate; a passage can carry values from several at once.

| Axis | What it answers | Example values |
|---|---|---|
| Situation | What is happening to or around the person | conflict with a neighbor, being wronged, a decision under pressure, lending money, correcting a child, being flattered, prosperity, poverty, grief |
| Attitude | The inner stance the passage addresses | anger, pride, humility, envy, fear, contentment, impatience, greed, gratitude |
| Characteristic | The trait of a wise or foolish person the passage describes | the Wisdom Deck's seven (trusts in God, exercises self-control, walks in healthy relationships, keeps balance, seeks good counsel, manages resources, speaks carefully), their opposites, and others such as diligence, laziness, honesty, discretion, teachability |
| Result | The outcome promised or warned of | ruin, honor, poverty, long life, shame, peace, favor, strife, security |
| Domain | The area of life | speech, money and work, family, friendship, leadership and rulers, justice, the fear of the Lord, learning and instruction, food and drink, the body |
| Role | Who the passage is about or addressed to | son, parent, king, friend, neighbor, servant, wife, the poor, the rich, the scoffer, the sluggard |
| Form (builder only) | How the saying works | antithetical pair, better-than saying, numerical saying, instruction, warning, observation. Decided 2026-11-03: a passage attribute in the builder, never a user-facing tag |

Open on the axes: whether Domain and Situation are one axis or two; whether Characteristic keeps the deck's seven as a fixed top level. Settled 2026-11-03: Form is not a user-facing axis; six axes reach the cloud.

### Links

- Automatic: passages sharing a category value, keyword, or tag.
- Editorial: hand-made links where two passages belong together regardless of vocabulary (26:4 and 26:5; repeated sayings such as 14:12 and 16:25). The repeated and near-repeated sayings are the first set of editorial links.
- User: any passage to any passage, with an optional note.

Every link carries a weight and links on a passage are presented in descending weight order. **How the weight is decided is not settled** (Open).

### Text versions

- Start with a freely available version: Berean Standard Bible (CC0) first; KJV, WEB, ASV are the other versions whose license permits a complete book offline without negotiation (Decided 2026-10-26, reversing an earlier ESV-first preference).
- ESV and other commercial translations are investigated only once a working prototype exists. Crossway's actual terms for a complete book in a freemium app are unknown.
- Which version the first App Store release ships is undecided (Open).
- The BSB keeps much of the KJV's cadence, so its register is closer to the ESV than a colloquial translation. A rule-based modernization of the KJV was assessed and judged to need an editorial read-through, not just a mechanical pass.
- Builder input format is USFM, the one format all four free texts ship in. The importer handles the marker subset Proverbs uses (chapter, verse, poetry lines q1/q2, blank, headings, parallel refs, list lines, paragraph, footnotes), records line breaks as structure on the verse, and lifts footnotes into their own table.
- A later possibility: a separate prebuilt cloud whose tags come from the original Hebrew words and phrases rather than English categories.

### Starter sources for the categorization pass

The Wisdom Deck's seven traits for the Characteristic axis; standard topical outlines of Proverbs (study Bible subject indexes, Kidner, Waltke) as a coverage check, without reusing publisher editorial names verbatim; the book's repeated sayings as the first editorial links. Public-domain commentaries (Henry, Clarke, JFB, Keil & Delitzsch, Wesley, TSK) are available for the later commentary layer.

## 7. Data architecture (Decided 2026-10-26 unless noted)

Decided with Android as a desired option not long after iOS, and shared data between platforms as a later goal (which implies some account or non-Apple sync backend later; that is an ISA-level change not yet made).

### Curated layer: a plain SQLite file in the bundle

- One artifact, `curated.sqlite`, read-only, stamped with a schema version and a data version. Both platforms read SQLite natively, so the schema is identical on each side. FTS5 provides full-text search.
- Relational: passages in many tags, tags of several types, weighted links, curated groups holding passages, version-specific tags with a version column.
- Produced by the export command-line tool from the builder's database (section 9). The curated file contains accepted items only.
- A curated update ships a new file; user rows are migrated against the new curated version.

### User layer: rows, not documents

The ISA's "clouds are the documents of the app" is the user's mental model, not the storage model. User data is rows in a plain SQLite schema the app owns.

- A graph: tags on passages, overrides per passage, notes on passages, trails, and tags; passages in many groups; trails attached to groups. Rows keep those relations queryable ("every note on this passage across all clouds").
- The weighted tag cloud, "which groups hold this passage," and session expiry are aggregate queries.
- Sync is per row with CloudKit records mapped to rows with timestamps. Sync metadata from day one: per-row UUID, modified timestamp, soft delete. Portable types only (UUID ids, ISO dates, no Apple-specific value types). The sync engine sits behind a dependency boundary so CloudKit can be replaced later.
- Exception: the session tree is a JSON column inside a sessions row, with denormalized columns for date and for the tags and passages touched. It is append-only, created on one device, and read whole.

### The cloud document is the export and import format

One JSON document per cloud, with stable UUIDs so re-import deduplicates, and a format version. It is at once the sharing payload, the backup format, and the migration path to Android. It is the one data contract that outlives the storage choice and is to be defined early.

## 8. App architecture (Decided 2026-10-26 to 2026-10-27)

| Item | Decision |
|---|---|
| Working mode | Spec driven: Claude writes the code to Doug's direction, with the ISA as spec and the ISCs as acceptance tests |
| Platforms | iPhone and iPad, both apps. iOS 27 minimum (device floor iPhone 11; on-device Foundation Models for situation-to-tags need iPhone 15 Pro or later, a higher floor for that feature only) |
| Architecture | TCA 2.0 (Point-Free's TCA26 beta, product `ComposableArchitecture`, traits `Dependencies`, `SwiftNavigation`, `Clocks`), in both the user app and the builder |
| Persistence | SQLiteData (Point-Free) for user data and for reading the bundled curated SQLite; its CloudKit sync engine is the v1 sync |
| Targets | Three: the user app (Get Wisdom), the data builder app (iPhone and iPad, TestFlight-only), and a macOS command-line export tool |
| Packages | Workspace with thin app shells and SPM packages. `GetWisdomData`: curated schema, curated-data model, loader, USFM importer, export logic; consumed by all three targets. `GetWisdomKit`: features, TCA; user app only. Builder features in their own package or the builder shell, decided at scaffold |
| Other dependencies | supabase-swift in the builder and export tool only, never in the user app. Nothing else until needed |
| Repo and IDs | `/d/ivgp/Proverbs`; workspace and project named GetWisdom; bundle IDs `com.ivygulch.GetWisdom` and `com.ivygulch.GetWisdom.DataBuilder`; team Ivy Gulch LLC |
| Testing | Swift Testing; ISC-named tests, one test target per package with ISC tests in their own suite (to confirm) |
| Design system | One: Liquid Glass, since iOS 27 is the floor |

## 9. The data builder (Decided 2026-10-27)

Tagging happens in the builder, not in files. The builder's store is the source of truth for tags, categories, links, groups, and split-verse passage boundaries; any file form is an export. The builder is therefore on the critical path before any categorization can begin, including the planned two-chapter scheme test.

- **Platform:** iPhone and iPad app, distributed privately by TestFlight to vetted people who help build and validate the data. Not an App Store product.
- **Store:** Supabase Postgres, because tagging is collaborative and needs server-side queries (disagreements, unresolved items, export) that CloudKit sharing cannot run. Durability by scheduled `pg_dump` committed to the repo. Offline tagging not supported at first (PowerSync is the answer if needed).
- **Roles:** `admin` (everything: text import, export, account management: invite, role change, deactivate), `editor` (accept, reject, resolve threads, edit any tag or application, comment; no import, export, or accounts), `tagger` (propose tags and applications, edit or withdraw own proposals, comment). Row-level security follows the roles.
- **Schema is a working record:** accounts with roles; tags and tag applications to passages, each with provenance (who, when) and status (proposed, accepted, rejected); comments on tags and on tag applications; resolution status on both comment threads; whatever else building the data needs.
- **Sign-in:** Sign in with Apple is the leading candidate; email one-time code is the fallback. Pick at setup.
- **Export tool:** reads Supabase and writes `curated.sqlite` through export logic in `GetWisdomData` so it is testable without a network. The data-level ISC tests run against the produced file before the user app sees it.

Open: the builder's authoring surface for tags, links, groups, passage boundaries, comments, and resolution; the review flow between taggers and editors; Supabase tier and dump schedule. The Builder has its own Ideal State Artifact, still at the drafting stage with no criteria yet.

## 10. Decisions log

- 2026-11-03 — Form is not a user-facing axis; it stays in the builder as a passage attribute and is never emitted as a tag. Six axes reach the cloud.
- 2026-11-02 — Selecting a tag suggests related tags from the curated index; a setting switches suggestions off; default on. ISC-45 and ISC-46 added.
- 2026-11-02 — Primary use case restated: a scenario is usually several tags across axes; the tags are a precomputed search index; the user wants counsel from the book on that scenario. ISC-44 added (full matches before partial matches).
- 2026-10-27 — Builder is an iPhone and iPad app on TCA 2.0 (superseding macOS-only); Supabase Postgres store; three roles; USFM confirmed as the import format; import is admin-only; supabase-swift never in the user app.
- 2026-10-26 — Working title Get Wisdom; repo, bundle IDs, iOS 27 minimum, TCA26 and SQLiteData; curated SQLite bundle plus row-based user layer; cloud JSON as export format.
- 2026-10-26 — Some tags are version-specific; added to Constraints.
- 2026-10-26 — Text order reversed: free version first, ESV investigated only after a working prototype.
- 2026-10-26 — Context group defined (a user-made, user-named cloud for something ongoing; may reference a curated group).
- 2026-10-26 — Session boundaries set by two configurable return thresholds (silent resume, ask, new session).
- 2026-10-26 — Unit of categorization is the passage, which may begin or end mid-verse.
- 2026-10-26 — Promoted from idea to project; the initial use case is following tags through the book's structure with the path kept as a backtrackable tree, rather than free-text situation search.

## 11. Open questions and undecided areas

These are the places where design alternatives are wanted.

### Interaction and UI (nothing chosen)

- **Composing a scenario from several tags.** The primary use case is a scenario that spans tags on different axes. How the user builds that combination (pick several in the cloud, narrow by axis, start from one and add others) and how the result is ranked (intersection first, then weighted by link strength, then the rest) are undecided. ISC-44 fixes only that full matches precede partial matches; ISC-11 remains the single-tag case.
- **Related-tag suggestions.** How relatedness is computed (shared passages, curated tag links, co-occurrence weighted by link strength) and how suggestions are presented beside the selected tag are undecided. ISC-45 fixes only that suggestions are existing tags from the index, exclude what is already selected, and are ordered by relatedness.
- **The cloud view.** The ISA says "a cloud of tags, a word map." How that renders on a phone and an iPad is undecided: weighted word cloud, clustered map by axis, list with weights, something else. The cloud must contain every curated tag and category (ISC-10), so density is a real problem.
- **The passage view.** Passage in full with its connections arranged around it. A speech-bubble arrangement is one option; nothing is decided. Must show all links to passages and tags, ordered by weight.
- **The tree view.** The session path is a true tree (a revisit makes a new node; no cycles or shared nodes). It must be viewable with elision when too long, every node reachable by tap. What to do when a tree grows very large is open.
- **Moving between the three.** Cloud, passage, tree: how the user moves among them, and whether the tree is a persistent surface or a pulled-up panel.
- **Visual register.** No direction chosen. Reference points from research: typographic and spare (stoic., Stoa), dark devotional (Dwell, Lectio 365), card-based (the Wisdom Deck's dark card with one verse in large type and seven trait icons on the back). Large type and respect for the system font size setting are recurring reviewer demands in this category.
- **Onboarding content.** A short skippable sequence; the specific screens are not designed.
- **Reminders.** Set on a tag or a cloud with a schedule; which passage is chosen for each notification is not specified.
- **Delivery surfaces beyond the app.** Flash-card presentation, home-screen widget, lock screen and StandBy, Watch, App Intents capture by keyboard or microphone, and a chapter-of-the-day habit hook are all in the backlog, none scoped.

### Content and data

- **Link weighting.** Weights exist and order links; how they are computed (shared axis values, keyword overlap, editorial weight, some combination) is unsettled.
- **Axis questions.** Domain versus Situation as one or two axes; whether Characteristic keeps a fixed top seven. (Form settled 2026-11-03: builder-only.) Whether a user can hide or rename app categories.
- **Fixed versus growing.** Whether the categorization ships as fixed data or grows over releases (the update path is designed either way).
- **Which version ships first,** and whether to ship two with a switch.
- **Whether the BSB's footnotes and cross-references** are under the same CC0 dedication as its text.

### Features marked later

- Situation-to-tags on device (ISC-32): approach not chosen (Foundation Models, embeddings over tag names and keywords, keyword matching).
- Curated update migration (ISC-33, 34).
- Commentary and application-note layer below the passage (ISC-40).
- Hebrew-word cloud. Other books as additional clouds, only after Proverbs has proven itself.
- Android, with shared user data, which implies an account or sync backend decision not yet made.

### Business

- Core app free; the working idea for revenue was a low-cost subscription for AI situation matching, but the ISA has since moved that feature on device with no prose output, so the paid line is open again. An earlier V1 proposal put unlimited context groups, flash-card review, and the AI matcher behind a one-time or annual purchase; not adopted.
- Year-two upkeep depends on text licensing, whether any hosted model is used, and whether the categorization grows.
- Kill criteria from the exploration plan, not yet formally adopted: fewer than 12 of 20 test situations find a satisfying passage; under 70 percent agreement on re-categorization; the whole-book pass projects to more than about 80 hours with no second reader.

## 12. Criteria summary

The ISA holds 46 Ideal State Criteria, all open, each with a named test. Grouped:

- **Data integrity (ISC-1 to 8, 41 to 43):** complete text (31 chapters, 915 verses); verbatim rendering; only Proverbs ships; passages cover the book with explicit split markers; every passage tagged; no dead ends; links weighted and ordered; curated groups read-only; version-specific tags hidden for other versions and never orphaned; development text freely licensed.
- **Finding (ISC-9 to 13, 44):** opens to the default cloud; default cloud is complete; a tag lists exactly its passages with overrides applied; a scenario of several tags lists full matches before partial matches, each row showing which chosen tags it carries; selecting a tag suggests related tags from the index, switchable off in settings (ISC-45, 46); passage view shows reference and full text; passage view exposes all links.
- **Sessions and trails (ISC-14 to 20, 23):** path is a tree; tree visible with elision; every step persists at once; return thresholds; naming makes a trail; trail attaches to a group; old sessions findable; unnamed sessions expire.
- **Clouds and groups (ISC-21, 22):** one document type; group kinds never merge.
- **User marks (ISC-24 to 28):** own tags; notes in three places; override removes and adds; curated data byte-identical after overrides; override filter.
- **Sync and offline (ISC-29 to 31):** follows across devices; full function without iCloud; fully offline.
- **Later (ISC-32 to 34, 40):** situation to tags on device; curated update precedence; user marks survive update; interpretation sits below.
- **Onboarding, reminders, sharing, purity (ISC-35 to 39):** first-run sequence with skip and reset; reminders opt-in; reminder carries a verbatim passage and opens it in context; sharing yields an independent copy; nothing app-written on screen.

## 13. Market context

Store scan 2026-10-03, US storefront. The largest Proverbs-specific app found is a KJV reader of Proverbs and Psalms with about 1,100 ratings after eight years; daily-verse apps and five new solo Proverbs apps from 2025 to 2026 sit well below that. General Bible apps (YouVersion, Bible Gateway) serve topical lists across the whole Bible without the user's own structure. AI Bible chat apps (Bible Chat, Haven, Creed) serve situation-to-verse at scale for $2.99 to $6.99 a week with price-driven one-star streams. Not found anywhere: multi-axis categorization of Proverbs, user tags or links on Proverbs passages, context groups for ongoing situations, or a Proverbs-scoped matcher backed by a curated index. Public categorization schemes are all single-axis topic lists. Of 17 Proverbs app listings reviewed, none describes the finding-by-structure experience. A UX survey of 33 apps found no phone app that lets a user link two passages of a fixed corpus, and no scripture app that draws a passage for a described situation.

## 14. Reference apps

Existing iOS apps worth studying, grouped by the design problem each informs. Store listings checked 2026-11-02 unless marked.

### Composing a scenario from several tags (the primary use case)

- **Apple Photos search**: type a term, results narrow, add another term, results narrow again; each term shows as a chip and can be removed. The clearest phone pattern for building a query one tag at a time from a precomputed index.
- **Bear**: tap several tags to intersect them; the note list updates live. Tag intersection as navigation rather than as a filter sheet.
- **Apple Reminders smart lists**: combine tags with "any" or "all", plus other facets, saved as a list. The any-versus-all choice is the ranking question in miniature.
- **Mela** and **Paprika** (recipe managers): multi-select filters across separate facets (category, cuisine, time, ingredient), with the match count updating as each is added. Separate facets map to separate axes.
- **Airbnb** and **Yelp** filter sheets: narrow by several independent facets, see the result count before committing, clear one facet without clearing the rest.
- **WebMD Symptom Checker** and **Ada**: pick several structured inputs (body area, symptoms, attributes) and get a ranked list from a curated index, with the reasons each result matched visible. The closest analog to "structured scenario in, ranked counsel out, nothing generated."
- **Things**: multiple tags selected in a list header narrow the list with AND; a lightweight in-place composer rather than a modal.

### The single-axis competitors (what the index improves on)

- **YouVersion** "How are you feeling?" emoji row returning verses, **Bible Gateway** topical index, **Oaysis: Bible Verses By Topic**, **Bible Verses World**: one topic in, a verse list out, no combination, no structure the user owns.
- **Bible Topics and Quiz** (in the vault landscape scan): the nearest feature analog with topic links and per-verse journals over the whole Bible.

### Results list and the passage as focus

- **Terminology** (Agile Tortoise): a word at the top, tappable lists of related words grouped by relation type, with history. A fixed corpus, links grouped by kind, no prose from the app. Structural match for the passage screen.
- **Blue Letter Bible**: per-verse Treasury of Scripture Knowledge cross references under the verse; TSK is public domain and is a worked example of editorial links on this text.
- **Bible Hub** and **Literal Word: Bible & Lexicon**: verse-centred layered reference, cross references and lexicon one tap down. Literal Word is the cleaner and is a solo-developer app.
- **Berean Standard Bible** (EthnosDev): the BSB with its own footnotes and cross references rendered; shows the chosen text's apparatus.
- **Kindle X-Ray**: terms linked to every passage where they occur, reached inside the reading view.

### The cloud view

- **Mindly 2**: radial bubble map, one level at a time, tap to drill in. The closest phone-native "cloud you can drill into."
- **SimpleMind** and **Xmind**: mind maps with per-branch collapse, for density on a phone.
- **Apple Music onboarding bubble picker**: floating tap-to-grow bubbles as a first-run surface. In the app, not the listing.
- **Obsidian** graph view: the reference force-directed cloud and why it is hard on a phone.

### The session tree

- **Lichess** and **Chess.com** analysis board: a true move tree; going back to a fork and choosing differently creates a sibling branch; long variations collapse; every node tappable. The best existing phone UI for "return to a fork and take the other branch."
- **MindNode** and **Xmind**: per-branch collapse for the elision rules.
- **Safari**: long-press back button history and Tab Groups as the linear baseline the tree improves on.

### Sessions, trails, context groups

- **Apple Maps Guides**: publisher Guides beside the user's My Guides, same object type, one list, never merging. The curated-group versus context-group distinction in a shipping Apple UI.
- **Safari History** grouped by date, each row a page title: the shape of the unnamed-sessions list.
- **Day One** journals and **Craft** Collections: naming and attaching.
- **LiquidText** (iPad): excerpts pulled from a fixed document into a workspace with drawn connections; relevant to a side-by-side iPad layout.

### Reading-first typography and the no-prose register

- **Literal Word**: fast, spare, serif, nothing but scripture and references on screen.
- **ESV Bible** (Crossway): cross references and footnotes as inline markers opening a sheet, text otherwise untouched.
- **Reeder** and **Unread**: article typography and type-size control.
- **stoic.**, **Stoa**, **Dwell**: devotional register (in the vault UX note).

### Situation-to-tags entry (later feature)

- **Finch** quick check-in and **Apple Journal** state of mind: chip grids as structured output.
- **Apple Health** State of Mind: slider, descriptor chips, "biggest impact" chips, no free text required.

Not verified today: Muse (spatial canvas) did not appear in store search. WikiLinks (Wikipedia browser with a visited-page graph) is no longer in the US store.

## 15. Sources

Vault notes this document condenses: Ideal State (ISA, 43 ISCs), Design (scaffold and data decisions), Builder Ideal State, Applying Proverbs (originating idea), Categorization Scheme, Idea Backlog, Exploration Plan, Text Version Comparison, BSB Download Formats, UX Pattern Research, Wisdom Deck Reference, App Store Titles and Descriptions, Name Testing, Public-Domain Proverbs Commentaries, and the Proverbs & Situational Scripture Apps landscape scan.
