---
type: note
status: exploring
created: 2026-09-09
tags: [skyjo, design, ui, card-games, interaction]
---

# Card Game UI Explorations

Interaction and experience exploration for card-game play — engaging and innovative, built above the engine. **Deliberately IP-agnostic**: SKYJO is the first vehicle, but everything here must work as a skin/behavior layer that applies to any grid-card or hand-card game on the engine. If the Magilano deal never lands, this page moves out of the Skyjo project and drives the next card game instead. Product constraints it serves: [[Projects/Skyjo/Design|Design]] (fidelity list, modes). Store/HIG constraints: [[Apple Design Guidance]].

## Design goals (derived from the clone complaint stack, inverted)

1. **Trust** — the player never suspects the game of cheating or manipulating. Every random event is visible or auditable; bots act legibly.
2. **Calm** — unhurried by default. No timers unless invited, no interstitial interruptions, no attention traps. The register is the family table, not the casino.
3. **Tactility** — cards feel like objects: mass, flip, slide, snap. The joy of handling pieces is a feature, not decoration.
4. **Readable at every age** — a 7-year-old and an 80-year-old parse the table at a glance. Dynamic Type on cards, glare-proof contrast, color-independent encoding.
5. **Personality** — opponents are characters with visible temperament, expressed through play style and micro-presentation, never through chatter that slows the game.

Anti-goals: coin economies, screen-shaking celebration spam, casino glitter, anything that makes a turn take longer than the player wants it to.

## Territory 1 — The physical-card feel

- Gesture-first card handling: drag with momentum, flip that pivots under the thumb (hinge physics, not a canned animation), placement that snaps with a settle.
- A **haptic vocabulary**: distinct, consistent transients for draw / flip / place / discard / column-clear / round-end. Learnable by feel — a player could play eyes-closed and know what happened. (HIG "Playing haptics": bring familiarity with the physical world in.)
- Sound identity to match: felt-table acoustics — card slide, snap, soft riffle. No music by default; the table has ambience, not a soundtrack.
- Material contrast: chrome (menus, HUD) can be Liquid Glass; **cards must be matte** — paper reads as paper. The contrast is what makes the cards feel real.
- Card faces built as a parameterized skin: color band + glyph + texture as slots (SKYJO trade dress becomes one skin under license; a generic skin ships without it).

## Territory 2 — Legible AI turns (the pacing + trust problem)

The clones' twin failures: bots that act instantly and inscrutably ("no logic"), and the house-cheating suspicion. Both are presentation problems as much as AI problems.

- Bots **visibly consider**: a brief hover over the draw pile, a glance-weight pause over a candidate column, then the act. Milliseconds of theater that make skill legible.
- Turn speed is a player setting (instant / natural / deliberate), never a fixed drag.
- **Post-round transparency**: an optional "what were they thinking?" replay — the bot's key decisions annotated in one line each. Directly attacks the cheating perception; no clone can copy it without real AI underneath. Differentiator sits on the trained-persona system.
- Last-turn replay glance (swipe down?) for "wait, what just happened" moments — supports the across-generations table where attention wanders.

## Territory 3 — The table as a place

- The board has depth and camera language: subtle push-in on your turn, pull-wide at round end. Motion conveys state (HIG "Motion"), never decorates.
- Opponent grids readable at a glance — and the table must read as *the game* in a static thumbnail (the App Store screenshot requirement doubles as a design test: if a still frame doesn't communicate state, the layout fails).
- One-handed portrait reach: every required action within thumb arc; the opponent area is glanceable, never touched.
- Round/score transitions as table rituals (cards sweep, next deal) rather than modal popups — the "Round over" sheet in the current prototype is exactly what to replace.

## Territory 4 — Accessibility as a design driver, not a checklist

- **Color-independent card encoding**: value bands carried by shape/pattern/position in parallel with color. Dual payoff: colorblind players parse the table, and the unlicensed skin needs no trade-dress colors at all — accessibility work and licensing caution are the same work here.
- Dynamic Type on card faces with layout that reflows rather than truncates.
- Reduced Motion path: every ritual has a dissolve equivalent.
- VoiceOver: the grid as a navigable table with meaningful summaries ("Sage's grid: nine hidden, two zeros, minus-one"), not 12 unlabeled buttons.

## Territory 5 — Form factors and moments

- **iPhone Duo postures**: half-fold tabletop = the card table (board on the flat half, hand on the raised half, or face-to-face pass-and-play across the hinge); closed-screen solo round continues onto the inner display when opened. This is the featuring story — see the Duo discussion in chat 2026-09-09.
- iPad face-to-face: two players, rotated hands, one device flat on the real table.
- Async "your move" as a **widget/StandBy moment** — the game reaches the player without a notification nag; the grandmother sees the pending move on her nightstand.
- SharePlay layer for the across-distance family game; Duo's dual-camera FaceTime view as the "hands and face" presence experiment.

## Territory 6 — Personality layer

- Personas expressed through: play-style (already real — trained champions), turn-pacing temperament, a restrained avatar micro-reaction at key beats (a wince at eating a 12, nothing chatty).
- Register check for every personality touch: family table, all-ages, never mocking the loser.

## Reuse architecture

Everything above lands in three separable layers, matching the engine split that already exists:

1. **Rules engine** (pure Swift, portable) — untouched by this work.
2. **Behavior layer** — turn pacing, AI legibility theater, rituals, haptic/sound vocabulary. Game-agnostic; parameterized per game.
3. **Skin layer** — card faces, colors, materials, table surface, personas' visual identity. SKYJO trade dress is one skin; a clean generic skin is the default and ships regardless of any license.

## Spike list (ordered, each independently buildable)

1. **Card physics playground** — one card, drag/flip/settle with haptics; tune until it feels like a card and not a rectangle. Everything else inherits this.
2. **Haptic + sound vocabulary demo** — the six transients on buttons; test eyes-closed recognizability.
3. **AI turn theater** — one bot turn rendered at three pacing settings with consider-hover; A/B against instant-act for perceived intelligence.
4. **Color-independent card encoding** — three candidate encodings (glyph, corner shape, fill pattern) screenshot-tested in grayscale.
5. **Round-transition ritual** — replace the "Round over" sheet with a table sweep; Reduced Motion variant alongside.
6. **Duo tabletop mock** — simulator-only posture layout study (board/hand split across the fold).

## Open questions

- How much motion is too much for the calm register — where's the line between tactile joy and fidget?
- Does post-round bot transparency spoil the "opponent" illusion, or deepen it? (Prototype and playtest with family.)
- Widget/StandBy async surface: does iOS's refresh budget make the nightstand moment reliable enough to promise?
- Which of the six spikes changes the most downstream decisions? (Candidate: card physics — it sets the app's entire feel vocabulary.)
