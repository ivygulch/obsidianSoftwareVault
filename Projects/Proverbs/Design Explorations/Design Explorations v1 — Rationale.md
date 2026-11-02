---
title: Design Explorations v1 — Rationale
project: Proverbs
date: 2026-11-02
status: exploration
companion: Design Explorations v1.html
tags: [design, ui, exploration]
---

# Design Explorations v1 — Rationale

Companion to [[Design Explorations v1.html]], the single-page presentation of thirteen iPhone mockups made on 2026-11-02 from the [[Get Wisdom Design Document]] snapshot of that date. This note records what the mockups were trying to find out, why they look the way they do, what was assumed, and what they cannot settle. The presentation is the artifact; this is the reasoning behind it. Neither supersedes the [[Ideal State]]; the ISA remains the source of truth for intent.

## 1. What the exploration was for

The design document lists the interaction and UI questions as entirely open (section 11): the cloud view, the passage view, the tree view, how the user moves between them, and the visual register. On the same day the primary use case was restated (ISC-44 to 46): a scenario is usually several tags across axes, and the user wants ranked counsel on that combination.

The exploration therefore had two jobs:

1. Put the three open views in front of Doug in enough contrasting forms that a reaction is possible before any code exists.
2. Take the newly decided primary use case and show how a multi-tag query could be built on a phone, using the reference apps in section 14 of the design document as the vocabulary.

It was not trying to choose. The screens are deliberately different from one another so the choice is visible, not so that one wins.

## 2. Method

**One session on every screen.** Every row walks the same meander: *conflict with a neighbor* → 15:1 → *anger* → 29:11 → a fork between 16:32 and 14:29. Holding the content fixed means a difference between two screens is a difference of design, not of example. The D row holds a second constant: the scenario *conflict with a neighbor + anger + neighbor (Role)*.

**Rows, not a flow.** Each visual direction is a row of three screens (cloud, passage, trail) rather than a tappable prototype. A prototype would have forced an early decision about navigation, which is itself one of the open questions. The screens link to one another only so the structure is visible.

**Constraints treated as hard.** The ISA's constraints shaped what could appear on a screen:

- *Nothing app-written on screen* (ISC-39). Every word on every mockup is scripture, a tag name, or a control label. No taglines, no summaries, no "this passage is about…", no empty-state copy that explains the book.
- *The passage is the focus.* The verse is always the largest type on the passage screen; connections are arranged around it, never above it.
- *Every link ordered by weight* (ISC-8, 13). Each passage screen shows a visible weight cue (dot darkness, border strength, bar fill) and states what the link shares.
- *The path is a true tree with elision* (ISC-14, 15). Each trail screen shows the fork as two children, marks the current node, and at least one (B) shows a collapsed segment.
- *Every curated tag in the cloud* (ISC-10). None of the cloud treatments hides tags; A scrolls, B maps, C ranks. D2 dims rather than hides.
- *Full matches before partial* (ISC-44). Both result treatments band the list, and every row shows which chosen tags it carries.
- *Suggestions are index tags, exclude what is chosen, ordered by relatedness* (ISC-45). Suggested tags are visibly distinct (dashed) and sit next to the thing they would extend.

**Reviewer demands honoured.** Large type and respect for the system font size are recurring one-star complaints in this category (design document, section 11). Verse text runs 27–36 pt on the passage screens; touch targets are 44 pt minimum; contrast was checked to 4.5:1 for body text and labels.

## 3. The three visual directions

The three registers come straight from the reference points in the design document's "Visual register" item. Each was pushed to its natural answer for all three views rather than mixed, so that the register and the interaction model could be judged together and apart.

### A · Typographic

*Reference: stoic., Stoa, Literal Word.* Warm white, Source Serif 4 for anything that is text or a tag, Inter for controls, one muted indigo for the thing currently on the trail.

