---
type: isa
project: Proverbs
status: building
criteria_open: 40
criteria_done: 0
created: 2026-10-26
updated: 2026-10-26
---

# Proverbs — Ideal State

> This document is the source of truth for what the project is for. Code is one implementation of it. When code and this document disagree, this document wins: fix the code, or change this document and record why under Decisions. Method: [[Craft/Ideal State Method/Method|Ideal State Method]]. Idea and research: [[Applying Proverbs]].
>
> **status** values: `drafting` (Ideal State still being written) · `building` (criteria exist, code in progress) · `checking` (a build exists, evals running) · `shipped` · `shelved`.

## Ideal State

Proverbs is how I find what the book says about what is happening in my life, by following the book's structure instead of reading it in chapter order. I open the app to a cloud of tags, a word map of the categories and keywords the book has been given. I pick the one that looks closest to what I am dealing with and it shows me its passages. From any passage, links lead outward to other passages and other tags, and the links are weighted, so the ones that belong together in sense stand out from the ones that merely share a word. How that weight is decided is not yet settled. I follow one, then another. The path I take is kept as a tree I can see and move back along, so a detour is never lost: I return to a fork and take the other branch. It works the way a wiki about one book would, if the book had been linked by someone who knows it. If a friend asks, it is Proverbs linked up like a wiki: you start from whatever you are dealing with, follow the threads, and keep the trail.

The passage is the focus. When one is selected it is shown in full, in the text's own words with its reference, and its connections are arranged around it. A speech-bubble look is one option for that arrangement; the exact UI is undecided. Nothing on the screen is written by the app. The words are the text, the tags, and my own notes. The app finds and arranges; it never interprets. My own application notes and the public-domain commentaries belong to a later layer, one level below the passage, and are not part of finding.

Clouds are the one kind of document in the app. The default cloud is the whole book. A named session is a cloud. A curated group is a cloud. A context group is a cloud. They differ in where they came from, not in what they are. Each time I meander, the session is kept automatically with its date and time, so nothing is lost, but the next session starts again from the default cloud unless I gave the previous one a name. A named session persists as a trail I can come back to and can attach to a context group. The unnamed ones are findable later in a list by date and time, each row showing the tags and passages it touched, and from there one can be named or attached to a group.

Groups come in two kinds, kept distinct. Curated groups ship with the book; I build them, along with the tags and categories, across the whole book before launch, and that curated layer is the product. Context groups are mine as a user: a person, an ongoing situation, a project, holding the passages, notes, and trails that belong to it. The first user the curated layer has to satisfy is me, in my own situations.

The text is the ESV if Crossway's terms allow it, and otherwise the Berean Standard Bible or another freely available text. One possibility for later is a separate prebuilt cloud whose tags come from the original Hebrew words and phrases rather than from English categories.

My own marks sit on top of the curated layer without damaging it. I tag passages with my own tags. I write notes on passages, on trails, and on the predefined tags themselves. I can override the curated tagging of a specific passage, removing a tag from it or adding a different predefined tag to it, and a filter lets me switch my overrides off for a while to see the book as shipped. All of it follows me to another iPhone or an iPad through iCloud, and the app works in full when iCloud is unavailable. Everything in the finding experience works with no network: the text, the cloud, the links, the sessions and trails, my notes and groups.

Besides picking a tag, I can type or speak what is going on and the app suggests tags to start from. It does this on the device and never writes a sentence back; it is a second door into the cloud, and it comes after the cloud itself.

When the curated layer is revised in a later version, the new curated groups take precedence, and the old ones are archived and still reachable somewhere unobtrusive such as a setting. My own tags, notes, and overrides survive the update untouched; an override on a tag that no longer exists simply stops applying.

The first run is a short sequence of screens that walks me through picking a tag and following a trail. Every screen has a box to skip it, and a setting resets the sequence so it can be seen again. Mostly I come to the app when something is happening, but a tag or a cloud can be asked to remind me: it generates local notifications on a schedule, each carrying a passage's text, and tapping one opens that passage inside the tag's or cloud's map. My overrides apply whenever I use the app; the filter shows the as-shipped view only while it is on.

A year on, I have a handful of named trails and context groups I return to, a cloud shaped by a year of my own tags and notes, and the habit of reaching for the app when something is happening rather than searching the web. Clouds and notes can be shared with another person, who receives a copy they own and can mark up, not a live link back to mine. Further out, the same approach could extend beyond Proverbs, with other books arriving as additional clouds inside the same app, each with its own curated layer, but only after finding out from users what works well here.

## Constraints

