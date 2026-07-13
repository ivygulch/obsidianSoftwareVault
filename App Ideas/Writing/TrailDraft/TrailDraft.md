---
area: Writing
status: seed
tags: [app-idea, dictation, hiking, voice-control, writing-tools]
created: 2026-04-26
updated: 2026-04-26
---

# TrailDraft

_Working name — replace when the real branding lands._

**One-liner:** A purpose-built iOS dictation app for first-draft writing on the move, controlled entirely by voice and headset gestures so the phone stays in the pocket.

**Target user:** Writers who dictate first drafts during physical activity (hiking, walking, paddling) where touching a phone is friction or impossible.

**Problem:** Generic recording apps capture audio fine but require touching the screen to pause, review, restart, mark sections, or consult notes. On a rough trail with a wired headset, that breaks both flow and footing. The current workflow (Just Press Record + manual review later) loses in-session editorial decisions to memory before they can be captured.

**Differentiator:** Voice-and-gesture-only control of the full dictation lifecycle — record, pause, mark sections, review, delete, tag, annotate, consult outline / synopsis — all hands-free during physical activity. Section-aware navigation (jump by silence-detected breaks) replaces scrubbing through long recordings.

## The Three Questions

_An idea cannot leave `status: seed` until these are filled in with real answers, not placeholders._

**Who pays, how often, how much?**
_(unanswered)_

**Year-2 maintenance cost:**
_(unanswered)_

**Kill criteria:**
_(unanswered)_

## Concept

Two-mode app with explicit transitions between modes. Once a session begins, all interaction is auditory.

**Recording mode**
- Captures audio from a wired or wireless headset.
- Continuously detects pauses and silences, marking section breaks for later traversal.
- Section breaks become navigation waypoints — like cairns on the recording.

**Control mode**
- Triggered by a custom headset gesture (long-press, double-press, etc.) or a spoken key phrase.
- Plays back snippets from the start and end of each section to orient.
- Per-section voice commands: delete, tag (e.g., "scene change", "important", "cut later"), add editorial note (e.g., "revise this transition").
- Voice access to reference material: outline, synopsis, prior chapter notes — surfaced via text-to-speech and audio playback only.

**Out of scope for v1**
- In-app transcription. Output is audio plus a structured metadata sidecar (section breaks, tags, editorial notes); transcription happens later in another tool the user already uses.

## Prior Art

Competitive matrix for the **creative writer dictating long-form prose during physical activity, with in-session voice control** use case. The dictation / voice-to-text space is crowded but each player targets a different user — none directly serve this workflow.

| App | Target user | What it does well | What it doesn't address |
|---|---|---|---|
| **Speakwise** | Knowledge workers capturing meetings and notes | AirPods hands-free recording (~95% accuracy); structured-note generation; Notion sync | Productivity-template framing; no session UX, no section traversal, no in-session review / edit / tag |
| **Dragon Anywhere** | Legal / medical / academic professionals; desk-based novelists | Voice formatting commands; continuous dictation; high accuracy with voice training | Desk-mindset adapted to mobile — assumes you can look at the screen; no hands-free session control |
| **Aqua Voice** | iOS users wanting better system-wide dictation | Keyboard replacement; works in any app; modern voice-to-text accuracy | Input method only; no session UX, no audio capture, no sectioning |
| **Apple Dictation** | All iOS users (built-in baseline) | Free, on-device, available everywhere | Input method only; no session UX |
| **Just Press Record / Voice Memos** | General audio capture (Just Press Record is the current incumbent for this user) | Reliable capture; basic transcription (Just Press Record) | No voice control; no section markers; no in-session review |
| **Apple Voice Control (accessibility)** | Users needing hands-free OS interaction | OS-level voice command of the entire iOS interface | Generic overlay; not workflow-specific; no audio session model |

**The real incumbent isn't any single app — it's the existing workflow**: Just Press Record on the trail plus manual post-hike review at a desk. TrailDraft would displace that workflow rather than any single product on the App Store.

**Strategic read**: the competitive niche is thin, which is encouraging. But the niche may be thin because the audience is small — the audience-size risk already named under Why It Might Not. Empty niches are moats only when there's a viable audience inside them; research before leaving `seed` should focus on whether enough outdoor-active dictating writers exist to support a paid app, not just whether competitors do.

**Standing criterion (2026-07-13): dictation itself is not a product.** Apple commoditizes speech-to-text a little more every OS release (SpeechAnalyzer in iOS 26; major systemwide dictation accuracy gains and conversational Voice Control in iOS 27 — see [[../../../Research/Tech/iOS 27 Features Relevant to App Ideas]]). If this idea's core value ever reduces to "it transcribes while you walk," kill it. The only defensible core is the layer above dictation: the session model — hands-free section marking and traversal, in-session editorial decisions (tag/delete/annotate while fresh), and voice access to outline and reference material mid-draft. Every scoping decision should protect that layer and treat transcription as a platform-provided commodity underneath it.

## Why It Could Work

- Real, repeated personal pain — the proof that the problem exists is the workflow this is built to fix.
- Apple platform alignment is good: SiriKit, Speech framework, AVFoundation for capture, headset gesture handling are native APIs already present on the target device.
- Niche but defined audience (outdoor-active dictating writers) is small enough to underwrite a focused v1 without competing with general-purpose recorders.
- Apple Watch could extend the control surface for environments where speaking aloud is unwanted (silent gestures, haptic confirmations).

## Why It Might Not

- The audience is narrow. Outdoor-active dictating writers are a thin slice; willingness to pay may not support a sustainable business at that scale.
- Voice-control reliability outdoors (wind, gear noise, irregular speaking patterns from exertion) is the engineering question that determines whether this actually solves the problem or just shifts the friction.
- Apple may close or reshape relevant APIs (background audio, custom wake words, Siri shortcut handling) in ways that break the model.
- "Review and edit while moving" may be cognitively impractical for many users; review may need a dedicated post-activity pass even with the best UX.

## Open Questions

- Headset gesture surface: what's actually controllable via wired vs. AirPods vs. third-party? Inventory the physical control bandwidth before designing the gesture vocabulary.
- Section detection: pure silence-threshold, or smarter (sentence-boundary detection via the on-device Speech framework, or pause-pattern recognition)?
- Wake-word activation: custom phrases on iOS are constrained (Siri owns "Hey Siri"); does a tap-then-speak gesture work better than a wake word?
- Apple Watch as a complementary control surface — useful, or feature creep?
- Output format: pure audio + JSON / markdown metadata sidecar, or also produce a formatted summary for downstream transcription tools?
- Privacy / on-device vs. cloud: dictation is draft-stage personal writing; users may be sensitive about cloud round-trips for transcription or processing.

## Related

- Personal originator of the use case: hiking-while-dictating with Just Press Record (currently in use).
