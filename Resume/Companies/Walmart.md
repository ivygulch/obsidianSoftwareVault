---
type: company
industry: [E-Commerce, Retail]
url: https://www.walmart.com
size: "Fortune 1"
headquarters: "Bentonville, AR"
status: past
first_engaged: 2014-04
last_engaged: 2026-02
created: 2026-04-22
updated: 2026-04-22
---

# Walmart

## About

The world's largest retailer by revenue. Walmart corporate operates the Walmart (US e-commerce), ASDA (UK grocery), and Sam's Club (US club retail) mobile apps on a shared iOS platform.

## Engagements

```dataview
TABLE role, employment, brand, start, end, status
FROM "Resume/Engagements"
WHERE contains(string(company), this.file.name)
SORT start DESC
```

## Notes

_References, relationships, return-readiness._
