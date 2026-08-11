---
created: 2026-08-11
updated: 2026-08-11
---

# Skyjo — Development Log

Prototype repo: `~/ivygulch/ios/projects/tca/Demo1` (`/d/ivgp/tca/Demo1`). Xcode workspace + thin app shell + `Demo1Package` (Point-Free Way layout), built against the TCA 2.0 preview checkout at `../TCA26`. The gameplay prototype was built in ~2 days; honest status: prototype, not product (no multiplayer, no polish/art/sound, no localization, no Android).

## 2026-08-07

- Project scaffolded (workspace, thin shell, package) via pfw-spm conventions; linked to local TCA26 preview.
- SKYJO rules sources committed under `rules/` (booklet transcription + figures + skyjo.info PDF); rules ambiguities resolved with the booklet as authority (positive-only doubling, triplet discard ordering).
- **SkyjoEngine** implemented: pure Swift, zero deps, deterministic (seeded SplitMix64 stored in GameState), `apply(_:) -> [GameEvent]`, `legalMoves()`, full rules incl. column rule, doubling, draw-pile recycling. 25 tests. (`5206e25`)
- `CardType` value bands (colors stay UI-side); `Constants` nested-enum convention adopted. (`3b18c9a`)

## 2026-08-08

- **Player identity**: `Player.ID`/`Kind`/`Profile` replacing seat Ints throughout. (`d7614b0`)
- **BasicStrategy** + `Strategy` protocol; full-game simulation test. (`da5cebc`)
- **GameFeature** (TCA 2.0 preview: `@Feature`, `Update`, `.onMount` bot loop) + GameView; verified in simulator.
- **StrategyParameters** genome (six families; two-axis CountingProfile) + **ParameterizedStrategy** (scored candidate selection: counting-degraded EVs, closing-vs-doubling-caution tradeoff, mimicry, temperature/blunders) + engine support (mutating Strategy, moveLog, roundHistory); design doc at `docs/strategy-parameters.md`. Personas in GameFeature. (`4a12582`)

## 2026-08-09

- **SkyjoTraining** module: ComputerPlayer/DifficultyTier/PlayerLibrary (6 personas × 4 tiers) + PlayerGenerator; **Tournament** runner (seeded round-robin, normalized-placement fitness; expert-beats-beginner validated); **Evolution** loop (elitism, tournament selection, crossover/mutation over key-path genes; champion-beats-unseen-beginners validated). (`8c9654d`)
- **Opponent selection UI**: SetupFeature sheet — by-difficulty or custom roster from the library. (`754a9cf`)
- **skyjo-train** executable; three training runs in distinct environments (balanced/chaotic/small-table) → champions **Nova** (0.819), **Vex** (0.750), **Orbit** (0.667) embedded as trained personas at all four tiers. Library feedback ratchet noted (later runs train against earlier champions). (`7338c13`)

## Backlog (product-gap list)

Async multiplayer; daily challenge; art/sound/polish; localization (DE/FR); Android strategy (engine is dependency-free by design); accessibility pass (Dynamic Type); haptics/settings; App Store presence. All contingent on the license.
