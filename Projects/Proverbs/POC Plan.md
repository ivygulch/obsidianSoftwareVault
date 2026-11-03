---
type: plan
project: Proverbs
status: proposed
created: 2026-11-03
updated: 2026-11-03
---

# Get Wisdom — Plan to a POC

Proposed 2026-11-03 in answer to "should the first step be a POC with all the screens and minimal behavior, for target users?" The answer is no: the product is the curated index, and nothing in the vault yet shows that the index returns satisfying passages for real scenarios. A nine-screen POC tests the shell before the thing inside it exists. The steps below put the data first, test retrieval without an app, and reach the full-screen POC as step 6. Steps 1 to 3 are the Exploration Plan's Phase 2 scheme test, which was never run, reshaped around the primary use case decided 2026-11-02 (a scenario is several tags across axes, ISC-44). Intent stays in [[Ideal State]]; this note is sequencing only.

## The steps

| # | Step | Needs code | Produces | Gate |
|---|---|---|---|---|
| 1 | Write 20 real scenarios | No | The test set for every later step | — |
| 2 | Hand-tag a slice of the book | No | The fixture: tagged passages with real BSB text, weights, a tag vocabulary | Axis questions answered by contact with the text |
| 3 | Run the retrieval test on paper | No | Scores for 20 scenarios under ISC-44 banding | Fewer than 12 of 20 satisfying is a stop |
| 4 | Pick one register and one composition pattern | No | A decision in the Design note | — |
| 5 | Thin prototype of the primary path | Throwaway SwiftUI | Composer, results, passage, one link hop, on the fixture; three to five target users | Do they compose multi-tag scenarios, does the top band satisfy, do they follow a link |
| 6 | Full-screen POC with minimal behavior | Throwaway or scaffold | Trail tree, sessions list, context groups, settings, onboarding | Hide versus dim; tree as surface versus panel; cloud density at full tag count |
| 7 | Schema and builder | Production | Curated SQLite schema, cloud JSON format, builder authoring surface, app scaffold | Vocabulary has stopped moving |

### 1. Write 20 real scenarios

Doug's own, since the first user the curated layer has to satisfy is Doug. Each is one sentence the way a user would say it, plus the tags Doug would expect it to need, across axes. Ten should be answerable from the chapters tagged in step 2 and ten should not, to catch false hits (from the Exploration Plan). Cost: about an hour.

Template, one row per scenario:

| # | Scenario, as a user would say it | Expected tags (axis: value) | Answerable from the slice? | Passages I already know should appear |
|---|---|---|---|---|
| 1 | | | yes / no | |

### 2. Hand-tag a slice of the book

Chapter 10 (32 two-line sayings) and chapter 3 (discourse), as the Exploration Plan proposed, plus whichever passages the 20 scenarios obviously reach elsewhere in the book. In a spreadsheet, not the builder; the builder is on the critical path for the whole book, not for a slice. Text is the BSB from the USFM download (see [[BSB Download Formats]]), copied verse by verse, so the fixture is the first place the real text is used. The v1 design explorations typed their verses from memory.

Columns for the passage sheet:

| Column | Content |
|---|---|
| passage_id | Stable id, for example `10.01` or `03.05-06` |
| reference | Display reference, for example `Proverbs 3:5–6` |
| start_verse, end_verse | Verse numbers; a split verse gets a `start_part` or `end_part` of `a` or `b` |
| text | BSB text, verbatim, line breaks kept |
| situation, attitude, characteristic, result, domain, role | One column per user-facing axis, values separated by `;` |
| form | Builder-only passage attribute (antithetical pair, better-than, numerical, instruction, warning, observation); never becomes a tag (ISA Decision 2026-11-03) |
| keywords | Free terms from the passage's own words and its sense |
| editorial_links | passage_ids this passage belongs with regardless of vocabulary (26:4 and 26:5; the repeated sayings) |
| time_minutes | Time spent on this passage, for the whole-book estimate |

Weights for automatic links are set by a rule for now, for example: shared axis value counts three, shared keyword counts one, editorial link counts five. The rule is a placeholder; the ISA leaves weighting open.