- No AI paraphrasing of the text, ever.
- No biblical text that is not in the shipped text. Nothing generated, nothing hallucinated.
- The app never interprets. Application notes and commentaries sit below the passage, never in the finding path.
- The finding experience works fully offline.
- Curated groups and the user's context groups are distinct kinds and never merge.
- User overrides of curated tagging never alter the curated data; they can always be switched off by a filter.
- Notifications exist only where the user asked for them on a tag or cloud. None by default.
- No book beyond Proverbs until the Proverbs cloud has shown what works for users.
- Suggesting tags from a described situation happens on device and never produces prose.
- Superseded curated groups are archived, never deleted.
- A curated update never alters or removes the user's tags, notes, or overrides.
- Sharing hands over a copy; nothing shared stays linked to the sender.

## Decisions

- 2026-10-26 — Promoted from `App Ideas/Miscellaneous/Applying Proverbs` to `Projects/Proverbs`; ISA created. The initial use case is following tags through the book's structure with the path kept as a backtrackable tree, rather than free-text situation search as in the idea note's one-liner. Decided in `/isa-discuss` round 1.

## Criteria

_Ideal State Criteria (ISCs): atomic, testable, each with its own eval. Together they are the build target and the test harness. Numbered in order of creation; never renumbered; dropped ones stay in place with status `dropped`. Derived with `/isa-criteria`, checked with `/isa-check`._

_**Eval level**, cheapest first: `assert` (a unit or UI test in the code) · `check` (a scripted multi-step: build, run, capture, compare) · `questions` (a fixed yes/no set answered by a fast model or by eye against a screenshot or output; all must be yes) · `judge` (a written rubric with a pass bar, graded by a stronger model or by Doug). Use the cheapest level that can actually fail._

_**Status** values: `open` · `done` · `dropped`. **Scope** is optional: `v1`, `later`, or a version tag._

### ISC-1 — Complete text
- **Criterion:** All 31 chapters and 915 verses of Proverbs are present in the shipped text.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_1_textIsComplete` (missing), data target; asserts chapter count 31 and verse count 915.
- **Status:** open
- **Last checked:** —

### ISC-2 — Verbatim rendering
- **Criterion:** Every passage string the app displays equals the shipped text for that reference, character for character.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_2_renderedTextIsVerbatim` (missing); renders every passage through the view model and compares to the data file. Covers the no-paraphrase and no-generated-text constraints.
- **Status:** open
- **Last checked:** —

### ISC-3 — Only Proverbs ships
- **Criterion:** The bundled data contains no book other than Proverbs.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_3_onlyProverbsShipped` (missing); asserts the set of book identifiers in the bundle is exactly Proverbs.
- **Status:** open
- **Last checked:** —

### ISC-4 — Passages cover the book
- **Criterion:** Every verse is covered by a passage. A verse belongs to one passage, except a verse marked as split, which belongs to exactly two adjacent passages, one taking its beginning and the other its end. No verse part is uncovered or covered twice.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_4_passagesCoverBook` (missing); asserts full coverage, at most two passages per verse, and an explicit split marker on every shared verse.
- **Status:** open
- **Last checked:** —

### ISC-5 — Whole book tagged
- **Criterion:** Every passage carries at least one curated tag.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_5_everyPassageTagged` (missing).
- **Status:** open
- **Last checked:** —

### ISC-6 — No dead ends
- **Criterion:** Every passage has at least one link to another passage or to a tag, so no passage is a dead end in the meander.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_6_noPassageIsADeadEnd` (missing).
- **Status:** open
- **Last checked:** —

### ISC-7 — Links are weighted
- **Criterion:** Every link carries a weight, and links on a passage are presented in descending weight order.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_7_linksOrderedByWeight` (missing). The weighting method is unsettled in the ISA; this tests only that weights exist and the order holds.
- **Status:** open
- **Last checked:** —

### ISC-8 — Curated groups are read-only
- **Criterion:** Curated groups ship in the bundle and cannot be created, renamed, or edited in the app.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_8_curatedGroupsReadOnly` (missing); asserts the model exposes no mutation path for curated groups and the bundle count is unchanged after a user session.
- **Status:** open
- **Last checked:** —

### ISC-9 — Opens to the default cloud
- **Criterion:** After onboarding is complete or skipped, launching the app lands on the default cloud, not on a list or a menu.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_9_launchLandsOnDefaultCloud` (missing); asserts the root state after launch is the default cloud.
- **Status:** open
- **Last checked:** —

### ISC-10 — Default cloud is complete
- **Criterion:** The default cloud contains every curated tag and category, none missing, none extra.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_10_defaultCloudHasEveryTag` (missing); set equality between cloud nodes and curated tags.
- **Status:** open
- **Last checked:** —

### ISC-11 — A tag shows its passages
- **Criterion:** Selecting a tag lists exactly the passages that carry it, with the user's overrides applied.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_11_tagListsItsPassages` (missing); for a sample of tags, the listed set equals the data set after overrides.
- **Status:** open
- **Last checked:** —

