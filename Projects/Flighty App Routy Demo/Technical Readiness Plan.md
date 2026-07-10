---
status: active
created: 2026-06-18
updated: 2026-06-18
---

# Technical Readiness Plan

Step-by-step plan for turning Routy from a promising internal demo into a credible Flighty outreach asset.

## Objective

Make the Flighty package safe to send by eliminating trust leaks first, then packaging the work as proof of product judgment, architecture direction, current-stack ramp, and end-to-end reasoning in Flighty's problem space.

The plan is intentionally ordered. Do not record videos, publish a landing page, or send outreach until the verification and public-material gates are green.

Flighty's role explicitly asks for production experience in iOS **and** backend systems. Routy reduces the backend-recency gap but does not erase it. The honest strategy is to show that the recent backend ramp is real and defensible, while not presenting an AI-assisted demo backend as equivalent to recent production Kotlin/JVM ownership.

## Definition of Done

- Swift and backend test suites pass from a clean checkout.
- Public-facing docs no longer describe stale scope, broken tests, or already-fixed risks as open work.
- Flighty resume/application material reflects current Routy evidence for Kotlin/Ktor and TCA.
- The backend-authorship story is honest: architecture/product/data decisions were mine; Kotlin/configuration implementation was heavily AI-assisted; I can still defend and change the system.
- At least one small backend hardening pass has been personally implemented and tested.
- The demo has one coherent seeded persona with honest data caveats.
- The app has a 10-15 second cinematic demo mode that creates a distinctive visual hook for the landing page.
- Outreach uses one link to a tailored landing page with video, live backend proof, concise engineering notes, resume, and scheduling CTA.
- The cold email frames Routy as proof of fit, not unsolicited product advice.

## Phase 0 — Confirm Role Fit

1. Re-read `Resume/Career Preferences.md`.
2. Re-read the Flighty requirement as written: iOS **and** backend systems.
3. Decide explicitly whether a role with real backend/data ownership is desirable, not merely useful as an interview target.
4. Decide whether the backend-recency gap is an acceptable risk.
   - Recent production work is iOS-heavy.
   - Historical backend work is substantial but not recent.
   - Routy shows current-stack ramp and judgment, not recent production Kotlin/JVM tenure.
5. If the answer is no, stop and reposition Routy as a portfolio artifact for iOS/platform roles instead of investing more Flighty-specific time.
6. If the answer is yes, update the private project notes to say the full-stack weighting is intentional for this target.

Gate:
- There is no unresolved mismatch between the Flighty role and current career preferences.
- The decision to proceed accepts that a strict backend-recency screen may still reject the application.

## Phase 0.5 — Backend Ownership Defense

1. Write down the authorship truth before changing copy.
   - I made decisions about what to build, what APIs/tools/data sources to use, what data to collect, and how to organize it.
   - Kotlin implementation and much of the configuration were heavily AI-assisted.
   - My verification was real but initially light in places.
   - I understand the system and need to prove I can personally change it.

2. Create a short backend-defense note.
   - Suggested file: `Projects/Flighty App Routy Demo/Backend Defense Notes.md`
   - Cover:
     - `AppIO` and event-loop blocking.
     - Striped mutexes for paid AeroAPI fetch coalescing.
     - Raw vs derivative data split.
     - `/stats` plus paginated `/flights`.
     - Why Postgres now; where Cassandra would earn its place.
     - Where NATS would earn its place.
     - Remaining honest risks.

3. Personally implement at least one small backend hardening change after reading the relevant files.
   - Good candidates:
     - Fix the remaining `userRepo.exists` blocking call in `AddToHistoryRoutes`.
     - Add distinct 429 handling for AeroAPI responses.
     - Replace manual `path_simplified` JSON string construction with structured serialization.
   - Add or update tests for the chosen change.

4. Practice one backend walkthrough out loud.
   - Pick one route file, one service file, and one repository file.
   - Explain what happens on a cache miss.
   - Explain what happens under concurrent first-adds for the same flight.
   - Explain what breaks at Flighty scale.

5. Update messaging to reflect ownership accurately.
   - Allowed:
     > I directed the architecture, data decisions, and trade-offs, used AI heavily as an implementation partner, then reviewed, corrected, tested, and hardened the backend until I could defend it.
   - Avoid:
     > I recently built a production-grade Kotlin backend.

Gate:
- I can explain and modify the backend without leaning on AI in real time.
- Routy is framed as current capability/ramp evidence, not as proof of recent production backend implementation tenure.

## Phase 1 — Restore Test Green

