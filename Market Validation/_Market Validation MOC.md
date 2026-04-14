---
tags: [moc, market-validation]
---

# Market Validation MOC

This folder is separate from `Research/` on purpose. Research is
"learn about the space." Market validation is "is there demand, will
they pay, at what price, and how do I know?"

If a note is answering _is this worth building?_ it belongs here. If
it is answering _how does this domain work?_ it belongs in Research.

## Conventions

- Every note carries a `confidence:` field: `verified` · `cited` ·
  `assumed` · `guessed`. Dashboard surfaces anything below `cited`
  so assumptions do not quietly become load-bearing.
- Never fabricate TAM, adoption, or pricing numbers. If a number is
  not fetched or cited, it does not go in the note — it goes in
  **Open Questions** as something to verify.
- Validation notes should end with a **Decision Implication** line:
  what would I do differently if this turned out to be wrong?

## Validation Types

- **Demand signal** — evidence that the problem is real and painful
  (forum threads, reviews complaining, "how do I..." queries, paid
  substitutes).
- **Willingness to pay** — evidence on pricing: what comparable tools
  charge, what users pay for substitutes, what they refuse to pay for.
- **Audience reachability** — can I actually get in front of the
  target user, and how expensively? An audience I cannot reach is
  not a market.
- **Kill-test** — a specific test designed to falsify the idea
  (landing page, waitlist, pre-order, manual concierge run).

## Active Validations

```dataview
TABLE confidence, type, updated
FROM "Market Validation"
WHERE type != null
SORT updated DESC
```

## Unverified Claims To Resolve

```dataview
LIST
FROM "Market Validation"
WHERE confidence = "assumed" OR confidence = "guessed"
```
