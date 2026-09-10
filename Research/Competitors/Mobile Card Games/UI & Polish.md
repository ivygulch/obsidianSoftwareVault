---
type: research
confidence: verified
tags: [card-games, mobile, competitors, skyjo]
created: 2026-09-10
updated: 2026-09-10
---

> Pillar report for [[Mobile Card Games — Landscape]]. Core gameplay UI/UX conventions, async patterns, juice catalog, accessibility. Data pulled 2026-09-10 (US App Store via the appstore MCP; web sources cited inline).

# Mobile Card Games — UI  Polish


Scope: what the best mobile card games do in core gameplay UI/UX, and the below-notice polish ("juice") that makes them feel good, filtered for a calm golf-family game (3x4 face-down grid per player, flip/swap/discard turns, solo vs AI, pass-and-play, async online). Claims are tied to sources in the final section; where something is my inference from a source rather than stated by it, it is marked *(inference)*.

## 1. Core gameplay UI/UX conventions

### The table is a physical object, not a form
- **Hearthstone (Derek Sakamoto, GDC 2015 "How to Create an Immersive User Interface")**: the team rejected flat UI and "got physical." Stated payoffs: physical objects read as valuable; consistent motion vocabulary (bounce, over-rotation) across every screen makes them feel like one thing "whether the player realizes it or not"; and physicality translated to touch "a little bit magical" because cards tilt as you drag, swoosh, and dust flies when you tap the board. Stated costs: hard to expand later, resource-intensive, navigation is less efficient because they design "flavor over efficiency." They shrank nothing to fit: scaling objects down "affects your perception of the value of these things." *(Applicable: keep card size constant; add opponents by re-laying the table, not by shrinking cards.)*
- **Hearthstone "board as toy" clickables**: fidget objects on the board with no gameplay function; Sakamoto's two-year-old asked to "play Hearthstone" meaning launch the rocket. Idle fidget surfaces are cheap and give the table an over-the-shoulder appeal.
- **Marvel Snap (Ben Brode, GDC 2023 "Designing MARVEL SNAP")**: mobile-first, six-turn, ~3-minute games explicitly inspired by Clash Royale's "if you have five minutes you are 100% sure you can get a game." Brode also describes reframing losing: the concede button became "Retreat," and the "you lose" announcer line was cut because it "emphasized exactly the emotions we're trying to minimize." *(Applicable: name the end-of-round state carefully; never punish the loser with a loud fail state in a family game.)*

### Tap vs drag
- **Solitaire (MobilityWare)** supports both drag-and-drop and tap-to-move; tap sends a card to its best legal destination. This is the convention the largest card audience has learned. Ship both; make tap the default for a grid game where every legal target is unambiguous *(inference)*.
- **Slay the Spire iOS (TouchArcade, Pocket Gamer)**: drag-card-to-enemy works on iPad but "many users struggled on iPhone and had to try several times"; inspecting a card without playing it was hard because touching starts a drag; potion menu and top-of-screen targets were too small. Lesson: separate *inspect* from *commit*, and keep no commit target near the top edge.
- **Balatro mobile (Engadget, TouchArcade)**: praised as an "almost perfect" port; drag-to-designated-area replaced menus for buy/sell/use. Its one cited misplay source was the Skip button placement causing fat-finger taps. Landscape-only was the main complaint; a community portrait mod added swipe-up-to-play / swipe-down-to-discard and a left/right-handed layout toggle, which is a good spec for one-thumb portrait play.
- **Card Crawl / Dawncaster**: cited as the reference for portrait, one-thumb card play with 2-minute rounds; Dawncaster's UI is responsive to any size/orientation and runs at 60 fps while "easy on battery."

### Preventing misplays and confirming
- Solitaire: unlimited undo is table stakes for the casual audience (MobilityWare, Microsoft Solitaire Collection). For a competitive turn game, offer undo *within* the turn until the turn is committed; the drawn-card decision (keep vs discard) is the one irreversible fork, so make it a two-step: draw, then tap a grid slot or the discard pile, with the drawn card hovering until placed *(inference from the Slay the Spire and Balatro findings)*.
- Hearthstone's turn is a single-player puzzle: "when it's my turn it's my turn," no out-of-turn responses. The same applies here; nothing should ever require the non-active player to act.
- Touch targets: Apple HIG minimum 44x44 pt; thumb contact is closer to 25 mm wide, so grid cells should be larger than the minimum and separated by gutters. Put commit actions in the bottom third for one-handed reach.

