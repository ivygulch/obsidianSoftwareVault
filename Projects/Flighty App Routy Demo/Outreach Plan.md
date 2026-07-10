---
status: active
created: 2026-06-14
updated: 2026-06-14
---

# Outreach Plan

The strategy, drafts, and decisions for reaching Ryan Jones. Context in [[Company & Founder Research]]; goal in [[Brief]].

## Core thesis
The bottleneck is **not** the code — Routy is build-complete and mirrors Flighty's exact stack end-to-end (SwiftUI/TCA + Kotlin/Postgres + AeroAPI, deployed on Fly.io). That stack-match + end-to-end ownership is a stronger signal than any single visualization. The job is to package it tightly and frame it correctly.

## Channel — email primary
- **Primary:** direct email to Ryan (likely `ryan@flighty.com` — verify before sending).
- **Belt-and-suspenders:** also apply through the official careers channel with the same package.
- **Forum:** use only to become a recognizable name *before* the email (genuine, non-pitch). Never pitch there.
- **Slack/group chat:** no prior relationship — cold DM is the weakest channel. At most, a one-line nudge *after* the email. Low priority.

## Demo decisions
- **Hook (email teaser, 5–10s, silent inline loop):** one visceral motion beat — altitude ribbon rising or fly-in to the glowing history. Shows the one thing Flighty's flat map can't. See First-touch composition below for delivery rules.
- **Reveal (landing page, 45–75s):** animated globe drawing a real flight history over a date range — glowing path, frequency-weighted color/thickness (framed as homage to Passport), altitude ribbons, projection toggle.
- **Cut:** user-vs-user comparison (duplicates Flighty Passport's "compare with friends").
- **Data:** one coherent persona, not a random sampler. e.g. Boston consultant's year — weekly BOS↔ORD, monthly BOS↔SFO, two transatlantic trips. Frequency corridor + international drama. Seed with true telemetry from real flights.

## Framing — the knife-edge
- ❌ "Here's a feature you should ship" → uninvited product advice.
- ✅ "I built this on your exact stack to prove I can own features in your problem space."
- Cover copy must land the second reading.

## First-touch composition (the email payload)
Keep it tight — one screenshot, one ultra-short clip, one link. Three execution rules:

1. **The clip must play without a click.** Deliver as a **silent looping GIF / animated preview** that plays inline, or a static frame with a play overlay linking out. A raw video link is a second CTA, not a hook; don't attach a video file (won't autoplay, spam-flag risk). If the motion needs a click, the involuntary-watch is lost.
2. **Screenshot and clip do different jobs — no redundancy.**
   - **Screenshot** = guaranteed-render beauty frame (fully-loaded globe, strongest framing); the floor if images/GIF are blocked.
   - **Clip (5–10s)** = the single most visceral *motion* beat a still can't convey — altitude ribbon rising, or the fly-in to the glowing history. One beat, not the whole sequence (the landing-page video carries the full arc).
   - Cleanest version: **one looping GIF whose first frame is the hero still** (beauty + motion in one asset); keep a separate static screenshot only as insurance against GIF-blocking.
