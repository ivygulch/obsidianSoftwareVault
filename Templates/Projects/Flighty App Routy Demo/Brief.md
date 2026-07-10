---
status: active
platform: iOS + Kotlin backend
created: 2026-06-14
updated: 2026-06-14
---

# Flighty App Routy Demo — Brief

**Concept:** Use the existing Routy flight-visualization app as a tailored portfolio piece to get a meeting with Flighty's founder for the Sr. Full Stack Engineer role.
**Target user (audience):** Ryan Jones, founder/CEO of Flighty, and his hiring group.
**Platform:** iOS (SwiftUI/TCA) + Kotlin/Ktor/Postgres backend, deployed on Fly.io.
**Status:** Build-complete for outreach. The backend's known HIGH/MEDIUM risks (blocking I/O, concurrent-fetch race, N+1, thin lazy-fetch tests) are now **fixed and committed** (verified 2026-06-14: `AppIO` off-event-loop dispatch, striped-mutex coalescing, `/stats` + paginated `/flights`, real lazy-fetch tests; Swift + Gradle suites pass). Remaining bottleneck is the outreach package — and updating stale public-facing docs/resume that still describe the old, unfinished state.

## Goals
- Land a 20–30 minute meeting with Ryan Jones.
- Demonstrate end-to-end ownership on Flighty's exact stack (the role's core requirement).
- Signal product taste and aviation curiosity (both explicit job requirements).

## Scope (MVP of the outreach)
- One short hook video (cinematic single-flight altitude flythrough, 8–15s).
- One longer reveal video (animated globe drawing a real flight history, 45–75s).
- A one-screen tailored landing page (reveal video + live backend link + "how I'd take it to production" + one CTA).
- A ~6-sentence cold email to Ryan, plus a parallel official-channel application.
- A coherent demo persona seeded with true telemetry from real flights.
- **Update stale public-facing docs** (README, `prep/ROUTY_PLAN.md`, `prep/BACKEND_REVIEW.md`) and resume/Flighty material so nothing describes the old unfinished state. High priority — wrong public material does damage a good video can't undo.

## Out of Scope (before first contact)
- Further backend hardening beyond what's already fixed/committed — diminishing returns; the HIGH/MEDIUM risks are done.
- TestFlight invite as a front-door ask (defer to a reply once he's interested).
- Intro-about-me video on the critical path (defer; lead with the work).
- User-vs-user comparison feature (cut — duplicates Flighty's existing Passport "compare with friends").

## Success Criteria
- Reply from Ryan or his team.
- A scheduled call.

## Risks
- **Framing risk:** reads as "here's a feature you should ship" (arrogant) vs. "I can do this job on your stack" (intended). Mitigated by cover copy.
- **Derivative risk:** globe map echoes Flighty's Passport map; mitigate by framing frequency-coloring as homage and leading with what they *can't* do (3D + real ADS-B tracks + altitude).
- **Cold-contact risk:** no prior relationship; mitigated by email-primary channel + optional forum warming.
- **Stale-docs risk:** README / prep notes / resume still describe the old unfinished state (backend unfixed, iOS "not built," Kotlin & TCA as gaps). If Ryan reads these they read "unfinished" — must be reconciled before any public link.
- **Synthetic-dates honesty:** demo track geometry/details are real telemetry, but dates are arranged/redistributed (AeroAPI search windows are short). Own the distinction if asked; don't imply a continuous real history.
- **Polish-loop risk:** over-polishing already-good code instead of shipping the outreach.

## Related
- [[_Flighty App Routy Demo MOC|MOC]]
- [[Company & Founder Research]]
- [[Outreach Plan]]
