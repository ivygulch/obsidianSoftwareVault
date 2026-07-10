---
area: Story Capture
status: seed
tags: [app-idea, story-capture, legacy, grandparents, family, faith, voice-recording]
created: 2026-07-10
updated: 2026-07-10
---

# Passalong

_Working name — replace when the real branding lands._

**One-liner:** A family story exchange where grandparents and grandchildren send each other questions and answer in their own voice — built so a recording is never lost and the family owns every word forever.

**Target user:** Multi-generation families spread across the country. The *user* spans ages (grandparent recording, grandkid asking); the *buyer* is the adult child in the middle who fears the stories will die with the storyteller.

**Problem:** The stories people most want to keep are held by the people least served by current tools. Web/book incumbents (StoryWorth, Remento) feel like homework and have no native app; native apps lose irreplaceable recordings (StoryCorps' review wall), claim broad content licenses, or hard-paywall grieving families. Nobody has built the two-directional exchange — kids asking, elders telling, both keeping — with capture you can trust.

**Differentiator:** (1) Never-lose-a-word capture — local-first, continuous save, survives calls/alarms/crashes, resume and retake. (2) The family owns the data — exportable always, never trains AI, no content license grab; CloudKit sync, no accounts on someone else's server. (3) Bidirectional age-aware prompts as designed craft, not a static question list. (4) Gift-first monetization with a generous free start. (5) Optional faith prompt packs (testimony, blessings, letters-for-later) — an empty niche confirmed by research.

## The Three Questions

_An idea cannot leave `status: seed` until these are filled in with real answers, not placeholders._

**Who pays, how often, how much?**
The adult child (roughly 35–55, parents aging, kids young enough to still ask questions) buys a family plan as a gift — Christmas, Mother's/Father's Day, milestone birthdays. Yearly, $49–79 family plan, primary form a non-renewing one-year family pass (see [[#Monetization & Sharing Model]]), anchored against StoryWorth/Remento's ~$99 gift price. Evidence: the ~$99/yr gift purchase is the category's proven model; individual hard-gate subscriptions are its proven failure ([[../../../Research/Competitors/Family Story & Legacy Capture Apps — Landscape|landscape scan]], pricing map + withyou reviews). Possible second payment: print-on-demand keepsake book per completed collection.

**Year-2 maintenance cost:**
Low infrastructure, real content burden. CloudKit means no servers to run and no per-user hosting bill. Ongoing costs: prompt-pack authorship (the product's editorial heartbeat — new packs seasonally, faith packs, age-band revisions), elder-facing support (this demographic emails support instead of churning silently; StoryCorps/withyou reviews show support quality gets named in ratings), and App Store platform churn. No LLM bills unless AI-assisted follow-up questions are added later — keep v1 free of model dependencies.

**Kill criteria:**
1. **CloudKit sharing spike fails** — if the shared-zone model can't pass the spike scope below, and the fallback requires running my own backend, the no-server privacy moat collapses; re-evaluate before writing feature code. Spike must verify: (a) shared-zone `CKAsset` audio at realistic sizes syncing to all participants; (b) invite/accept flow across different Apple IDs in different Apple Family groups, tolerable for a non-technical elder; (c) storage accounting — confirm assets in the shared zone count against the *zone owner's* iCloud quota and measure real consumption per story; (d) an entitlement record written by the owner propagating to participants promptly enough to gate features; (e) behavior when a participant has no Apple device — what a web/read-only fallback would require.
2. **Beta families don't finish** — recruit ≥5 families (mine plus four not related to me); if fewer than half complete a 10-story exchange within 6 weeks, the homework problem has beaten the design and the mechanic isn't retention-proof.
3. **Incumbent ships the same thing** — if StoryWorth or Remento launches a native iOS app with credible capture reliability before my v1, the whitespace is gone; compete only if the bidirectional exchange still isn't theirs.
4. **Gift season flops** — if the first holiday season after launch converts poorly (family-plan sales fail to cover the year's costs, i.e. low hundreds of units), the gift thesis is wrong and the idea goes to Shelved with data attached.

## Concept

Two roles, one loop. A family space holds members across generations. Anyone can send a question ("Grandpa, what's the dumbest thing you did in college?"); the recipient answers in voice (or video later), in one tap, guided one question at a time — never a questionnaire. Answers become a growing, listenable family archive; stories can also flow unprompted ("I want to tell you about my brother").

- **Capture engine first.** Recording writes to disk continuously; an interruption (call, alarm, crash, dead battery) costs seconds, not the session. Retake a clip, resume a story, edit the transcript's names. This is the engineering center of gravity and the marketing headline.
- **Prompts as editorial product.** Age-banded question packs (asking-up and telling-down), seasonal packs, and optional faith packs — testimony, blessings, letters-for-later, "what I believe and why." Prompt craft is a writer's job; that's an unfair advantage, not a cost.
- **Ownership as policy.** Everything exportable (audio + transcript + metadata), nothing used for training, no license grab in the ToS. Say it on the App Store page; reviews show users read for it.
- **Legacy delivery.** Stories can be sealed for future moments ("open on your 18th birthday") — the time-capsule mechanic (Dott/Capsle) folded in rather than a separate app.
- **Out of scope for v1:** voice cloning of the deceased (Forevermore's Echo — ethically loaded, not this product), Android, print books (partner later), AI interviewer.

### Android-later design guardrails

Android support, if it ever comes, is a **backend migration, not a client port** — no realistic Android client talks to CloudKit (Web Services would force Apple IDs on Android relatives). These v1 choices keep that migration cheap; all cost ~nothing now:
1. **SQLite is the source of truth; CloudKit is a quarantined sync transport** (the spike's Arm B posture). Domain code never touches CK types.
2. **Members are first-class records** (UUID, name, role); the `CKShare` participant is only the access mechanism, never the member list — so identity isn't welded to Apple IDs.
3. **The canonical export format doubles as the migration vehicle** — the ownership promise (full export: audio + transcript + metadata JSON) is specified early and kept complete; export→import is how a space would move to a server.
4. **Entitlements are platform-neutral data** (a date in a record); only the writer knows StoreKit. Web pass codes are the cross-platform purchase path.
5. **Universal formats:** AAC/`.m4a`, transcripts as plain text/JSON — no persisted Apple-specific structures.
6. **Rejected hedge:** Kotlin Multiplatform now — taxes iOS velocity and the TCA/SwiftUI stack for a platform that may never ship. (If migration day comes, the server side is familiar ground — Routy's Kotlin/Ktor + Postgres backend is prior art.)

## Monetization & Sharing Model

**The subscription attaches to the family space, not to people.** One member — the organizer, usually the buying adult child — pays; the payment entitles the whole space. Every other member installs the app free, joins by invite, and never sees a paywall. Rationale: the buyer graph is cross-household, so Apple's Family Sharing (purchaser's Apple Family group, max 6, same household in practice) cannot be the sharing mechanism — enable the StoreKit family-shareable flag as a bonus, but never rely on it.

**Entitlement mechanics (no server):** the organizer's device validates its own purchase via StoreKit 2 and writes an entitlement record ("active through [date]") into the shared CloudKit zone; members' apps read it to unlock. Known trade-off: this is a client-side check that a determined user could spoof — accepted; no backend gets built to police memory prompts.

**Free tier, always:** join any space, answer questions sent to you, listen, export. The elder and the grandkids must never hit friction or a purchase screen.

**Paid space unlocks:** unlimited stories (free space capped ~5–10), prompt packs beyond the starter set (incl. faith packs), sealed time-capsule deliveries, video answers (post-v1). **Export is never gated** — the ownership promise outranks any conversion tactic.

**Lapse policy (positioning-critical):** when a pass expires, recording new stories locks; listening and exporting everything remains free forever. Recordings are never held for ransom — the explicit anti-withyou stance, stated on the App Store page.

### Primary path
**Non-renewing one-year family pass, ~$59.** Matches the gift cadence honestly (bought each Christmas / Mother's Day / Father's Day, no surprise auto-charge in July); Apple's non-renewing subscription IAP type exists for exactly this, and Apple offers no way to gift auto-renewing subscriptions anyway — the "gift" is the organizer buying a pass for the space they administer. Cost: the renewal must be won on merit every year; given the no-hostage positioning, treat that as a feature. Any member — not just the original buyer — can purchase the renewal ("this year the other sibling pays").

### Options to test against it
- **Auto-renewing yearly sub ($49–79/yr)** — predictable renewal revenue, standard tooling; risks the resentment the category punishes (withyou). Can coexist with the pass as a second SKU; let data decide.
- **Auto-renewing monthly (~$7–9/mo)** — on-ramp for hesitant buyers; poor fit for gift psychology and invites churn-timed cancellations. Offer only if funnel data shows yearly sticker shock.
- **Lifetime family pass (~$149–199)** — appeals to exactly this demographic ("buy once for the family, done"); caps long-term revenue and creates an eternal support obligation. Consider as a launch-window or grandparent-direct offer, not the default.
- **Keepsake add-ons** — print-on-demand book per completed collection, archival USB/audio-CD for elders; one-time purchases that monetize completion instead of anxiety. Likely the second revenue line, competing directly for StoryWorth's book dollar.
- **Organizational gift packs** — a church, ministry, or similar org buys a pack of passes to distribute (grandparents' ministry, grief/hospice care, new-member gifts; adjacent: homeschool co-ops, senior communities, genealogical societies, schools — StoryCorps' classroom usage proves the school case). Doubles as the faith-channel distribution answer: the org isn't just a buyer, it's the marketing. Apple mechanics are the constraint, three routes: (a) **subscription offer codes** — Apple-native bulk codes, but they only attach to *auto-renewing* subscriptions and grant free/discounted periods, so the org pays by direct invoice and recipients redeem codes (works, but forces an auto-renew SKU to exist and code-redeeming users must cancel-or-convert at period end); (b) **external purchase (US)** — post-2025 US storefront rules allow linking out to web purchase, so orgs buy pass-code packs on the website and the app redeems them — cleanest fit for the non-renewing pass, US-only and rules still shifting; (c) **manual B2B pilot** — invoice the org, provision spaces by hand for the first few partner churches before building any redemption machinery. Start with (c); it validates the channel with zero code. Review-guideline risk (3.1.1 vs. org-purchased digital goods) needs a check before (b) ships.
- **Sponsored plans (professional/org co-branding)** — the org-pack machinery with a branding layer, for estate attorneys, financial advisors, funeral pre-planning, and similar. Primary form: *full sponsorship* — the professional pays a wholesale-plus-co-branding rate, the client family gets the pass free as a gift ("This family space is a gift from Smith Estate Law" on the space welcome screen; sponsor's name on the keepsake book's gift page). One payer, one invoice, reuses pass codes — no split billing. Ethics-clean for attorneys: they *give* a modest client gift rather than *receive* referral compensation, and the annual renewal hands the sponsor a legitimate yearly client touchpoint (worth more to them than the pass costs). Secondary form: *co-pay* — pro buys discount codes, client pays a reduced price; only for volume cases where full sponsorship is too expensive, since split value weakens the gift moment. **True white-label (rebranded per-client apps) is rejected for now:** Apple's template-app rules (4.3/4.2.6) force per-client listings and dev accounts, the ops burden doesn't fit a solo dev, and the family's-iCloud ownership story must not look like it lives inside the professional's product.

**Storage economics:** shared-zone assets count against the *organizer's* iCloud quota, not participants'. Audio-first keeps this trivial (~1 MB/min AAC; a hundred stories is negligible); video is the quota risk and stays post-v1. Onboarding states it plainly: "stored in [organizer]'s iCloud, shared with your family." The public-database alternative (storage on the app's quota) is rejected — it weakens the "your family's iCloud" privacy story.

**Edge cases recorded now:** one person can belong to multiple spaces (member of their kids' space, organizer of a siblings/cousins space) — entitlement is per-space; a space with two willing payers just alternates renewals; an organizer who dies must be survivable — zone-ownership transfer or full-export-and-reimport is part of the spike's follow-up questions.

## Marketing & Validation Channels

- **Homeschool conferences** — high-density fit: multi-kid families, intergenerational orientation, large faith overlap, and "interview a grandparent" already exists as a project/unit-study genre (StoryCorps' classroom reviews prove the mechanic in education). Insider standing: we homeschooled all four kids through high school (co-ops, unit studies, mixed curriculum) — I know the conference culture, the co-op decision dynamics, and can author a credible living-history unit study around the app rather than a brochure. Two distinct uses, staged: *pre-launch* — walk the halls without a booth: idea testing, prompt-pack feedback, and beta-family recruitment for kill criterion #2 (a venue full of candidate families not related to me); *post-launch* — a booth (~$500–2,000 per event) selling the family pass and co-op packs, pitched as a living-history curriculum piece as much as a keepsake app. Homeschool co-ops are also organizational-pack buyers alongside churches.
- **Secular homeschool groups** — SEA (Secular, Eclectic, Academic) Homeschoolers, secular co-ops and conferences: same unit-study/co-op mechanics as the faith-side homeschool world with a general-audience frame. The living-history unit study works unchanged; only the prompt packs differ. Keeps the channel mix from being all-faith concentration.
- **Question-list SEO + free printables** — "questions to ask your grandmother" is high-volume evergreen search that StoryWorth built its funnel on; free downloadable question packs are the lead-magnet form, and the content is prompt-pack work I'm doing anyway. Cheapest channel here and it compounds. First to resource.
- **Genealogy ecosystem** — the strongest secular community: RootsTech (huge annual conference + virtual audience), genealogical societies, genealogy podcasts/YouTube. Family historians already pay to preserve history and lament unrecorded relatives. (Upgraded from note-and-defer.)
- **Oral-history education hook** — StoryCorps' Great Thanksgiving Listen makes November a ready-made "interview an elder" moment; a free classroom/lesson kit (incl. Teachers Pay Teachers) rides it with zero sales force. Pairs with the homeschool unit study.
- **Churches / ministries** — the organizational gift-pack channel (see Monetization): grandparents' ministries, grief and hospice care, new-member gifts. Manual B2B pilot first.
- **Gift-season calendar + gift-guide press** — the marketing year has four peaks: Christmas, Mother's Day, Father's Day, National Grandparents Day (first Sunday after Labor Day). Aim launches and spend at peaks, and pitch gift-guide writers ("gifts for grandparents who have everything") ahead of each — StoryWorth's proven playbook, alongside parenting/history podcast ads once there's revenue to fund them.
- **Senior-living activity directors** — reminiscence programming is established practice in senior communities; an org pack sold to the activity budget is the secular twin of the church pack. Boundary: memory-care/dementia positioning is a different product with clinical expectations — stay on the social side of that line.
- **Hospice, end-of-life services, estate attorneys** — legacy letters sit naturally beside wills and pre-planning; long sales cycles, high tone sensitivity.
- **Professional referral program (post-traction)** — once conversion data exists to price payouts, give adjacent professionals a referral code that earns them money: financial advisors, senior move managers, end-of-life doulas, funeral pre-planning services. Mechanics ride the web pass-code infrastructure (external-purchase route), which makes per-code attribution straightforward where App Store IAP alone couldn't. **Attorney caveat:** state bar rules widely restrict lawyers taking compensation for client referrals — for estate attorneys specifically, use the clean variants: (a) codes that discount the *client* (attorney adds value, takes nothing), or (b) attorneys buy pass packs at wholesale as client-appreciation gifts — a will-signing closing gift is a natural moment. Cash referral fees stay for professions without fee-sharing rules, with disclosure baked into the program terms. For the give-rather-than-receive form of this channel, see **Sponsored plans** under Monetization — often the better fit for attorneys.
- **Apple editorial featuring** — a family app with a genuine no-servers, lives-in-your-iCloud story is what App Store editorial features around Mother's Day/holidays; the architecture decision doubles as the pitch. Pitch it, don't wait for it.
- **Grief-adjacent content** — Forevermore proves the acquisition moment ("I have nothing saved of them"); the ethical version is capture-while-they're-here urgency, not voice-cloning demos. Tone risk is high; test copy carefully.
- Family-reunion networks — natural group-onboarding moment but no concentrated venue to buy access to; treat as content topic, not channel.

**Channel priority (first resourced):** question-list SEO → genealogy ecosystem → Thanksgiving education hook. Cheap, secular, and built from assets (prompt packs, unit study) already being produced. The insider channels (church, homeschool) run in parallel on standing rather than spend. Beta group must include families outside the faith/homeschool ecosystems to test whether the product works without that shared cultural frame.

## Prior Art

_Full teardown: [[../../../Research/Competitors/Family Story & Legacy Capture Apps — Landscape]] (2026-07-09)._

- **Capsle Stories** — proves the bidirectional send-a-question mechanic; loved (22/22 five-star reviews, praised by a 90-year-old user) but unknown. Gets the loop right; hasn't solved distribution.
- **StoryCorps** — proves the guided two-person interview at scale, including grandkid↔grandparent and classroom use. Fails on the thing that matters most: chronic lost/corrupted recordings and a content-ownership ToS users resent.
- **Forevermore** — proves demand is current (369 ratings in 5 months, 4.73) and that grief drives acquisition. Gets emotional urgency right; monetizes voice-cloning of the dead, which I won't build.
- **StoryWorth / Remento (web)** — prove the ~$99 gift-purchase model and the printed-book payoff. Both absent from the App Store; both induce the "homework" feeling that stalls elders (named verbatim in a Forevermore review).
- **withyou** — proves the anti-pattern: emotional onboarding into a hard paywall earns a wall of 1-stars calling it emotional blackmail.

## Why It Could Work

- Whitespace is verified, not assumed: no native app combines reliable capture + bidirectional exchange + data ownership; the two category brands have no App Store presence at all (as of 2026-07-09).
- The moat is an engineering problem (interruption-proof capture) — favorable ground for a veteran iOS dev, unfavorable for the content-company incumbents.
- Prompt craft is a second moat, and it's a writing problem — the other thing I do.
- I am the target user twice over: grandfather of seven (ages 1–16) and the adult child who lost a brother with too little recorded. Beta family included.
- Faith prompt packs open a confirmed-empty niche with a distribution channel (churches, Bible study networks) I personally have.
- The two strongest channels are both insider ground: church networks (board member, adult-class teacher) and the homeschool world (homeschooled four kids through high school — co-ops, conferences, unit studies). Early marketing runs on standing, not ad spend.

## Why It Might Not

- Category retention is inherently episodic — families burst, then go quiet. If the gift-renewal cycle doesn't carry year 2, revenue is one-shot.
- StoryWorth/Remento can enter any time with brand, email lists, and book fulfillment already built. The whitespace is structural only until it isn't.
- CloudKit sharing across a mixed-device extended family is unproven for this use (kill criterion #1); the privacy moat depends on it.
- Elder-side UX is unforgiving; one bad first session with a 78-year-old ends the family's use. Capsle's obscurity may mean the market is smaller than its reviews suggest.
- Two-sided prompting needs kids to actually ask — if engagement has to be parent-puppeteered, the "exchange" collapses into StoryWorth-with-extra-steps.

## Open Questions

- Brand fork: one app with optional faith packs, or a second faith-branded skin sharing the engine? (Research says decide at positioning time, not build time.)
- How did Forevermore acquire users so fast — and is that channel (grief-content social video) available to a solo dev with a different ethical stance?
- Print-on-demand partner for a keepsake book — necessary to win the gift dollar, or v2?
- Non-Apple relatives: web playback page? Android member as second-class listener? Where's the line before the no-server model breaks?
- Organizational packs: will churches actually buy and distribute passes (test with 2–3 partner churches via manual invoicing before building redemption), and does app-side code redemption for org-purchased passes clear App Review guideline 3.1.1?
- What does the 6-week/10-story beta actually measure — completion, or delight? Define the instrument before recruiting families.

## Related

- [[CloudKit Spike Plan]] — the technical-validation plan for kill criterion #1 (planned, ~5 days)
- [[../../../Research/Competitors/Family Story & Legacy Capture Apps — Landscape]] — market scan that seeded this idea
- [[../_Story Capture MOC|Story Capture MOC]] — home area (LLM-assisted interviews, heirloom & ethical wills focus areas)
- StoryRiffs (Writing area) — shares the "family creates together" DNA; different mechanic, same household playtesters
