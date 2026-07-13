---
type: spike-results
area: Story Capture
tags: [passalong, cloudkit, sqlitedata, spike, stage-1]
created: 2026-07-13
updated: 2026-07-13
status: in-progress
---

# Passalong — CloudKit Spike Results

Companion to [[CloudKit Spike Plan]]. One section per stage; verdicts marked PASS / FAIL / CONSTRAINT / PENDING.

## Stage 1 — Sync-layer decision: **Arm B (SQLiteData SyncEngine)** ✅

Desk evaluation 2026-07-13 against the library's own documentation (skill reference + `CloudKitSharing.md` / `CloudKitSync.md` from the repo, fetched same day). Verdict: **Arm B is viable and preferred.** Hands-on stages run on Arm B, with the constraints below baked into the schema from the start.

### Question-by-question

**Can a share cover the whole space? YES, with a hard schema constraint.** `SyncEngine.share(record:)` shares a *root record* (a table with **no foreign keys**) plus all its associations, recursively. The rule: every shared association must have **exactly one foreign key**, directly or transitively pointing at the root — the shared schema must be a strict tree. Many-to-many relationships (any table with two FKs) silently drop out of sharing entirely.

*Consequence for Passalong:* `Space` is the root. But `Question` naturally wants member references (`askedBy`, `askedOf`) **in addition to** `spaceID` — declared as foreign keys, those would make Question a multi-FK table and exclude it from sharing. The workaround is to store member references as plain UUID columns without `REFERENCES` clauses (app-enforced integrity, no schema-level FK). Same applies anywhere else a record wants to point at two things. This is the single biggest design consequence of Arm B.

Sketch that satisfies the tree rule:

```
Space (root, no FKs)
├── Person (spaceID FK; display name, photo; optional accountUserID —
│            a Person may have no device/account, e.g. the v1 storyteller;
│            kinship/role is NOT a column — roles are per-story)
├── Entitlement (spaceID FK = PRIMARY KEY; activeThrough)   ← one-to-at-most-one pattern
└── Question (spaceID FK; askedOf as optional plain UUID → Person)
    ├── QuestionAsker (questionID FK; askerPersonID plain UUID → Person)   ← many askers per question
    └── Story (questionID FK; duration, transcript text)
        ├── StoryTeller (storyID FK; tellerPersonID plain UUID → Person)   ← many tellers per story
        └── StoryAudio (storyID FK = PRIMARY KEY; audio BLOB) ← asset table pattern
```

_(Sketch updated 2026-07-13, twice. First: `Person` replaces `Member` per the association-agnostic + elder-no-device decisions — account-holding members and device-less storytellers are one table; roles are per-story, never a person type. Second: **multiple tellers per story and multiple askers per question** via `StoryTeller` / `QuestionAsker` child tables. This is the general recipe for many-to-many under the single-FK tree rule: the child row's one real FK points up the tree (so it shares/syncs), and the Person side is a plain-UUID reference (app-enforced integrity). Bonus over a JSON-array column: each association is its own row, so two kids adding themselves as askers from different devices **merge naturally instead of last-write-wins clobbering an array** — a real sync-correctness win, not just style.)_

**Do audio-scale blobs ride it? YES — first-party answer.** From the library docs, verbatim: *"The library packages all BLOB columns in a table into CKAssets and seamlessly decodes CKAssets back into your tables."* Docs explicitly recommend the separate-asset-table pattern (`StoryAudio` above). CKAsset limits are effectively unbounded for our sizes. Stage 2 still must verify real-device behavior at 45-minute sizes with interruptions — the mechanism exists; the reliability numbers don't yet.

**Can a non-owner write (kid sends a question)? YES.** CKShare read-write permission is enforced by the library at local write time (`SyncEngine.writePermissionError` on violation), and permission state is queryable via `SyncMetadata` to hide UI pre-emptively. Participants with readWrite create and edit records in the shared space.

**Can the entitlement record be owner-writable / participant-readable? NO — and this is a CloudKit constraint, not a library gap.** Share permissions are per-participant for the *whole share*; there is no per-record ACL. A readWrite participant (which the kids must be) can technically edit the `Entitlement` row. Options considered: (a) accept it — client-side policy enforcement, identical threat model to the already-accepted StoreKit-receipt spoofing (a family hacking its own pass is a non-problem); (b) `privateTables` would keep Entitlement un-shared, but then participants can't read it and gating breaks. **Decision: (a), accept and document.** The spike plan's Stage 5 expectation is amended accordingly — the stage now verifies propagation latency and *documents* the write-model honestly instead of asserting an enforcement CloudKit can't provide.

**iOS floor imposed:** iOS 17 (CKSyncEngine underneath) — irrelevant under the iOS 26 floor already chosen.

### Additional findings worth carrying forward

- **Invite/accept is provided machinery:** `CloudSharingView` (UICloudSharingController wrapper) for the organizer; `acceptShare(metadata:)` + scene-delegate hooks for the joiner; `CKSharingSupported` Info.plist key required. Stage 3's elder tap-count test runs against system UI, not custom code.
- **Un-sharing / participant removal** flows through the same `CloudSharingView` ("Stop sharing").
- **`privateTables`** gives per-user-private sibling tables (synced to your devices, never shared) — useful later for drafts or personal notes on a story; also the documented pattern for per-user data like ordering.
- **`startImmediately: false`** on SyncEngine init — sync as an explicitly gated feature if ever needed.
- **Schema restrictions to respect from day one:** no compound primary keys; no unique indexes other than the PK (uniqueness becomes app logic); avoid CloudKit-reserved column names (`creationDate`, `modificationDate`, `recordID`, …).
- **Stage 7 outlook improved:** every participant holds a full local SQLite replica of the shared data, so organizer-death recovery ("export and rebuild under a new owner") is a local-database copy into a new `Space`, not a CloudKit fetch-everything exercise. Still needs the hands-on test, but Arm B makes it structurally easier.

### Why Arm B over raw CloudKit

Same underlying CKShare/CKSyncEngine semantics either way (the tree rule and no-per-record-ACL are CloudKit facts, not library choices), but Arm B adds: SQLite as source of truth (the Android-later guardrail, satisfied by construction), automatic BLOB→CKAsset packaging, local permission enforcement, provided share/accept UI, queryable sync metadata, and the observation tooling (`@FetchAll`) the app would want anyway. Raw CloudKit would re-implement all of that to end up at the same constraints. No finding argued for Arm A.

### Stages 2–8: PENDING (hands-on, Doug in Xcode)

Nothing in Stage 1 removes any hands-on stage. The measured questions remain: asset sync reliability at size with interruptions (2), elder invite tap-count across Apple IDs (3), quota accounting to the organizer (4), entitlement propagation latency (5, amended), no-Apple-device constraint statement (6, desk), participant-run space rebuild (7).
