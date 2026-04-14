# StoryRiffs: Collaborative Storytelling App

## Project Overview

**Concept:** A mobile app for collaborative, turn-based storytelling inspired by campfire storytelling and improv comedy's "yes, and" principle. Players take turns adding to a shared narrative, building stories together asynchronously.

**Domain:** storyriffs.com (registered)

**Current Status:** Proof-of-concept phase with beta testers

**Creator Context:** New author building Backcountry Mysteries series, exploring tools for reader engagement while keeping StoryRiffs separate from author platform initially.

---

## Core Value Proposition

### The Problem
- Traditional collaborative storytelling games (like "Pass the Story") work well in person but have poor digital implementations
- Existing solutions are either web-only, inactive/stagnant (FoldingStory, Byline), or overly complex (Storium)
- No well-designed, mobile-native collaborative storytelling app exists

### The Solution
A simple, fun, mobile-first app where:
- Friends can create stories together asynchronously
- Players add paragraphs in turns
- Stories have clear endings (not endless)
- Finished stories can be read and shared
- Works offline (critical requirement)

### Target Users (POC Phase)
- Beta testers (friends, fellow authors, writing groups)
- People who enjoy creative writing games
- Friend groups looking for asynchronous social activities

### Future Vision
Could evolve into a white-label platform for authors to engage their readers through collaborative storytelling in their fictional universes.

---

## Market Research Findings

### Direct Competitors Analysis

**FoldingStory (foldingstory.com)**
- Web-only, founded ~2011
- Stories take years to complete (one took 6+ years)
- "Blind" mechanic (only see previous line)
- Technically alive but barely breathing

**Storium (storium.com)**
- RPG-style structured storytelling
- $251K Kickstarter (6,676 backers, 1005% of goal)
- Still active with small loyal community
- Web-only, complex card-based mechanics
- Last platform update: May 2023

**Byline (byline.page)**
- Simple web app
- Exquisite corpse style (line-by-line)
- Minimal traction

**StoryPass (storypass.app)**
- Claims iOS/Android but not found in app stores
- Likely vaporware - nice landing page, no actual product

**Pass the Story (design case study)**
- Comprehensive UX design by Abhinandan Pande in 2024
- Never actually built
- Extensive design thinking already done

### Key Insight
**The market is essentially empty.** What appears as competition is actually abandoned projects, niche communities, or vaporware. No serious, well-designed, mobile-native collaborative storytelling app exists.

### Adjacent Markets (For Context)

**Interactive Fiction (Different Model)**
- Episode: 139M downloads, $256M revenue
- Choices: 63.5M installs, $231M revenue
- These are consumption apps (reading branching stories), not creation/collaboration

**Fan Engagement Platforms**
- Market size: $5.9B in 2024, growing at 16.3% CAGR to 2034
- Fan fiction platforms: $1.2B in 2024, projected $3.7B by 2033
- Wattpad: 90M users, sold for $600M

**Indie Author Tools Market**
- Self-publishing market: $1.85B in 2024, projected $6.16B by 2033
- 500,000 US self-published works in 2023 vs 10,000 traditional
- Authors spend $2,940-$5,660 per book on services
- BookFunnel, BookBub, Shopify widely adopted

---

## Technical Architecture

### Platform Strategy

**Phase 1 (POC): iOS Only**
- Native SwiftUI app
- Fastest path to testable product
- Leverages your existing iOS skills

**Phase 2 (If Validated): Cross-Platform**
- Same Firebase backend
- Web client (simple HTML/JS)
- Android native (Kotlin) - or web-first for Android users

### Technology Stack

**Frontend (iOS)**
- SwiftUI
- Firebase SDK for iOS
- Offline-first design

**Backend (Firebase)**
- Firestore - database with built-in offline sync
- Cloud Functions - server-side validation (optional for POC)
- Firebase Auth - anonymous or simple authentication
- FCM - push notifications (phase 2)

**Why Firebase:**
- Excellent offline support (critical requirement)
- Real-time sync built in
- Cross-platform SDKs (iOS, Android, Web)
- Free tier sufficient for testing
- Faster than building custom backend
- You're already comfortable with it

### Architecture Decision: No TCA

**Considered:** The Composable Architecture (TCA)
- Excellent for testability and state management
- Good fit for complex multiplayer state
- But: iOS/Swift only, doesn't transfer to web/Android

**Decision:** Simple SwiftUI with @Observable
- Faster to build POC
- Learnings about game mechanics transfer cross-platform
- Can refactor to TCA later if concept validates
- Focus on validating the experience, not the architecture

---

## Data Model

### Firestore Structure

