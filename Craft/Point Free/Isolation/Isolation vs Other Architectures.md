---
type: synthesis
series: Isolation
created: 2026-10-19
---

# Isolation vs Other Architectures

Where the Point-Free isolation advice ([[Isolation Principles]]) agrees with, and departs from, other publicly promoted Swift concurrency and architecture guidance. Assessed 2026-10-19.

## Where it aligns with public guidance

- Apple's WWDC25 "Embracing Swift concurrency" says most classes should not be actors, UI-facing and model classes should stay non-Sendable or on the main actor, and you add concurrency only when profiling shows main-thread load. Same posture as [[361 - Actors]] and [[369 - MainActor Default]].
- Matt Massicotte's "Non-Sendable First Design" (December 2025) argues the identical thesis, credits nonisolated-nonsending-by-default for making it workable, and frames actors as data protection rather than background execution. His glossary calls `nonisolated(nonsending)` the main technique for avoiding Sendable types.
- Swift itself is moving their way. Both approachable-concurrency flags are slated to become language defaults, which [[365 - Approachability]] notes.

## Where it conflicts

- **Default MainActor isolation.** Apple turns it on for new Xcode 26 app projects and recommends it for app and UI modules. Point-Free say it "doesn't really carry its weight" once nonsending is default, and [[369 - MainActor Default]] shows it fighting any Sendable-inheriting protocol. A genuine disagreement about the default, not about safety. TCA26 hedges by shipping a test target that compiles under `defaultIsolation(MainActor.self)`.
- **Actor-per-service or repository-actor layering.** Clean Architecture and SwiftData guides promote a dedicated actor per repository or service, and `@ModelActor` is Apple's own version. The [[363 - Actor Reentrancy]] argument is that making mid-level objects actors leaks `await` into every call path and kills atomic operations, so they prefer one isolation shared by a whole feature graph. Massicotte's "ModelActor is Just Weird" raises the same objection to that specific case. Apple's "move networking into its own actor" advice sits in between: one actor at a real boundary, not one per layer.
- **Sendable-by-default dependency clients.** The 1.x TCA and swift-dependencies pattern of `@DependencyClient` structs with `@Sendable` closure properties, which Point-Free themselves popularized and many teams copied, is what [[369 - MainActor Default]] calls their mistake. Anyone following the 1.x skills or older Point-Free material is still being pointed at the pattern 2.0 abandons.
- **Locks as the pragmatic alternative.** A common community position is that `Mutex` or `OSAllocatedUnfairLock` is simpler and faster than actors for shared caches and services. [[358 - Legacy Locking]] through [[364 - Performance]] reject that directly, calling the performance comparison "almost never apples to apples." Apple's guidance is silent on this, so it is a Point-Free versus community disagreement, and the performance claim rests on their benchmarks under the `run`-on-executor trick.

## Where they are ahead of the field rather than in conflict

- Region-based isolation and `sending` as a routine design tool ([[366 - Regions]], [[367 - Sending Values]], [[368 - Sending Closures]]) are barely discussed outside the Swift Evolution proposals. No competing pattern contradicts it; most simply do not use it yet.
- Shared-executor actor graphs for synchronous cross-actor calls ([[363 - Actor Reentrancy]]) are novel enough that TCA 2.0 is the main worked example.

## Calibration

The Apple and Massicotte points are verified from the sources below. The characterization of Clean Architecture guidance comes from SwiftData-specific articles, so "actor per layer is widely promoted" is a reasonable inference, not a surveyed fact.

## Sources

- [Embracing Swift concurrency, WWDC25](https://developer.apple.com/videos/play/wwdc2025/268/)
- [Explore concurrency in SwiftUI, WWDC25](https://developer.apple.com/videos/play/wwdc2025/266/)
- [Non-Sendable First Design](https://www.massicotte.org/blog/non-sendable-first-design/)
- [When should you use an actor?](https://www.massicotte.org/actors/)
- [ModelActor is Just Weird](https://www.massicotte.org/model-actor/)
- [A Swift Concurrency Glossary](https://www.massicotte.org/concurrency-glossary/)
- [Concurrent Programming in SwiftData](https://fatbobman.com/en/posts/concurret-programming-in-swiftdata/)
- [Mastering SwiftData Architecture in SwiftUI](https://www.appxiom.com/blogs/swiftdata-architecture-swiftui-best-practices/)
