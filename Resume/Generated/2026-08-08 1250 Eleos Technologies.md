# Eleos Technologies — Remote Senior iOS Engineer

- **Generated**: 2026-08-08 12:50
- **Company**: Eleos Technologies
- **Job title**: Remote Senior iOS Engineer

## Job description

Eleos Technologies logo
Remote Senior iOS Engineer
United StatesEngineering – Engineering /Engineer /Remote
About us

Eleos Technologies is a growing 12-year-old company building communication software for truck drivers and field workers.

We're helping a diverse mix of customers, from mom and pop operations to thousand-truck fleets, improve how they communicate with their employees by tackling information overload, reducing phone calls, and eliminating obsolete technologies. As we help fleets develop better tools, we aspire to be known for our innovation, reliability, and ability to make a difference for them and their drivers.

Our engineering team has been 100% distributed since day one. This means we're tooled up to handle product, architectural, technical, and ops work all from home or remote. You won't miss out on office conversations, and you won't have to learn to drive a telepresence robot.

We began life as a bootstrapped startup, which allowed us to focus on building products our customers love. Today, we're part of the Knight-Swift family, which has allowed us to keep our focus and the freedom to build the best products we can for the transportation industry. We offer robust healthcare (dental, medical, vision), paid time off, and a generous equipment budget.

About the role
Our app is more than the usual "CRUD and chat": in addition to industry-leading truck navigation and planning tools, we've got advanced algorithms for identifying the best and safest vehicle route, document scanning, and more—all on the device.

As a senior member of our iOS team, you'll get to leave your mark across the app's architecture, UI, and all the way down to the database and network guts. You'll work directly with peers who maintain our Android app and the server systems that provide our customers with a stable API and handle user data synchronization.

Tens of thousands of people across the country rely on our app to do their jobs, and we take quality seriously. We have an automated acceptance test suite we run in a cloud-hosted provider, plus a great dedicated QA team responsible for manual testing and helping reproduce issues reported from the field. You'll write automated tests for the code you write and work to both share and expand your skills around automated testing. We have CI that produces builds for the whole team to try within a few minutes of a commit or pull request being opened and a similar process for cutting release-ready builds for distribution, so you can generally stay focused on the work you love and not Xcode toil.

About you

We're looking for a senior engineer who can help maintain, evolve, and improve our iOS app, which is the single pane through which about half of our users experience our core product. (The other half use Android!)

We're looking for a product-minded engineer who wants to understand the problem behind the requirement, not just implement the requested solution. You'll partner closely with members of the team to refine ideas, identify edge cases, and suggest approaches that may not have been apparent when the work was originally defined.

You should be comfortable asking thoughtful questions, respectfully challenging assumptions, and presenting technical tradeoffs in a way that helps the team make better decisions. We value engineers who take ownership of the outcome, not just the completion of the ticket, and who remain involved through testing and real world feedback.

You should be extremely comfortable working with Xcode, implementing and evolving user interfaces with both UIKit and SwiftUI, managing network requests and model state, and persisting to disk using Core Data or SQLite. You should have experience working with both Swift and Objective-C, as we have a mixture of both. (We write almost all new code in Swift, but as a small team, we're in no hurry to rewrite battle-tested Objective-C portions of the app until there's a compelling reason to do so.)

We'll work together and pair often to get you ramped up, and the nature of our product means you'll continue to work closely with the whole team to move it forward even as you settle in. We'd like someone who's both ready to teach others (you'll know things we don't!) and learn from co-workers in a fun, productive, and respectful environment.

You must live in the United States to be eligible for this role.

Key skills

