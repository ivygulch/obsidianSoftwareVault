---
type: company
industry: []
url:
size: ""
headquarters: ""
status: past
first_engaged: YYYY-MM
last_engaged: YYYY-MM
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# {{title}}

> **status** values: `active` (still engaged) · `past` (completed) · `defunct` (company no longer exists) · `acquired` (absorbed by another entity).

## About

_One short paragraph: what they do, what made them notable in your engagement. Stick to facts you can source._

## Engagements

```dataview
TABLE role, start, end, status
FROM "Resume/Engagements"
WHERE contains(string(company), this.file.name)
SORT start DESC
```

## Notes

_Private context about the company — relationship quality, how you got in, whether you'd return, who to contact for a reference._