### ISC-12 — Passage view shows the reference
- **Criterion:** A selected passage is shown with its reference and its whole text, never truncated.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_12_passageViewShowsReferenceAndFullText` (missing); view model carries the reference string and the whole passage text for every passage.
- **Status:** open
- **Last checked:** —

### ISC-13 — Passage view shows its connections
- **Criterion:** The passage screen presents all of that passage's links, both to passages and to tags.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_13_passageViewExposesAllLinks` (missing); view model link set equals the data link set for a sample of passages.
- **Status:** open
- **Last checked:** —

### ISC-14 — The path is a tree
- **Criterion:** The session path is a tree. Going A to B to C, back to B, then to D gives B two children, C and D. Revisiting a tag or passage already on the path adds a new node carrying the same data; the tree never contains a cycle or a shared node.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_14_sessionPathIsATree` (missing); builds that sequence plus a revisit of A on the session model and asserts the tree shape, two children at B, a fresh node for the revisit, and no cycles.
- **Status:** open
- **Last checked:** —

### ISC-15 — Tree is visible with elision
- **Criterion:** The session tree can be viewed; when it is too long for the screen, nodes are elided with a way to reveal them, and every node stays reachable by tap. What to do when the tree grows very large is open and not tested here.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_15_treeViewElidesAndReachesEveryNode` (missing).
- **Status:** open
- **Last checked:** —

### ISC-16 — Every step persists
- **Criterion:** Each navigation step is saved at once under the current session; killing the app loses no step. Session boundaries are the ISC-17 thresholds.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_16_stepPersistsImmediately` (missing); reload after each step and compare.
- **Status:** open
- **Last checked:** —

### ISC-17 — Return thresholds
- **Criterion:** Two internally configurable thresholds. Returning under the first resumes in place with no prompt; between them, the app asks whether to resume; beyond both, a new session starts at the default cloud and the old one stays findable.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_17_returnBehaviorByThreshold` (missing); three cases with an injected clock.
- **Status:** open
- **Last checked:** —

### ISC-18 — Naming makes a trail
- **Criterion:** Naming a session keeps it as a trail that can be reopened by name.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_18_namedSessionReopens` (missing).
- **Status:** open
- **Last checked:** —

### ISC-19 — Trail attaches to a group
- **Criterion:** A named trail can be attached to a context group and appears in it.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_19_trailAttachesToContextGroup` (missing).
- **Status:** open
- **Last checked:** —

### ISC-20 — Old sessions are findable
- **Criterion:** Unnamed sessions appear in a list by date and time, each row showing the tags and passages it touched, and from a row the session can be named or attached to a group.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_20_sessionListRowsAndActions` (missing).
- **Status:** open
- **Last checked:** —

### ISC-21 — One document type
- **Criterion:** The default cloud, a named session, a curated group, and a context group are all the same cloud type and open in the same cloud view.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_21_allFourOriginsAreClouds` (missing); each conforms to the cloud model and the cloud view accepts each.
- **Status:** open
- **Last checked:** —

### ISC-22 — Group kinds never merge
- **Criterion:** A curated group cannot become a context group and a context group cannot become curated; each is created only by its own origin. A context group may reference a curated group.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_22_groupKindsAreDistinct` (missing); also asserts a context group can hold a reference to a curated group without copying or mutating it.
- **Status:** open
- **Last checked:** —

### ISC-23 — Unnamed sessions expire
- **Criterion:** Unnamed sessions older than a configurable age are removed from the list and from storage; named ones never expire.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_23_unnamedSessionsExpire` (missing).
- **Status:** open
- **Last checked:** —

### ISC-24 — Own tags on passages
- **Criterion:** The user can add their own tag to any passage and it shows in the cloud and on the passage.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_24_userTagOnPassage` (missing).
- **Status:** open
- **Last checked:** —

### ISC-25 — Notes in three places
- **Criterion:** A note can be attached to a passage, to a trail, and to a predefined tag, and each shows where it was attached.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_25_notesAttachToPassageTrailAndTag` (missing); one assertion per place.
- **Status:** open
- **Last checked:** —

### ISC-26 — Override a passage's tags
- **Criterion:** On a specific passage the user can remove a curated tag and add a different predefined tag, and the cloud and tag lists reflect it.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_26_overrideRemovesAndAddsTag` (missing).
- **Status:** open
- **Last checked:** —

### ISC-27 — Curated data untouched
- **Criterion:** After any set of overrides, the bundled curated data is byte-identical to shipped.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_27_overridesLeaveCuratedDataIntact` (missing); hash before and after.
- **Status:** open
- **Last checked:** —

