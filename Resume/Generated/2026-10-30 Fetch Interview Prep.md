# Fetch — Interview Prep: Technical Interview

- **Created**: 2026-10-30
- **Company**: Fetch (Fetch Rewards)
- **Job title**: Senior iOS Engineer I
- **Interview**: Stage 2 technical interview, Monday 2026-11-02, 10:00–11:00 AM ET, with Tyler Weidel (Sr iOS Eng I), Zoom. Live collaborative coding in own IDE, AI tools visible on a shared whole-screen share. Xcode + Swift 6.2. Private repos closed. Zoom Notetaker transcribes unless opted out by reply.
- **Recruiter steer**: "the tech interviews will definitely focus on modern swift concurrency, actors, isolation, when to use what, etc."
- **Materials**: `/d/dl/Interview Guide - iOS.pdf`, `/d/dl/3 Steps to a Fantastic Fetch Interview..pdf`, `/d/dl/IDE_AI Tooling Extension Set Up.pdf`
- **Related**: [[Walmart - Checkout Platform 2021-2026]], [[CLEAR - Senior iOS Subcontract 2026-present]], [[Isolation Principles]], [[Isolation vs Other Architectures]]

## Preparation plan

### Thursday evening: environment

- Clean sample package, `swift-tools-version 6.2`, Swift 6 language mode, approachable-concurrency flags on (default MainActor isolation, `NonisolatedNonsendingByDefault`) so defaults match what Fetch will have.
- One AI tool on screen, signed in and tested on that package (Claude Code beside Xcode, or in VS Code). A claude.ai browser tab as the fallback the setup guide asks for.
- Whole-screen share: close the vault, Mail, private repos, and the TCA26 beta checkout. Zoom test at zoom.us/test with the share running.
- Decide on the Zoom Notetaker opt-out.

### Friday: six exercises, written from scratch, talking aloud, AI assisting

1. Wrap a completion-handler API with `withCheckedThrowingContinuation`, then add cancellation with `withTaskCancellationHandler`. Why resume exactly once; what happens if it never resumes.
2. An actor with in-flight deduplication (cache storing the `Task` and awaiting it). The reentrancy exercise: state can change across every `await` inside an actor, and that is not a data race.
3. A retrying API client: exponential backoff, jitter, retry budget, cancellation that stops the loop. When Combine's `retry` would be used instead.
4. Fix a data race in a class three ways: actor, `Mutex` from Synchronization, `MainActor` confinement. When each is right.
5. Bridge a delegate-based API into an `AsyncStream`, buffering policy chosen on purpose, continuation finished on deinit.
6. Test an actor with Swift Testing: controllable clock, `confirmation`, a test proving the dedup in exercise 2 dedups.

Concepts to explain in one or two sentences each: structured vs unstructured tasks and why `Task {}` in an initializer is a smell; task groups and error propagation; `Sendable`, `sending`, region-based isolation; `nonisolated(nonsending)` and `@concurrent` in Swift 6.2; `Task.immediate`; `isolated` parameters and `#isolation`; `assumeIsolated` and when it is a lie; global actors and custom executors; backpressure in Combine vs demand in `AsyncSequence`. Point-Free's "most types should not be Sendable" position is defensible and aligns with Apple's 6.2 direction; lead with the standard framing and offer it as a tradeoff.

### Saturday and Sunday: rehearse the format

- Saturday: two timed 25-minute drills on a generated 150-line view model with five concurrency defects (unstructured task in `init`, non-Sendable capture in `Task.detached`, missing cancellation, dispatch queue mixed with an actor, double fetch from reentrancy). Review, narrate, prioritize, fix, with the AI visibly assisting and visibly checked. Record the first with QuickTime and watch it.
- Saturday, one hour: tradeoff lines from own work for architecture, state management, networking, testing, UX. Material: the Walmart unidirectional MVVM-C system, the TCA client and Kotlin backend split on Flighty Routes, offline-first SQLite plus CloudKit on Get Wisdom, the TCA 2.0 beta work. One decision, its cost, what would change, each.
- Sunday: one full hour-long simulation including setup minutes. Install the Fetch app and scan a receipt. Three questions for Tyler. Stop early.

### Monday morning

Ten minutes before: open the sample package, confirm the AI tool answers a prompt, start Zoom early with the share ready. Ask clarifying questions before touching code, say the plan out loud, read AI output aloud and say what is being checked before accepting it.

