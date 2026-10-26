# Projects

Ideas that have graduated from [[_App Ideas MOC|App Ideas]] into active work. Each project gets its own folder with a Brief, Design, Research, Development Log, Marketing, and Notes page.

The vault holds planning and thinking. Code lives in Xcode projects (accessible via the xcode mcp server).

## Active Projects
- [[_Skyjo MOC|Skyjo]] — official licensed SKYJO app; licensing outreach to Magilano in progress, working prototype built
- [[_Proverbs MOC|Proverbs]] — Proverbs linked like a wiki: tag cloud, weighted links, saved trails; promoted 2026-10-26, Ideal State in progress

## Archived (moved to App Ideas/Archive, 2026-10-26)
- [[_Flighty App Routy Demo MOC|Flighty App Routy Demo]] — outreach package to land a meeting with Flighty's founder using the Routy flight-viz app
- [[_Volunteer Fire Department Coordinator MOC|Volunteer Fire Department Coordinator]] — department-funded replacement for an old PC-only scheduling system (Jason Poremba); pre-built options first, then custom-build decision
- [[Spec Q&A|FirefighterSpot v1.1]] — v1.1 spec questions for the single-org App Store release

## All Project Briefs (Dataview)

```dataview
TABLE status, updated
FROM "Projects"
WHERE file.name = "Brief"
SORT updated DESC
```

## Ideal State Artifacts (Dataview)

Projects using the [[Craft/Ideal State Method/Method|Ideal State Method]]: criteria counts come from the ISA frontmatter, kept current by `/isa-criteria` and `/isa-check`.

```dataview
TABLE status, criteria_done, criteria_open, updated
FROM "Projects"
WHERE type = "isa"
SORT updated DESC
```