```
/games/{gameId}
    ├── inviteCode: String (6-char code)
    ├── status: "waiting" | "inProgress" | "completed"
    ├── currentPlayerIndex: Number
    ├── totalRounds: Number
    ├── currentRound: Number
    ├── createdAt: Timestamp
    ├── createdBy: String (playerId)
    │
    ├── /players/{playerId}
    │       ├── name: String
    │       ├── joinedAt: Timestamp
    │       ├── order: Number
    │
    └── /paragraphs/{paragraphId}
            ├── playerId: String
            ├── playerName: String
            ├── text: String
            ├── order: Number
            ├── round: Number
            ├── createdAt: Timestamp
```

### Swift Models

```swift
import FirebaseFirestore

struct Game: Codable, Identifiable {
    @DocumentID var id: String?
    var inviteCode: String
    var status: GameStatus
    var currentPlayerIndex: Int
    var totalRounds: Int
    var currentRound: Int
    var createdAt: Date
    var createdBy: String
}

enum GameStatus: String, Codable {
    case waiting      // Players joining
    case inProgress   // Taking turns
    case completed    // All rounds done
}

struct Player: Codable, Identifiable {
    @DocumentID var id: String?
    var name: String
    var joinedAt: Date
    var order: Int
}

struct Paragraph: Codable, Identifiable {
    @DocumentID var id: String?
    var playerId: String
    var playerName: String
    var text: String
    var order: Int
    var round: Int
    var createdAt: Date
}
```

---

## User Experience Design

### Core User Flow

```
1. CREATE GAME
   - Enter your name
   - Write opening paragraph
   - Set number of rounds (default: 3)
   - Get shareable invite code
   - Wait in lobby for players

2. JOIN GAME
   - Enter 6-character invite code
   - Enter your name
   - See current players in lobby
   - Wait for creator to start

3. PLAY
   - Creator starts when ready (2+ players)
   - Players take turns in join order
   - On your turn: see full story, add paragraph, submit
   - Off your turn: read story updates, wait for notification
   - Progress indicator shows current round

4. END
   - After N rounds (each player writes N times)
   - Everyone sees completed story
   - Stories can be read and shared
```

### Screen List (7 Screens)

1. **Home**
   - "Start a Story" button
   - "Join a Story" button
   - List of active/completed games (phase 2)

2. **Create Game**
   - Name text field
   - Opening paragraph text view
   - Rounds stepper (default 3, range 1-5)
   - "Create" button

3. **Lobby - Creator View**
   - Large display of invite code (tap to copy)
   - Share button (iOS share sheet)
   - List of joined players
   - "Start Game" button (enabled when 2+ players)

4. **Join Game**
   - 6-character code input field (auto-uppercase)
   - Name text field
   - "Join" button

5. **Lobby - Joiner View**
   - "Waiting for [creator name] to start..."
   - List of current players
   - Your position in turn order

6. **Game Play**
   - Scrollable story view (all paragraphs, player attribution)
   - Current player indicator
   - Progress: "Round 2 of 3"
   
   **If your turn:**
   - Text editor for paragraph
   - Character count (optional)
   - "Submit" button
   
   **If not your turn:**
   - "Waiting for [player name]..."
   - Read-only story view

7. **Completed Story**
   - Full story, nicely formatted
   - Player attribution for each paragraph
   - Story title (generated or voted - TBD)
   - Share button

### Design Decisions from Research

Based on "Pass the Story" case study and competitor analysis:

**Visibility:** Full story visible (not blind like FoldingStory)
- Blind approach creates humor but incoherent narratives
- Full visibility allows building on previous content

**Turn Length:** Paragraph, not sentence
- Sentences too short to move story meaningfully
- Paragraphs give room for development

**Pacing:** Asynchronous, not real-time
- No scheduling coordination required
- Works with busy lives
- Notifications when it's your turn

**Game End:** Fixed rounds with clear endpoint
- Prevents stories trailing off forever
- Creates natural closure
- Example: 4 players × 3 rounds = 12 paragraphs

**Group Size:** 3-6 players optimal
- Enough variety in voices
- Not too many to coordinate
- Faster completion

**Access:** Private invite-only (POC)
- No public matchmaking yet
- Avoids moderation issues
- Controlled testing environment

---

## Offline Support (Critical Requirement)

### Why Offline Matters

- Users may be in areas with poor connectivity (outdoors, subway, travel)
- Want to draft paragraphs without pressure of live connection
- Reading completed stories should work anywhere
- Aligns with adventure/outdoor theme of creator's work

### How Firebase Handles Offline

```swift
// Enable offline persistence (once at app launch)
let settings = FirestoreSettings()
settings.cacheSettings = PersistentCacheSettings()
Firestore.firestore().settings = settings
```

**Offline Behavior:**

| Action | Online | Offline |
|--------|--------|---------|
| Read game/story | From server | From local cache |
| Draft paragraph | Writes to server | Queued locally, syncs when online |
| Listen for updates | Real-time | Fires from cache, updates when reconnected |
| Submit paragraph | Immediate | Queued, syncs when online |
| Join game | Works | Fails (needs server verification) |