3. **One link, not three.** Screenshot + clip + the single webpage link. No resume/TestFlight links in the email — the webpage holds everything downstream. Visuals create the click; copy creates the meaning (don't let the visual-forward approach starve the stack-match sentence).

## Draft — cold email (~6 sentences, one CTA)
> **Subject:** Built a 3D flight-history globe on your stack to see if I could do the job
>
> Ryan —
>
> I saw the Sr. Full Stack role and, instead of leading with a resume, I wanted to find out whether I could actually do the work — so I built a flight-history visualizer on Flighty's stack: SwiftUI/TCA up front, Kotlin/Postgres on the back, pulling real ADS-B trajectories from FlightAware, deployed on Fly.io.
>
> *[inline: hero screenshot + 5–10s looping clip]*
>
> It renders *actual recorded tracks* — not great circles — on a 3D globe with exaggerated altitude, so you watch a flight's real climb and descent. The longer demo, the live backend, and how I'd reason about Cassandra/NATS in this domain are here: **[landing page — single link]**.
>
> I'm US Eastern and looking for exactly the small-team, own-it-end-to-end work the post describes. Worth 20 minutes?
>
> — Doug

Each line maps to a job requirement: stack match + end-to-end ownership + aviation curiosity (line 1); "not great circles" = flight-nerd credibility; Cassandra/NATS mention = "make and defend decisions" before the call; one CTA. Resume link lives on the landing page, not in the email.

## Draft — landing page (one screen, one button)
**Above the fold:**
1. **Hero:** reveal video, autoplay-muted-loop. Headline: *"A year of flights, on your stack."* Nothing competing.
2. **One paragraph:** what it is + the stack. Link the **live backend** (`/healthz` → version/uptime) here as proof it's real.
3. **CTA:** one button — "Grab 20 minutes" → Calendly.

**Below the fold** (keep concise — Ryan evaluates craft/product first; front-loading engineering proof reads as engineer-proving-themselves):
4. **"What I deliberately fixed"** (past tense — done & committed, demonstrated > promised):
   - Blocking JDBC/OkHttp moved off Ktor event-loop threads (`AppIO`).
   - Per-flight lazy-fetch race coalesced (striped mutexes) so concurrent first-adds don't double-spend paid AeroAPI calls.
   - Monolithic visualization payload split into `/stats` + paginated `/flights`; N+1 removed; render tracks simplified.
   - Lazy-fetch tested: cache hit/miss, upstream failures, gaps, timeouts, concurrent fetch.
5. **"Where I'd take it next"** (future tense — Cassandra/NATS live HERE, as thresholds not keywords): NATS for async backfill/worker queue if lazy-fetch becomes a user-visible latency/throughput issue; Cassandra/Scylla modeling for high-write position telemetry at Flighty scale (not demo-scale relational data); production auth/privacy before real user data.
6. **"How it's built" (method line — frame as leverage, NOT confession):**
   > Built the way I work now: I architected and directed it, with Claude Code and Codex doing most of the implementation under tight review. The stack choices, the data-licensing schema, the backend-risk triage, and every trade-off are mine — and I can walk through any of them.
   - Keep method OUT of the cold email (dilutes the hook, invites skepticism before he's intrigued). Lean into it in conversation/interview, where the nuance lands as a positive.
   - Prerequisite, not optional: be able to defend any line they probe (why `AppIO`, how the mutex coalescing works). If you can, AI-authorship is a non-issue/plus; if you can't, no phrasing saves it. Avoid "full disclosure / I should admit" framing.
7. **On request:** TestFlight build offer (direct-to-demo launch, token can't fail); short intro-about-me video.

## Path forward (time-boxed — resist the polish loop)
1. **Reconcile stale public-facing material FIRST** — README, `prep/ROUTY_PLAN.md`, `prep/BACKEND_REVIEW.md` (mark fixed vs. remaining), and resume/Flighty lines (kill "Kotlin is a gap" / "TCA not production"; add a Routy project entry). Wrong public material undercuts everything downstream.
2. Seed the demo persona with true telemetry (own the synthetic-dates caveat).
3. Record + edit the two videos (recording task, not dev — both features already exist in code).
4. Build the one-screen landing page.
5. Verify Ryan's email; finalize the cold email; submit official application in parallel.
6. Send. **Backend HIGH/MEDIUM risks are already fixed/committed** (verified 2026-06-14) — do NOT re-open them; frame as "found and fixed," not future work.

## Open / TODO
- [ ] **Reconcile stale docs** (README, `prep/ROUTY_PLAN.md`, `prep/BACKEND_REVIEW.md`) — backend risks are fixed; iOS is built. Do this before any public link.
- [ ] **Fix resume/Flighty lines** — remove "Kotlin is a gap" and "TCA not production experience"; add a Routy project entry (see [[ChatGPT recommendations]] for exact rewrites).
- [ ] Verify Ryan's email address.
- [ ] Build demo persona + seed data (own synthetic-dates caveat).
- [ ] Record hook + reveal videos.
- [ ] Stand up landing page + Calendly.
- [ ] Finalize paste-ready landing-page copy (the "what I fixed" bullets above are drawn from verified committed code, not the stale review).

See [[ChatGPT recommendations]] for the parallel review this plan was reconciled against (2026-06-14).
