---
status: exploring
created: 2026-08-19
related: "[[Discovery Questions]]"
---

# Volunteer Fire Department Coordinator — Existing (No-Custom-App) Solutions

Stated need: department-only calendar, monthly events, reminders, attendee status (committed / possible / can't make it), visible to members, editable from phone by admins.

## Free general-purpose group apps

### BAND (band.us)
- Free private-group app (iOS/Android/web) with a built-in group calendar; members RSVP per event and see who can/can't attend.
- Upcoming-schedule reminders; members can also set their own per-event reminders. Sign-up sheets can be attached to events for tracking participation.
- Admins create/edit events from the phone. Private, invite-only groups.
- Unverified: whether RSVP includes a "maybe/possible" middle status — confirm hands-on.

### Spond
- Free (revenue comes from optional payments/fundraising features). Built for clubs/teams but generic: private groups, events, one-tap RSVP, waiting lists.
- Reminders and targeted messaging by response bucket (confirmed / unanswered / declined); can nudge non-responders.
- Post-event attendance confirmation (admin can mark who actually showed) — covers the "record who attended" need.
- Gap: RSVP model is accept/decline/unanswered; no explicit "maybe" status found in docs.
- Syncs events to members' personal phone calendars.

### TeamSnap
- Availability tracking is yes/no/maybe — the closest literal match to committed/possible/can't.
- Automated event reminders, private roster, mobile admin editing.
- Paid: availability/RSVP tracking is locked behind the paid tier (~$120/yr billed annually per Capterra).

### Google Calendar (shared calendar + invites)
- Zero cost; invite responses are Yes/No/Maybe with email/phone reminders.
- Gaps: requires everyone to live in Google accounts, no roster/headcount view built for this use, weak "nudge non-responders" and no attendance record. Workable only if the department already runs on Google.

## Fire-department-specific platforms

These do the calendar piece and add department records (incidents, training hours, LOSAP, truck checks). Worth raising if the real need is bigger than a calendar.

### IamResponding
- Widely used by volunteer departments; Events Calendar module integrates scheduling, invitations, and automated notifications/reminders through its messaging system; availability/crew scheduling; training and event reporting.
- Subscription priced per department (site is quote-based; feature pages blocked direct fetch — verify RSVP-status granularity in a demo).
- Many departments already have it for dispatch alerting — first question: do they already subscribe?

### Responserack
- Volunteer-FD records platform; all tiers include Events & Trainings: calendar of events, members register/see who else registered, mobile app.
- Priced by annual call volume: Lieutenant $300/yr (≤50 calls), Captain $720/yr (≤350 calls), Chief $1,200–1,800/yr (≤1,000 calls).
- RSVP-status granularity (committed/possible/can't) not documented publicly — verify in demo.

### Station Boss
- Volunteer-FD software; tracks meeting attendance, training hours, station duty; exports for municipal reporting, grants, LOSAP.
- Transparent pricing from $150/mo (up to 20 personnel, 100 incidents/yr), all features included, no per-user fees, month-to-month available.
- Considerably more money than the calendar-only need justifies on its own.

## Fit summary vs. the captain's ask

| Requirement | BAND | Spond | TeamSnap | IamResponding | Responserack |
|---|---|---|---|---|---|
| Private to department | Yes | Yes | Yes | Yes | Yes |
| Monthly/recurring events | Yes | Yes | Yes | Yes | Yes |
| Reminders | Yes | Yes | Yes | Yes | Unverified |
| 3-state RSVP (committed/possible/can't) | Maybe-status unverified | No "maybe" | Yes (yes/no/maybe) | Unverified | Unverified |
| Members view, admins edit from phone | Yes | Yes | Yes | Yes | Yes (mobile app) |
| Cost | Free | Free | ~$120/yr | Quote | $300+/yr |

## Currency, adoption, and support (checked 2026-08-25)

App Store figures are US store, iOS, as of 2026-08-25.

| System | How current | How widespread | Support |
|---|---|---|---|
| BAND | Very active — v30.0.1 updated 2026-08-24; on the store since 2012; event features still shipping (external-attendee RSVP, invite codes in latest release) | Large — 50M+ users claimed worldwide; 62.5K US ratings at 4.7. Backed by NAVER, a major Korean tech company | Self-serve help center only; no phone or named rep. Consumer-grade |
| Spond | Active — v4.61.0 updated 2026-08-20; on the store since 2017 | Solid but Europe-weighted — 3.5M+ active users claimed (1.4M UK); 3.3K US ratings at 4.85 | Help center + email (support@spond.com); staffed customer-success team. A UK phone number circulates on third-party sites (unverified) |
| TeamSnap | Active (v7.70.0, 2026-08-20; since 2010) — but the company is mid-transition: a new invite-only "TeamSnap ONE" app is rolling out from its innovation lab, so the classic app's long-term path is worth watching | Large — claims 25M users in 196 countries; 59.5K US ratings at 4.76 | Email + chat; limited phone. Ads on the free tier |
| Google Calendar | Ubiquitous, Google-maintained, effectively permanent | Ubiquitous | Self-serve only on free accounts; human support requires a Workspace subscription |
| IamResponding | Active — v2.25.0 updated 2026-08-19; on the store since 2013. App rating middling: 3.94 across only 333 ratings | The in-domain standard — site claims 11K+ agencies and 500K+ members (2026-08-25) | Ticket-based department support (explicitly does not monitor App Store reviews); quote-based sales with demos |
| Responserack | Product is web-first; the iOS companion app was released Nov 2023 and last updated Oct 2025, with zero App Store ratings | Small — essentially a one-person company (founder Adam Jack, a Colorado volunteer firefighter, founded 2019); no public adoption numbers | Founder-direct + help site — likely personal and responsive, but bus factor of one |
| Station Boss | Very active on a young codebase — V2 app released Feb 2026, updated 2026-08-20 (v4.2.13) | Small — 1 US App Store rating; no public department counts | Vendor-direct (small LLC); transparent pricing, no per-user fees |

Read on the three tiers:

- **General-purpose apps (BAND, Spond, TeamSnap)** are all current, mass-market, and in no danger of disappearing; support is consumer-grade self-service. TeamSnap carries a mild platform-transition risk (TeamSnap ONE).
- **IamResponding** is the only fire-specific option with proven scale. Its mobile app reviews are the weakest of the group, but department-level support is a real channel the general-purpose apps don't offer.
- **Responserack and Station Boss** are small vendors — attentive support from the people who built it, but adoption is thin and continuity depends on one person / one small LLC. Station Boss is investing heavily right now; Responserack's mobile app has been quiet for ~10 months.

## Fire-specific platforms — three-way comparison (checked 2026-08-25)

### Features

All three are per-department subscriptions with unlimited members, mobile apps, an events/training calendar, and incident records. Centers of gravity differ:

- **IamResponding** — alerting-first: mobile dispatch notifications, "who is responding" board, TwoToneDetect pager-audio capture, live responder tracking/AVL, mutual aid, hydrants, pre-plans, custom station displays, messaging/chat, scheduling, events calendar, incident reporting with free NFIRS, training records, records management. All features in every subscription, unlimited users and devices.
- **Responserack** — records-first for volunteer departments: incident reports with validated NFIRS/NERIS export, events & trainings with member calendars and certification tracking, truck checks and maintenance records, member contacts, groups & notifications, email messaging, CAD integration (auto-starts incident reports). Notifications exist but it is not a dispatch-alerting system.
- **Station Boss** — all-in-one ops platform: NERIS incident reporting with real-time validation, dispatch console with push alerts (map links, preplan data, response tracking), personnel management (certifications, training, scheduling, payroll), equipment/SCBA/hose/ladder inspection tracking, ISO-ready training reports, offline pre-plans, shift scheduling, inspections, ePCR, website builder, report builder, financial management. All modules in every tier.

### Costs

| | IamResponding | Responserack | Station Boss |
|---|---|---|---|
| Up-front | $50 one-time setup fee (per flyer; verify) | None stated | None; no contract |
| Subscription | Site (2026-08-25): "Starting from **$349/Year**," otherwise quote-based. Older ND Firefighters Assn flyer shows the tier shape: ≤100 incidents/yr $300/yr; 100+ $800/yr ($725/yr on 3-year, $650/yr on 5-year terms); plus $5–10/yr telephone-call fee | ≤50 calls/yr: **$300/yr**; ≤350: **$720/yr**; ≤1,000: **$1,200–1,800/yr** | **$150–550/mo** ($1,800–6,600/yr) by personnel count + incident volume; e.g. $150/mo = 20 personnel / 100 incidents |
| Tier basis | Incident volume | Call volume | Personnel + incident volume |
| Trial | Free 60-day (per flyer) | None stated ("contact me" for budget constraints) | Free 14-day, no credit card |
| Feature gating | None — all features every tier, unlimited users and devices | Core features all tiers; Chief tier ($1,200+) adds custom CAD integration, custom reports, phone support, 5GB storage | None — all modules every tier; phone support included |

Caveat: IamResponding publishes only "Starting from $349/Year" (confirmed on their site via browser 2026-08-25 — the site blocks normal fetching; /pricing/ redirects to the homepage). The tier structure comes from an undated ND Firefighters Association flyer (stats 8K+ entities vs. 11K+ agencies / 500K+ members on today's site, so the flyer is a few years old and its dollar figures have drifted ~15%) — get exact numbers in a demo. Responserack and Station Boss pricing is published on their sites.

For a typical small volunteer department, the annual spread: IamResponding $300–800, Responserack $300–720, Station Boss $1,800 minimum — Station Boss costs 2–6x the other two but bundles the widest ops scope (ePCR, payroll, financials, website).

### Independent reviews (checked 2026-08-25)

Coverage is thin for all three fire-specific platforms; only IamResponding has any meaningful independent footprint.

- **IamResponding** — G2: 4.2/5 from 11 reviews (category scores: support 8.7, ease of use 8.3). Capterra listing exists but has zero reviews. US App Store: 3.94 across 333 ratings — polarized (a 100-review sample: 27% five-star vs 23% one-star; recurring themes are stability/crash complaints, pricing gripes, and UX). Old Firehouse-forum threads praise the "who's responding" core while calling scheduling not user-friendly.
- **Responserack** — effectively no independent reviews anywhere: Capterra listing is bare (no reviews), zero App Store ratings, no forum presence found. Evaluation would rest entirely on a demo/trial and direct references from other departments (ask the founder for referenceable customers).
- **Station Boss** — Capterra listing exists with zero reviews; 1 US App Store rating. Same situation: demo + references only.
- Contrast: the general-purpose apps carry large genuine review bases (BAND 62.5K US App Store ratings at 4.7, TeamSnap 59.5K at 4.76, Spond 3.3K at 4.85), so their day-to-day quality is far better evidenced than any of the fire-specific tools.

## Sources

- [Spond events](https://www.spond.com/events/) · [Spond attendance tracking](https://www.spond.com/en-us/news-and-blog/attendance-tracking-on-spond/) · [Spond event features (help)](https://help.spond.com/app/en/articles/129730-features-in-events) · [Capterra: Spond](https://www.capterra.com/p/181253/Spond/)
- [BAND on the App Store](https://apps.apple.com/us/app/band-app-for-all-groups/id542613198) · [BAND calendars](https://medium.com/bandapp/how-do-i-use-calendars-on-band-ba6c9e1ffc3d)
- [Capterra: TeamSnap](https://www.capterra.com/p/123208/TeamSnap/) · [TeamSnap pricing overview](https://checkthat.ai/brands/teamsnap/pricing)
- [IamResponding features](https://iamresponding.com/features/) · [IamResponding Events Calendar (support)](https://support.iamresponding.com/hc/en-us/articles/36160929645332-Events-Calendar) · [IamResponding scheduling (support)](https://support.iamresponding.com/hc/en-us/articles/16293478213140-Scheduling)
- [Responserack pricing](https://www.responserack.com/pricing/) · [Responserack mobile](https://www.responserack.com/mobile/) · [Responserack volunteer FD software](https://www.responserack.com/fire-department-software/volunteer/)
- [Station Boss pricing](https://stationboss.net/pricing/) · [Station Boss volunteer FD software](https://stationboss.net/volunteer-fire-department-software/)
- Currency/adoption/support check (2026-08-25): US App Store listings for [BAND](https://apps.apple.com/us/app/band-app-for-all-groups/id542613198), [Spond](https://apps.apple.com/us/app/spond/id755596884), [TeamSnap](https://apps.apple.com/us/app/teamsnap/id393048976), [TeamSnap ONE](https://apps.apple.com/us/app/teamsnap-one/id6670517733), [IamResponding](https://apps.apple.com/us/app/iamresponding-iar/id614677924), [Responserack Responder](https://apps.apple.com/us/app/responserack-responder/id6450862494), [Station Boss V2](https://apps.apple.com/us/app/station-boss-v2/id6737058034) · [IamResponding FAQs](https://iamresponding.com/faqs/) (9,000+ departments) · [About Responserack](https://www.responserack.com/about/) · [Spond contact](https://www.spond.com/contact/) · [TeamSnap ONE support](https://help.teamsnap.com/article/1907-contacting-customer-support) · [TeamSnap support](https://helpme.teamsnap.com/article/1278-contacting-customer-support)