## SOLID and Clean Architecture

Worked through 2026-10-30 against the SOLID summary at geeksforgeeks and Martin's 2012 post [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

### Liskov Substitution, the rectangle and square

The violation only appears once `Rectangle` has mutable width and height. The base class promises that setting one dimension leaves the other alone, so `area` is width times height after `setWidth(5); setHeight(4)`. A `Square` subclass must override both setters to change both dimensions, so the same two calls produce 4×4 and the assertion that held for every `Rectangle` fails. The caller never mentioned squares; the subclass changed the observable behavior of the base type's methods. "A square is a rectangle" is true of values, not of a mutable type with setters. Passing fixes: make both immutable, or drop inheritance for a shared `Shape` protocol with `area`.

### Dependency Inversion vs Clean Architecture

DIP is a rule about one dependency edge: high-level modules and low-level modules both depend on abstractions, and the abstraction is owned by the high-level side. Clean Architecture is DIP applied at every boundary of a system, plus a layering scheme (Entities, Use Cases, Interface Adapters, Frameworks and Drivers), the inward Dependency Rule, and a rule that only plain data crosses a boundary. You can follow DIP without layering, and a Clean folder structure can still violate DIP.

### The adapter-to-driver edge

Martin's post says no code inward of Interface Adapters knows about the database, and in the same paragraph puts all the SQL in the adapters ring. So the adapters do depend on the ring outside them. The post's reconciliation: the outer ring is mostly vendor code plus `main` ("you don't write much code in this layer other than glue code"), the adapter is the designated knower of the external system's shape, and the rule's teeth are on the inner rings. A strictly inward version applies DIP once more: the adapter defines a storage protocol and an outermost type implements it against the driver. Martin's post and the 2017 book do not do this.

### The Walmart system in Martin's terms

What it was: utilities and raw networking; a data service layer wrapping GraphQL calls behind primitives and simple structs, returning plain data-model structs with no GraphQL leaking out; other service layers encapsulating other external systems the same way; view controllers and views with one view model in and one delegate protocol out; a coordinator per feature (plus a bootstrap coordinator) watching Combine streams, converting data models to view models, assigning delegates, and wiring calls. Unidirectional, Redux-style flow. No local database; the Node.js server behind GraphQL owned the domain rules.

Mapping, app alone:

| Martin's ring | Walmart layer | Note |
|---|---|---|
| Entities | Data-model structs | Thin, data only; depended on nothing, consumed by every outer ring |
| Use Cases | Coordinators | Also did Presenter (data model to view model) and `main` (wiring, delegate assignment) |
| Interface Adapters | Data service and other service layers | Gateways; GraphQL in place of Martin's SQL, confined to this ring |
| Presentation detail | View models, view controllers, views | Humble views: one input, one output |
| Frameworks and Drivers | Utilities, raw networking, GraphQL client | |

Mapping, whole system: the Node server held the Entities and most Use Cases; the iOS app sat in the outer rings as an adapter for GraphQL plus presentation, with coordinators as client-side use cases for screen sequencing and local concerns the server did not care about.

Points settled in the discussion:

- The services layer is not the Entities ring, because ring assignment follows dependencies: code that imports the networking utilities and issues queries is outer to code that does not. The services module contained two rings, the entity types and the gateway that produced them.
- GraphQL schema definitions are not Entities either. They are an external contract owned by the backend; using them as the center would point the Dependency Rule outward. The plain structs the services returned were where the app asserted its own entity shapes.
- The coordinator spanning three roles is a packaging choice, not a dependency-direction problem. Its cost is that orchestration cannot be tested without also constructing the view-model mapping and wiring.
- Unidirectional and Redux-style flow are orthogonal to Martin; he says nothing about state flow.
- The business rules Martin expects at the center lived on the Node server, applied before data reached the app.

### One-paragraph version for the interview

The Walmart checkout app was unidirectional MVVM-C with Clean Architecture's boundary discipline. Plain data-model structs were the center; service layers were gateways that kept GraphQL from leaking past them; coordinators were the use cases, one per feature, and also did presenting and wiring; views were humble with one view model in and one delegate out. The enterprise rules lived on the Node server, so the entity ring in the app was thin by design. The one place it departed from Martin was the coordinator holding three of his roles in one object, which was the main testability cost.