- **Cloud as a weighted word list grouped by axis.** The word-map idea taken literally: tags are words, sized by weight, under small-caps axis headers. Density is solved by scrolling. The cost is that the cloud reads as an index, not a map; the gain is that it degrades gracefully to any tag count and any system font size.
- **Passage as a reading page.** Reference above, version below, tags as chips, linked passages as a ruled list with the shared tag named per row. The most conventional of the three, chosen so that the other two have a baseline.
- **Trail as an indented tree with a left rail.** The fork appears as two siblings under 29:11. Simple to render at any depth; elision would be a collapsed row, not shown here.

### B · Dark devotional

*Reference: Dwell, Lectio 365; Mindly 2 and Obsidian's graph for the cloud; Terminology for the passage.* Dark ground, Fraunces, amber for the trail.

- **Cloud as a clustered map.** Tags as pills inside faint axis rings, weight as pill size and border strength, axis chips to filter. This is the ISA's "cloud" most literally. It is also the treatment most at risk from density: the mockup shows about thirty tags; the real vocabulary will be several times that, and the filter chips are the proposed escape.
- **Passage as a conversation.** The speech-bubble option named in the design document, made concrete: the verse is the central bubble, linked passages are replies beneath it in weight order, tags sit above. The arrangement makes "connections around the passage" spatial rather than listed.
- **Trail as a pulled-up panel.** The tree is drawn as a real branch (lines and nodes) over the dimmed map, so the user never fully leaves the cloud. This answers "persistent surface or pulled-up panel" with the panel; A and C answer with a surface.

### C · Card

*Reference: the Wisdom Deck card; Safari History for the trail list.* Near-black, Newsreader, a single muted green.

- **Cloud as a ranked list with weight bars.** The least "cloud-like" and the most honest about density: every tag is a row with its axis, passage count and a bar. Sortable. Nothing is hidden and nothing is spatial.
- **Passage as one card.** One verse at 36 pt on a card with note, tag and group actions on the card itself; threads to follow are smaller cards beneath. Closest to the deck Doug already uses.
- **Trail as a stack of steps.** Numbered cards; the fork becomes two half-width cards side by side labelled 5a and 5b. Elision would be a collapsed card.

## 4. The D row: composing a scenario

The restated primary use case (ISC-44) arrived after the first three rows were drawn, so it got its own row rather than being retrofitted. The four screens each borrow a pattern from section 14 of the design document and keep the visual register of one of A, B or C so they can be slotted into a row later.

| Screen | Pattern borrowed | Register | What it tests |
|---|---|---|---|
| D1 Search-first | Apple Photos search, Things | A | Chips accumulate in one field; suggestions in a row beneath; results directly below in two bands with per-row dots for the chosen tags. Fastest when the user already knows the words. |
| D2 Pick in the cloud | Bear tag intersection | B | The cloud stays the surface. Chosen tags fill solid, suggested get a dashed outline, tags sharing no passages with the set go dim. A composer panel shows the count before committing. |
| D3 One axis at a time | Mela, Paprika, Reminders smart lists | C | A card per axis; suggestions inside the axis they belong to; empty axes collapse to "Any". The count bar previews the full-versus-partial split. Slowest, but the axis structure becomes the teaching surface. |
| D4 Results | WebMD Symptom Checker, Ada | C | The "why it matched" view: each card wears the chosen tags it carries; the missing one is struck through in the partial band; a suggestion sits at the band boundary where widening is most tempting. |

Two deliberate choices in D:

- **Suggestions are placed where they extend something**, not in a global tray: beside the field (D1), in the cloud (D2), inside the axis (D3), at the band boundary (D4). The hypothesis is that a suggestion is only useful at the moment the user is deciding whether the scenario is wide enough.
- **Partial matches are shown, not hidden**, and the missing tag is named per row ("not neighbor"). ISC-44 requires the banding; naming the gap is an addition, on the theory that a partial match is only useful if the user can see what it lacks.

## 5. Assumptions made to draw anything

These are not decisions and should not be read back into the ISA.

