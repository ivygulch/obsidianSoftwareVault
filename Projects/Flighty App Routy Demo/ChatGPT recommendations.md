---
status: active
created: 2026-06-14
updated: 2026-06-14
source: ChatGPT review
---

# ChatGPT recommendations

These notes consolidate the ChatGPT review of the Routy app, Flighty role, company context, outreach strategy, and path forward.

## Bottom line

Routy is already past "interesting side project." The strongest signal is:

> I built a Flighty-shaped slice end to end, found the sharp backend risks, fixed the most important ones, and can explain the product/data tradeoffs clearly.

Do not expand broadly. Add one guided demo path, polish the capture experience, update stale docs/resume material, and send.

## What Flighty appears to value

From the current Flighty Sr. Full Stack Engineer role and public materials, the hiring signal is not "can you make a map." It is:

- End-to-end ownership: client, API, data, rollout, iteration.
- Polished iOS craft, especially SwiftUI and TCA.
- Backend/data judgment in Kotlin/JVM, Postgres, Cassandra, and NATS territory.
- Reliability, latency, crash-rate, uptime, and observability thinking.
- Ability to turn messy aviation data into simple, reliable user experiences.
- Product taste and comfort making/defending decisions without a ticket backlog.
- Genuine aviation/travel curiosity.

Public Flighty positioning also emphasizes pilot-grade data, perfectly timed notifications, quality design, reducing traveler stress, personal travel history, airport intelligence, and clear explanations rather than raw data dumps.

## Current Routy assessment

The app is stronger than the older project notes imply.

### iOS strengths

- Real SwiftUI/TCA implementation, not a prototype shell.
- `VisualizationFeature` owns paginated loading, stats, filters, focus, projection, altitude magnification, selected flight state, and pure style derivation.
- `GlobeView` renders a Mapbox globe using a single source plus glow/main/selected layers.
- It supports dark/satellite style, globe/mercator projection, altitude ribbons in mercator, tap-to-select, legend focus, filters, settings, and progressive loading.
- The Mapbox code is quarantined in `VisualizationView`; feature logic remains testable without Mapbox.
- Demo launch hooks already exist:
  - `ROUTY_AUTO_GLOBE_USER_ID`
  - `ROUTY_GLOBE_STYLE`
  - `ROUTY_GLOBE_PROJECTION`
  - `ROUTY_GLOBE_ALTITUDE`

### Backend strengths

- Kotlin/Ktor backend on Postgres/Supabase, deployed on Fly.io.
- FlightAware/AeroAPI lazy-fetch write-through cache.
- Raw vs derivative data split for license discipline.
- Structured logging and request IDs.
- Paid upstream call cost awareness.
- Blocking JDBC/OkHttp work is now moved off Ktor event-loop threads via `AppIO`.
- Concurrent first-fetches of the same flight are coalesced with striped mutexes.
- Monolithic visualization loading has been replaced by `/stats` and paginated `/flights`.
- Batched flight loading removes the previous N+1 visualization shape.
- Lazy-fetch has meaningful unit tests, including the paid-call race.

### Verification run

Commands run during review:

```shell
swift test --package-path /d/ivg/flighty-routes/RoutyApp/RoutyKit
```

Result: 28 Swift tests passed. The run had expected TCA unimplemented-client known issues and Mapbox package resource warnings; neither changes the demo strategy.

```shell
./gradlew test
```

Result: backend Gradle test task passed.

## Important correction to older notes

Some existing project notes are stale. They still describe backend risks as unfixed or describe the iOS app as not yet built.

Update before sharing anything public:

- README: current status, app location, actual backend, current data source, actual endpoints.
- `prep/ROUTY_PLAN.md`: iOS is built; backend risks #1, #2, #3, and lazy-fetch tests are no longer just future work.
- `prep/BACKEND_REVIEW.md`: either mark fixed items clearly or split into "fixed" and "remaining."
- Resume/Flighty materials: older generated copy says Kotlin and TCA are gaps; Routy now provides concrete Kotlin/Ktor and TCA evidence.

This matters because Ryan/hiring group may read stale notes as a signal that the project is unfinished or that you do not know the current state.

## Feature recommendation

### Priority 1: Guided cinematic history globe

Use the existing globe as the hero.

Show:

- Real flight tracks on a 3D globe.
- Cold open/fly-in to the home hub.
- Recency/frequency grouping.
- One filter/focus change.
- One selected flight.
- Progressive data loading only if it feels intentional; otherwise capture once fully loaded.

Why this is strongest:

- It matches Flighty's "beautiful visualizations" and "messy data made useful" language.
- It demonstrates the whole stack without overexplaining.
- It is visually differentiated from a resume.
- It is already mostly built.

### Priority 2: Single-flight spotlight

Add or script a short moment where one flight is selected and the camera follows/highlights it.

Best version:

- Begin with the whole personal history globe.
- Tap/select one route.
- Switch to mercator/altitude exaggeration.
- Show climb, cruise, descent as an elevated ribbon.

Why this is high value:

- It gives the demo an emotional rhythm: global story -> specific flight -> data detail.
- It shows product judgment rather than just visual density.
- It makes use of the existing altitude-ribbon work without needing a large new feature.

### Priority 3: Do not prioritize multi-user comparison

Do not spend remaining time on user-vs-user comparison before outreach.

Reason:

- Flighty already has Friends/Passport-style comparison and recent "Runway Regulars" positioning.
- A rushed comparison feature could read as derivative.
- It is a larger product surface with more edge cases.
- It is less useful for proving the actual role fit than the end-to-end data/rendering path.

Mention it only as a future direction if asked.

## Demo package recommendation

The first message should include:

- 2 screenshots.
- One 20-30 second silent clip.
- A link to a tailored page.

The goal is curiosity, not exhaustive proof.

### Screenshot set

Use 2, maybe 3.

1. Hero globe, fully loaded, no loading pill, strongest framing.
2. Same data grouped/focused by a meaningful dimension.
3. Optional altitude/selected-flight shot if visually clean.

Existing screenshots are good enough to show the concept, but look like dev-state captures. For outreach, capture with deliberate framing:

- Fully loaded state.
- No token setup screen.
- No accidental loading state.
- No awkward camera crop.
- Minimal chrome.
- Clear map contrast.
- One strong selected route or focused dimension.

### Short hook video

Target length: 20-30 seconds.

Shape:

1. Globe opens with full history.
2. Camera settles at the home hub.
3. A focus/grouping change reveals signal in the data.
4. One flight is selected.
5. Brief altitude-ribbon moment if clean.

No voiceover needed for the teaser. Let the visuals create the click.

### Longer landing-page video

Target length: 60-90 seconds.

Suggested structure:

1. What it is: a Flighty-shaped full-stack demo.
2. Data path: FlightAware/AeroAPI -> Kotlin/Ktor -> Postgres/Supabase -> SwiftUI/TCA -> Mapbox.
3. Product path: history globe, grouping/focus, selected flight, altitude.
4. Engineering path: paid API cache, coalesced fetches, paginated rendering, tests.
5. Short close: "This is the kind of feature ownership I want to do at Flighty."

## Landing page recommendation

Above the fold:

- Hero video.
- One sentence:
  - "A Flighty-shaped full-stack demo: real FlightAware trajectories, Kotlin/Ktor + Postgres backend, SwiftUI/TCA + Mapbox client."
- One clear CTA:
  - "Grab 20 minutes"

Below:

- TestFlight link.
- Resume link.
- Optional short intro video.
- A concise "what is real" section.
- A concise "what I deliberately fixed" section.
- A concise "where I would take it next" section.

### Suggested landing page bullets

What is real:

- Real FlightAware/AeroAPI trajectories.
- Kotlin/Ktor backend deployed on Fly.io.
- Supabase/Postgres cache and reference data.
- SwiftUI/TCA client with Mapbox rendering.
- Paginated `/stats` and `/flights` data path.
- Test-covered feature logic and backend fetch behavior.

What I deliberately fixed:

- Blocking backend work moved off Ktor event-loop threads.
- Per-flight lazy-fetch race coalesced so concurrent first-adds do not double-spend paid API calls.
- Visualization loading moved from monolithic payload to stats plus paginated flights.
- Batched loading and simplified render tracks reduce memory/payload pressure.
- Lazy-fetch behavior is tested, including cache hit, miss, upstream failures, corpus gaps, timeouts, and concurrent fetches.

Where I would take it next:

- NATS for async backfill/worker queue if lazy fetch becomes a user-visible latency or throughput issue.
- Cassandra/Scylla-style modeling for high-write flight-position telemetry at Flighty scale, not for demo-scale relational data.
- Better single-flight detail view with route, altitude, timing, and "why this path" context.
- Production auth/privacy boundaries before any real user data.

## Cold message recommendation

Use a short message. Do not lead with a long cover letter.

Draft:

```text
Ryan,

I built a small Flighty-shaped project because your Sr. Full Stack posting is unusually close to the kind of work I like: polished iOS, messy aviation data, and backend ownership.

It is a SwiftUI/TCA + Mapbox app backed by a Kotlin/Ktor + Postgres API. It lazy-fetches real FlightAware/AeroAPI trajectories, caches them, and renders a personal flight-history globe with grouping, filters, selected-flight detail, and altitude exaggeration.

Short demo: <link>
Longer walkthrough + TestFlight + resume: <link>

If it looks relevant, I'd value 20 minutes with you or the hiring group.

Doug
```

### Message framing

Lead with:

- "I built this to see if I could do the work."
- "It is on your stack."
- "It handles real aviation data."
- "I found and fixed real backend issues."

Avoid:

- "Here is a feature you should ship."
- "I have advice for Flighty."
- Overexplaining Cassandra/NATS in the email.
- Sending a generic resume-first application without the demo.

## Resume/application updates

The generated Flighty material should be revised before sending.

Changes:

- Replace "my JVM experience is Java, not Kotlin" with a more current and precise line:
  - "My production JVM history is Java/J2EE; my current Flighty-shaped demo backend is Kotlin/Ktor, deployed and tested."
- Replace "TCA is not production experience" with:
  - "Routy uses TCA in a modular Swift package with tested reducers and dependency-injected clients; my production background adds years of unidirectional/reactive iOS architecture."
- Add a short project entry or portfolio paragraph for Routy:
  - "Built a FlightAware-backed flight-history visualization app: SwiftUI/TCA + Mapbox client, Kotlin/Ktor + Postgres backend, Fly.io deployment, Supabase cache, paginated visualization endpoints, coalesced paid API fetches, Swift and Kotlin tests."
- Keep the CLEAR aviation/FlightAware work, aviation event apps, Walmart scale/reliability, and FirefighterSpot end-to-end ownership.

## TestFlight recommendation

Include TestFlight on the landing page, but do not make TestFlight the primary hook.

Before sharing TestFlight:

- Ensure the app opens directly into the curated demo user or a polished demo path.
- Ensure runtime Mapbox token setup cannot fail for the tester.
- Avoid making Ryan choose from a generic "Travelers" list as the first experience.
- Keep the backend warm or at least make the first-load wait feel intentional.

## Concrete next steps

1. Update stale docs and generated resume material.
2. Pick/seed one coherent demo persona.
3. Add or script a guided demo path if needed.
4. Capture final screenshot set.
5. Record short hook video.
6. Record longer walkthrough video.
7. Build the tailored landing page.
8. Prepare TestFlight with direct-to-demo launch.
9. Send the cold message and apply through the official careers channel in parallel.

## Demo persona guidance

Use one coherent travel history rather than a random sampler.

Good options:

- Boston consultant:
  - frequent BOS/ORD or BOS/AUS corridor.
  - occasional West Coast flights.
  - one or two transatlantic trips.
- Austin-based product/engineering traveler:
  - AUS/ORD, AUS/SFO, AUS/JFK, occasional Europe.
- Chicago hub-heavy traveler:
  - dense ORD spokes, useful for corridor frequency.

The persona should make the visual encoding obvious:

- Repeated corridor = frequency signal.
- Recent vs old = recency signal.
- Time-of-day or airline = grouping/focus signal.
- One long flight = altitude/detail moment.

## What not to build before outreach

- Multi-user comparison.
- A full social/share model.
- Full auth/privacy system.
- Cassandra/NATS implementation just to match keywords.
- A complete single-flight production detail surface.
- More backend hardening unless it directly affects the demo.
- A broad landing page or personal portfolio site.

## Remaining technical caveats to own if asked

- Demo dates are partly synthetic/redistributed because AeroAPI search windows are short. Track geometry and flight details are the substance; be clear about date treatment.
- FlightAware/AeroAPI licensing requires care around raw payload retention; keep the raw/derivative split visible.
- No production auth/privacy model yet; this is a portfolio demo.
- Cassandra/NATS belong at scale thresholds, not in the demo by default.
- Flighty production data quality is a much harder problem than this demo; do not imply equivalence.

## Source/context links

Public sources consulted during review:

- Flighty role: https://flighty.com/careers/engineer
- Flighty About: https://flighty.com/about
- Flighty Press: https://flighty.com/press
- Flighty App Store listing: https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008
- WSJ profile: https://www.wsj.com/tech/personal-tech/flighty-app-flight-cancellations-delays-900a8aad

Local code/docs referenced:

- `/d/ivg/flighty-routes`
- `/d/ivg/flighty-routes/RoutyApp`
- `/d/ivg/flighty-routes/backend`
- `/d/ivg/flighty-routes/RoutyApp/RoutyKit/Sources/VisualizationFeature/VisualizationFeature.swift`
- `/d/ivg/flighty-routes/RoutyApp/RoutyKit/Sources/VisualizationView/GlobeView.swift`
- `/d/ivg/flighty-routes/backend/service/src/main/kotlin/com/ivygulch/flightyroutes/service/flights/LazyFetchService.kt`
- `/d/ivg/flighty-routes/backend/service/src/main/kotlin/com/ivygulch/flightyroutes/service/flights/UserFlightsRoutes.kt`
- `/d/ivg/flighty-routes/backend/service/src/main/kotlin/com/ivygulch/flightyroutes/service/flights/FlightDetailRepository.kt`
- `/d/ivg/flighty-routes/backend/service/src/test/kotlin/com/ivygulch/flightyroutes/service/flights/LazyFetchServiceTest.kt`

## Related notes

- [[Brief]]
- [[Company & Founder Research]]
- [[Outreach Plan]]
- [[_Flighty App Routy Demo MOC]]
