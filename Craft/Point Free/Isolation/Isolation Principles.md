---
type: synthesis
series: Isolation
created: 2026-10-19
---

# Isolation Principles

Key principles distilled from the Point-Free Isolation series (episodes 355–369). Episode numbers in parentheses point to the transcript notes in this folder.

## What isolation is for

- The goal of Swift concurrency is that strict-mode code is free of data races unless you use an escape hatch. Race conditions are a broader class and remain your responsibility. ([[357 - What Is It]])
- An isolation domain is the unit of safety. Every piece of mutable state belongs to exactly one domain, and crossing domains is where the compiler inserts checks. ([[357 - What Is It]], [[361 - Actors]])

## Locks are a crude, local tool

- Locks protect individual accesses, so they spread through every method, obscure the logic, and are not reentrant, which blocks ordinary refactoring into helpers. Recursive locks only trade deadlocks for other bugs. ([[358 - Legacy Locking]], [[359 - OSAllocatedUnfairLock]])
- A lock on a Sendable container does nothing for non-Sendable objects it hands out. The `account(for:)` escape compiled cleanly and was still a data race. ([[358 - Legacy Locking]], [[360 - Mutex]])
- `Mutex` improves on `OSAllocatedUnfairLock` by using `sending` instead of `@Sendable`, so you can capture and return non-Sendable values as long as they are never touched again afterward. ([[360 - Mutex]])

## Actors give static, compiler-enforced isolation

- Inside an actor you get unfettered synchronous access with no locking and no deadlocks. The price is proving you are in the domain, usually by awaiting. ([[361 - Actors]])
- Every `await` on an actor is a potential interleaving point. Reduce them by batching work into a single enqueued job, and eliminate them entirely by running work on the actor's executor. ([[362 - Actor Enqueuing]])
- Reentrancy enters when an actor does async work. Making leaf objects into actors leaks suspension points everywhere and destroys atomic operations. Instead, let actors share one isolation so they talk synchronously, and make the outside world await once at the boundary. ([[363 - Actor Reentrancy]])
- Actors are not slower than locks when used correctly. Proving isolation once and then doing a lot of synchronous work beats locking on every access, and only actors can offer that from the outside. ([[364 - Performance]])

## Keep things non-Sendable

- Sendability is rare and surgical. Non-Sendable objects are the strength of the model: lock-free access plus a compiler proof that they never leak across domains. Avoid Sendable on protocols too. ([[361 - Actors]], [[369 - MainActor Default]])
- `nonisolated(nonsending)` makes async methods on non-Sendable objects inherit the caller's isolation instead of hopping to the global concurrent executor. Turn on `NonisolatedNonsendingByDefault` rather than annotating per method. ([[365 - Approachability]])
- Isolated conformances let a global-actor type conform to a nonisolated protocol. Sendable-inheriting protocols fight this and force the conformance into an extension. ([[365 - Approachability]], [[369 - MainActor Default]])

## Regions and sending move values instead of making them shareable

- Each non-Sendable value lives in a region: disconnected, task-isolated, actor-isolated, or invalid. Aliasing merges regions, and passing a value into an actor moves it there. ([[366 - Regions]])
- `sending` disconnects a value from its region so it can cross a boundary once. After that the original reference is unusable. Branches are analyzed per path, but loops cannot send because the compiler cannot count iterations. ([[366 - Regions]], [[367 - Sending Values]])
- Sendable `let` constants can be read off a non-Sendable object from any region. ([[367 - Sending Values]])
- `sending` on a closure's arguments, its return value, and the closure itself each mean something different. A function cannot return two values in one region if they must go to different owners. ([[368 - Sending Closures]])

## Defaults

- Default MainActor isolation is a per-target switch that simplifies UI code, but with nonsending becoming the default they judge it does not carry its weight, and it conflicts with any Sendable conformance. ([[368 - Sending Closures]], [[369 - MainActor Default]])
- The TCA 2.0 design is the payoff: the store fixes one isolation for the whole feature lifecycle, from action send through state update to effect start, which is what makes synchronous deterministic tests possible with no yields. ([[355 - Isolation, ~Copyable, ~Escapable]], [[356 - Superpowers]], [[363 - Actor Reentrancy]])
