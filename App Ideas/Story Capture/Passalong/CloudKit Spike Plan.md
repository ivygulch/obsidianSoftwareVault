---
type: spike-plan
area: Story Capture
tags: [passalong, cloudkit, spike, technical-validation]
created: 2026-07-10
updated: 2026-07-10
status: planned
---

# Passalong — CloudKit Sharing Spike

**Purpose:** resolve [[Passalong]] kill criterion #1 before any feature code exists. The no-server privacy moat depends on CloudKit shared zones carrying the whole family-space model. If this spike fails, the idea gets re-evaluated, not rationalized around.

**Definition of done:** each scope item below ends in a written PASS / FAIL / CONSTRAINT finding in a results note (`CloudKit Spike Results.md`), and the Passalong page's kill criterion #1 gets a verdict. Spike code is throwaway — spike-quality UI is fine; findings are the deliverable.

**Total timebox: ~5 working days.** If any stage blows through its timebox by 2×, that is itself a finding (complexity signal) — stop and write it down.

## Architecture question the spike must answer first

Two candidate sync layers; the spike picks one:

- **Arm A — raw CloudKit:** custom zone in the private database, zone-wide `CKShare`, `CKSyncEngine` (iOS 17+) for delta sync, `CKAsset` for audio.
- **Arm B — SQLiteData `SyncEngine`** (Point-Free): advertises SQLite-to-CloudKit sync *including sharing records with other iCloud users*. If its sharing model supports a whole-space share (one share, many participants, assets included), it collapses most of Arm A's plumbing into the stack already in use (TCA/SPM/pfw). Advertised capability — verify, don't trust.

Run Arm B's evaluation first (Stage 1); it's a half-day read-and-prototype against a library you already have skills coverage for. If B can express the model, run the remaining stages on B with spot-checks of the underlying CK behavior. If not, proceed on A. Either way, record *why*.

## Data model for the spike (minimal)

One custom zone = one family space. Records: `Space` (root/metadata), `Entitlement` (activeThrough date, written only by organizer), `Question` (text, askedBy, askedOf), `Story` (answer: audio `CKAsset` + duration + optional transcript stub). Two test devices minimum, three ideal: **Organizer** (your Apple ID), **Elder** (second Apple ID, different Apple Family group — critical), **Kid/observer** (third Apple ID if available). Dev builds on physical devices; note that share links in the CloudKit *development* environment only resolve for dev-build devices — do invite testing accordingly.

## Stages

### Stage 1 — Sync-layer decision (0.5 day)
Read SQLiteData SyncEngine's sharing API against the model above. Questions: Can a share cover the whole space (zone-wide or root-hierarchy) rather than per-record? Do `CKAsset`-scale blobs ride it? Can a non-owner write records (kid asks a question) into the shared space? What iOS floor does it impose?
**Output:** Arm A or Arm B, with reasons. No pass/fail — this is a fork, not a gate. Note the stakes beyond plumbing: Arm B's SQLite-as-source-of-truth posture is also the Android-later hedge (see the guardrails section in [[Passalong]]) — if Arm A wins, the spike write-up must say how CK types stay quarantined anyway.
**→ DONE 2026-07-13: Arm B selected.** See [[CloudKit Spike Results]] Stage 1 — includes the single-FK tree schema constraint, automatic BLOB→CKAsset confirmation, and the no-per-record-ACL finding that amends Stage 5.

### Stage 2 — Shared space + audio round-trip (1 day) → scope (a)
Organizer creates space, shares to Elder, both devices exchange: Elder records audio answers at realistic sizes — 1 min (~1 MB), 10 min (~10 MB), 45 min (~45 MB AAC) — Organizer receives; Kid (or Organizer) sends questions the other direction. Measure upload/download times on Wi-Fi and on LTE (or Link Conditioner "3G" profile). Test mid-transfer interruptions: airplane mode during upload, app kill during download.
**PASS:** all sizes round-trip reliably; interrupted transfers recover without data loss; a 45-min story syncs on LTE in single-digit minutes.
**FAIL:** silent asset loss, unrecoverable partial syncs, or zone/share limits that cap a realistic family archive.