4+ years professional experience building or maintaining a shipping native iOS app in some mixture of Swift and Objective-C, including ownership of substantial features or technical systems
Ability to turn product requirements into technical and UX options
A collaborative mindset and willingness to respectfully challenge requirements and surface overlooked edge cases and recommend simpler or more valuable solutions
Strong ownership instincts that follows the work from planning, implementation, to ongoing support once released
Experience writing UI automation tests
Ability to diagnose nondeterministic failures involving async behavior, networking, and differences between simulators and real devices
Effectively use Xcode's Instruments suite to diagnose and fix bottlenecks, UI hitches, and memory leaks
Experience diagnosing issues using crash reporting, logging, analytics, and CI or automated test output
Able to balance human- and LLM-driven software development workflows and bring experience, judgement, and curiosity to the process while retaining ownership of the output and results
The ability to quickly convey ideas, opinions, and technical details in written English
Able to work 9-5 Eastern, Central, or Mountain Time, to facilitate real time collaboration when needed
Not requirements, but things to mention if they apply to you

An app you've worked on is available in the App Store
Android development experience
Experience writing JavaScript or TypeScript
C++, C, Rust, or Zig skills
Experience with GIS, mapping, or location-driven apps
Maps, routing, navigation, geofencing
Document capture, barcode scanning, image processing
Dynamic type scaling and other adaptive improvements for accessibility
$150,000 - $180,000 a year
If this sounds like an interesting product space and your kind of environment, get in touch and let's talk!
Eleos Technologies Home Page
Jobs powered by Lever logo

## Cover letter

Dear Eleos engineering team,

The codebase you describe — almost all new code in Swift, battle-tested Objective-C left alone until there's a compelling reason — is the shape I worked in for years at WalmartLabs, and I think that restraint is the right call. On the ASDA team (UK grocery, 500K+ DAU) I maintained legacy Objective-C modules across three years of releases while rewriting components in Swift and converting the architecture to RxSwift; on Sam's Club (~2M daily active users) I helped drive the Objective-C-to-Swift migration with uninterrupted service. I've lived on both sides of the mixture and know when a rewrite earns its cost and when it doesn't.

On product-mindedness and ownership through release: at Walmart, every feature I led carried the full arc as a matter of course — I built in the analytics and telemetry, kept the team dashboards current, and monitored behavior through production rollout, with all new checkout features shipping behind feature flags and more than half as A/B experiments. Earlier this year I took that to its logical extreme: an iOS incident-management app for volunteer fire departments, where I translated a non-technical customer's requirements into formal specifications and owned everything from the local-first SwiftUI client with cross-device sync through the Supabase backend to shipped v1.0. Understanding the problem behind the requirement was the whole job — the customer could describe his volunteers' pain, not a feature list.

Quality and testing are where I've invested most visibly. At Walmart checkout I established the automated testing discipline — unit, integration, and UI with XCTest and XCUITest — raising coverage to roughly 85% with a measurable drop in post-release defects, while maintaining 99.9%+ crash-free sessions with ~90% of core flows instrumented. Your line about sharing testing skills lands well: I've taught automated testing for years, from TDD and mock-object seminars at 360iDev and CocoaConf to org-wide testing and accessibility training across Walmart's iOS engineering group.

On balancing human- and LLM-driven workflows: this is my current daily practice, and I hold exactly the stance your posting asks for. At CLEAR I mentor a six-engineer iOS team on integrating Claude Code and Codex into everyday development — codebase research, architectural proposals, test development — while leading the production app's migration to Swift 6.2 structured concurrency. The fire-department app was built spec-first with GitHub Spec Kit generating specifications and Claude Code assisting implementation. My framing throughout: these tools are accelerators for engineering judgment, not substitutes for it, and the engineer owns the output.

A few of your "mention if they apply" items do: 20+ of my apps have shipped to the App Store; I've done document/barcode work (an iOS framework integrating the LineaPro barcode and magstripe reader SDK); persistence experience spans Core Data and Realm including distributed sync for a healthcare app; and I taught the accessibility implementation sessions across Walmart's iOS org at their accessibility team's request. I'm in Ohio — Eastern time — and US-based, so the collaboration window is my normal workday. I'd enjoy talking about where the iOS app is headed and where I could take ownership first.

Douglas Sjoquist
dwsjoquist@sunetos.com

## ATS Resume

### Summary