- **Verse text.** BSB wording was typed from memory for 15:1, 15:18, 29:11, 14:29, 16:32, 25:15, 24:28–29, 3:29–30 and 25:8–9. It must be checked against the shipped USFM before any screen is reused. The reference `24:29` is shown as a passage on its own in D4 and as `24:28–29` in D1; passage boundaries are the builder's to set.
- **Tag vocabulary.** Tag names are taken from the example values in the axis table. "self-control" stands in for "exercises self-control"; "conflict" is used as a short form on result cards. Whether tags have short forms is open.
- **Counts and weights.** "61 passages", "3 carry all three", weight bars and dot darkness are illustrative. No index exists yet.
- **Which tags the scenario passages carry.** The claim that 24:28–29, 3:29–30 and 25:8–9 carry all three of *conflict with a neighbor*, *anger* and *neighbor* is a guess at what the categorization would say, chosen to make the bands visible.
- **Controls for later features.** The axis filter chips (B), the "What's going on?" microphone button (C), "Save as context group" (D) and the "+ tag" chip are placed for position only. Situation-to-tags is marked later in the ISA; saving a scenario as a context group is not in the ISA at all.
- **Session metadata.** "Expires in 30 days", "Today, 3:42 PM" and "8 steps" are placeholders for the configurable thresholds.
- **No status bar.** The mockups omit the iOS status bar and Dynamic Island on purpose; they are 390 × 844 content areas, not device frames.
- **Liquid Glass.** The design document fixes Liquid Glass as the one design system (iOS 27 floor). None of the mockups attempts it; they are register studies, and the glass treatment of bars, sheets and chips is a separate pass once a register is chosen.

## 6. What the screens raise but cannot settle

Each of these needs a decision or a prototype, not another mockup.

1. **Hide or dim.** D2 dims tags that share no passages with the chosen set. Hiding them is cleaner and is what Bear does, but violates ISC-10 as written. Either the criterion allows a filtered cloud, or dimming is the rule.
2. **Order within a band.** ISC-44 fixes only that full matches precede partial. Within a band the mockups assume link weight; book order and "how many chosen tags" are the alternatives. The choice is invisible until the index exists.
3. **Saving a scenario.** "Save as context group" on a results screen makes the scenario the front door to context groups. That may be right (a context group *is* an ongoing situation) or may blur the two kinds of groups the ISA keeps distinct.
4. **Tree as surface or panel.** B's panel keeps the cloud visible; A and C make the trail a destination. The difference is how often the user is reminded there is a fork to return to.
5. **Cloud density.** A scrolls, B maps, C ranks. Only a prototype with the full tag count will show which survives. B is the most attractive and the most at risk.
6. **Short forms for tags.** Result cards need something shorter than "conflict with a neighbor". Either tags carry a short form in the index or the card design changes.
7. **iPad.** Nothing here is an iPad layout. The composer-beside-results and cloud-beside-passage arrangements are the obvious candidates and were left for a second pass.

## 7. Provenance and how to regenerate

- Drawn in Claude's design canvas on 2026-11-02 from the design document of the same date, against the reference apps listed in its section 14. The canvas remains editable; the HTML page is a snapshot of it.
- Sizes: 390 × 844 per screen. Fonts: Inter (controls); Source Serif 4 (A); Fraunces (B); Newsreader (C), all loaded from Google Fonts. Colours: A `#FBFAF7` ground / `#1C1B19` ink / `#3A4A8C` accent; B `#14151A` / `#ECE8DF` / `#D8A657`; C `#0E0E10` / `#F2EFE8` / `#7FB7A6`.
- Links between screens in the HTML page are in-page jumps; in the canvas they are prototype links.
- To regenerate after revising the canvas: ask for the HTML presentation to be rebuilt from the current canvas. The build strips each screen's markup from its canvas file and inlines it; nothing is hand-copied.

## 8. Suggested next step

Pick one register (or name the pieces to take from each) and one composition pattern from D, then carry that pair through all four views as a single tappable prototype, with the full tag vocabulary in the cloud. That prototype, not another set of alternatives, is what will answer items 1, 4 and 5 above.

Related notes: [[Ideal State]], [[Get Wisdom Design Document]], [[UX Pattern Research]], [[Wisdom Deck Reference]], [[Categorization Scheme]], [[Idea Backlog]].
