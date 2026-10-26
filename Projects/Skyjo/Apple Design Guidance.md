---
type: reference
created: 2026-08-14
updated: 2026-08-14
tags: [skyjo, design, apple, appstore, hig]
---

# Apple Design Guidance

Reference for the UX/UI brainstorm. Two distinct Apple documents govern two distinct things: the [asset best practices](https://developer.apple.com/app-store/asset-best-practices/) page governs the **App Store presence** (how Skyjo sells); the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) govern the **in-app experience** (how Skyjo works). Don't brainstorm screens against the asset page. Product decisions these must serve: [[Projects/Skyjo/Design|Design]].

## App Store asset best practices (fetched 2026-08-14)

- **App icon** — legible at every size, expressive of personality; Apple now wants layered "Liquid Glass" icons built in Icon Composer (one design → iPhone/iPad/Mac/Watch variants). Straddles marketing and product; for a licensed game, how much Magilano trade dress the icon echoes is a licensing conversation, not just a design one.
- **Screenshots (up to 10)** — real UI in actual use, strongest feature first, sequenced as a story; no accolades, CTAs, pricing, or unverifiable claims (App Review 2.3). Up to 3 appear in search results.
- **App previews (up to 3 videos)** — real gameplay capture only, strong first seconds, seamless loop, must work muted (audio off by default), deliberate pacing over quick cuts.
- **Product-page header + search-results asset** — single clear idea, designed for first-time visitors; a universal creative asset can serve both for brand consistency.
- **In-App Events cards** — 16:9 event card + 9:16 details page, visually continuous; relevant later for seasonal/daily-challenge events.
- **Localization** — all assets localized per storefront, text overlays included. Matches [[Projects/Skyjo/Marketing|Marketing]]: DE/FR/EN metadata and screenshots per storefront.
- **All-ages bar** — store assets must meet 4+ regardless of app rating.
- **Tooling** — Figma/Photoshop/Pixelmator templates from Apple; product-page preview tool in App Store Connect; custom product pages and A/B testing (product page optimization) available.
- Design implication worth carrying into UI work: the table/board screen must read instantly as SKYJO in a static thumbnail — card grid, colors, score state legible without motion.

## HIG sections relevant to Skyjo

Apple's own one-line descriptions (harvested 2026-08-14); read the full pages in a browser — the HIG site is JS-rendered and resists archiving.

| Page | Apple's description |
|---|---|
| [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games) | "When people play your game on an Apple device, they dive into the world you designed while relying on the platform features they love." |
| [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) | "Precise, intuitive game controls enhance gameplay and can increase a player's immersion in the game." |
| [Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) | "Game Center is Apple's social gaming network… boosts the discovery of your game across players' devices." |
| [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) | "A unique, memorable icon expresses your app's or game's purpose and personality…" |
| [Color](https://developer.apple.com/design/human-interface-guidelines/color) | "Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback…" |
| [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | "…display legible text, convey an information hierarchy, communicate important content, and express your brand or style." |
| [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | "A consistent layout that adapts to various contexts… on all their devices." |
| [Motion](https://developer.apple.com/design/human-interface-guidelines/motion) | "Beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction…" |
| [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) | "…engage people's sense of touch and bring their familiarity with the physical world into your app or game." |
| [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) | "Feedback helps people know what's happening, discover what they can do next, understand the results of actions, and avoid mistakes." |
| [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | "Accessible user interfaces empower everyone to have a great experience with your app or game." |
| [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) | "…a dark color palette to provide a comfortable viewing experience tailored for low-light environments." |
| [Launching](https://developer.apple.com/design/human-interface-guidelines/launching) | "A streamlined launch experience helps people start using your app or game immediately." |
| [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) | "Onboarding can help people get a quick start using your app or game." |
| [In-app purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase) | "People can use in-app purchase to pay for virtual goods… securely within your app." |

## Skyjo-specific implications (ours, not Apple's)

- **Color** carries double duty: the official card-color bands (-2/-1 purple, 0 blue, 1–4 green, 5–8 yellow, 9–12 red) are a fidelity requirement from review mining — HIG color guidance (status/feedback, contrast, color-blind support) must work *around* that fixed palette, not replace it. Color-blind accessibility likely needs a secondary channel (numerals are already there; consider patterns).
- **Accessibility/Typography**: Dynamic Type on cards is a competitive weapon — a clone earned a 1★ purely for unreadable cards. Card numerals must scale.
- **Game Center**: the daily-challenge leaderboard maps directly onto Game Center leaderboards; achievements fit the retention design. Also a discovery channel.
- **Launching/Onboarding**: "play as soon as installation completes" — family users, zero tutorial walls; the physical game's players already know the rules, so onboarding should be skippable rules-refresher, not forced tutorial.
- **Motion/Haptics**: card flip/swap/discard are the moments that make digital SKYJO *feel* like table SKYJO — the physical-world-familiarity framing in the haptics guidance is exactly the brief. Unhurried play option (Design.md) constrains motion pacing: animations must be interruptible/quick-settable.
- **In-app purchase**: one-time unlock + expansion IAP (Handelabra model) — HIG IAP patterns govern the paywall presentation; no dark patterns, which is also the brand position against the clones.