### Turn indication and timers
- **Hearthstone**: 75-second turn; a burning rope appears with ~20 s left and reaches the End Turn button; an idle player's next turn starts with a ~7 s fuse until they act. The visual countdown avoids a numeric clock and fits the table's material language. A calm game can use a soft version: a slow fill around the player's avatar, no sound until the last few seconds *(inference)*.
- **Marvel Snap**: whose nameplate glows tells you whose cards reveal first; the reveal order itself carries information. Use a single persistent "who's up" cue (avatar glow plus a subtle drop shadow lift on their grid) rather than a modal banner.
- **Exploding Kittens 2**: real-time only; a turn time limit was added to online play after launch, and it has a "Your Turn" notification. The developers also explicitly shipped "faster animations for a snappier gameplay experience," a common post-launch fix worth avoiding up front by making animation speed a setting.

### Watching opponents at a readable pace, and AI "thinking"
- Hearthstone's sound team designs to the fixed timing of turn-based play: "when you drag a card out of your hand and drop it into play" is a known beat, and they take "a more rhythmic and musical approach to sound design in terms of pacing." Opponent turns should be choreographed to a fixed beat: pause, draw, brief hover, place, flip, settle *(inference)*.
- Research on response latency (Neuroscience News summary; "The Robot That Waited") finds that people rate an instant machine answer as less thoughtful and read a short deliberate pause as reflection, even when they know it is scripted. An AI opponent should pause proportionally to the decision's difficulty, not with a fixed sleep, and the pause should have a visible tell (a card lifting slightly, an avatar glance).
- Play Nine and the unofficial Skyjo apps draw review complaints that bots make moves "no reasonable real life person would" and that the bot "will replace a 10 with a 9." Perceived-fairness complaints are the dominant negative theme for golf-family apps; readable AI turns (you can see what it drew and why it swapped) are the UX mitigation.

### Win, end-of-round, and celebration
- Windows Solitaire's bouncing-card cascade (1990 to XP) is the most-remembered win state in casual gaming; it was a "standing ovation" at a time of few rewards. MobilityWare now ships multiple win animations plus a setting to skip them. Ship one signature end-of-round moment, keep it under a few seconds, make it skippable by tap, and never repeat it for hand-level events *(inference)*.
- Hearthstone (Eric Dodds, GDC 2014): pay attention to emotional state even in the matchmaking spinner; its copy was changed because promising a "perfect opponent" felt like a lie after a blowout. Copy in waiting and result screens should be honest and low-stakes.

### Daily hooks and session shape
- Microsoft Solitaire Collection: daily challenges, unlimited undo, non-intrusive hint highlighting. Solitaire Grand Harvest wraps the same loop in rewards and a farm meta; reviewers frame that as "casual mobile game" rather than card game. For a premium no-ads title the Microsoft shape (daily deal, streak, personal bests) fits better than the Grand Harvest shape.

## 2. Multiplayer and async UX patterns

- **Invite by code**: Play Nine's friends mode is a closed game joined by sharing a code "via text or any platform." It also has in-game chat, 2 to 4 players, and a selectable number of holes. This is the expected baseline for a physical-brand adaptation.
- **Apple GameKit turn-based matches**: store-and-forward model; one designated current player; the next player receives a push notification when a turn ends; the match inbox view is the fallback when notifications are missed; "exchanges" let non-current players take side actions. The design constraint is that only the current player needs to act, which fits a golf-family game exactly. Developer forum threads show push delivery is not fully reliable, so an in-app inbox with unread badges is required, not optional.
- **Async is not universal**: Exploding Kittens 2 is real-time only because the Nope card needs everyone watching. A golf-family game has no interrupts, so async is safe.
- **Returning to a game**: Board Game Arena's "Replay last moves" button exists because async players need to see what happened while away; users note it plays too fast. Spec: on open, replay opponent moves since your last visit at the same choreographed pace as a live opponent turn, tappable to skip, with a text log as the accessible equivalent *(inference from BGA and the pacing sources)*.
- **Turn notifications**: Exploding Kittens 2's "Your Turn" push and GameKit's built-in turn push. Keep the notification body informative ("Ana flipped a 12 and it's your turn, round 3") so the notification itself is the last-move summary *(inference)*.
- **Pass-and-play**: none of the reviewed apps document a good handoff. The missing conventions: a handoff screen that hides both grids until the next player taps "I'm ready," and per-player face-down state preserved across the handoff *(inference)*.
- **Session length as design**: Marvel Snap's six turns and Clash Royale's guaranteed five-minute game are cited by Brode as the origin of the format. A single hole should complete in about a minute; a nine-hole game is the "long session."

