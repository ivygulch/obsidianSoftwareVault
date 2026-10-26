---
type: spec-qa
project: FirefighterSpot v1.1
created: 2026-10-22
updated: 2026-10-22
status: open
---

# FirefighterSpot v1.1 — Specification Q&A

Fill in each **A:** line. Leave blank or write "defer" for anything not decided yet.

Scope change 2026-10-22: multi-organization structure dropped. v1.1 is single-org (the current department) plus a simple account table and sign-in. The org dropdown, org-admin tier, and org-creation screen are out. The earlier multi-org questions are kept at the bottom under "Parked" for when orgs come back.

## Baseline (from the 1.0.1 repo)

- No sign-in: Supabase anon key only, every table has an RLS policy of "Allow all".
- `departments` is the root table; one department (Southampton) is seeded.
- Every device fetches all departments, units, crew, apparatus, and incidents on sync.
- First screen is role selection: Create Incident (IC), Join Incident (UC), or rejoin an active incident.
- Settings → Manage Data lets anyone edit departments, units, crew, apparatus, and companies.
- No TestFlight, App Store, or CI history in the repo. Distribution to date was direct install.
- Hydrant data is Southampton-specific and loaded as global reference data.

## v1.1 goals (revised)

- Release to App Store.
- Single org: the current department. No org selection in the app.
- Simple account table on the backend.
- Sign-in screen with a "Request account" button that opens the default mail app with a prefilled email.
- System-admin flag set only directly in Supabase.
- System admin has an in-app management screen to create member accounts. (Assumption: the former org-admin screen collapses into this one. Confirm in Q4.)

---

## A. Account model

**Q1.** What does "simple account table" mean concretely: (a) Supabase Auth users, with a companion `accounts` table holding role and profile fields, or (b) a custom `accounts` table with username and password that the app checks itself? Note on (b): with the anon key and "Allow all" RLS, password hashes would be readable by any client, and the app would have to hash and compare locally.

**A:** (b) Custom `accounts` table, as simple as possible. No Supabase Auth, no Edge Function. (Decided 2026-10-22.)

**Q1a.** Password storage in the custom table: plaintext, or hashed by the app before insert and compare (for example SHA-256 with a per-row salt)? Either way the column is readable by any client with the anon key; hashing only limits what a reader learns.

**A:**

**Q1b.** Sign-in check: app fetches the row by username/email and compares locally, or a Postgres function (`rpc`) does the compare and returns the account row without exposing the password column?

**A:**

**Q2.** Fields on the account row: email, display name, system-admin flag, active flag, link to a `department_crew_members` row? Anything else?

**A:**

**Q3.** Sign-in credential: email + password or username + password? Is the unique key the email?

**A:**

**Q4.** Roles in 1.1: just system admin and member? Or does the admin tier split (system admin set in Supabase, department admin set in-app)?

**A:**

**Q5.** Who creates member accounts in 1.1: the system admin from an in-app screen, or directly in Supabase with no in-app screen yet?

**A:**

**Q6.** How does the new member get credentials? Admin sets the password and relays it out of band. Forced change on first sign-in, or not in 1.1?

**A:**

**Q7.** Dropped: Edge Function question no longer applies with a custom table (Q1).

**Q8.** Password reset and change-password: in scope for 1.1 or deferred?

**A:**

**Q9.** Can the admin deactivate or delete an account in 1.1? What happens to a signed-in device when its account is deactivated?

**A:**

## B. Sign-in behavior

**Q10.** Is sign-in required for every use, including the offline 4-digit-code UC join?

**A:**

**Q11.** Session lifetime: stay signed in indefinitely on the device until explicit sign-out, or expire? What happens when Supabase is unreachable at launch: proceed on the cached session?

**A:**

**Q12.** Where does Sign Out live (Settings?) and does it clear local incident data?

**A:**

**Q13.** Once signed in, does the account change anything beyond gating access: does Manage Data become admin-only, and is the IC/UC identity on an incident tied to the account?

**A:**

**Q14.** Server-side enforcement: with a custom table there is no Supabase-authenticated user, so RLS stays "Allow all" and sign-in is a client-side gate only. Confirm that is accepted for 1.1.

**A:**

## C. Request account

**Q15.** What email address receives the request, and what subject line?

**A:**

**Q16.** Body fields: name, email, phone, reason for request. Keep organization name and website now that it is single-org, or drop them?

**A:**

## D. App Store release

**Q17.** Whose Apple Developer account publishes: Jason's or Ivy Gulch's? Is it enrolled, and is the bundle ID / team already set in the project?

**A:**

**Q18.** Is the Supabase project the current POC one or a new production project? Does the POC data get wiped?

**A:**

**Q19.** Hydrant data: stays as loaded, or ships empty?

**A:**

**Q20.** Listing materials: app name availability, category, privacy policy URL, support URL, age rating, screenshots. Who produces the policy and the screenshots?

**A:**

**Q21.** App Review needs a working demo login. Which account do we hand them, and does the database contain sample data for them?

**A:**

**Q22.** Pricing: free with no in-app purchase in 1.1?

**A:**

**Q23.** TestFlight beta first? Who are the testers and for how many builds?

**A:**

**Q24.** Any devices currently running 1.0.1 that need a graceful upgrade path, or is the install base effectively zero?

**A:**

## E. Working mode

**Q25.** Prior builds were spec-first with GitHub Spec Kit (238 numbered specs). Continue that, one spec per feature area under `specs/` before code?

**A:**

**Q26.** Who drives implementation: Doug building with Claude spot help, or Claude implementing end to end as on the earlier FirefighterSpot specs?

**A:**

**Q27.** Where should the final specification live: the repo's `specs/` folder or this vault folder?

**A:**

---

## Open items added while answering

- 

---

## Parked: multi-organization questions (out of scope for 1.1)

- Is an organization the existing `departments` row or a new level above it?
- Account membership in multiple orgs; per-membership vs per-account roles.
- Org dropdown before or after credentials; remembered on device; switch-org without sign-out.
- Per-org data scoping in the sync engine and in RLS.
- Mutual aid across orgs.
- Org-admin tier and its management screen; attaching existing accounts from other orgs.
- System-admin screen for creating orgs and first org admins.
