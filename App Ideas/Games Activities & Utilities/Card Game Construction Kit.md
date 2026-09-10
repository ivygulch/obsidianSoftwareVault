---
area: Games Activities & Utilities
status: seed
tags: [app-idea, card-games, ugc, ai-bots]
created: 2026-09-09
updated: 2026-09-09
---

# Card Game Construction Kit

**One-liner:** A card-game platform that ships with polished prebuilt folk games (Golf, Rummy, …) and lets players create custom decks, custom rules, and trainable robot opponents — then share all of it with other players.
**Target user:** Families and casual card players with house rules and home-invented games; the same people who buy scorekeeper apps by the swarm today.
**Problem:** Every family's card game is slightly different (house rules, homemade variants, invented games), and no mobile platform lets them play *their* game — with worthy computer opponents — rather than someone else's fixed implementation.
**Differentiator:** Trainable/coachable bot opponents for user-created games. Deck editors and rule tweaks exist elsewhere; nobody gives a home-invented game a computer player that actually plays it well.

## The Three Questions

_Seed stage — drafts below are candidates to confirm or replace, not answers._

**Who pays, how often, how much?**
_(draft)_ The prebuilt-games tier is the paid product (one-time, $5–10, consistent with the indie pricing research); the construction kit is the retention/moat layer. Alternative: kit as subscription for creators, prebuilt games one-time for players. Undecided — and the honest version of this answer needs a named person: does the family that plays "Grandma's rummy variant" pay, or only the hobbyist inventor?

**Year-2 maintenance cost:**
_(draft)_ The heavy items are (1) shared-content moderation — UGC decks/rules/names need review or reactive takedown, an ongoing human cost; (2) sharing backend hosting; (3) bot-training compute if training runs server-side. A local-first version (sharing via files/links, training on-device) keeps year-2 near zero but caps the network effects. This tension is the idea's central portfolio-fit question.

**Kill criteria:**
_(draft)_ (1) If the rules-expressiveness spike shows that covering even the folk-game canon requires a scripting language rather than parameterized templates, the kit collapses into a programming tool — kill or descope to "variants of shipped games only." (2) If playtesting shows families won't build (only play), the kit is a feature, not a product — fold it into whichever card game ships. (3) Store evidence that toolkit apps in this space monetize worse than single games at equal effort.

## Concept

Four layers, in dependency order:

1. **Prebuilt games** — polished implementations of public-domain folk games: Golf (the SKYJO ancestor — ships regardless of any license), Rummy, Crazy Eights, Hearts, etc. Each is a complete, family-grade game on its own; together they prove the engine and seed the catalog.
2. **Custom decks** — deck editor: card faces, values, suits/bands, art within a template system. (The skin layer from [[Projects/Skyjo/UI Explorations|UI Explorations]], exposed to users.)
3. **Custom rules** — the hard problem. Spectrum runs from parameterized variants of shipped games (house-rules toggles: deal counts, scoring tweaks, wildcard behavior) to a full rules-construction system for novel games. Where on that spectrum v1 sits determines the whole project's scope.
4. **Robot players** — bots for custom games, built two ways: **training** (self-play evolution, the SkyjoDemo trained-champion system generalized) and **suggesting strategies** (natural-language coaching — "hold high cards early, dump on the discard when an opponent knocks" — translated into bot parameters; an operational-tier LLM task, cheap at small-model prices, plausibly on-device).

**Sharing** wraps all four: decks, rule sets, bots, and complete games as shareable artifacts. Spectrum again: file/link sharing (no backend, no moderation burden) → in-app community gallery (network effects, real moderation and hosting costs).

## Prior Art

_(from general knowledge — needs a store-side verification pass before this leaves seed)_