## 3. Polish and juice catalog

| Technique | What it does | Who does it | Applicability to a calm card game |
|---|---|---|---|
| Easing, never linear | Objects decelerate into position; overshoot ("go slightly past our target") reads as luxurious | Juice It or Lose It; Balatro's `(0.34, 1.56, 0.64, 1)` overshoot curve | High. Every card move and flip uses ease-out or a spring; never linear. |
| Random stagger on group animations | Adding "a little bit of delay, a random delay to everything" makes a deal look dealt rather than pasted | Juice It or Lose It | High. Deal the 12-card grid with 30 to 60 ms jitter per card; same for round-end reveal. |
| Springs that inherit velocity, interruptible | Motion starts from the current value, carries the finger's velocity, can be grabbed mid-flight | Apple WWDC18 Designing Fluid Interfaces | High. A dragged card released early springs back; a second tap mid-animation redirects instead of queueing. |
| One-to-one tracking during drag | Content stays under the finger; no lag | WWDC18 Fluid Interfaces | High. The drawn card must track the thumb exactly; only the drop is animated. |
| Card tilt toward drag direction | Card rotates a few degrees toward the cursor while dragged, plus a lift and shadow | Hearthstone (Sakamoto); itch.io physics drag-drop write-up | High. Small angle (under 8 degrees), decays with a spring on release. |
| Hover lift and shadow deepening | Selected card rises and its shadow grows, signaling "in hand" | Balatro (translateY -12px scale 1.05; selected -24px) | High. Use for the drawn card and the tapped grid slot. |
| Flip with anticipation | Card lifts slightly at mid-flip so the hinge reads as 3D; ease-in-out ~0.25 to 0.4 s | Auroratide "realistic flip" write-up; common CSS flip specs | High. Flip is the core verb; give it a lift, a tiny y-rise at 90 degrees, and a settle. |
| Snap-to-slot with settle | Object overshoots the slot and settles; bounce equation for emphasis | Juice It or Lose It | High. Placing into the grid gets a 1-bounce settle; discarding gets a softer settle. |
| Squash and stretch on impact | Ball scales up on hit and eases back; UI elements around it pulse | Juice It or Lose It | Low-medium. A 2 to 3 percent scale pulse on the discard pile when a card lands; nothing more. |
| Hit-stop / sleep frames | Pause 20 ms at moments of impact so the brain registers them | Vlambeer, Art of Screenshake | Low. Only at the round-end column-clear moment. |
| Screen shake, proportional | Shake scales with significance; Balatro tiers 2/4/8 px by score magnitude | Balatro; Vlambeer; Juice It or Lose It | Very low. Vlambeer notes players got nauseous and Nuclear Throne added a disable. Reserve for a column clear, at 2 px, and expose a toggle. |
| Proportional feedback | "Feedback should be proportional to significance"; the same channel at different intensities becomes a data channel | Balatro (Crosley guide) | High. Flip a 1 vs flip a 12 should sound and move differently. |
| Number tick-up / digit roll | Score digits roll with 50 ms per-digit stagger and overshoot | Balatro | High. Hole score and running total roll rather than jump; column-clear subtracts with a visible roll. |
| Color as label | Chips blue, mult red, money gold; "no labels needed" | Balatro | High. Card value tiers by color are the whole readability model of golf games; keep it but pair with numerals. |
| Layered sound stack | Rising pitch notes per card in a flush; distinct layer per event type; bass on threshold | Balatro; Hearthstone sound team (layered synthesis, "subjective sound design" on key beats: cast, hit) | High. Slide, snap, flip, and discard each get their own short layer; column clear gets a rising 3-note. |
| Sound sells collision | Two circles passing through each other read as bouncing once a sound is added | Juice It or Lose It, citing Swink | High. Sound is the cheapest way to make a flat card feel like it landed. |
| More bass in the impact sound | A designer "fixed" an unpopular gun by bass-boosting the sample | Vlambeer | Medium. A faint low layer on card landing makes it feel heavier than a click. |
| Rhythmic timing of turn events | Turn-based games have fixed beats; audio and animation designed to that beat | Hearthstone sound team | High. Author opponent turns as a fixed rhythm; users learn the rhythm and stop watching the screen. |
| Permanence | Corpses and shells stay on the floor so the arena records what happened | Vlambeer | Medium. The discard pile shows a slightly messy stack with prior cards peeking; do not reset it to a clean single card. |
| Idle micro-motion | Constant micro-motion makes the hand feel alive; foil shimmer loop | Balatro | Medium. A barely visible breathing on the active player's grid; nothing on the opponents'. |
| Eyes and personality | Adding eyes and a smile to the paddle for near-zero cost | Juice It or Lose It, via Kyle Gabler | Medium. Opponent avatars react (glance at the discard, wince at a flipped 12) for the AI-readability problem noted above. |
| Consistent motion vocabulary | Same bounce and over-rotation across every screen makes the app feel like one object | Hearthstone (Sakamoto) | High. One spring, one duration scale, one shadow model across menus and table. |
| Haptic transients synced to visuals | Short transient events for taps and landings; synchronize with sound and visuals; never as the only channel; user-optional | Apple HIG Playing Haptics; Core Haptics transient vs continuous | High. Light transient on flip completion, medium on placement, notification-style on your turn; a toggle. |
| Celebrate without spam | One signature win animation, skippable, plus a setting to skip | Windows Solitaire cascade; MobilityWare skip setting | High. |
| Speed control | Game speed setting at 0.5 to 4x | Balatro; Exploding Kittens 2 post-launch "faster animations" | High. Ship an animation speed setting on day one. |