**Key Features:**
- Writes succeed "locally" immediately (optimistic UI)
- Firestore queues pending writes
- Auto-syncs when connection returns
- Conflict resolution handled by Firestore

---

## Game Mechanics Details

### Turn Logic

```swift
// Determine current turn
var currentPlayer: Player {
    let activePlayers = players.sorted { $0.order < $1.order }
    return activePlayers[currentPlayerIndex % activePlayers.count]
}

// Check if it's my turn
var isMyTurn: Bool {
    guard status == .inProgress else { return false }
    return currentPlayer.id == myPlayerId
}

// Advance to next turn
func advanceTurn() {
    currentPlayerIndex += 1
    
    // Check if round is complete
    if currentPlayerIndex % players.count == 0 {
        currentRound += 1
    }
    
    // Check if game is complete
    if currentRound > totalRounds {
        status = .completed
    }
}
```

### Invite Code System

```swift
// Generate unique 6-character code
func generateInviteCode() -> String {
    let chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789" // No ambiguous characters (O/0, I/1)
    return String((0..<6).map { _ in chars.randomElement()! })
}

// Find game by code
func findGame(byCode code: String) async throws -> Game? {
    let snapshot = try await db.collection("games")
        .whereField("inviteCode", isEqualTo: code.uppercased())
        .whereField("status", isEqualTo: "waiting")
        .limit(to: 1)
        .getDocuments()
    
    return try snapshot.documents.first?.data(as: Game.self)
}
```

---

## POC Scope

### Must Have (Phase 1)

**Core Gameplay:**
- Create game with opening paragraph
- Generate and share invite code
- Join game via code
- Lobby with player list
- Turn-based paragraph writing
- See full story while writing
- Round tracking
- Game completion
- Read finished stories

**Technical:**
- Firebase Firestore integration
- Offline persistence
- Real-time updates via listeners
- Basic error handling

**UI:**
- All 7 core screens
- Simple, functional design
- Clear turn indicators
- Story display with player attribution

### Don't Need Yet (Phase 2+)

- Push notifications (use polling for POC)
- User accounts/profiles
- Game history/archive
- Story editing after submission
- Public game discovery
- Voting on story elements
- AI participants
- Story illustration
- Advanced moderation
- Analytics

### Success Metrics for POC

**Engagement:**
- Do testers finish games they start?
- Do they start multiple games?
- How long does a typical game take?

**Quality:**
- Are the stories coherent?
- Do players report having fun?
- What makes stories succeed vs fail?

**Friction Points:**
- Where do players drop off?
- What's confusing?
- What feels slow or tedious?

---

## Open Design Questions

### To Decide During Development

1. **Turn time limits:** Should there be timeouts? Auto-skip if no response in 48 hours?

2. **Paragraph constraints:** Min/max length? Character counter?

3. **Story title:** How is it determined? Last player chooses? Vote? Auto-generate?

4. **Player identity:** Anonymous IDs? Device-based? Simple name-only?

5. **Game abandonment:** What if someone ghosts mid-game? Can others continue?

6. **Editing:** Can you edit your paragraph after submitting? Time limit?

7. **Visibility of drafts:** Can other players see "Player X is writing..."?

---

## Future Evolution Paths

### Path 1: Consumer Social App
- Public game discovery
- User profiles and reputation
- Genre-specific communities
- Featured stories
- Monetization via subscriptions or ads

### Path 2: White-Label Author Tool
- Authors create branded versions for their readers
- Seed stories set in their fictional worlds
- Fan engagement and list building
- B2B SaaS pricing ($20-50/month per author)
- Your own Backcountry Mysteries implementation as proof

### Path 3: Educational Platform
- Classroom writing exercises
- Teacher dashboards
- Student portfolios
- School/district licensing

**Current Strategy:** Build POC first, let user feedback guide which path to pursue.

---

## Development Approach

### Philosophy: Build Fast, Learn Fast

1. **POC First** - Validate the core experience is fun
2. **Simple Architecture** - No over-engineering for uncertain future
3. **Real Testers** - 5-10 engaged beta testers
4. **Tight Iteration** - Weekly feedback cycles
5. **Decide Later** - Cross-platform, monetization, features come after validation

### Why Not Over-Architect

**Don't optimize for:**
- Scale you don't have yet
- Platforms you haven't validated
- Features users haven't requested
- A future that might not happen

**Do optimize for:**
- Speed to first playable build
- Learning what makes the game fun
- Iterating based on real usage
- Validating the core concept

---

## Key Insights from Research

### Why Previous Apps Failed/Stayed Small

