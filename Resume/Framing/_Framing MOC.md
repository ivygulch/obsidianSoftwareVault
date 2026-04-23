---
type: moc
created: 2026-04-23
updated: 2026-04-23
---

# Framing MOC

Narrative pieces for the focused / pillar-forward resume output. Content here is editorial material that doesn't belong on any single engagement — Summary, Core Focus Area pillars, Conference Talks, and Earlier Career condensed narrative.

The ATS resume generator ignores most of this folder and pulls only the Summary plus reverse-chronological engagement bullets. The focused resume generator pulls Summary + Pillars + Conference Talks + Earlier Career Summary alongside curated engagement bullets tagged by each pillar.

## Framing content

```dataview
TABLE framing_kind, applies_to
FROM "Resume/Framing"
WHERE type = "framing"
SORT framing_kind ASC
```

## Two resume outputs — framing role differs

**ATS resume (reverse-chronological, keyword-dense):**
- Emit Summary (narrative only, from `Summary - iOS.md`).
- Reverse-chronological Experience block pulled from `Engagements/` with `status != archive` (plus selected archive entries if relevant).
- Skills block consolidated from engagement `tech` + `practices` frontmatter.
- Education block from `Education.md`.
- No tables, no pillar framing.

**Focused resume (pillar-forward):**
- Summary at top (same source as ATS).
- Core Focus Area pillars from `Pillar - *.md` files — each pillar's narrative is included verbatim, and tagged engagement bullets may be pulled by `pull_bullet_tags` if the generator supports it.
- Selected Engagements block — curated subset in reverse-chronological order.
- Conference Talks and Teaching block from `Conference Talks and Teaching.md`.
- Earlier Career Summary from `Earlier Career Summary.md` — condensed narrative replacing a full chronological archive section.
- Education block from `Education.md`.

## Editorial policy

- Keep the Summary short (3-4 sentences). It's the first thing any reader sees on a focused resume and needs to work on its own.
- Pillars should each correspond to a distinct axis of value you want the reader to remember — don't duplicate themes across pillars.
- Conference Talks and Teaching is a discovery hook, not a credentials list. If a target resume doesn't care about speaking history, skip it.
- Earlier Career Summary should summarize depth and breadth — don't try to list every pre-2010 engagement; that's what Engagements/ is for.

## Still optional

- Generator script to render both resume types (ATS + focused) from engagement + framing content.
- Target-specific pillar variants if recurring resume targets have distinct pillars.
