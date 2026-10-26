---
status: active
created: 2026-10-26
updated: 2026-10-26
---

# Proverbs — Design

How the app is built. Intent lives in [[Projects/Proverbs/Ideal State|Ideal State]]; this page holds the implementation decisions and their dates.

## Working mode (2026-10-26)

Spec driven. Claude writes the code according to Doug's direction, with the ISA as the spec and the ISCs as the acceptance tests. Doug writes or edits code only when necessary. This differs from the default iOS working mode in other projects, where Doug builds and Claude assists.

## Scaffold decisions (2026-10-26)

| Question | Decision |
|---|---|
| Who drives | Claude implements, Doug directs |
| Repo path and product name | TBD |
| Architecture | TCA 2.0 |
| Package layout | Thin app shell + SPM package + workspace (the usual layout) |
| Separate data package for curated text and loader | Open; "yes" was given to the layout, the sub-question was not answered |
| Dependencies at scaffold time | TBD |
| Minimum iOS version | TBD |
| Developer team | Ivy Gulch LLC |
| Deployment targets | iPhone and iPad |
| Testing | Swift Testing; ISC-named tests. Whether one test target per package and whether ISC tests sit in their own suite: "yes" given, read as one target per package with ISC tests in their own suite; confirm |

## Still open before the scaffold

- Repo path and product name (sets bundle ID and App Store name check)
- Dependencies: TCA 2.0 source (local TCA26 preview as Skyjo used, or a tagged release); SQLiteData or SwiftData for user data; Dependencies library
- Minimum iOS version
- Whether curated data gets its own package

## Related

- [[Projects/Proverbs/Ideal State|Ideal State]]
- [[Categorization Scheme]] — data model inputs
- [[Exploration Plan]] — Phase 3 storage sketch (bundled SQLite vs JSON; SwiftData + CloudKit for user data)