iOS engineer with fifteen-plus years of mobile design and architecture — shipping production iOS from solo POCs through core-team work on apps serving 5M+ daily active users within Walmart's 120+ engineer iOS organization. Fluent in modern Swift 6.2 concurrency, SwiftUI, Swift Testing, and AI-native delivery using Claude Code, Codex, and GitHub Spec Kit across the full lifecycle. Equally effective translating a non-technical customer's requirements into working software, evaluating a mature codebase to recommend architectural direction, and extending into the backend services and APIs an iOS product depends on. Most recent role at Walmart was Principal Software Engineer on the iOS checkout platform (2021-2026).

### Experience

**CLEAR — Senior iOS Subcontractor** (2026–present)

- Enhance the user experience of CLEAR's flagship iOS app — the primary focus of the engagement — for an airline-traveler user base.
- Built a phased plan to migrate CLEAR's production iOS app to Swift 6.2+ with structured concurrency — async/await, actors, Sendable, and strict concurrency checking — and am implementing the migration step by step across the production codebase.
- Use SwiftUI for all recent and new-feature work; write new test coverage with the Swift Testing framework.
- Maintain and extend the team's Fastlane CI/CD configuration as build-automation needs evolve.
- Mentor a six-engineer iOS team on development practices, modern Swift usage, and integrating agentic tooling (Claude Code, Codex) into day-to-day workflow.
- Research the flagship iOS codebase using Claude Code and Codex to surface architectural patterns, technical debt, and improvement opportunities; develop architectural proposals from that research.

**Independent Client — Lead iOS Engineer & Architect, incident-management app for volunteer fire departments** (2026)

- Delivered a working iOS incident-management app from initial customer requirements to shipped v1.0, owning client, backend, and rollout end-to-end.
- Translated non-technical customer requirements into formal specifications, then implemented a local-first SwiftUI client on Swift 6.2 concurrency that synchronizes across devices.
- Built and operated a Supabase backend; validated with the Swift Testing framework and iterated on-platform with stakeholders.
- Built spec-first using GitHub Spec Kit for specification generation and Claude Code for implementation.

**Walmart — Principal Software Engineer, iOS Platform / Checkout** (2021–2026)

- Owned iOS technical strategy for checkout: architecture evolution, modularization with Swift Package Manager, and long-term platform maintainability for the checkout flow serving 5–6 million daily active users.
- Key contributor to UI development for the checkout component of the Walmart iOS app — rated 4.8 stars on the App Store across 18 million ratings.
- Established automated testing discipline (unit, integration, UI) with XCTest and XCUITest; raised coverage to ~85% with a measurable drop in post-release defects.
- Maintained 99.9%+ crash-free sessions; instrumented ~90% of core checkout flows.
- Owned analytics and telemetry for every feature I led — built in instrumentation, updated team dashboards for org-wide visibility, and monitored behavior through production rollout.
- Rolled out all new checkout features behind feature flags; more than half launched as A/B experiments measuring customer and business impact before full rollout.
- Architected and scaled reactive iOS systems using Swift, Combine, and GraphQL for high-traffic checkout flows; drove real-time performance and reliability initiatives handling traffic spikes and event-driven interactions.
- Collaborated with backend teams on GraphQL schema design and mobile-optimized APIs for checkout and payments.
- Defined and enforced iOS engineering standards across architecture, performance, security, and testing for the full 120+ iOS engineer organization.
- Taught sessions across the iOS engineering organization on accessibility reasoning and iOS implementation techniques, at the request of the engineering accessibility team.
- Trained 80+ iOS engineers on AI-assisted development workflows through live sessions, with additional engineers onboarded via session recordings; assisted the platform team in evaluating and integrating Builder.io, adopted as the standard for new iOS view work.
- Led multi-team delivery and release readiness on a large inner-sourced codebase with frequent production releases; mentored 12+ engineers and built standardized iOS onboarding materials; served as an iOS interview bar-raiser.

**McGraw-Hill Education — Data Engineer & iOS Developer, Sharpen** (2022–2023, concurrent contract)

- Contributed to the iOS in-app subscription experience ("Sharpen Plus") on RevenueCat and StoreKit as part of the product team, including paywall and purchase/restore flows.
- Delivered settings, onboarding, and authentication features for the Sharpen iOS app; integrated five analytics tools.
- Built seven internal tools including email/SMS automation, an AWS data lake, and push notifications.

