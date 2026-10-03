---
type: note
status: draft
tags: [proverbs, app-idea, bible-text, kjv, bsb, licensing]
created: 2026-10-03
updated: 2026-10-03
---

# Applying Proverbs — Text Version Comparison

Side-by-side samples of the two license-free candidates for the app's text: the King James Version (public domain in the US) and the Berean Standard Bible (CC0 since 2023). Both texts were fetched 2026-10-03 (KJV from bible-api.com, BSB from biblehub.com/bsb). Context: [[Bible Text Licensing & APIs]] found that no major copyrighted translation permits a complete book without a negotiated license, which rules out the preferred ESV for a freemium app unless Crossway licenses it.

## Samples

**Proverbs 3:5–6**

- KJV: Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.
- BSB: Trust in the LORD with all your heart, and lean not on your own understanding; in all your ways acknowledge Him, and He will make your paths straight.

**Proverbs 11:1** ([[Wisdom Deck Reference|Wisdom Deck]] card 2)

- KJV: A false balance is abomination to the LORD: but a just weight is his delight.
- BSB: Dishonest scales are an abomination to the LORD, but an accurate weight is His delight.

**Proverbs 14:31** (Wisdom Deck card 12)

- KJV: He that oppresseth the poor reproacheth his Maker: but he that honoureth him hath mercy on the poor.
- BSB: He who oppresses the poor taunts their Maker, but whoever is kind to the needy honors Him.

**Proverbs 26:4–5**

- KJV: Answer not a fool according to his folly, lest thou also be like unto him. Answer a fool according to his folly, lest he be wise in his own conceit.
- BSB: Do not answer a fool according to his folly, or you yourself will be like him. Answer a fool according to his folly, lest he become wise in his own eyes.

## What the sample shows

- 3:5–6 is almost exactly what a mechanical pronoun-and-verb pass over the KJV would produce; the one wording difference is "direct thy paths" against "make your paths straight."
- 11:1 and 14:31 are the cases a mechanical pass cannot reach. "False balance" to "dishonest scales" and "reproacheth" to "taunts" are vocabulary and sense decisions, and in 14:31 the KJV's second half reads the other way around from the BSB's (honoring God leads to mercy, versus mercy honors God).
- The BSB keeps the KJV's cadence and some of its vocabulary ("lest," "abomination"), so the register is closer to the ESV than a fully colloquial translation would be.

## Modernizing the KJV by rule (assessment, 2026-10-03)

The mechanical layer is a few hundred rules: pronoun mapping (thou, thee, thy, thine, ye to you and your, losing the singular-plural distinction that modern English lacks anyway), verb endings (-est and -eth, plus a lexicon of irregulars such as art, hast, hath, doth, wilt, shalt, canst, wast, saith), function words (unto, whoso, wherefore, hither), and spelling (subtil, shew). Proverbs is about 15,000 words in 915 verses; a tokenizing pass with a lexicon and an exception list is a day or two of work, with a unit test per rule and a diff log.

The editorial layer is what makes it not one-for-one. Words whose meaning has shifted need a decision per occurrence: froward (about 20 times), simple (naive), strange woman (adulteress), prevent (go before), let (hinder), conversation (conduct), bowels (compassion), surety, reprove, instruction (discipline). Word order and idiom ("Go to the ant, thou sluggard") stay 1611 after the pronoun swap, and every reordering moves the result further from "exactly the same." The KJV's italics for supplied words and small-caps LORD need a convention. A full read-through after the mechanical pass is the real work: days for someone who knows the book.

Prior modernizations exist: the Updated King James Version and the World English Bible (a revision of the 1901 ASV) are public domain, and several "KJV with modern pronouns" editions exist with varying copyright status (current terms not verified). The KJV is public domain in the US; in the UK it is under perpetual Crown copyright administered through Cambridge University Press, generally not enforced against digital apps but a known wrinkle for a worldwide listing.

## Open

- Whether a modernized KJV or the BSB is the base text, or whether to ship both with a version switch.
- Whether any existing public-domain modernization already matches the intent.
- A larger sample across the discourse chapters (1–9) and the numerical sayings (30–31), where the two texts may diverge more than in the two-line sayings.

## Related

- [[Applying Proverbs]]
- [[Bible Text Licensing & APIs]]
- [[Idea Backlog]] — Text section
