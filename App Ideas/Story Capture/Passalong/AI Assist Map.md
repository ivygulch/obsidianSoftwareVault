---
type: design
area: Story Capture
tags: [passalong, ai, foundation-models, brainstorm, roadmap]
created: 2026-07-13
updated: 2026-07-13
status: brainstorm
---

# Passalong — AI Assist Map (brainstorm)

> Brainstorm (2026-07-13) of AI assistance across every phase, using on-device and cloud models as each job warrants. Raw material to prune — ★ marks the entries judged strongest; ⚠ marks ones with real tension against product values. Grounded in the [[../../../Research/Tech/iOS 26 Features Relevant to App Ideas|iOS 26]] / [[../../../Research/Tech/iOS 27 Features Relevant to App Ideas|iOS 27]] research (SpeechAnalyzer, Foundation Models gen-2 with image inputs, Private Cloud Compute, provider protocol).

## Governing principle

**AI prepares, assists, and drafts; humans ask, tell, and decide.** The asker's voice, the storyteller's words, and the curator's judgment are the product — AI output is always a suggestion or draft, never auto-published, and never rewrites what a person said. (Sibling of the dictation-is-not-a-product criterion: if a feature's value reduces to "the model does the family's part," kill it.)

## Preparation phase

- ★ **Material ingestion → focused question lists** (Doug's seed idea): feed it emails, letters, notes, scans of photos/documents/memorabilia; get back a focused question list with the supporting material already attached to each question. iOS 27 image inputs read scans directly; Vision `RecognizeDocumentsRequest` structures documents. Privacy posture: ingestion runs on-device; derived questions are stored, **source material is not retained** (data minimization — the letter stays in Mail, only "ask about the 1962 letter from Ray" persists with a thumbnail).
- ★ **Archive gap analysis**: build a coverage map of the storyteller's life from existing stories (timeline, people, places, themes) and propose questions targeting the blanks — "nothing yet about 1958–1964, nothing about her sister." Turns the archive itself into the prompt engine; gets better every visit.
- ★ **Question craft coaching**: rewrite yes/no questions into story-eliciting ones ("Did you like the Navy?" → "Tell me about your first day aboard"); flag questions that will get one-word answers. Oral-history craft, encoded — this augments the human-authored prompt packs, not replaces them.
- **Asker-fit rewording**: same question phrased for the 7-year-old vs. the 16-year-old to read aloud naturally.
- **Photo-driven prompts**: point at an album; model proposes "ask about this photo" questions (iOS 27 image inputs; already noted on the idea page).
- **Queue dedup/merge suggestions**: three family members queued variations of the same question — propose a merge, keep all askers attached (`QuestionAsker` rows make this clean).
- **Occasion planning**: "90th birthday, ~45 minutes, three grandkids" → proposed session plan from the queue (order, timing, who asks what). Suggestion only; the printable sheet is the output.

## During the session (⚠ the device-recedes principle governs everything here)

- ★ **Auto-noting**: the live transcript stream yields provisional, timestamped entity notes — "12:34 mentions Uncle Ray," names, places, dates — without anyone lifting a pen. The curator's raw material accumulates silently; nothing surfaces during the session itself. This is the least intrusive and highest-value in-session assist because it has *no* in-session UI.
- **Follow-up nudge at the turn boundary** ★⚠ (refined 2026-07-13; Doug: "intriguing, but only if done well"): the *during-story* whisper is killed — a suggestion arriving mid-story pulls the asker's eyes down while Grandma talks, and no implementation quality fixes that. The surviving version surfaces at the **between-stories moment**, when the asker is already glancing at the screen to pick the next question: "before you move on — she mentioned the farm and moved past it." Done-well bar: one suggestion, glanceable, phrased as an observation not a script (the AI points, the human words the question); pull not push (no animation/badge, possibly behind an explicit "what else could I ask?" tap); silent when confidence is low; never on storyteller-visible surfaces (excluded from selfie mode's shared screen). Beta kill-test: if askers' eye-contact pattern changes or the room notices the phone more, the feature dies regardless of how smart it is.
- **Speaker attribution assist**: diarization proposes `StoryTeller` tags in multi-teller sessions (Grandma vs. Grandpa), confirmed by the curator afterward.
- **Contextual photo surfacing** ⚠ (far roadmap, prompter-display role only): Grandma mentions the lake house; the iPad quietly surfaces the lake-house photo. Magical when right, derailing when wrong; needs an indexed family photo set and an on-device-only pipeline. Park it.