**Walmart — Senior iOS Engineer (Contractor)** (2020–2021)

- Core contributor on the small initial team for the complete ground-up rewrite of the Walmart iOS app.
- Established architectural patterns in Swift and Combine that became the foundation for subsequent checkout platform work.

**WalmartLabs (Sam's Club) — Senior iOS Engineer** (2017–2020)

- Migrated the Sam's Club Objective-C codebase to Swift with uninterrupted service for ~2M daily active users.
- Led refactor of checkout to unidirectional, reactive architecture; drove a significant increase in checkout test coverage during the refactor.
- Continued reactive architecture conversion using RxSwift and prepared the migration path to SwiftUI and Combine.

**WalmartLabs (ASDA) — Senior iOS Engineer** (2014–2017)

- Maintained ASDA legacy Objective-C modules across multiple releases over three years for 500K+ daily active users.
- Converted the ASDA app's internal architecture to reactive programming using RxSwift; rewrote legacy Objective-C components in Swift.
- Contributed to ASDA iOS release cycles as a WalmartLabs team member.

**Sunetos Inc — Independent iOS Developer** (2010–2019; concurrent with WalmartLabs from 2014)

- Shipped 20+ custom iOS apps from inception to the App Store across healthcare, aviation events, training, real estate, and consumer domains, in Objective-C and Swift.
- Developed TherexRx (therapy-prescription platform for physical therapists) with data synchronization between the iOS client, a backend API, and a distributed Realm database; implemented auto-renewable RevenueCat subscriptions and took them through App Store review.
- Developed MyFactor (patient event tracking for a specialty pharmacy) on Core Data with multiple App Store releases and long-term maintenance.
- Built an iOS framework integrating the LineaPro barcode and magstripe reader SDK; built server-driven UI including dynamic form generation from server templates and a configurable conference-app framework reused across annual events.

### Skills

Swift, Objective-C, Swift 6.2, Swift Concurrency (async/await, actors, Sendable, strict concurrency checking), UIKit, SwiftUI, Combine, RxSwift, MVVM, Unidirectional Architecture, Xcode, Swift Package Manager, Modularization, XCTest, XCUITest, Swift Testing, UI Automation Testing, Core Data, Realm, Data Synchronization, RESTful APIs, GraphQL, Networking, Supabase, StoreKit, RevenueCat, In-App Subscriptions, Push Notifications, Crash-Free Session Monitoring, Analytics Instrumentation, Telemetry, Production Monitoring, Feature Flags, A/B Testing, Performance Optimization, Reliability Engineering, Release Management, CI/CD, Fastlane, TestFlight, App Store Deployment, Barcode Scanning Integration, Accessibility, Claude Code, Codex, GitHub Spec Kit, AI-Assisted Development, Spec-First Development, Technical Leadership, Mentorship, Cross-Functional Collaboration

### Education

B.A. Business Administration, Computer Information Systems emphasis — Cedarville College

## Focused Resume

### Summary

iOS engineer with fifteen-plus years of mobile design and architecture — shipping production iOS from solo POCs through core-team work on apps serving 5M+ daily active users within Walmart's 120+ engineer iOS organization. Fluent in modern Swift 6.2 concurrency, SwiftUI, Swift Testing, and AI-native delivery using Claude Code, Codex, and GitHub Spec Kit across the full lifecycle. Equally effective translating a non-technical customer's requirements into working software, evaluating a mature codebase to recommend architectural direction, and extending into the backend services and APIs an iOS product depends on. Most recent role at Walmart was Principal Software Engineer on the iOS checkout platform (2021-2026).

### Core Focus Areas

#### iOS Architecture → Implementation on Current Standards

- Ship new work against Swift 6.2 concurrency (structured concurrency, actors, strict concurrency checking), SwiftUI with the Observation framework, SwiftUI NavigationStack, SwiftData, and Swift Testing.
- Structure apps for scale using Swift Package Manager modularization — feature modules, shared libraries, and clean dependency graphs.
- Evolve iOS codebases across eras: Objective-C → Swift (Sam's Club, ~2M DAU), RxSwift conversion and Combine preparation (ASDA and Sam's Club), unidirectional reactive architecture (Sam's Club checkout refactor, Walmart FTE checkout platform).
- Raised automated test coverage to ~85% at Walmart checkout (XCTest / XCUITest); drove earlier significant coverage increases during the Sam's Club checkout refactor; maintained 99.9%+ crash-free sessions with ~90% instrumentation on core checkout flows.
- Defined iOS engineering standards — architecture, code quality, performance, security, testing — for a 120+ iOS engineer organization.

#### Agentic Tooling Across the App Lifecycle

- **Walmart internal evaluation and rollout, late 2024 – February 2026.** Personal experimentation began with Microsoft Copilot and Visual Studio, alongside evaluation of various Xcode plugins (found deficient for iOS-specific workflows). During 2025, assisted the platform team in evaluating and integrating Builder.io — connecting Walmart's design library with Figma to generate and update iOS views. Engineering management adopted Builder.io as the standard for new iOS view work and as an option for updating existing views; adoption was actively growing across the 120+ iOS engineer organization at time of departure. Trained 80+ engineers directly through live sessions, with additional reach via session recordings. Participated in engineering working groups evaluating tools for broader adoption.
- **iOS incident management app (volunteer fire departments), February–May 2026.** Full lifecycle, solo. Built spec-first via GitHub Spec Kit for specification generation and Claude Code for implementation, in SwiftUI + Supabase, from initial customer requirements to shipped v1.0. The value I bring is requirements-to-spec translation and architectural judgment; the tools are the implementation partner.
- **CLEAR senior iOS subcontract, 2026–present.** Use Claude Code and Codex to research the flagship iOS codebase, develop architectural proposals and PRDs, and apply to day-to-day code assistance and test development. Mentor the 6-engineer iOS team on bringing agentic tooling into day-to-day work.
- Apply agentic tools across planning, specification, implementation, testing, verification, and deployment — as accelerators for engineering judgment, not substitutes for it.

#### Cross-Industry Delivery at Varied Team Sizes

| Engagement | Industry | Team context | Role |
|---|---|---|---|
| Volunteer fire dept. incident app, 2026 | Public safety / nonprofit | Solo | Architect + implementer |
| CLEAR, 2026– | Identity / travel | 6-engineer team | Senior subcontractor, mentor |
| Walmart checkout, 2021–2026 | E-commerce | 120+ iOS engineers | Principal, platform owner |
| McGraw-Hill *Sharpen*, 2022–2023 (concurrent) | EdTech | Product team | Core iOS + data engineer |
| Walmart-branded app (ground-up rewrite), 2020–2021 | E-commerce | Small initial team | Senior contractor |
| Sam's Club, 2017–2020 | Club retail | Large team, ~2M DAU | Senior iOS engineer |
| ASDA, 2014–2017 | Grocery retail | Multi-release team, 500K+ DAU | Senior iOS engineer |
| Clinically Relevant (TherexRx), 2016–2019 | Healthcare / physical therapy | Small team (1–3) | Independent |
| BioRx (MyFactor), 2013–2016 | Healthcare / specialty pharmacy | Small cross-vendor team | Independent |
| Other custom client apps, 2010– | Real estate, aviation events, training, consumer, healthcare | Typically 1–3 | Independent |

Over 20 shipped iOS apps across the independent engagements — including hemophilia-factor tracking, attendee access control, conference guides, physical therapist tools, employee training with video and quizzes, real-estate sales tools, and childhood learning.

### Selected Engagements

**CLEAR — Senior iOS Subcontractor** (2026–present)

- Enhance the user experience of CLEAR's flagship iOS app for an airline-traveler user base; all new feature work in SwiftUI, new coverage in Swift Testing.
- Built a phased plan to migrate the production app to Swift 6.2+ structured concurrency and am implementing it step by step across the codebase.
- Mentor a six-engineer iOS team on development practices, modern Swift usage, and integrating agentic tooling into day-to-day workflow.

**Independent Client — Lead iOS Engineer & Architect, volunteer fire department incident-management app** (2026)

- Took the app from a non-technical customer's initial requirements to shipped v1.0 (February–May 2026) — solo, owning the local-first SwiftUI client, cross-device sync, and Supabase backend end-to-end.

**Walmart — Principal Software Engineer, iOS Platform / Checkout** (2021–2026)

- Owned iOS technical strategy for checkout — architecture evolution, modularization, long-term platform maintainability — for the flow serving 5–6 million daily active users.
- Established automated testing discipline (unit, integration, UI) with XCTest and XCUITest; raised coverage to ~85% with a measurable drop in post-release defects; maintained 99.9%+ crash-free sessions with ~90% instrumentation of core checkout flows.
- Owned analytics and telemetry for every feature I led, and rolled out all new checkout features behind feature flags — more than half as A/B experiments.
- Taught accessibility and automated-testing sessions across the iOS engineering organization; mentored 12+ engineers.

**WalmartLabs (Sam's Club) — Senior iOS Engineer** (2017–2020)

- Migrated the Objective-C codebase to Swift with uninterrupted service for ~2M DAU; led the checkout refactor to unidirectional, reactive architecture with a significant test-coverage increase.

**WalmartLabs (ASDA) — Senior iOS Engineer** (2014–2017)

- Maintained legacy Objective-C modules across three years of releases for 500K+ DAU while rewriting components in Swift and converting the architecture to RxSwift.

### Conference Talks & Teaching

- Sessions on automated testing (TDD, BDD, mocks), iOS architecture, in-app subscriptions (RevenueCat), and specialized techniques at 360iDev, CocoaConf, and local iOS meetups (CocoaHeads Columbus / Cincinnati / Cleveland / Indianapolis).
- Co-organizer of Cincinnati CocoaDev.
- Led accessibility and automated-testing training across Walmart's iOS engineering organization.

### Education

B.A. Business Administration, Computer Information Systems emphasis — Cedarville College

## Notes / Flags

- **Instruments suite.** The JD explicitly asks for effective use of Xcode Instruments (bottlenecks, UI hitches, memory leaks). The vault documents performance and reliability outcomes at Walmart but never Instruments usage specifically, so neither resume claims it and the skills list omits it. Supplement from memory before interviews — this is a named key skill.
- **Nondeterministic async / device-vs-simulator debugging.** Another named key skill with no direct vault evidence. The Swift 6.2 structured-concurrency migration work at CLEAR is strong adjacent signal (the cover letter leans on it), but there's no bullet about diagnosing flaky async failures or simulator/device divergence. Supplement from memory.
- **Mapping / routing / geofencing bonus.** No vault evidence (CLEAR's flight detection is calendar + backend API work, not mapping). Omitted entirely — worth a sentence from memory if any exists, given how central navigation is to their product.
- **Android / JavaScript / C-family bonuses.** Not addressed: the vault documents Java (backend, pre-2013) but not JS/TS, and no documented C/C++/Rust work. The Kotlin backend work you've done recently is not in the vault as an engagement, so it wasn't used — consider whether to add it, since "works with Android/server peers" is part of this role's shape.
- **Dynamic type.** The accessibility bonus is covered via the Walmart accessibility-training bullet, but dynamic type specifically isn't documented. The cover letter stays at the accessibility-teaching level.
- **Summary wording.** Both resumes use the "5M+ daily active users" summary phrasing you approved for Whatnot. The vault's `Framing/Summary - iOS.md` still carries the older "2M+ DAU" wording — update the framing file when you're ready to make that permanent.
- **Unverified/drifting metrics reused.** Standing spot-checks: 5–6M DAU checkout, 4.8 stars / 18M ratings (App Store data drifts), ~2M DAU Sam's Club, "more than half" A/B proportion (kept unsharpened). The ~85% coverage figure is documented.
- **SQLite.** JD says "Core Data or SQLite" — vault evidence is Core Data and Realm; SQLite isn't claimed anywhere. Covered adequately by Core Data, but don't claim SQLite if asked directly unless it's true from memory.
