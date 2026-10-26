---
type: research
confidence: cited
tags: [swiftdata, coredata, persistence, ios27]
created: 2026-10-19
updated: 2026-10-19
---

# SwiftData vs Core Data Coverage

> **confidence** values: `verified` (fetched, URL in Sources) · `cited` (from a source already in the vault) · `assumed` (plausible but unchecked) · `guessed` (reasoning from priors, no source).

## Summary

As of the iOS 27 cycle, SwiftData does not do everything Core Data does. Most of the gaps from the 2023 launch are closed, but batch operations, ordered relationships, derived and fetched properties, CloudKit shared/public sync, and fine-grained merge/fault/migration control remain Core Data only.

## Details

### Gaps closed since 2023

- Model inheritance (iOS 26).
- Custom data stores via the `DataStore` protocol, and persistent history tracking (iOS 18).
- Unique constraints and indexes with `#Unique` and `#Index` (iOS 18).
- Sectioned fetches with `sectionBy:` on `@Query` (iOS 27).
- Opaque `Codable` attributes with `@Attribute(.codable)`, with limits on filtering, sorting, and migration (iOS 27).
- Observation outside SwiftUI through `ResultsObserver` and `HistoryObserver`, the rough stand-in for `NSFetchedResultsController` (iOS 27).
- Enum and composite predicates (iOS 27).

### Still Core Data only

- Batch operations. `NSBatchDeleteRequest`, `NSBatchUpdateRequest`, and `NSBatchInsertRequest` write directly to SQLite. SwiftData routes every write through a `ModelContext`, so objects are materialized.
- Ordered relationships backed by `NSOrderedSet`.
- Derived attributes computed at save time.
- Fetched properties.
- CloudKit shared and public database mirroring. SwiftData syncs only the private database, while `NSPersistentCloudKitContainer` has handled shared records since iOS 15.
- Merge-policy control, explicit faulting control, and dictionary or aggregate result types from fetch requests.
- Custom migration policies with `NSEntityMigrationPolicy`. SwiftData offers `VersionedSchema` with lightweight and custom stages, which covers less.

### Calibration

The remaining-gap list comes from secondary sources dated 2025 and 2026 and from third-party summaries of the WWDC26 session. Confidence is `cited` for the closed gaps (Apple session plus Point-Free review) and `assumed` for individual items in the still-missing list until checked against Apple's documentation.

## Sources

- [What's new in SwiftData, WWDC26 (session 274)](https://developer.apple.com/videos/play/wwdc2026/274/)
- [WWDC26 session 274 summary](https://wwdc.ai/2026/274)
- [Point-Free ep 372: WWDC26 SwiftData](https://www.pointfree.co/episodes/ep372-wwdc26-swiftdata)
- [Michael Tsai: SwiftData and Core Data at WWDC25](https://mjtsai.com/blog/2025/06/19/swiftdata-and-core-data-at-wwdc25/)
- [Core Data vs SwiftData: When Each Wins](https://llmbestpractices.com/ios/core-data-swiftdata-comparison)
- [SwiftData vs Core Data, Hacking with Swift](https://www.hackingwithswift.com/quick-start/swiftdata/swiftdata-vs-core-data)
- [SwiftData iOS 26 Production Guide](https://swiftcrafted.dev/article/swiftdata-from-zero-to-production-models-queries-migrations-and-performance)
- [Fatbobman's Swift Weekly #140](https://weekly.fatbobman.com/p/fatbobmans-swift-weekly-140)
- Web search, 2026-10-19

## Relevant To

- [[iOS 27 Features Relevant to App Ideas]]
- [[Craft/Point Free/Isolation/Isolation vs Other Architectures|Isolation vs Other Architectures]] (ModelActor discussion)