1. Fix the Swift package test failure.
   - File: `/d/ivg/flighty-routes/RoutyApp/RoutyKit/Sources/AppFeatureView/FlightManagerView.swift`
   - Current failure: `.navigationBarTitleDisplayMode(.inline)` is unavailable when `swift test` builds the package on macOS.
   - Preferred fix: wrap the modifier in an iOS availability/platform extension, or move it behind `#if os(iOS)` without changing runtime iOS behavior.

2. Fix the backend test fake.
   - File: `/d/ivg/flighty-routes/backend/service/src/test/kotlin/com/ivygulch/flightyroutes/service/flights/InstanceRoutesTest.kt`
   - Current failure: `StoreUserRepo` does not implement `UserRepository.delete(id: Int)`.
   - Preferred fix: implement `delete(id: Int)` in the fake and remove the user's rows from the shared `InstanceStore`, matching production cascade intent closely enough for route tests.

3. Re-run verification.
   - Swift:
     ```shell
     swift test --package-path /d/ivg/flighty-routes/RoutyApp/RoutyKit
     ```
   - Backend:
     ```shell
     cd /d/ivg/flighty-routes/backend/service
     ./gradlew test
     ```

4. If either suite fails, fix the failure before continuing.

Gate:
- Both suites pass.
- Record command results and date in this note or `Brief.md`.

## Phase 2 — Remove Remaining Technical Overclaims

1. Audit blocking I/O claims.
   - File: `/d/ivg/flighty-routes/backend/service/src/main/kotlin/com/ivygulch/flightyroutes/service/flights/AddToHistoryRoutes.kt`
   - Current caveat: `userRepo.exists(userId)` is still called directly in the route before `lazyFetch.addToHistory(...)`.
   - Fix: wrap it in `withContext(AppIO)` or otherwise move it off the Ktor event-loop path.

2. Review all route handlers for direct blocking repository/service calls.
   - Search:
     ```shell
     rg -n "userRepo\\.|repo\\.|flightRepo\\.|lazyFetch\\.|svc\\." /d/ivg/flighty-routes/backend/service/src/main/kotlin/com/ivygulch/flightyroutes/service
     ```
   - Ensure blocking calls are either inside `withContext(AppIO)` or inside a service that does that internally.

3. Re-run backend tests.

4. Decide whether to fix or explicitly document remaining lower-risk backend issues.
   - No retry / no distinct 429 handling in `OkHttpAeroApiClient`.
   - `(0,0)` fallback for missing airport coordinates.
   - Manual JSON string build for `path_simplified`.
   - Upsert can overwrite richer trajectory data with later partial data.

Gate:
- Landing-page copy can honestly say the major backend risks were fixed without a sharp reviewer finding an obvious exception in the first route file they open.

## Phase 3 — Reconcile Public Docs

1. Rewrite the top of `/d/ivg/flighty-routes/README.md`.
   - Replace the old "spaghetti map" / OpenSky / TBD backend+iOS framing with the current product:
     - SwiftUI/TCA iOS app.
     - Kotlin/Ktor backend.
     - Postgres/Supabase.
     - AeroAPI/FlightAware trajectory source.
     - Fly.io deployment.
     - Mapbox globe visualization.
   - Keep the old route-spaghetti prototype as historical background only.
   - Keep the demo-data honesty note, but align attribution with the implemented AeroAPI source.

2. Update `/d/ivg/flighty-routes/prep/ROUTY_PLAN.md`.
   - Mark the iOS client as built.
   - Replace `GET /visualization` as the main path with `/stats` and paginated `/flights`.
   - Replace "known weaknesses to fix" with "fixed" plus "remaining known risks."
   - Remove any "you write the iOS; I drive Kotlin" language that reads like the work is split or incomplete.

3. Update `/d/ivg/flighty-routes/prep/BACKEND_REVIEW.md`.
   - Convert it from stale adversarial review into a current readiness review.
   - Use sections:
     - Fixed.
     - Still open.
     - Deliberately out of scope.
     - How to discuss in interview.
   - Keep the critical thinking, but do not leave fixed high-severity issues presented as current defects.

4. Update `Projects/Flighty App Routy Demo/Brief.md`.
   - Correct the verification status after Phase 1.
   - If any caveat remains, state it precisely.

5. Update `Projects/Flighty App Routy Demo/Outreach Plan.md`.
   - Change TODOs as they are completed.
   - Keep the "do not pitch this as a feature Flighty should ship" warning.

Gate:
- A reviewer can open README and prep docs in any order and get one consistent state of the project.

## Phase 4 — Update Resume and Application Material