### Stage 3 — Invite/accept across Apple IDs (0.5 day) → scope (b)
Organizer invites Elder via share link in Messages (`ShareLink`/`CKShareTransferRepresentation`, or SQLiteData's equivalent; note `UICloudSharingController` deprecation status). Elder's device: tap link → app opens → space visible. Count every tap and decision from message-received to first-question-visible. Then revoke access and re-invite; remove a participant; test acceptance when the app is NOT yet installed (what does the link do?).
**PASS:** ≤3 comprehensible steps post-install for a non-technical elder; revoke/re-invite works; the not-installed path is at least explainable ("install first, then tap again").
**FAIL:** flows that require the elder to understand iCloud, or acceptance dead-ends.

### Stage 4 — Storage accounting (0.5 day) → scope (c)
After Stage 2's assets exist: on both devices check Settings → Apple ID → iCloud → Manage Storage. Confirm assets bill the **zone owner** (Organizer) and the participant's quota is untouched. Record actual MB per story length → project a 100-story archive. Document (don't necessarily reproduce) over-quota behavior: expected `CKError.quotaExceeded` on save — write the handling policy (block new recordings with clear message; never lose a local recording because the cloud is full — local-first means the recording already exists on disk).
**PASS:** billing lands on the organizer as designed and a 100-story audio archive stays trivially small relative to typical iCloud plans (~50 GB base tier).
**CONSTRAINT finding if:** billing model differs from expectation — that rewrites onboarding copy and possibly the whole storage story.

### Stage 5 — Entitlement propagation (0.5 day) → scope (d)
Organizer flips `Entitlement.activeThrough`; measure time-to-visible on Elder's device via (i) silent push (database subscription / sync-engine notification) and (ii) foreground fetch. ~~Also verify a participant cannot modify the entitlement record~~ **Amended per Stage 1 finding:** CloudKit share permissions are per-participant for the whole share — no per-record ACL exists, so a readWrite participant *can* technically edit the entitlement row. Accepted (same threat model as receipt spoofing: a family hacking its own pass). The stage instead documents the write model honestly and confirms app-level gating ignores participant-written entitlement changes where feasible.
**PASS:** foreground fetch reflects the change in seconds; push arrives typically <1 min; the accepted write-model is documented in the results.
**Design note to confirm in writing:** feature gating uses last-known-value with a grace window, so propagation latency can never lock a grandmother out mid-recording.

### Stage 6 — No-Apple-device fallback (0.5 day, research not code) → scope (e)
Desk research with a short written conclusion: what can a relative with no Apple device/account get? Check current CloudKit web/JS reality (CloudKit JS against a shared database requires Apple ID web auth — a no-Apple-ID relative likely cannot join a private share at all). Enumerate the actual options: organizer-exported audio bundles, a future minimal web service (breaks no-server), or accepting iOS-only membership with export as the escape hatch.
**Output:** a constraint statement for the Passalong page — this stage cannot FAIL the spike, but it must kill any hand-waving about "we'll add web later."

### Stage 7 — Organizer-death survivability (0.5 day) → follow-up question
CloudKit has no zone-ownership transfer. Test the workaround: as a *participant*, fetch every record and asset from the shared zone and re-import into a new zone the participant owns (becoming the new organizer). Measure effort and completeness (do assets survive re-upload; do relationships rebuild).
**PASS:** a participant-run export→reimport rebuilds the space without the original owner's account.
**FAIL finding if:** participants can't read enough to reconstruct — that forces routine export snapshots as a design requirement, which is worth knowing now.

### Stage 8 — Write-up (0.5 day)
`CloudKit Spike Results.md` in this folder: verdict per stage, measured numbers (sync times, quota MB, propagation latency, invite tap-counts), the Arm A/B decision and its reasons, and a one-paragraph go/no-go against kill criterion #1. Update [[Passalong]] — either clear the kill criterion or invoke it honestly.

## Known gotchas to watch for (so they don't burn timebox)

- **Dev vs production environment:** share links, subscriptions, and quotas behave differently across CloudKit environments; the spike runs in development — flag any finding that might differ in production rather than re-verifying everything.
- **Zone-wide sharing requires a custom zone in the private DB** — the default zone cannot be shared. Participants see it through their *shared* database, which has its own subscription type.
- **Asset chunking/timeout on large files over cellular** — if 45-min uploads misbehave, test whether background `CKOperation` configuration (long-lived operations, `qualityOfService`) fixes it before declaring FAIL.
- **Second Apple ID hygiene:** the Elder test account must genuinely be outside your Apple Family group, or Stage 3 tests the wrong thing.
- **Simulator lies about CloudKit sharing** — physical devices only for Stages 2–5.

## Explicitly out of scope

Recording UX, audio quality/codec choices beyond size math, transcription, StoreKit purchase flow (the entitlement *record* is in scope; the *purchase* that writes it is not), Android/web clients, TestFlight distribution.

## Related

- [[Passalong]] — kill criterion #1 defines this spike's authority
- [[../../../Research/Competitors/Family Story & Legacy Capture Apps — Landscape]] — why reliability and ownership are the moat
