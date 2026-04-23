---
type: skill
category: framework
ats_name: ""
aliases: []
first_used: YYYY-MM
proficiency: proficient
current: true
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# {{title}}

> **category** values: `language` · `framework` · `tool` · `practice` (e.g., TDD, BDD) · `domain` (e.g., payments, analytics) · `platform`.
>
> **ats_name** is the canonical spelling an ATS will match on. **aliases** are other strings that should resolve to this skill.
>
> **proficiency** values: `expert` (deep, production, teaching others) · `proficient` (shipped repeatedly) · `familiar` (used in earnest once or twice) · `exposure` (read up, experimented).

## Summary

_One or two sentences on how you use this — angle of expertise, what you've shipped with it._

## Engagements Using This

```dataview
TABLE role, start, end
FROM "Resume/Engagements"
WHERE contains(tech, this.file.name) OR contains(ats_skills, this.ats_name)
SORT start DESC
```

## Notes

_Talks given, articles written, notable incidents, opinions worth remembering._
