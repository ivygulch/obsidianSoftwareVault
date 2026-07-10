---
type: engagement
company: "[[McGraw-Hill Education]]"
brand: "Sharpen"
role: "Data Engineer & iOS Developer"
employment: contractor
start: 2022-06
end: 2023-09
concurrent_with: ["[[Walmart - Checkout Platform 2021-2026]]"]
industry: [Education Technology, Mobile Applications]
team_size: "product team"
team_context: "core iOS + data engineering contributor"
scale: "consumer education app"
tech: [Swift, iOS SDK, RevenueCat, StoreKit, In-App Subscriptions, AWS, Analytics Integration, Push Notifications, Email Automation, SMS Automation]
practices: [Data Engineering, Data Lake, Authentication, Onboarding, Feature Development, Internal Tools, Subscription Integration, Paywall Development, Entitlement Management]
themes: [onboarding, authentication, analytics, internal-tools, data-engineering, subscriptions, in-app-purchase, monetization, revenuecat, paywall, entitlements]
deliverables: [sharpen-ios-features, sharpen-plus-subscriptions, internal-tools-suite, aws-data-lake]
status: past
created: 2026-04-22
updated: 2026-06-17
---

# McGraw-Hill - Sharpen iOS 2022-2023

## Context

Concurrent contract alongside Walmart full-time role. Core team member on McGraw-Hill Sharpen, a mobile study application for students. Work included the iOS in-app subscription system ("Sharpen Plus"), built on RevenueCat.

## Role

Core iOS developer and data engineer on the Sharpen product team — delivered user-facing features (settings, onboarding, authentication), contributed to the RevenueCat-based in-app subscription ("Sharpen Plus") experience as part of the iOS team, and built internal tooling plus AWS-backed data infrastructure.

## Achievements

- Contributed to the iOS in-app subscription experience ("Sharpen Plus") on RevenueCat (purchases-ios) as part of the product team — Offerings and pricing configured server-side and fetched at runtime (no hard-coded product IDs), with a single "Premium" entitlement gating premium features. #revenuecat #in-app-subscriptions #storekit #monetization #ios
- Worked on paywall and purchase/restore flows over StoreKit via RevenueCat, including free-trial / introductory-offer eligibility handling and generic subscription-period and price-per-month presentation across recurring durations. #paywall #storekit #free-trial #in-app-subscriptions
- Helped tie subscriptions to the user's McGraw-Hill account (app user ID = account URN, not device) and sync entitlement state to the McGraw-Hill backend after purchase/restore with retry. #entitlements #backend-sync #revenuecat
- Delivered settings, onboarding, and authentication features for the Sharpen iOS app. #features #onboarding #authentication
- Integrated five analytics tools into the Sharpen iOS app. #analytics #integration
- Built seven internal tools including email/SMS automation, AWS data lake, and push notifications. #internal-tools #aws #data-engineering #push-notifications

## Tech Stack

Swift, iOS SDK, RevenueCat (purchases-ios), StoreKit, in-app subscriptions, AWS (data lake), analytics SDKs, push notification services, email/SMS automation systems.

## Private Notes

_Cleared for résumé and profile use (confirmed 2026-06-08); previously marked "not for any resume."_

_Describe Sharpen as a "mobile study app." A "TikTok-style / short-video" characterization is unverified against this engagement record — don't use it unless confirmed._

_RevenueCat/subscription work was shared across the iOS team — Doug was one of the engineers building it, not the sole owner. Frame as "contributed to" / "worked on" / "helped build," never sole authorship._

_RevenueCat detail confirmed 2026-06-17 by investigating the Sharpen-iOS source repo: purchases-ios v4.25.2, branded "Sharpen Plus," code under `Sharpen/Sharpen Plus/FreeTrial/`. Single "Premium" entitlement; auto-renewing subscriptions with optional intro/free-trial discounts; `Purchases.configure` keyed by build config `SHARPEN_KEY_REVENUECAT` with appUserID = account URN; `apiClient.syncSubscriptionStatus` pushes entitlement state to the MH backend after purchase/restore. Concrete SKUs/prices live in the RevenueCat dashboard / App Store Connect, not in source — so don't cite specific product IDs, prices, or renewal periods. RevenueCat also fronts Apple/Play/Stripe across the Android (purchases:6.9.4) and Web (GraphQL-proxied) clients, but this engagement's verified work is the iOS integration — don't claim the Android/Web implementations. A newer PurchaseManager under `Sharpen Plus/FreeTrial/Managers/` is the live path; an older `FreeTrial/Manager/` variant looks like legacy/dead code._

## Related

- Company: [[McGraw-Hill Education]]
- Concurrent engagement: [[Walmart - Checkout Platform 2021-2026]]
- Skills: _(to be linked once Skills/ pages exist)_
