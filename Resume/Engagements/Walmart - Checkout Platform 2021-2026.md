---
type: engagement
company: "[[Walmart]]"
brand: ""
role: "Principal Software Engineer, iOS Platform / Checkout"
employment: employee
start: 2021-06
end: 2026-02
concurrent_with: ["[[McGraw-Hill - Sharpen iOS 2022-2023]]"]
industry: [E-Commerce, Retail, Mobile Applications]
team_size: "120+ iOS engineers (org); checkout team within"
team_context: "platform owner, checkout"
scale: "high-volume e-commerce"
tech: [Swift, Combine, MVVM, UIKit, SwiftUI, XCTest, XCUITest, GraphQL, Swift Package Manager, Microsoft Copilot, Visual Studio, Builder.io, Figma]
practices: [Technical Leadership, Code Review, Mentorship, iOS Architecture, Modularization, Performance Optimization, Reliability Engineering, Release Management, Unit Testing, Integration Testing, UI Testing, Engineering Standards, AI-Assisted Development, Agentic Tooling Evaluation, Cross-Team Training]
themes: [architecture, testing, mentorship, standards, platform-ownership, reactive, real-time, event-driven, scale, dau, api-design, release-management, agentic-tooling, ai-development, training, builder-io, design-system-integration]
deliverables: [checkout-platform, ios-engineering-standards, testing-discipline, interview-onboarding]
status: past
created: 2026-04-22
updated: 2026-06-04
---

# Walmart - Checkout Platform 2021-2026

## Context

Converted from contractor to full-time Walmart employee in June 2021 after a one-year contractor stint on the same app (see `Walmart - Contractor iOS 2020-2021`, to be created). Owned checkout platform architecture and delivery for Walmart's high-volume e-commerce iOS app. iOS organization of 120+ engineers across Walmart, ASDA, and Sam's Club brands. Engagement concluded February 2026.

## Role

Principal Software Engineer with ownership over iOS technical strategy for checkout — architecture evolution, modularization, long-term platform maintainability, and engineering standards across the full iOS organization. Checkout is the highest-stakes flow in the app: payment, fulfillment, and the final conversion step.

## Achievements

- Owned iOS technical strategy for checkout: architecture evolution, modularization, long-term platform maintainability. #architecture #platform-ownership
- Responsible for the checkout flow in Walmart's flagship iOS app, serving 5–6 million daily active users. #scale #checkout #platform-ownership #dau
- Architected unidirectional, reactive iOS systems in Swift and Combine with MVVM-style patterns. #architecture #reactive
- Architected and scaled reactive iOS systems using Swift, Combine, and GraphQL for high-traffic checkout flows serving millions of users. #architecture #reactive #combine #graphql #scale
- Drove real-time performance and reliability initiatives handling traffic spikes and event-driven interactions. #reliability #performance #real-time #event-driven
- Rolled out all new checkout features behind feature flags; more than half launched as A/B experiments measuring customer and business impact before full rollout. #experimentation #ab-testing #feature-flags #data-driven #rollout
- Owned analytics and telemetry for every feature led — built in instrumentation, updated team dashboards for org-wide visibility, and monitored behavior through production rollout, per the standard responsibility of every Walmart feature lead. #analytics #telemetry #instrumentation #dashboards #monitoring #rollout #data-driven
- Established automated testing discipline (unit, integration, UI) with XCTest and XCUITest; raised coverage to ~85% with a measurable drop in post-release defects. #testing #metrics
- Maintained 99.9%+ crash-free sessions; instrumented ~90% of core checkout flows. #reliability #metrics #instrumentation
- Defined and enforced iOS engineering standards across architecture, performance, security, and testing for the full 120+ iOS engineer organization. #standards #leadership
- At the request of the engineering accessibility team, taught sessions across the entire iOS engineering organization on the reasoning behind accessibility and iOS implementation techniques for building accessible apps. #accessibility #training #mentorship #standards #inclusive-design
- Collaborated with backend teams on GraphQL schema design and mobile-optimized APIs for checkout and payments. #graphql #api-design #backend-collaboration
- Led multi-team delivery and release readiness on a large inner-sourced codebase with frequent production releases. #release-management
- Mentored 12+ engineers and built standardized iOS onboarding materials. #mentorship #onboarding
- Served as an iOS interview bar-raiser: developed standardized interview materials and interviewed dozens of prospective engineers each year. #hiring #bar-raiser #interviewing
- Drove personal experimentation with AI development tooling across iOS work from late 2024 through February 2026 — beginning with Microsoft Copilot and Visual Studio, evaluating various Xcode plugins (most deficient for iOS-specific workflows), and expanding to design-integrated tooling as options matured. #agentic-tooling #ai-development #experimentation #microsoft-copilot
- Assisted the platform team during 2025 in evaluating and integrating Builder.io — connecting Walmart's design library with Figma to generate and update iOS views. Engineering management subsequently adopted Builder.io as the standard for new iOS view work and as an option for updating existing views; adoption was actively growing across the 120+ iOS engineer organization at time of departure. #builder-io #figma #design-system-integration #ai-development #view-generation #training #adoption-mandate
- Participated in Walmart engineering working groups evaluating AI development tools for adoption across the 120+ iOS engineer organization — contributed evaluation criteria, hands-on usage assessments, and integration recommendations. #agentic-tooling #working-groups #evaluation #cross-team-leadership
- Trained 80+ iOS engineers on AI-assisted development workflows through live sessions, with additional engineers onboarded via session recordings; folded selected tools into day-to-day iOS development processes. #training #mentorship #process-integration #agentic-tooling #scale-80