### ISC-28 — Override filter
- **Criterion:** Overrides apply by default; a filter switches them off to show the as-shipped tagging and back on again.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_28_overrideFilterTogglesView` (missing).
- **Status:** open
- **Last checked:** —

### ISC-29 — Follows me across devices
- **Criterion:** Tags, notes, groups, sessions, and trails made on one device appear on another signed into the same iCloud account.
- **Scope:** v1
- **Eval level:** check
- **Eval:** 1. On device or simulator A, create one user tag, one note, one context group, one named trail. 2. Launch on B with the same account; wait for sync. 3. Capture screenshots of the cloud and the group on both. 4. Pass if all four items appear on B. Likely run by Doug.
- **Status:** open
- **Last checked:** —

### ISC-30 — Works without iCloud
- **Criterion:** With iCloud unavailable, every feature in ISC-9 through ISC-28 still works locally.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_30_fullFunctionWithoutCloud` (missing); sync dependency injected as unavailable, the ISC-9 to ISC-28 tests rerun.
- **Status:** open
- **Last checked:** —

### ISC-31 — Fully offline
- **Criterion:** With no network at all, finding, sessions, notes, and groups all work.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_31_findingWorksOffline` (missing); network dependency injected as failing.
- **Status:** open
- **Last checked:** —

### ISC-32 — Situation to tags, on device
- **Criterion:** Typing or speaking a situation returns a list of existing tags to start from, computed on device, with no prose in the result.
- **Scope:** later
- **Eval level:** assert
- **Eval:** `ISC_32_situationReturnsOnlyTags` (missing); result type is tags only and no network dependency is touched.
- **Status:** open
- **Last checked:** —

### ISC-33 — Curated update precedence
- **Criterion:** After a curated update, the new groups and tags are what the cloud shows, and the superseded groups are reachable from a setting, never deleted.
- **Scope:** later
- **Eval level:** assert
- **Eval:** `ISC_33_curatedUpdateArchivesOld` (missing); migrate a fixture from v1 data to v2 data.
- **Status:** open
- **Last checked:** —

### ISC-34 — User marks survive an update
- **Criterion:** After a curated update, every user tag, note, and override is unchanged, and an override on a removed tag no longer applies without error.
- **Scope:** later
- **Eval level:** assert
- **Eval:** `ISC_34_userMarksSurviveUpdate` (missing).
- **Status:** open
- **Last checked:** —

### ISC-35 — First-run sequence
- **Criterion:** On first launch a short sequence walks through picking a tag and following a trail; every screen has a skip box; a setting resets the sequence.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_35_onboardingSkipAndReset` (missing); first launch shows it, skip ends it, reset shows it again.
- **Status:** open
- **Last checked:** —

### ISC-36 — Reminders are opt-in
- **Criterion:** No notification is scheduled until the user asks for one on a specific tag or cloud.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_36_noNotificationsByDefault` (missing); after fresh install and a session, scheduled count is zero.
- **Status:** open
- **Last checked:** —

### ISC-37 — Reminder carries the passage
- **Criterion:** A scheduled reminder's notification body is a passage's verbatim text from the tag or cloud it was set on, and tapping it opens that passage inside that tag's or cloud's map.
- **Scope:** v1
- **Eval level:** check
- **Eval:** `ISC_37_reminderBodyIsPassage` (missing) asserts the body. Then in the simulator: 1. Set a reminder on a tag. 2. Deliver the notification. 3. Tap it. 4. Screenshot the landing screen; pass if it is that passage inside that tag's map.
- **Status:** open
- **Last checked:** —

### ISC-38 — Sharing hands over a copy
- **Criterion:** A cloud or note can be exported; importing it on another account yields an owned, editable copy with no reference back to the sender.
- **Scope:** v1
- **Eval level:** assert
- **Eval:** `ISC_38_importedShareIsIndependentCopy` (missing); export, import, mutate the copy, assert the original is unchanged and the copy holds no sender identifier.
- **Status:** open
- **Last checked:** —

### ISC-39 — Nothing app-written on screen
- **Criterion:** On the cloud, tag, passage, tree, and group screens, every sentence is scripture, a tag name, a user note, or a fixed UI label.
- **Scope:** v1
- **Eval level:** questions
- **Eval:** Against screenshots of the five screens. 1. Is every sentence on screen scripture, a tag name, a user note, or a fixed UI label? (yes) 2. Is there any explanation, summary, or application of a passage written by the app? (no) 3. Is there any text not in the shipped data, the user's data, or the UI strings file? (no)
- **Status:** open
- **Last checked:** —

### ISC-40 — Interpretation sits below
- **Criterion:** Application notes and commentaries, when present, are reached from a passage by a deliberate step down and never appear in the cloud, tag, or tree views.
- **Scope:** later
- **Eval level:** questions
- **Eval:** Against the ISC-39 screenshots plus the passage screen. 1. Is any commentary visible without a tap? (no) 2. Does the finding path contain any interpretive text? (no)
- **Status:** open
- **Last checked:** —
