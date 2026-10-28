---
status: active
created: 2026-10-26
updated: 2026-10-27
---

# Proverbs — Design

How the app is built. Intent lives in [[Projects/Proverbs/Ideal State|Ideal State]]; this page holds the implementation decisions and their dates.

## Working mode (2026-10-26)

Spec driven. Claude writes the code according to Doug's direction, with the ISA as the spec and the ISCs as the acceptance tests. Doug writes or edits code only when necessary. This differs from the default iOS working mode in other projects, where Doug builds and Claude assists.

## Scaffold decisions (2026-10-26)

| Question | Decision |
|---|---|
| Who drives | Claude implements, Doug directs |
| Product name | Working title **Get Wisdom** (Proverbs 4:7), chosen 2026-10-26; no exact match in the store as of that date; App Store Connect availability unconfirmed |
| Repo | `/d/ivgp/Proverbs` (`~/ivygulch/ios/projects/Proverbs`), decided 2026-10-26. Workspace and project name `GetWisdom` |
| Bundle IDs | User app `com.ivygulch.GetWisdom`, builder `com.ivygulch.GetWisdom.DataBuilder`. Confirmed 2026-10-26 |
| Architecture | TCA 2.0, in the user app and in the builder (builder confirmed 2026-10-27). The TCA26 access and version-alignment items below therefore sit on the builder's path |
| App targets | Two app targets plus one command-line target. The primary user app (Get Wisdom). The data builder app, an iPhone and iPad app (decided 2026-10-27, superseding the 2026-10-26 macOS-only decision) used to import text versions, define passages, and build the tags, links, and curated groups. The builder is distributed privately by TestFlight to vetted individuals who help build and validate the data; it is not a general-access app and not an App Store product. An export command-line tool (macOS) reads the builder's store and writes the bundled curated SQLite; see Data |
| Package layout | Workspace with thin app shells and SPM packages. `GetWisdomData` holds the curated schema, the curated-data model, the loader, the text importer, and the export logic, and is consumed by the user app, the builder, and the export tool. `GetWisdomKit` (features, TCA) is consumed by the user app only. Builder features live in their own package or in the builder shell; decide at scaffold time |
| Dependencies at scaffold time | Decided 2026-10-26. **TCA 2.0** from the TCA26 beta, `https://github.com/pointfreeco/TCA26` (Point-Free Max private beta). Product `ComposableArchitecture2`; the package also ships `Dependencies` and `SwiftNavigation`, so neither is a separate dependency. Package platforms: iOS 17, macOS 14. **SQLiteData** (`pointfreeco/sqlite-data`) for user data and for reading the bundled curated SQLite; its CloudKit sync engine is the v1 sync. **supabase-swift** (`supabase/supabase-swift`) in the builder and the export tool only, never in the user app (decided 2026-10-27). Nothing else until needed |
| Minimum iOS version | iOS 27, decided 2026-10-26. Device floor is the iPhone 11 (2019); iOS 27 kept iOS 26's device list. On-device Foundation Models (ISC-32) need iPhone 15 Pro or later, a higher floor for that feature only. Reasons: one code path, current Foundation Models and App Intents APIs, one design system (Liquid Glass), no install base to protect |
| Developer team | Ivy Gulch LLC |
| Deployment targets | iPhone and iPad, for both the user app and the builder |
| Testing | Swift Testing; ISC-named tests. Whether one test target per package and whether ISC tests sit in their own suite: "yes" given, read as one target per package with ISC tests in their own suite; confirm |

## Data (2026-10-26)

Decided with Android as a desired option not long after iOS, and with shared data between platforms as a later goal. Android with shared user data implies some kind of account or non-Apple sync backend later; that is an ISA-level change when it comes and is not decided here.

### Curated layer: a plain SQLite file in the bundle, produced by the data builder app

