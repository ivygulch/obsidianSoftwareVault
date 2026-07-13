---
type: research
confidence: cited-beta
tags: [ios27, wwdc26, foundation-models, siri, voice-control, app-intents, passalong, traildraft, tech-research]
created: 2026-07-13
updated: 2026-07-13
status: active
---

# iOS 27 Features Relevant to App Ideas (WWDC26)

> Companion to [[iOS 26 Features Relevant to App Ideas]]. Sourced entirely from post-WWDC26 coverage and Apple session listings (fetched 2026-07-13). **iOS 27 is in developer beta; ships ~September 2026 — details can still shift before release**, so treat this as directional planning input, not locked API fact. Confidence: cited-beta.

## Headline: the AI layer went from "one small local model" to "any model, anywhere" — and voice control became a platform feature

Two WWDC26 moves matter most for these app ideas: (1) the Foundation Models framework opened up — rebuilt on-device model with **image inputs**, a **provider protocol** for plugging in any LLM (local MLX, Private Cloud Compute, or third-party providers like Anthropic and Google), Private Cloud Compute access with reasoning and a 32K context window; and (2) **Siri AI + conversational Voice Control** — natural-language command of visible UI, with App Intents as the mandatory (and now SiriKit-deprecating) integration surface.

## 1. Foundation Models framework, generation two

**What changed:** the on-device system model was rebuilt — better instruction following and **direct image inputs**. A new `LanguageModel` / `LanguageModelExecutor` protocol pair opens the framework to any provider: local models via MLX/CoreAI, Apple's **Private Cloud Compute** model (reasoning, 32K context, Apple's no-retention privacy guarantees), and third-party cloud providers (Anthropic and Google named). Full tool calling; one source claims on-device fine-tuning (single-source — verify before relying on it).

**Passalong:**
- **Image inputs are the sleeper unlock.** "Hand the model a photo, get interview questions about it" — photo-driven memory prompts ("who is this, what was happening?") generated on-device. Object stories and photo-anchored prompts were already in the Story Capture MOC's focus list; this makes them cheap.
- **Private Cloud Compute changes the AI-capability ceiling without fully breaking the privacy story.** The ownership promise ("never trains AI, stays in your family's control") can coexist with PCC's no-retention guarantees for *transient* prompt generation — but this is a positioning decision to make deliberately: "on-device only" is a cleaner marketing sentence than "on-device plus Apple's private cloud." Decide before writing App Store copy.
- The provider protocol means a future richer-model option (even Claude) is a configuration, not an architecture change — quarantine AI behind one interface and the choice stays open.
- Device floor unchanged in practice: Apple Intelligence hardware (iPhone 15 Pro+). The progressive-enhancement posture from the iOS 26 note stands.

**StoryRiffs party variant / TrailDraft:** 32K context handles a whole story-so-far or a full trail session's transcript in one prompt; streaming responses fit read-back-while-generating UX.

## 2. Siri AI + conversational Voice Control

**What changed:** Siri rebuilt on Apple Intelligence — multi-turn conversation, personal context, on-screen awareness. Separately (and previewed through accessibility), **Voice Control now takes natural conversational commands about visible UI** ("tap the guide about best restaurants"). App Intents is now the *only* path for new Siri integrations; SiriKit is formally deprecated (~2–3 year window). App Intents adds streaming responses, multi-turn follow-ups, richer entities, the **View Annotations API** (map your views to entities so users can voice-reference what's on screen), and an **App Intents Testing framework** (validate Siri/Shortcuts/Spotlight through real system pathways).

**TrailDraft — this is the biggest single-idea impact in either OS release.** The seed's core premise is voice-only control of a recording session, and its risk list included "Apple may close or reshape relevant APIs." Apple built *toward* the premise instead: conversational voice command of app UI + multi-turn App Intents means the control vocabulary ("mark that", "play back the last section", "tag this as revise") can ride system machinery rather than custom wake-word workarounds. Two edges to respect: (a) hands-free eyes-free on a trail is still not what system Voice Control is tuned for — it assumes you can glance at the screen; the session-model design work remains; (b) **sherlock risk is now real** — systemwide dictation got a major accuracy bump and Apple is clearly investing in voice capture; TrailDraft's defensible core narrows to the *session model* (sections, in-session review, editorial tags, reference-material readback), not dictation itself.

**Passalong:** conversational Voice Control is an elder-accessibility gift — "answer today's question" spoken at the phone, no navigation. View Annotations + App Intents Testing slot straight into the capture-entry-points plan from the iOS 26 note.

## 3. Smaller but relevant

- **Systemwide dictation accuracy** improved via the larger model — benefits every voice-first idea for free; raises the baseline TrailDraft must beat.
- **Expressive Siri voices / TTS improvements** — Passalong could read prompts (or finished stories) aloud in warmer voices; relevant to elders with low vision and to TrailDraft's audio-only reference readback.
- **SwiftUI Document API** — potentially a clean home for Passalong's canonical export format; evaluate when the export format is specified.
- **On-Demand Resources deprecated → Managed Background Assets** — the delivery path for Passalong prompt packs; use MBA from day one, not ODR.
- **Xcode 27 on-device AI code completion**, faster simulators — dev-workflow only.
- **CloudKit:** nothing headline surfaced for iOS 27 either — the [[CloudKit Spike Plan]] stands.

## Adoption guidance (supersedes nothing, extends the iOS 26 note)

1. **Floor decision by ship date:** anything shipping after ~September 2026 should assume iOS 26 floor / iOS 27 enhancements at launch, re-evaluated at build start. SpeechAnalyzer (26) is floor-safe; Foundation Models features remain hardware-gated regardless of OS version.
2. **Build the AI seam as a protocol now** — iOS 27's provider model rewards exactly the quarantined-AI-interface design the Android-later guardrails already prescribe for sync. Same principle, second subsystem.
3. **For TrailDraft:** re-read the seed's open questions against Siri AI/Voice Control betas before any spike — several may already be answered by the platform, and the sherlock-risk assessment belongs in the idea page if it moves off seed.
4. **Verify before relying on:** on-device fine-tuning (single source), PCC pricing/quotas (not covered in sources), Voice Control API availability to third-party apps vs. system-only (accessibility-preview framing leaves this ambiguous).

## Sources

Fetched 2026-07-13: apple.com newsroom (June 2026, next-gen Apple Intelligence/Siri); developer.apple.com WWDC26 sessions 102 (State of the Union), 241 (What's new in Foundation Models), 339 (Bring an LLM provider), 345 (App Intents) and WWDC26 Apple Intelligence/iOS guides; dev.to WWDC26 Foundation Models provider coverage; andrew.ooo WWDC26 developer-tools recap; medium.com WWDC26 iOS-developer recaps; macrumors.com Siri AI hands-on + iOS 27 voice-control coverage; macworld.com iOS 27 Voice Control accessibility preview; theaiinsider.tech Siri voice-customization beta note; ecorpit.com App Intents migration guide; chatforest.com iOS 27 Foundation Models builder guide (sole source for on-device fine-tuning claim); lushbinary.com WWDC26 summary.

## Relevant To
- [[iOS 26 Features Relevant to App Ideas]] — the shipping-today baseline this note extends
- [[../../App Ideas/Story Capture/Passalong/Passalong|Passalong]] — photo-prompted interviews, PCC positioning decision, prompt-pack delivery via MBA
- TrailDraft (App Ideas/Writing) — platform built toward its premise; sherlock risk now material