## 4. Accessibility observations

- **Reduce Motion**: Apple guidance flags large fly-in/fly-out animations and oscillation near 0.2 Hz as problematic, and says motion must never be the only carrier of information. Balatro's "Reduced Motion" option is criticized on Steam for leaving moving text and the shop sign animated, and its screen shake is a separate slider. Spec: when Reduce Motion is on, replace slides with crossfades (PCalc's approach), disable idle motion and shake entirely, keep the flip but drop its overshoot.
- **Color-independent encoding**: golf-family games lean on value-tier colors. Accessible Solitaire and other AppleVis-listed apps offer custom suit colors and a red-green safe mode. Always render the numeral; consider optional shape or pattern on tiers for negative cards.
- **VoiceOver**: Accessible Solitaire (AppleVis) announces card details as you move, can announce available moves and the current game state, and supports Voice Control and Switch Control so every card can be moved without a drag. Blindfold Solitaire is fully VoiceOver-driven. For a grid game, each cell should be an accessibility element labeled "row 2 column 3, face down" or "row 2 column 3, seven," with custom actions for "flip" and "swap with drawn card," and an accessible text log of opponent moves in place of the animated replay.
- **Dynamic Type**: Slay the Spire mobile was criticized for text-heavy cards that strain on phones. Card numerals should scale with Dynamic Type up to the point where the grid still fits; score labels and logs should scale without limit.
- **Touch targets**: 44 pt HIG minimum is undersized for thumbs; Slay the Spire's small potion and top-edge targets and Balatro's Skip-button fat-fingering are the cited failures. No commit action within a thumb's width of a destructive or unrelated action.
- **Bad examples worth studying**: Play Nine and the unofficial Skyjo apps draw review complaints about unreadable bot behavior, busy layouts where more than three players do not fit on screen, and glitches between rounds. These are readability and pacing failures, not feature gaps.

## 5. Sources

