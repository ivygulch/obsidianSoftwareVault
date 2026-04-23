---
type: company
industry: [Healthcare, Physical Therapy]
url:
size: "small"
headquarters:
status: past
first_engaged: 2016-10
last_engaged: 2019-04
created: 2026-04-22
updated: 2026-04-22
---

# Clinically Relevant

## About

Healthcare startup founded and run by Dan Rhon and Ben Hando, focused on clinical tooling for physical therapists. Primary product was TherexRx, an iOS app for therapists to develop and prescribe individualized treatment and exercise plans for rehabilitation patients.

## Engagements

```dataview
TABLE role, employment, brand, start, end, status
FROM "Resume/Engagements"
WHERE contains(string(company), this.file.name)
SORT start DESC
```

## Notes

_References, relationships, return-readiness._
