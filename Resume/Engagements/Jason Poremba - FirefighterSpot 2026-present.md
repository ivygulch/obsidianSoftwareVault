---
type: engagement
company: "[[Jason Poremba]]"
brand: "FirefighterSpot"
role: "Lead iOS Engineer & Architect"
employment: independent
start: 2026-02
end: 2026-06
concurrent_with: ["[[CLEAR - Senior iOS Subcontract 2026-present]]"]
industry: [Public Safety, Fire Service, Nonprofit, Mobile Applications]
team_size: "solo"
team_context: "sole engineer with individual client"
scale: "initial requirements to shipped v1.0 and a 1.0.1 maintenance release"
tech: [Swift, Swift 6, Swift Concurrency, SwiftUI, SwiftData, MapKit, Core Location, UserNotifications, VisionKit, Swift Package Manager, SwiftLint, Supabase, Supabase Realtime, PostgreSQL, Local-First, Offline-First, Data Synchronization, Swift Testing, XCTest, XCUITest, OSLog, GitHub Spec Kit, Claude Code, Codex, XcodeBuildMCP]
practices: [iOS Architecture, Local-First Architecture, Offline-First Architecture, Data Synchronization, Conflict Resolution, SPM Modularization, MVVM, Protocol-Oriented Services, Spec-First Development, Agentic Development, Backend Integration, Backend Operations, Release Management, Technical Documentation, Customer Issue Troubleshooting]
themes: [public-safety, fire-service, agentic-tooling, solo, spec-first, local-first, offline-first, sync, maps, location, notifications, modularization]
deliverables: [firefighterspot-ios-app, firefighterspot-supabase-backend, firefighterspot-user-guide, firefighterspot-admin-guide]
status: past
created: 2026-04-22
updated: 2026-10-20
---

# Jason Poremba - FirefighterSpot 2026-present

## Context

Independent engagement on FirefighterSpot, an iOS incident-command and personnel-accountability app for volunteer fire departments. Personally funded by the client (Jason Poremba) — distinct from his architecture firm's work. Contracted via Upwork. Took the app from initial customer requirements to a shipped version 1.0 (February–May 2026), then a 1.0.1 maintenance release driven by client bug reports (June 2026). The app is offline-first: every action writes local storage first and sync is treated as a bonus. An Incident Commander (IC) device is the system of record during an active incident; Unit Commander (UC) devices join by code or QR and sync when connectivity allows. Built spec-first, with GitHub Spec Kit generating specifications and Claude Code assisting implementation; 238 numbered specs and 662 commits between January 25 and June 5, 2026.

## Role

Lead iOS engineer and architect, sole engineer on the engagement. Translated non-technical customer requirements into formal specifications, designed and implemented an offline-first SwiftUI client with cross-device synchronization, built and operated the Supabase backend (schema, migrations, seed data, Realtime), covered the client with Swift Testing, wrote the user and admin guides, and iterated with the client and volunteer-fire-department stakeholders through v1.0 and a post-release maintenance cycle.

## Achievements

