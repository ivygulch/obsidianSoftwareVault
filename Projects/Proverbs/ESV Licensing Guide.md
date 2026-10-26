---
type: research
confidence: assumed
tags: [proverbs, bible-text, esv, licensing, crossway]
source: Grok research summary, 2026-10-26, supplied by Doug; not verified against the linked Crossway pages
created: 2026-10-26
updated: 2026-10-26
---

> Provenance: compiled by Grok at Doug's request on 2026-10-26 and moved here unedited from `/d/dl/`. Confidence is `assumed` until the Crossway pages linked below are fetched and checked. The broader version survey is [[Bible Text Licensing & APIs]]; the ISA's text decision (free text first, ESV investigated after a working prototype) is in [[Projects/Proverbs/Ideal State|Ideal State]].

# ESV (English Standard Version) Licensing for an iOS App  
**Focus: Book of Proverbs**  
*Research summary — October 2026*

> **Disclaimer**: This is a research summary based on publicly available information from Crossway and ESV.org. It is **not legal advice**. Always review the current official terms and consult Crossway or a qualified attorney for your specific use case.

---

## 1. Copyright Ownership

- The English Standard Version (ESV) is copyrighted **© 2001 by Crossway**, a publishing ministry of Good News Publishers.
- Modern Bible translations create new copyrights even though the underlying ancient texts are in the public domain.
- Crossway controls reproduction, distribution, and display of the ESV text.

---

## 2. Standard Use Guidelines (No Formal License Required)

Crossway allows quoting the ESV in print, digital, and audio formats **up to and including 500 verses** without written permission, provided:

- The verses do **not** amount to more than **one-half of any one book** of the Bible (or the equivalent measured in bytes).
- The verses do **not** account for **25% or more** of the total text of the work in which they appear.
- The verses are **not** used in a commentary or other biblical reference work.

These limits apply to digital media, including apps.

### Book of Proverbs Specifics
- Proverbs contains **915 verses**.
- Half of Proverbs is approximately **457–458 verses**.
- Therefore, the half-book limit is the stricter constraint for Proverbs. Quoting more than about half the book (or the entire book) exceeds the free guidelines and requires a formal license.

---

## 3. Free Non-Commercial Use via the ESV API

Crossway provides a free **ESV API** (`https://api.esv.org`) primarily for websites, but also permits its use in mobile apps **without formal permission** if all general conditions are met.

### Key Conditions
- **Non-commercial use**: No charge for access to any part of the app or the ESV text. The app should not be primarily designed to drive purchases, paid services, donations, or accept advertising/sponsorships. Intended for personal, church, and Christian ministry organization use.
- Display / storage / query limits: No more than 500 verses (or half a book, whichever is less) per page, query, or local storage/caching.
- Rate limits apply (e.g., 5,000 queries per day on the free tier).
- Do not alter the wording of the text.
- Must include the required copyright notice and identify passages as ESV.

### Required Copyright Notice (example)
> Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved. The ESV text may not be quoted in any publication made available to the public by a Creative Commons license. The ESV may not be translated into any other language. Users may not copy or download more than 500 verses of the ESV Bible or more than one half of any book of the ESV Bible.

The “ESV” and “English Standard Version” are registered trademarks.

---

## 4. When a Formal License Is Required

A formal license is needed when:
- You exceed the Standard Use Guidelines (e.g., full Book of Proverbs or more than ~half of it).
- The use is commercial (paid app, in-app purchases tied to the text, ads, etc.).
- You want broader storage, distribution, or offline rights beyond the API limits.

**Crossway’s policy**: They license to **organizations** (companies or ministries), **not to individuals or solo developers**.

### How to Request a Formal License
1. **Primary form for mobile/app distribution rights**:  
   [ESV Digital Licensing Proposal](https://crosswaygnp.formstack.com/forms/esv_digital_licensing_proposal)

2. **General digital permissions form**:  
   [https://www.crossway.org/permissions/digital/](https://www.crossway.org/permissions/digital/)

3. Main permissions overview:  
   [https://www.crossway.org/permissions/](https://www.crossway.org/permissions/)

**Contacts**
- Licensing inquiries: licensing@crossway.org
- General ESV questions: esvquestions@crossway.org
- Contact page: [https://www.crossway.org/contact/](https://www.crossway.org/contact/)

---

## 5. Commercial License Cost

- Crossway does **not** publish standard pricing. Fees are negotiated case-by-case.
- **Only public data point found**: One developer (Reverent Lutheran app/website) reported that Crossway approved ESV use for a **$200 annual fee** (October 2026). This was for a relatively focused ministry app, not a high-volume commercial product.
- No other concrete fee schedules, royalties, or tiered pricing for commercial app licenses are publicly available.
- Non-commercial use within the guidelines + ESV API remains free.

---

## 6. Practical Recommendation: Develop a Prototype First

**Yes — developing an initial version first is generally the better approach.**

### Benefits
- The licensing form asks for a detailed description of the product. A working prototype, screenshots, or demo video makes the request clearer and more credible.
- Lets you validate the idea and refine the experience before committing to a paid license.
- You can develop and test using the free ESV API (within limits) or public-domain alternatives.

### How to Do It Safely
- Stay strictly within the free non-commercial guidelines during development.
- Use the official ESV API for limited text, or public-domain translations (e.g., WEB, BSB, ASV) for fuller testing of Proverbs.
- Do not publicly distribute a version that exceeds the limits or is commercial until you have a license.
- Include the required copyright notice even in prototypes.

### Suggested Path
1. Build the core app experience using free/limited ESV text or a public-domain stand-in.
2. Prepare a clear description + screenshots or a short demo.
3. Submit the digital licensing proposal form.
4. Consider applying as an organization if possible (given Crossway’s preference).

---

## 7. Key Official Links

| Resource | URL |
|----------|-----|
| ESV API | https://www.esv.org/api/ |
| Permissions overview | https://www.crossway.org/permissions/ |
| Digital permissions form | https://www.crossway.org/permissions/digital/ |
| ESV Digital Licensing Proposal | https://crosswaygnp.formstack.com/forms/esv_digital_licensing_proposal |
| Contact | https://www.crossway.org/contact/ |

---

## 8. Summary Checklist for an iOS App Featuring Proverbs

| Goal | Approach | License Needed? |
|------|----------|-----------------|
| Limited verses (≤ ~457 of Proverbs), non-commercial | ESV API + proper attribution | No |
| Full Book of Proverbs | Formal license | Yes |
| Commercial app (paid, ads, etc.) | Formal license | Yes |
| Early prototype / testing | ESV API (limited) or public-domain text | No (if within limits) |

---

*Compiled from public information on Crossway.org, ESV.org, and related sources as of October 2026.*