- **Tabletop Simulator (PC/Steam)** — proves demand for build-your-own tabletop; gets sandbox freedom right, but enforces no rules (players self-referee) and has no AI opponents; desktop-only, hobbyist-tier complexity.
- **Board Game Arena (web)** — proves the multi-game platform with enforced rules; huge catalog, but every game is staff/volunteer-implemented — users can't create, and bots are scarce.
- **playingcards.io / Screentop-tier web sandboxes** — prove lightweight custom card play with friends; free-form tables, no rules enforcement, no bots, no mobile-native experience.
- The mobile App Store gap mirrors all three: fixed single-game apps (Mattel163 tier) and scorekeeper swarms, but no construction kit with enforced rules and worthy bots found so far — verify.

## Why It Could Work

- **The three-layer architecture already exists** — rules engine (pure Swift, portable), behavior layer, skin layer ([[Projects/Skyjo/UI Explorations|UI Explorations]]). The kit is those layers with the lids opened to users.
- **The trained-bot system is the moat piece.** Bot quality is the #1 complaint against existing card-game clones (per the [[Licensed IP Game Adaptations — Landscape]] review mining), and it's the one component a UGC platform can't fake — a home-invented game with a bot that plays it *well* is genuinely new.
- **Hedges the licensing thread.** Folk Golf ships without Magilano; if SKYJO lands, it becomes a premium licensed title on the same platform. The kit and the licensed-IP strategy feed each other rather than compete.
- **Small-model economics** make the strategy-coaching feature viable at consumer pricing (operational LLM task, not frontier — see the small-models discussion, 2026-09-07).
- **Through-line fit**: house rules are family heirlooms — "the way Grandma plays" as a shareable artifact is passing-things-on in software form.
- The scorekeeper swarm across every card-game search is indirect evidence that players bring *their own table culture* to phones and get no support for it.

## Why It Might Not

- **Rules expressiveness is a tarpit.** General card-game engines converge on being programming languages; the space of "simple" folk games hides enormous mechanical variety (trick-taking vs. shedding vs. draw-and-discard vs. melding). The 80/20 may not exist.
- **A construction kit can be a clone factory.** The same research that motivates the licensed thread shows what UGC sharing invites: users will rebuild SKYJO, UNO, Skip-Bo with names and trade dress attached, and the platform becomes the infringement vector its own Magilano letter complains about. Mitigations (no trademarked names in shared content, art templates rather than free image upload, takedown flow) are real work and real year-2 cost — and an unavoidable conversation if the Magilano relationship exists.
- **Toolkits historically sell worse than games.** Most buyers want to play, not build; the build audience may be a sliver of an already-niche market.
- **Sharing needs network effects; the portfolio model wants low upkeep.** A gallery with ten users is worse than no gallery; sustaining one is a service business, not a small app.
- **App Review**: UGC apps carry moderation/reporting requirements (guideline 1.2) that raise the compliance floor.

## Open Questions

- Where on the rules-expressiveness spectrum does v1 sit? (Candidate answer: parameterized variants of shipped games only — "house rules," not "new games" — with novel-game construction as the v2 bet after evidence.)
- Is sharing v1, v2, or never-in-app (file/link export only)? The moderation cost hinges on this.
- Does "suggest strategies" run on-device (Foundation Models) or cloud (small-model API)? Privacy, cost, and offline play all point on-device; capability may not.
- What's the v1 folk-game set? (Golf is strategic — the SKYJO hedge; Rummy is the biggest folk name; what's the third?)
- Does the kit strengthen or complicate the Magilano pitch if it ships first? ("We build official versions" vs. "we run a platform where users clone games" — the framing needs care.)
- Name/branding: descriptive working title only; naming comes after scope.

## Related

- [[Projects/Skyjo/UI Explorations|UI Explorations]] — the three-layer architecture this idea generalizes
- [[Projects/Skyjo/Design|Skyjo Design]] — fidelity/monetization positions that carry over
- [[Licensed IP Game Adaptations — Landscape]] — review-mining evidence (bot quality, clone dynamics) and the IP-risk mirror
- SkyjoDemo repo (`~/ivygulch/ios/projects/tca/SkyjoDemo`) — engine + trained champions, the technical seed
