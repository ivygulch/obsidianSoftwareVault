---
type: moc
created: 2026-04-22
updated: 2026-04-22
---

# Resume MOC

Navigation hub for the career database.

- **Engagements/** — source of truth for achievement bullets. Every resume bullet lives on exactly one engagement.
- **Framing/** — narrative pieces for the focused / pillar-forward resume: Summary, Core Focus Area pillars, Conference Talks, Earlier Career Summary.
- **Companies/** — metadata and navigation layer. Pure lookup; no substantive content.
- **Education.md** — degree entry.
- **Applications/** (not yet created) — outbound targeting pipeline (resumes sent, cover letters, outcomes).

## Current engagements

```dataview
TABLE role, company, start, team_size
FROM "Resume/Engagements"
WHERE status = "current"
SORT start DESC
```

## All engagements, reverse-chronological

```dataview
TABLE role, company, start, end, industry
FROM "Resume/Engagements"
WHERE type = "engagement"
SORT start DESC
```

## Companies

```dataview
TABLE industry, status, first_engaged, last_engaged
FROM "Resume/Companies"
WHERE type = "company"
SORT first_engaged DESC
```

## Engagements by industry

```dataview
TABLE WITHOUT ID industry AS Industry, length(rows) AS Count, rows.file.link AS Engagements
FROM "Resume/Engagements"
WHERE type = "engagement"
FLATTEN industry
GROUP BY industry
SORT length(rows) DESC
```

## Engagements by theme

```dataview
TABLE WITHOUT ID themes AS Theme, length(rows) AS Count, rows.file.link AS Engagements
FROM "Resume/Engagements"
WHERE type = "engagement"
FLATTEN themes
GROUP BY themes
SORT length(rows) DESC
```

## Tech coverage

```dataview
TABLE WITHOUT ID tech AS Tech, length(rows) AS Engagements
FROM "Resume/Engagements"
WHERE type = "engagement"
FLATTEN tech
GROUP BY tech
SORT length(rows) DESC
```

## Still optional

- `Skills/` folder — reference pages per skill cluster with Dataview rollups. ATS-canonical strings already live in engagement `tech` / `practices` / `industry` frontmatter; `Skills/` adds navigation, not data.
- `Applications/` pipeline — migrate `coverletters/` into `Applications/<date> <company>/` folders with JD, cover letter sent, targeted resume sent, interview notes, and outcome.
- ATS resume generator (reverse-chronological, keyword-dense, no tables).
- Focused resume generator (pillar-forward, pulls from `Framing/` + tagged engagement bullets).
