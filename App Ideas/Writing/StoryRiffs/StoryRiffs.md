# StoryRiffs

**Concept:** A mobile app for collaborative, turn-based storytelling inspired by campfire storytelling and improv comedy's "yes, and" principle. Players take turns adding paragraphs to a shared narrative, building stories together asynchronously.

**Domain:** storyriffs.com (registered)
**Status:** Design complete, ready for implementation
**Platform:** iOS first (SwiftUI + Firebase), cross-platform later if validated

---

## Core Idea

Friends create stories together asynchronously. One person starts with an opening paragraph, invites others via a code, and players take turns adding to the narrative. Stories have a fixed number of rounds so they actually end. Finished stories can be read and shared.

**Key design decisions:**
- Full story visible (not blind/exquisite corpse style)
- Paragraph-length turns (not single sentences)
- Asynchronous (not real-time)
- Fixed rounds with clear endpoints
- Private invite-only (POC phase)
- Offline-first (works without connectivity)

---

## Why It Could Work

The market is essentially empty. Existing attempts are either:
- **Abandoned** (FoldingStory — stories take years to complete)
- **Overly complex** (Storium — RPG-style card mechanics)
- **Vaporware** (StoryPass — nice landing page, no product)
- **Never built** (Pass the Story — design case study only)

No serious, well-designed, mobile-native collaborative storytelling app exists.

---

## Adjacent Markets

| Market | Size | Notes |
|--------|------|-------|
| Interactive fiction apps | Episode: $256M rev, Choices: $231M rev | Consumption, not collaboration |
| Fan engagement platforms | $5.9B (2024), 16.3% CAGR | Growing fast |
| Fan fiction platforms | $1.2B (2024), projected $3.7B by 2033 | Wattpad sold for $600M |
| Self-publishing tools | $1.85B (2024), projected $6.16B by 2033 | 500K self-pub works/year |

---

## Future Evolution Paths

### Path 1: Consumer Social App
Public game discovery, user profiles, genre communities, featured stories. Monetize via subscriptions or ads.

### Path 2: White-Label Author Tool
Authors create branded versions for their readers. Seed stories set in their fictional worlds. Fan engagement and list building. B2B SaaS pricing ($20-50/month per author). Own series as proof of concept.

### Path 3: Educational Platform
Classroom writing exercises, teacher dashboards, student portfolios, school/district licensing.

**Strategy:** Build POC first, let user feedback guide which path.

---

## Critical Success Factors

1. **Completion rate** — games must finish more often than not
2. **Story quality** — results need to be fun to read/share
3. **Low friction** — easy to start, easy to invite, easy to play
4. **Right pacing** — fast enough for momentum, slow enough for thoughtful writing

## Why Previous Apps Failed

1. Retention is brutal — async games die when one person stops responding
2. Quality control — collaborative content goes off rails
3. Network effects — need friends to play, friends won't download until you're playing
4. Unclear monetization
5. Web-first in a mobile-first world

---

## Open Questions

- Turn time limits / auto-skip if someone ghosts?
- Paragraph length constraints?
- How story titles are determined
- AI fill-in for absent players (future)
- Moderation approach

---

## References

- **FoldingStory** (foldingstory.com) — web-only, founded ~2011, barely active
- **Storium** (storium.com) — $251K Kickstarter, small loyal community, complex
- **Byline** (byline.page) — simple web app, minimal traction
- **"Pass the Story"** — comprehensive UX case study by Abhinandan Pande (2024), never built

*Full project brief with technical architecture: [[storyriffs-project-brief.md]]