## After the session

- ★★ **Family-lexicon transcript repair** — the single strongest AI feature available to this product: SpeechAnalyzer has no custom vocabulary (iOS 26 finding), so family names *will* misrecognize; an on-device model pass that corrects the transcript against the space's `Person` names and recurring places/terms directly answers the #1 transcription complaint in the review mining (Remento's name-mangling), stays fully on-device, and compounds as the family lexicon grows. Correction suggestions are tracked, reversible, and never touch the audio.
- ★ **Story titling, summaries, chapter markers, topic tags**: every story gets a human-editable title/summary; entity extraction cross-links the archive ("every story mentioning Uncle Ray") — which is also what makes gap analysis (above) possible.
- ★ **Teaser extraction**: identify the 30-second heart of an answer as the shareable notification payload — "Grandpa answered your question" with the best moment attached drives far-family listening, which drives the flywheel.
- **Follow-up generation**: from each answer, propose next-visit questions ("he mentioned a storm at sea and moved on — ask about it") straight into the prep queue. Closes the loop between phases.
- **Unfinished-thread detection**: stories that trail off or defer ("that's a story for another day") get flagged so the promise is kept.

## Curation & artifacts

- ★ **Text-based edit assist**: propose clip boundaries from the transcript (remove crosstalk, dead air, false starts) as *suggestions* on the non-destructive `CompilationItem` layer; select-sentences-get-clips stays the interaction, model pre-proposes the selects.
- **Compilation drafting**: cluster stories by theme ("the Navy years"), propose a running order and chapter structure for the memory archive; curator rearranges and approves.
- **Best-frame extraction**: pull the photo-quality stills from video sessions (Vision) for the book/PDF rungs of the artifact ladder.
- **Artifact assembly assist** ⚠: layout the PDF/book draft from curated content — formatting yes; **prose rewriting no**. The moment the model "improves" Grandpa's words into smoother text, the faithful-transcription promise is broken in print. Format the voice; never ghostwrite it.

## Explicitly not doing (standing exclusions, restated for AI scope)

- No voice cloning of anyone, living or deceased (Forevermore's Echo territory).
- No AI interviewer replacing the human asker in v1's loop (the kid is the interface; a model asking Grandpa questions inverts the product's purpose). Remote-mode may revisit an *assist* role someday; the bar is high.
- No training on family data, ever — already the ownership promise; applies to every feature above.
- No auto-publish: every AI output lands as a draft or suggestion attributed to "suggested," awaiting a human yes.

## Capability tiers (from the iOS 26/27 research)

| Tier | Runs | Fits |
|---|---|---|
| On-device Foundation Models (iPhone 15 Pro+/M-series) | free, offline, private | lexicon repair, titling/tagging, question coaching, auto-noting, follow-ups |
| Private Cloud Compute (iOS 27) | bigger model, 32K context, no-retention guarantees | whole-archive gap analysis, compilation drafting, big ingestion jobs — **positioning decision required** ("on-device only" vs. "plus Apple's private cloud") before App Store copy |
| Third-party providers (via the iOS 27 provider protocol) | most capable | probably never — hard to reconcile with the ownership story; the protocol seam keeps the option technically open at zero cost |

**Hardware reality check:** every AI feature is progressive enhancement — the app is fully functional with none of them (older devices, Apple Intelligence off, model unavailable). The AI seam is a protocol behind which tiers are configuration (already an Android-later guardrail; now doing double duty).

## Related
- [[Passalong]] — product intent and standing exclusions these respect
- [[UX Flows]] — the phases this map decorates
- [[../../../Research/Tech/iOS 27 Features Relevant to App Ideas]] — Foundation Models gen-2, PCC, provider protocol