- Delivered a working iOS incident-command and accountability app for volunteer fire departments from initial customer requirements through shipped v1.0 and a 1.0.1 maintenance release, owning client, backend, and rollout end-to-end. #ios #end-to-end #public-safety #rollout #release-management
- Translated non-technical customer requirements into formal specifications (238 numbered specs) before implementation, iterating with the client and volunteer-fire-department stakeholders. #spec-first #requirements #stakeholder-engagement
- Designed an offline-first architecture: every operation writes to local SwiftData storage first, with background synchronization to Supabase when connectivity returns and the IC device authoritative during an active incident. #offline-first #local-first #architecture #swiftdata #sync
- Built a bidirectional SwiftData-to-Supabase sync engine with a persisted pending-upload queue, a Supabase Realtime channel subscription for live updates, last-write-wins conflict resolution on update timestamps, soft-delete tombstones so deletions survive reconnect, orphan cleanup, and a server schema-version flag that forces a stale-data reset. #sync #conflict-resolution #supabase #realtime #data-synchronization #backend-integration
- Implemented offline join: a Unit Commander with no signal enters a 4-digit code, operates against a local placeholder incident, and the sync engine reconciles the placeholder to the real incident when connectivity returns. #offline-first #sync #ux
- Built QR-code unit transfer (VisionKit scanner, CoreImage generator) so an IC without connectivity can add a UC's unit, including a conflict-resolution sheet when the unit already exists locally. #offline-first #visionkit #qr #conflict-resolution
- Wrapped CLLocationManager in an async/await LocationService using checked continuations for authorization and location fixes, with on-device permission handling and GPS centering. #core-location #swift-concurrency #location
- Built the MapKit incident map: unit pins with drag-to-reposition and long-press add, incident radius overlay, hydrant layer loaded off the main thread, and inline address search with MKLocalSearchCompleter. #mapkit #maps #performance
- Implemented the Personnel Accountability Report (PAR) workflow as an explicit IC-driven state machine (MAYDAY, Emergency, Tactical Benchmark, Scheduled) with UC digital acknowledgment synced in real time. #public-safety #state-machine #feature-delivery
- Made the PAR-due timer resilient to backgrounding by computing the deadline from wall-clock time, recovering on scene-phase changes, and scheduling a UserNotifications local notification so the IC is alerted while the app is backgrounded or the device is locked. #usernotifications #background-resilience #reliability
- Structured the app as 16 Swift Package Manager modules behind a thin app shell (one module per feature, protocol-first services, ViewModel plus ActionHandler pattern) with SwiftLint enforced as a build plugin and Swift 6 strict concurrency throughout. #architecture #modularization #spm #mvvm #swift6 #swift-concurrency
- Covered the client with 433 Swift Testing test functions across 15 test targets using in-memory SwiftData, plus XCTest and an XCUITest flow. #swift-testing #xctest #xcuitest #testing
- Parallelized the initial sync fetch with async let, replacing 11 sequential network requests with concurrent reads before a dependency-ordered apply phase. #performance #swift-concurrency #sync
- Diagnosed and fixed client-reported production issues from verbatim bug reports to root cause to spec to fix (timer not firing while backgrounded, deleted roster members resurrected by sync). #troubleshooting #customer-issues #maintenance
- Built and operated the Supabase backend: PostgreSQL schema mirroring the SwiftData models, migrations, seed data, and credential handling via a gitignored xcconfig flowing into Info.plist. #supabase #postgresql #backend #security
- Wrote the user guide and admin guide (markdown, docx, pdf), a technical architecture guide, and per-release notes surfaced in-app on first launch; tagged releases 0.3 through 1.0.1. #technical-documentation #release-management
- Made extensive use of Claude Code, Codex, XcodeBuildMCP, and other AI tools to build out the system; used GitHub Spec Kit to drive spec-first development and Claude Code for implementation, applying agentic tooling across the lifecycle. #agentic-tooling #agentic-development #spec-first #claude-code

## Tech Stack

Swift 6 with strict concurrency, SwiftUI, SwiftData (local persistence), MapKit and Core Location (incident map, GPS), UserNotifications (local PAR-due alerts), VisionKit and CoreImage (QR transfer), Swift Package Manager (16 modules), SwiftLint build plugin, Supabase Swift SDK (PostgREST, Realtime) over PostgreSQL, OSLog, Swift Testing, XCTest, XCUITest, GitHub Spec Kit, Claude Code, Codex, XcodeBuildMCP.

## Private Notes

_Repo investigated 2026-10-20 at `/c/jasonthomas/projects/FirefighterSpot/` for the First Due generation; the Achievements above are drawn from the code, specs, release tags, and docs there. Counts (238 specs, 662 commits, 433 @Test functions, 16 modules, 204 source files, ~19.4K lines) are as of the 1.0.1 commit on 2026-06-05._

_Not in the repo (do not claim from this engagement): BGTaskScheduler or background modes; Firebase, Crashlytics, Luciq, or any analytics SDK (logging is OSLog only); Fastlane, GitHub Actions, or any CI config; TestFlight; user sign-in (Supabase anon key only). Per Doug (2026-10-20), those JD items are covered by Walmart, CLEAR, and other engagements._

_Swift version: Package.swift and the project CLAUDE.md say Swift 6.0 with strict concurrency, not 6.2. Resume copy says "Swift 6 concurrency," which is accurate; do not say 6.2 for this engagement._

_End date: previously recorded as 2026-05 (v1.0). Repo shows 1.0 finalized, then 1.0.1 and client-reported fixes through 2026-06-05, so `end` is now 2026-06. The RevenueCat-era resume baseline and `Career Preferences.md` still say February–May 2026; update them when next regenerating if the June maintenance month should show._

_Client: Jason Poremba (jason@jasonthomasarchitect.com) — architect by profession, principal of Jason Thomas Architect. FirefighterSpot is a personal project separate from his firm. Contract through Upwork. Initial client contact 2026-01-08, contract 2026-01-12; first commit 2026-01-25; active development and v1.0 delivery are framed as February–May 2026 (user and admin guides delivered 2026-04-21). Supabase project experienced an ops pause 2026-04-19. A `v2/` folder with client questions exists in the repo; no v2 work is recorded here._

_The earlier "~30 days to prototype / ~5x time-to-market" framing was retired — it conflicts with the February–May v1.0 timeline and was a rough self-comparison, not a measured benchmark. Do not reintroduce it._

_Filename and H1 still read "2026-present"; left unchanged to avoid breaking inbound wikilinks ([[Jason Poremba - FirefighterSpot 2026-present]]) from the Framing pillars and the CLEAR engagement. Status is past (ended 2026-06)._

## Related

- Company: [[Jason Poremba]]
- Concurrent engagement: [[CLEAR - Senior iOS Subcontract 2026-present]]
- Skills: _(to be linked once Skills/ pages exist)_