## Tech Stack

Swift, Combine, MVVM, XCTest, XCUITest, Swift Package Manager, GraphQL, inner-source monorepo patterns, CI/CD pipelines.

## Private Notes

_AI tooling arc at Walmart: early efforts (late 2024) centered on Microsoft Copilot + Visual Studio. Various Xcode plugins were tested and found deficient for iOS-specific workflows. During 2025 the focus shifted to deep evaluation, training, and integration of Builder.io — connecting Walmart's design library with Figma to generate and update iOS views. Claude Code and Codex were not yet available during the Walmart tenure; that work (FirefighterSpot and CLEAR) is 2026-onward and tracked on those engagements._

_Adoption scale: 80+ iOS engineers trained directly in live sessions, with additional engineers onboarded via session recordings. Builder.io was mandated by engineering management for all new iOS view work and offered as an option for updating existing views; adoption was actively growing across the 120+ iOS engineer organization at time of departure. Percentage-of-view-work numbers (if a target resume needs them) are still to be captured._

_UI framework context: primary UI was UIKit (Swift + Combine + MVVM). SwiftUI was just beginning to ramp up during the Principal era; included in `tech` for ATS keyword match but was not a dominant framework on this engagement. Testing was XCTest and XCUITest throughout — Swift Testing (the newer framework) was not used here; that's FirefighterSpot and CLEAR era._

_Scale figures: checkout flow cited at 5–6 million daily active users; "high-traffic / millions of users" and the real-time / traffic-spike / event-driven framing added 2026-06-04. Confirm the exact DAU number before a target resume leans on it._

_Feature-flag / A/B bullet added 2026-07-11 from Doug's direct recollection (prompted by the Thumbtack Customer Growth JD): all new checkout features rolled out behind feature flags, over half of which were used in A/B tests. "More than half" is his stated proportion — don't sharpen it to a specific percentage._

_Analytics/telemetry-ownership bullet added 2026-07-11, same source: every Walmart engineer who led a feature (small or large) was responsible for building in analytics and telemetry, updating dashboards for team-wide visibility, and monitoring behavior on rollout. This was an org-wide norm Doug practiced, not a distinction unique to him — keep the "per the standard responsibility" qualifier so the bullet stays honest._

## Related

- Company: [[Walmart]]
- Concurrent engagement: [[McGraw-Hill - Sharpen iOS 2022-2023]]
- Prior engagement at same company: [[Walmart - Contractor iOS 2020-2021]]
- Related WalmartLabs-era engagements: [[Walmart - ASDA 2014-2017]], [[Walmart - Sams Club 2017-2020]]
- Skills: _(to be linked once Skills/ pages exist)_