- One artifact, `curated.sqlite`, read-only in the bundle, stamped with a schema version and a data version. Both platforms read SQLite natively (iOS: SQLiteData or GRDB; Android: Room or SQLDelight), so the schema is identical on each side. FTS5 provides full-text search.
- The layer is relational: passages in many tags, tags of several types, weighted links, curated groups holding passages, and version-specific tags with a version column (ISC-41, 43). JSON would make each platform reimplement the indexing and turn cloud and link queries into scans.
- Inputs to the builder are the translation texts, one per version, in **USFM** (confirmed 2026-10-27). USFM is the one format all four free texts ship in; see [[BSB Download Formats]]. The importer lives in `GetWisdomData`, handles the marker subset Proverbs uses (chapter, verse, `q1`/`q2` poetry lines, blank, headings, parallel refs, list lines, paragraph, footnotes), carries the current verse across lines, records line breaks as structure on the verse, and lifts footnotes into their own table. Import is an admin process run from the builder app, available only to the admin role (decided 2026-10-27).
- Tagging happens in the builder (decided 2026-10-26). The builder's store is the source of truth for tags, categories, links, groups, and split-verse passage boundaries; any file form of that structure is an export, not the source. Consequence: the builder is on the critical path before the Phase 2 two-chapter test and any categorization can begin.
- The builder's store is a Supabase Postgres database (decided 2026-10-27), chosen because tagging is collaborative: several vetted people tag and validate, and the data needs server-side queries (disagreements, unresolved items, export) that CloudKit sharing cannot run. Durability: a scheduled `pg_dump` committed to the repo, since the free tier has no point-in-time recovery and pauses idle projects; tier to be chosen. Offline tagging is not supported at first; a local-first layer (PowerSync) is the answer if a tagger needs it.
- The builder's schema is a working record, not just the curated result. It holds: accounts with three roles (decided 2026-10-27): `admin` has everything, including text import, export, and account management (invite, role change, deactivate); `editor` accepts, rejects, resolves threads, edits any tag or application, and comments, but cannot import, export, or manage accounts; `tagger` proposes tags and applications, edits or withdraws its own proposals, and comments. Account management stays with admin because the role that grants roles is the root of trust. Row-level security follows the roles: every signed-in account reads everything, taggers write their own rows, editors write all content rows, admins write all rows including accounts and text versions; tags and tag applications to passages, each with provenance (who, when) and a status (proposed, accepted, rejected); comments on tags; comments on tag applications; a resolution status on both comment threads; and whatever else facilitates building the data as it comes up. The curated SQLite export contains accepted items only.
- The export command-line tool produces the curated SQLite file from Supabase, through export logic that lives in `GetWisdomData` so it is testable without a network. The data-level ISC tests (1 through 8, 41 through 43) run against the produced file before the user app sees it.
- A curated update ships a new file. ISC-33 and 34 become a migration of user rows against the new curated version.
- If Android arrives through Kotlin Multiplatform, SQLDelight can own this schema on both platforms.

### User layer: rows, not documents

The ISA's "clouds are the documents of the app" is the user's mental model, not the storage model. User data is stored as rows in a plain SQLite schema the app owns (tilts the store choice to SQLiteData over SwiftData; SwiftData's on-disk schema is private to Apple's framework).

- The data is a graph: tags on passages, overrides per passage, notes on passages, trails, and tags, passages in many groups, trails attached to groups. Rows keep those relations queryable ("every note on this passage across all clouds").
- The weighted tag cloud, "which groups hold this passage," and session expiry (ISC-23) are aggregate queries.
- Sync is per row. CloudKit records map to rows with timestamps; a later server does the same. Document sync means whole-document conflicts and last-writer-wins data loss between two devices.
- Curated updates (ISC-33, 34) and the override filter (ISC-28) are row-level operations.
- Portable types only: UUID ids, ISO dates, no Apple-specific value types. Sync metadata from day one: per-row id, modified timestamp, soft delete. The sync engine sits behind a Dependencies-style boundary so CloudKit can be replaced later; ISC-30 already forces most of this.

Exception: the session tree is stored as a JSON column inside a sessions row, with denormalized columns for date and for the tags and passages touched (what the ISC-20 list needs). It is append-only, created on one device, and read whole.

### The document structure is the export and import format

One JSON document per cloud, with stable UUIDs so re-import deduplicates, and a format version. It is at once the sharing payload (ISC-38), the backup format, and the migration path to Android. Define it early; it is the one data contract that outlives the storage choice.

## Still open before the scaffold

- App Store Connect name check for "Get Wisdom"
- **TCA26 remote access** (on the builder's path, since the builder uses TCA26). On 2026-10-26 the GitHub URL returned "not found" from the API (signed in as dwsjoquist) and "Repository not found" on `git fetch` from the local clone's SSH remote. The local checkout `/d/ivgp/tca/TCA26` is on `main` at `25dd5e5` (2026-08-06) and is the only working copy. Check the Point-Free beta page for the repo's current location or re-accept the invitation; until then the scaffold can depend on the local checkout by path, as the Skyjo prototype does.
- **Version alignment.** TCA26 and SQLiteData both depend on swift-dependencies (and SQLiteData on swift-structured-queries); confirm the resolved versions agree at scaffold time.
- The builder's authoring surface for tags, links, groups, passage boundaries, comments, and resolution, and the review flow between taggers and the editor
- Supabase setup: tier and the `pg_dump` schedule. Sign-in requirement (decided 2026-10-27): the simplest process available for vetted testers, with row-level security behind it. Sign in with Apple is the leading candidate because it is one tap on the device and needs no password or mail round trip; email one-time code is the fallback if Apple sign-in setup proves heavier than it is worth. Pick at setup

## Related

- [[Projects/Proverbs/Ideal State|Ideal State]]
- [[Categorization Scheme]] — data model inputs
- [[Exploration Plan]] — Phase 3 storage sketch (bundled SQLite vs JSON; SwiftData + CloudKit for user data)