1. **Retention is brutal** - Async games die when one person stops responding
2. **Quality control hard** - User-generated collaborative content goes off rails
3. **Network effects problem** - Need friends to play, but friends won't download until you're playing
4. **Unclear monetization** - Hard to find business model that works
5. **Timing matters** - Too early (2011-2014) for mobile-first social gaming

### What Could Make StoryRiffs Different

1. **Mobile-native from start** - Previous attempts were web-first
2. **Offline-first design** - Works with spotty connectivity
3. **Clear game endpoints** - Stories finish, not endless
4. **AI potential** - Could fill in for slow/absent players (future)
5. **Author platform angle** - B2B path if consumer doesn't scale

### Critical Success Factors

1. **Completion rate** - Games must finish more often than not
2. **Story quality** - Results need to be fun to read/share
3. **Low friction** - Easy to start, easy to invite, easy to play
4. **Right pacing** - Fast enough to maintain momentum, slow enough for thoughtful writing

---

## Competitive Advantages

### For POC Phase
- Only modern, mobile-native implementation
- Offline support (competitors mostly web-only)
- Clean, simple UX vs overly complex alternatives
- Actually shipping (vs case studies and vaporware)

### For Future Phases
- Cross-platform readiness (Firebase backend)
- Potential AI integration (keep games moving)
- White-label capability (author platform pivot)
- Creator's insight as indie author (dogfooding)

---

## Resources and References

### Existing Products Analyzed
- FoldingStory.com - longest running, minimal activity
- Storium.com - most successful, complex mechanics
- Byline.page - simple, minimal traction
- StoryPass.app - appears to be vaporware

### Design Research
- "Pass the Story" case study by Abhinandan Pande (2024)
- Story Toss Rails app by Felipe Vogel (2021)
- Various classroom implementations of fold-over stories

### Market Data Sources
- Fan engagement platform market research
- Self-publishing industry statistics
- Interactive fiction app revenue data
- Indie author tool adoption patterns

---

## Next Steps for Development

### Immediate (Week 1-2)
1. Set up Firebase project
2. Create Xcode project with Firebase SDK
3. Implement core data models
4. Build Create Game flow
5. Build Join Game flow

### Short-term (Week 3-4)
6. Implement lobby screens
7. Build game play screen
8. Add real-time listeners
9. Implement turn logic
10. Test with 2-3 people

### Before Beta (Week 5-6)
11. Polish UI/UX
12. Add error handling
13. Implement completed story view
14. TestFlight setup
15. Recruit 5-10 beta testers

### Beta Testing (Week 7-8)
16. Monitor completion rates
17. Gather qualitative feedback
18. Identify friction points
19. Iterate on core mechanics
20. Decide: continue, pivot, or stop

---

## Contact and Project Info

**Creator:** Doug (indie author, iOS developer)
**Domain:** storyriffs.com
**Current Phase:** Pre-development (design complete)
**Target:** TestFlight beta within 4-6 weeks
**Budget:** Bootstrap (Firebase free tier, own labor)

---

## Appendix: Technical Snippets

### Firebase Setup

```swift
// FirebaseApp.swift
import FirebaseCore
import FirebaseFirestore

class FirebaseApp {
    static let shared = FirebaseApp()
    let db = Firestore.firestore()
    
    private init() {
        // Configure offline persistence
        let settings = FirestoreSettings()
        settings.cacheSettings = PersistentCacheSettings()
        db.settings = settings
    }
}
```

### Game Creation Example

```swift
func createGame(playerName: String, openingParagraph: String, rounds: Int = 3) async throws -> Game {
    let gameRef = db.collection("games").document()
    let playerId = UUID().uuidString
    
    let game = Game(
        inviteCode: generateInviteCode(),
        status: .waiting,
        currentPlayerIndex: 0,
        totalRounds: rounds,
        currentRound: 1,
        createdAt: Date(),
        createdBy: playerId
    )
    
    try await gameRef.setData(from: game)
    
    // Add creator as first player
    let player = Player(name: playerName, joinedAt: Date(), order: 0)
    try await gameRef.collection("players").document(playerId).setData(from: player)
    
    // Add opening paragraph
    let paragraph = Paragraph(
        playerId: playerId,
        playerName: playerName,
        text: openingParagraph,
        order: 0,
        round: 0,
        createdAt: Date()
    )
    try await gameRef.collection("paragraphs").document().setData(from: paragraph)
    
    return game
}
```

### Real-time Game Listening

```swift
func listenToGame(gameId: String) -> AsyncStream<Game> {
    AsyncStream { continuation in
        let listener = db.collection("games").document(gameId)
            .addSnapshotListener { snapshot, error in
                guard let game = try? snapshot?.data(as: Game.self) else { return }
                continuation.yield(game)
            }
        
        continuation.onTermination = { _ in listener.remove() }
    }
}
```

---

*Last Updated: March 2026*
*Project Status: Design Complete, Ready for Implementation*