Record as you go: how many values each axis produced; how many passages carry more than one axis; where Domain and Situation wanted to be one axis; which tag names needed a short form on a card.

Done when: both chapters and every scenario-reached passage carry at least one value on at least one axis, every passage has at least one link, and the time estimate for 915 verses is written down.

### 3. Run the retrieval test on paper

For each of the 20 scenarios, compose the tag set and list what the slice returns: the passages carrying every tag first, then the ones carrying some, the banding ISC-44 fixes. Score each scenario: a satisfying passage in the top five, a weak one, or nothing. A week later, re-tag ten passages without looking at the first pass and compare; if a second reader who knows the book is available, have them tag the same ten blind.

Stop criteria, from the Exploration Plan: fewer than 12 of 20 scenarios satisfying; axes beyond topic each with under five values; re-tagging agreement under about 70 percent. Any of these means the differentiator does not hold and the idea reduces to a topical reader, which already exists at small scale.

Also record: how many scenarios were mostly full matches and how many were mostly partials. This decides step 4.

### 4. Pick one register and one composition pattern

From [[Design Explorations v1 — Rationale]], whose own closing note asks for this choice: one of the A, B, C registers (or named pieces from each) and one of the D1 to D3 composition patterns. Step 3 informs it: if results are mostly full matches, the results screen carries the weight and D4's "why it matched" view matters most; if mostly partials, the composer and its suggestions (ISC-45) carry the weight. Record the choice as a dated entry in [[Design]].

### 5. Thin prototype of the primary path

Composer, results, passage, one link hop. Nothing else: no sessions, no groups, no settings, no onboarding. A throwaway SwiftUI app reading the step 2 spreadsheet exported as JSON. One register. Real BSB text. Claude writes it under Doug's direction, per the working mode in [[Design]].

Put it in front of three to five target users who know the book. Watch for, without prompting: do they compose a scenario from more than one tag; does the top band satisfy them; do they follow a link from a passage. Each session produces a filled copy of the step 1 table with the user's own scenarios, which grows the test set.

This is the first user test worth running. It does not answer ordering within bands or link weighting; those wait for the real index.

### 6. Full-screen POC with minimal behavior

The nine surfaces the ISA implies: cloud, composer, results, passage, trail tree, sessions list, context groups, settings (override filter, suggestions on or off, reminders, reset onboarding), onboarding. Minimal behavior on each, built on what step 5 showed. Either extend the throwaway or build on the real scaffold; the choice depends on whether the vocabulary from step 2 has stopped moving.

The questions this POC exists to settle, from the v1 rationale's unsettled list: hide versus dim in the cloud (ISC-10 as written forbids hiding); tree as surface versus panel; whether the cloud survives the full tag count. The last needs the full vocabulary, which may mean tagging more chapters first or synthesizing a plausible full tag list from the slice.

### 7. Schema and builder

Turn the spreadsheet into the curated SQLite schema and the cloud JSON export format already decided in [[Design]]. Only then design the builder's authoring surface, against a vocabulary that has stopped moving; the Builder ISA is still at the drafting stage. Scaffold the production app (TCA26, SQLiteData, iOS 27, two packages, three targets) once the schema exists. The data-level ISC tests (1 to 8, 41 to 44) run against the produced file.

## What this plan does not decide

- Which version ships in the first release (BSB is the development text).
- Link weighting and ordering within result bands; both wait for the real index.
- Whether "save as context group" belongs on the results screen (raised by the v1 rationale; not in the ISA).
- Anything marked later in the ISA: situation-to-tags, curated updates, commentary layer.

## Related

- [[Ideal State]] — source of truth; ISC-44 to 46 are the criteria this plan tests first
- [[Get Wisdom Design Document]] — snapshot of decisions and open questions
- [[Design Explorations v1 — Rationale]] — the register and composition alternatives step 4 chooses between
- [[Exploration Plan]] — Phase 2 and 3, which steps 1 to 3 and 7 descend from
- [[Categorization Scheme]] — the axes the fixture columns follow
- [[Design]] — working mode, scaffold, and data decisions