- Derek Sakamoto, "Hearthstone: How to Create an Immersive User Interface," GDC 2015: https://www.youtube.com/watch?v=axkPXCNjOh8
- Eric Dodds, "Hearthstone: 10 Bits of Design Wisdom," GDC 2014: https://www.youtube.com/watch?v=pyjDMPTgxxk and https://www.gdcvault.com/play/1020775/Hearthstone-10-Bits-of-Design
- Ben Brode, "Designing 'MARVEL SNAP'," GDC 2023: https://www.youtube.com/watch?v=HjhsY2Zuo-c
- Martin Jonasson and Petri Purho, "Juice it or lose it," 2012: https://www.youtube.com/watch?v=Fy0aCDmgnxg
- Jan Willem Nijman (Vlambeer), "The Art of Screenshake," INDIGO 2013: https://www.youtube.com/watch?v=SkgkIXZ_13Y
- Steve Swink, Game Feel (three building blocks; 100 ms correction cycle): https://lizengland.com/blog/review-game-feel-by-steve-swink/ and https://en.wikipedia.org/wiki/Game_feel
- Blake Crosley, "Balatro: Juicy Feedback in a Poker Roguelike": https://blakecrosley.com/guides/design/balatro
- TouchArcade Balatro interview with LocalThunk (mobile port): https://toucharcade.com/2024/03/18/balatro-interview-mobile-port-localthunk-dlc-plans-updates-new-jokers-demo-feedback/
- Engadget, "Balatro is an almost perfect mobile port": https://www.engadget.com/gaming/balatro-is-an-almost-perfect-mobile-port-163050971.html
- Balatro portrait/one-handed community mod (spec reference): https://github.com/KtourzaJeremy/balatro-portrait-mobile
- Balatro reduced-motion and screen-shake discussions: https://steamcommunity.com/app/2379780/discussions/0/4348864737704763435/
- Blizzard, "Meet the sound team behind Hearthstone's harmonic design": https://hearthstone.blizzard.com/en-us/news/23964694/inside-battle-net-meet-the-sound-team-behind-hearthstone-s-harmonic-design
- Hearthstone turn timer and rope: https://hearthstone.wiki.gg/wiki/Turn
- Marvel Snap reveal order (nameplate glow): https://marvelsnap.helpshift.com/hc/en/3-marvel-snap/faq/38-whose-cards-are-revealed-first-during-a-turn/
- Unity case study, Marvel Snap CAT tool and card parallax: https://unity.com/case-study/marvel-snap
- MobilityWare Solitaire (tap-to-move, drag, undo, hints, skip win animation): https://apps.apple.com/us/app/solitaire-by-mobilityware/id284791396
- Windows Solitaire win animation history: https://knowyourmeme.com/memes/cards-when-you-win-in-solitaire and https://github.com/zeke/solitaire
- Slay the Spire iOS review (touch problems): https://toucharcade.com/2020/06/15/slay-the-spire-ios-review-iphone-ipad-performance-icloud-megacrit-humble-games/ and https://www.pocketgamer.com/slay-the-spire/review/
- Card Crawl review (one-thumb play): https://toucharcade.com/2015/03/13/card-crawl-review/ ; Dawncaster review (portrait, 60 fps): https://www.148apps.com/dawncaster/dawncaster-review/
- Play Nine: Golf Card Game (App Store, invite by code, reviews): https://apps.apple.com/us/app/play-nine-golf-card-game/id1567060312
- Sky-jo: Golf Card Game and Skyjo-o (unofficial; review complaints): https://apps.apple.com/us/app/sky-jo-golf-card-game/id1567186753 and https://apps.apple.com/us/app/skyjo-o-flip-your-skylza/id6744247458
- Exploding Kittens 2 (real-time only, turn limit, Your Turn notification): https://apps.apple.com/us/app/exploding-kittens-2/id6478287619 and https://steamcommunity.com/app/2999030/discussions/0/4515507601681902080/
- Apple GameKit turn-based matches: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/GameKit_Guide/ImplementingaTurn-BasedMatch/ImplementingaTurn-BasedMatch.html
- Board Game Arena "Replay last moves": https://forum.boardgamearena.com/viewtopic.php?t=20295
- Apple HIG, Playing haptics: https://developer.apple.com/design/human-interface-guidelines/playing-haptics ; WWDC21 "Practice audio haptic design": https://www.youtube.com/watch?v=qcO9NMKn3Ao
- Apple WWDC18, "Designing Fluid Interfaces": https://developer.apple.com/videos/play/wwdc2018/803/
- Reduce Motion guidance and PCalc example: https://useyourloaf.com/blog/reducing-motion-of-animations/
- Touch target sizing and thumb zones: https://www.lukew.com/ff/entry.asp?1085= and https://www.72technologies.com/blog/tap-targets-thumb-zones-mobile-ux
- Accessible Solitaire (AppleVis): https://www.applevis.com/apps/ios/games/accessible-solitaire
- AI response latency perception: https://neurosciencenews.com/latency-perception-thoughtful-ai-30597/ and https://medium.com/@nigeleplatt/the-robot-that-waited-why-ai-should-sometimes-hesitate-babd24677ffb
- Realistic card flip with mid-flip lift: https://auroratide.com/posts/realistic-flip-animation/
- Physics-based card drag with tilt (implementation reference): https://itch.io/blog/1325095/ui-physics-based-drag-drop-system-with-holographic-card-shaders-in-unity