1. Update `Resume/Generated/2026-05-21 1447 Flighty.md` or create a fresh generated Flighty application note.
   - Remove stale phrasing that Kotlin is only a future ramp.
   - Replace "I have not used TCA directly" with current Routy evidence.
   - Keep backend recency honest.

2. Add a concise Routy project paragraph:
   > Built Routy, a Flighty-shaped full-stack demo: SwiftUI/TCA iOS client with tested reducers and dependency-injected REST client, Mapbox globe rendering, Kotlin/Ktor backend on Fly.io, Postgres/Supabase cache, and real FlightAware/AeroAPI ADS-B trajectories.

3. Keep honesty about production experience.
   - Kotlin/Ktor: current project evidence, not production tenure.
   - Backend authorship: architecture/product/data decisions were mine; implementation/configuration were heavily AI-assisted; I reviewed, corrected, tested, and can defend the system.
   - TCA: current project evidence plus years of production unidirectional/reactive architecture.
   - Cassandra/NATS: modeling and thresholds, not operated-in-production claims.

4. Decide where Routy belongs in the public package.
   - Landing page: prominent.
   - Resume: short project entry or portfolio link.
   - Cold email: one sentence only.

Gate:
- Flighty-specific material no longer undermines the demo by describing Kotlin/TCA as pure gaps.
- Flighty-specific material does not overstate recent backend production implementation experience.

## Phase 5 — Seed a Coherent Demo Persona

1. Define one believable traveler.
   - Example: Boston-based consultant.
   - Repeating corridor: BOS to ORD.
   - Secondary corridor: BOS to SFO.
   - Occasional international trips.
   - Enough density for frequency corridors and enough variety for visual drama.

2. Seed with true telemetry.
   - Use existing `scripts/seed-demo-user.sh` if it still matches the current backend API.
   - Ensure the seeded data renders fully without manual cleanup.

3. Make the synthetic-date caveat explicit.
   - Track geometry, duration, and times of day are from real flights.
   - Calendar dates are arranged for demo continuity because AeroAPI search windows are short.

4. Verify the app launches directly into the persona's globe.
   - Use `ROUTY_AUTO_GLOBE_USER_ID`.
   - Use a private `MAPBOX_ACCESS_TOKEN`.
   - Choose default visual mode intentionally.

Gate:
- One command or documented launch recipe opens the strongest demo state without setup friction.

## Phase 6 — Build a 10-15 Second Cinematic Hook

1. Build a bounded demo-mode feature, not a broad product feature.
   - Timebox: one day target, two days maximum if capture tooling needs cleanup.
   - Purpose: create a cooler first 10-15 seconds for the landing page and email hook.
   - Non-goal: add a general-purpose feature surface.

2. Preferred concept: "One real flight, from map line to altitude ribbon."
   - Start on the full 3D globe with the persona's flight history.
   - Pulse or brighten one selected route.
   - Camera dives toward the selected flight.
   - Transition to tilted mercator altitude view.
   - A glowing marker travels along the actual ADS-B track while the ribbon shows climb, cruise, and descent.
   - End on a clean hero frame with route, aircraft, and "actual recorded track, not great circle" if that can be done without clutter.

3. Implementation shape.
   - Add explicit cinematic state to `VisualizationFeature`.
   - Add a launch environment variable, for example `ROUTY_CINEMATIC=1`.
   - Add a way to select the featured flight by id from the seeded persona.
   - Script a short timeline:
     - 0s: full globe loaded.
     - 2s: dim all routes except selected flight.
     - 4s: fly/zoom toward route.
     - 6s: switch to mercator and altitude magnification.
     - 7-13s: animate progress marker along selected track.
     - 14s: settle on final frame.

4. Keep the minimum viable version acceptable.
   - A clean scripted transition from globe history to altitude-ribbon spotlight is enough.
   - A true morph is optional.
   - Do not add multi-user comparison, route-reliability analytics, or a broad new interaction model.

5. Test and verify.
   - Add reducer tests for cinematic state transitions if timeline state enters the reducer.
   - Manually verify the Mapbox render path on simulator.
   - Confirm the sequence can be launched repeatedly for recording without manual taps.

Gate:
- The first 10-15 seconds are distinctive, visually legible, and more compelling than the static sample-user globe.
- The feature improves the video package without delaying credibility work.

## Phase 7 — Polish Demo Capture Path

1. Remove accidental demo chrome where practical.
   - Avoid visible loading pills in hero screenshots unless the clip deliberately shows progressive loading.
   - Avoid token setup screens, awkward camera crops, and developer-only controls in first-frame visuals.

