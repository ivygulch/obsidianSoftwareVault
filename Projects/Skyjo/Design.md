---
created: 2026-08-11
updated: 2026-08-11
---

# Skyjo — Design

Product decisions to date, largely derived from the clone review mining (what players complain about is the spec) and adaptation-usage patterns (solo-vs-AI dominates; async beats real-time).

## v1 modes

- Solo vs. computer opponents — the majority mode; the trained-opponent system is the differentiator (personas with real skill gradients; see the prototype's parameterized strategies and evolution-trained champions).
- Pass-and-play — zero-cost, fits the family table.
- Async online play — "your move" notifications; the grandmother-to-grandkids use case is the brand's killer digital scenario. No real-time in v1.

## Retention

- Daily challenge: seeded daily deal + leaderboard — procedurally generated, zero content treadmill, no clone has one.

## Fidelity requirements (from review mining)

- Official card colors (the physical bands: -2/-1 purple, 0 blue, 1–4 green, 5–8 yellow, 9–12 red) — players notice when they're wrong.
- Faithful rules incl. the doubling penalty's positive-scores-only restriction and triplet discard ordering (booklet-authoritative; encoded in the prototype engine's Rules).
- Unhurried/untimed play option.
- Accessibility: Dynamic Type and beyond — a clone earned a 1★ purely for unreadable cards.
- Skillful, trustworthy bots — no house-cheating perception; difficulty tiers with preserved personality.

## Monetization

- Free-to-try, one-time unlock (~$4.99–6.99). No ads, ever.
- Official expansions (SKYJO Action) as IAP — Handelabra model.
- House-rule variations as a feature (licensor-approved officialness the clones can't copy).

## Localization

- DE / FR / EN as launch equals (France ≈ US demand; Germany ~2/3). NL/IT/ES/PL fast follows.
- Rules text from Magilano's official rulebook translations under the license.

## Platform

- iOS first (prototype exists), Android required for family mixed households; engine is pure Swift with no framework dependencies, designed for portability.