2. Capture a hero still.
   - Fully loaded globe.
   - Strong home-hub framing.
   - No awkward loading state.
   - Shows actual recorded routes clearly.

3. Capture a 5-10 second inline hook.
   - One motion beat only.
   - Use the cinematic hook from Phase 6.
   - Export as GIF or silent looping video preview suitable for email.

4. Capture a 45-75 second reveal.
   - Structure:
     - Full history globe.
     - Group/focus change.
     - Selected flight callout.
     - Altitude/projection moment.
     - Brief engineering proof frame.

5. Review the visuals as a Flighty recipient would.
   - Does it feel polished, not like a debug view?
   - Does it read as a hiring signal within 5 seconds?
   - Does it avoid implying Flighty should build this exact feature?

Gate:
- The first frame and first 5 seconds are strong enough to earn a click without explanation.

## Phase 8 — Build the Landing Page

1. Create a one-page landing page.
   - Location can be inside the Routy repo or an external portfolio site, but it must produce one stable public URL.

2. Above the fold:
   - Autoplay muted reveal video or hero loop.
   - Headline: "A year of flights, on your stack."
   - One short paragraph:
     > A Flighty-shaped full-stack demo: real FlightAware trajectories, Kotlin/Ktor + Postgres backend, SwiftUI/TCA client, and Mapbox globe rendering.
   - One CTA: "Grab 20 minutes."

3. Below the fold:
   - What is real.
   - What I deliberately fixed.
   - Where I would take it next.
   - Resume link.
   - Live backend health link.
   - Optional TestFlight note: available on request.

4. Live backend proof:
   - Use `https://flighty-routes-dws.fly.dev/healthz`.
   - Consider improving the health output before publishing:
     - real git SHA/version instead of `"dev"`.
     - acceptable cold-start behavior or no reliance on first-hit speed.

5. Do not over-explain agentic tooling above the fold.
   - If included, place it below the engineering proof:
     > Built the way I work now: I directed the architecture, data choices, and trade-offs, with Claude Code and Codex doing much of the implementation under review. I then corrected, tested, and hardened the backend until I could defend it.

Gate:
- The landing page is the only link needed in the cold email.

## Phase 9 — Final Outreach Package

1. Verify official application details on the current Flighty careers page before sending.
2. Submit through the official jobs address with required materials.
3. Send a short founder note only if the direct address is verified.
4. Use the short email form:
   - One sentence about why this role.
   - One sentence about what was built.
   - Inline visual.
   - One landing-page link.
   - One 20-minute CTA.

5. Avoid these phrasings:
   - "You should build this."
   - "I made a better Passport."
   - "I used AI to build an app" as the lead.
   - "Kotlin/TCA are gaps" without immediately tying to current Routy evidence.
   - "I recently owned production Kotlin systems" unless that is backed by non-demo production work.

Gate:
- A recipient can understand the fit, see the work, and choose one action in under one minute.

## Phase 10 — Post-Send Follow-Up

1. Wait 5-7 business days.
2. Send one brief follow-up if there is no response.
3. Do not send repeated artifacts or feature suggestions.
4. If there is no response after the follow-up, preserve Routy as a portfolio asset and reuse selectively for other senior iOS/full-stack targets.

## Final Pre-Send Checklist

- [ ] `swift test --package-path /d/ivg/flighty-routes/RoutyApp/RoutyKit` passes.
- [ ] `./gradlew test` passes from `/d/ivg/flighty-routes/backend/service`.
- [ ] Backend defense note exists.
- [ ] At least one personally implemented backend hardening change is complete and tested.
- [ ] README top section is current.
- [ ] `prep/ROUTY_PLAN.md` is current.
- [ ] `prep/BACKEND_REVIEW.md` is current.
- [ ] Flighty resume/application copy is current.
- [ ] Demo persona is seeded.
- [ ] Cinematic demo mode exists and launches by env var.
- [ ] Hero still is captured.
- [ ] Hook GIF/video is captured.
- [ ] Reveal video is captured.
- [ ] Landing page is published.
- [ ] Live backend health endpoint is acceptable.
- [ ] Cold email has one link and one CTA.
- [ ] Official application is submitted in parallel.

## Priority Order

1. Fix tests.
2. Prove backend ownership with a small personal hardening pass.
3. Fix technical overclaims.
4. Reconcile public docs.
5. Update Flighty resume/application copy.
6. Seed persona.
7. Build the cinematic hook.
8. Capture visuals.
9. Publish landing page.
10. Send.
