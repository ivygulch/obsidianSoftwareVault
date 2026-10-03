---
type: research
confidence: verified
tags: [licensing, bible, scripture, api, proverbs]
created: 2026-10-03
updated: 2026-10-03
---

# Bible Text Licensing & APIs

> **confidence**: `verified` for terms quoted from fetched primary pages; items marked (unverified) came from search snippets because the publisher's site blocked fetching (Biblica, HarperCollins Christian, Zondervan, Thomas Nelson returned 403; YouVersion pages are JavaScript shells). Researched for [[Applying Proverbs]] but applies to any app shipping scripture text.

Scope: all 31 chapters of Proverbs (~915 verses) shipped offline in an indie iOS app; core free, optional subscription adds an AI feature that sends a user's situation plus candidate verses to a third-party model. Researched 2026-10-03. Quotes are from fetched primary pages unless marked (unverified), meaning search-snippet or secondary-site only because the primary page blocked fetching (Biblica, HarperCollins Christian, Zondervan, Thomas Nelson returned 403; YouVersion pages are empty JS shells).

## Summary

No major copyrighted translation (ESV, NIV, NASB, LSB, CSB, NLT, NKJV) permits a complete book under its free-quotation guideline, and a whole Proverbs is a complete book, so each needs a negotiated license for this app regardless of the AI feature. ESV adds two more walls: Crossway's free API is non-commercial only (a subscription tier makes the app commercial) and caps caching at 500 verses, and a secondary source says Crossway licenses organizations, not individuals (unverified). Biblica (NIV) additionally requires an express AI license for any AI feature. The NET Bible can be given away whole but not "bundled with anything sold." The options that allow a full offline Proverbs in a freemium app with no license are the public-domain and CC0 texts: Berean Standard Bible (CC0 since 2023-04-30, modern English), World English Bible, KJV and ASV; and with share-alike obligations, the Free Bible Version and unfoldingWord ULT (CC BY-SA 4.0). Practical path: ship BSB (WEB or KJV as alternates) and treat ESV/NIV as a later add-on contingent on a commercial license from Crossway or Biblica.

## Version Table

| Version | Copyright holder | Free quotation limit | Complete book? | API / download for apps | Commercial / subscription? | Offline storage? | License more via | Source |
|---|---|---|---|---|---|---|---|---|
| ESV | Crossway | 500 verses, no more than half of any book, under 25% of the work | No | api.esv.org, free key | API non-commercial only; app needs formal license | API cache max 500 verses | Crossway digital licensing form | crossway.org/permissions, api.esv.org |
| NIV | Biblica, Inc. (via HarperCollins Christian) | 500 verses, under 25% (unverified) | No (unverified) | api.bible / YouVersion, non-commercial Express License, no AI (unverified) | No without Standard Publishing License (unverified) | Not stated | Biblica; AI needs separate license (unverified) | biblica.com (blocked) |
| NASB | Lockman Foundation | 1,000 verses, under 50% | No | api.bible Express | api.bible Pro Commercial or Lockman form | Max 1,000 verses in electronic retrieval system | Lockman request form | lockman.org |
| LSB | Lockman / Three Sixteen Publishing | 1,000 verses, under 50% | No | None found | Not stated | Max 1,000 verses stored | lsbible.org request form | lsbible.org |
| CSB | Holman Bible Publishers | 1,000 verses, under 50% | No; whole-book requests "will not be approved" | api.bible Express | api.bible Pro Commercial | Not stated | csbible.com form | csbible.com/permissions |
| NLT | Tyndale House Foundation | 500 verses, under 25% | No | api.bible Express | api.bible Pro Commercial | Not stated | Tyndale questionnaire | tyndale.com/permissions |
| NKJV | Thomas Nelson | 250 verses, under 25% (unverified; another source says 1,000/50%) | No (unverified) | api.bible Express | api.bible Pro Commercial | Not stated | Thomas Nelson Bible Rights (unverified) | thomasnelson.com (blocked) |
| NET | Biblical Studies Press | No numeric limit stated | Yes, if given away free | bible.org (blocked) | No; commercial via HarperCollins Christian | Yes for free distribution | permissions@bible.org | netbible.com/copyright |
| BSB | Public domain (CC0) | Unlimited | Yes | berean.bible | Yes | Yes | None | berean.bible/terms.htm |
| WEB | Public domain; name trademarked by eBible.org | Unlimited | Yes | ebible.org, bible-api.com | Yes | Yes | None | worldenglish.bible |
| KJV | Public domain in US; UK Crown patent (unverified) | Unlimited (US) | Yes | bible-api.com, api.bible | Yes (US) | Yes | None | snippets (unverified) |
| ASV 1901 | Public domain (unverified) | Unlimited | Yes | bible-api.com | Yes | Yes | None | bible-api.com |
| Open English Bible | CC0 | Unlimited | Proverbs not translated | openenglishbible.org | Yes | Yes | None | openenglishbible.org |
| Free Bible Version | CC BY-SA 4.0 | Unlimited with attribution + share-alike | Yes | freebibleversion.org | Yes under BY-SA | Yes | None | freebibleversion.org |
| unfoldingWord ULT | CC BY-SA 4.0 | Unlimited with attribution + share-alike | Yes | unfoldingword.org | Yes under BY-SA | Yes | None | unfoldingword.org/ult |

## Details

### ESV (Crossway)

Permissions page: "The ESV text may be quoted in print, digital, and audio formats up to and inclusive of five hundred (500) verses without a formal license" provided "the verses quoted do not amount to more than one-half of any one book of the Bible" and "nor do the verses quoted account for twenty-five percent (25%) or more of the total text of the work". "The ESV text may not be quoted in any publication made available to the public by a Creative Commons license." Apps: "Crossway allows you to access the ESV Bible text from our server and include it on your website or app, free of charge for non-commercial use." Beyond that: "Permission or license requests that exceed the above guidelines require written permission or a formal license. To obtain written permission or a formal license as required, please complete and submit our Online Form." The digital form is crosswaygnp.formstack.com/forms/esv_digital_licensing_proposal; no fees are published.

API terms (api.esv.org): "You may request up to 500 verses per query, or half a book, whichever is less." "5,000 queries per day, with no more than 1,000 requests in an hour and no more than 60 requests per minute." "You can cache up to 500 verses. We encourage you to periodically clear out your cache." "You must use the text for non-commercial purposes, and your website must be non-commercial." (The page defines commercial as charging for access, accepting advertising, or soliciting donations.) "You must include the standard ESV copyright notice on your site and identify the passages as coming from the ESV. Each page on which you use the text must include a link to www.esv.org." "You may not sell, share, or publish your access key." A sword-devel list post states Crossway licenses organizations, not solo developers (unverified); apply as Ivy Gulch LLC.

### NIV (Biblica / HarperCollins Christian)

All (unverified), from search snippets of biblica.com/permissions: "The NIV may be quoted in any form (written, visual, electronic or audio) up to and inclusive of five hundred (500) verses without the express written permission of the publisher, providing the verses quoted do not amount to a complete book of the Bible nor do the verses quoted account for more than 25 percent (25%) or more of the total text of the work in which they are quoted." "Using Biblica text in an app or website requires written permission, which could be in the form of an Express License if your use qualifies, or under a Standard Publishing License." Express Licensing "is available for truly non-commercial uses (no sales, subscriptions, advertising, monetization, or commercial exploitation of any kind) that do not include artificial intelligence or machine learning features or functionality," delivered through "api.bible by the American Bible Society or platform.youversion.com by YouVersion." API.Bible's FAQ confirms NIV has no commercial licensing on its platform. This app would need a Standard Publishing License plus an AI license from Biblica; no fees published.

### NASB and LSB (Lockman / Three Sixteen)

NASB (lockman.org/permission-to-quote): up to 1,000 verses provided the "verses do not amount to a complete book of the Bible" and do not exceed "50% of the total text of the work in which they are quoted"; cannot store "more than 1,000 verses...in an electronic retrieval system"; digital uses need the full notice with www.Lockman.org as "a click-enabled web link"; beyond that, the "Permission to Quote Request Form."

LSB (lsbible.org/permission-to-quote-the-lsb): same 1,000-verse, complete-book and 50% terms, and "nor may more than 1,000 verses be stored in an electronic retrieval system." Proverbs is under 1,000 verses but is a complete book, so both still need a license.

### CSB, NLT, NKJV

CSB: "up to 1,000 verses without the written permission of the publisher" as long as "a complete book of the Bible is not quoted" and not "more than 50 percent of the work in which they are quoted"; whole-book requests "will not be approved." NLT: up to 500 verses provided "a complete book of the Bible is not quoted" and under "25 percent of the work in which they are quoted"; beyond that the Permissions Questionnaire, with the page noting commercial uses may involve fees. NKJV: page blocked; secondary sources (unverified) report 250 verses / 25% / no entire book, or 1,000 / 50%.

### NET Bible (Biblical Studies Press)

netbible.com/copyright: "The NET Bible® Scripture text (without the NET Bible notes) may be quoted in any form (written, visual, electronic, projection, or audio without written permission." "You may copy the NET Bible® and print it for others as long as you give it away, do not charge for it and comply with our guidelines for content control." "It cannot be bundled with anything sold, used as a gift to solicit donations, nor can you charge for shipping, handling, or anything." "When quotations from the NET Bible® are used in mobile apps, youtube channels, free apps, Internet apps or not-for-sale media...The abbreviation (NET) must be used at the end of the quotation." "Commercial Publication -Please contact HarperCollins Christian Publishing [licensing] for more information." A subscription tier arguably makes the text "bundled with anything sold"; confirm with permissions@bible.org before relying on it.

### Public-domain and open options

BSB (berean.bible/terms.htm): "officially dedicated to the public domain as of April 30, 2023" under CC0; "All uses are freely permitted"; may be "freely reproduced, integrated, and adapted for both free and commercial resources"; attribution "appreciated but not required"; verbatim-text apps are "invited to bear the Berean name," while divergent works are asked not to use it. No fetched source compares its readability to the ESV; it is a modern-English essentially-literal translation in a similar register (unverified).

WEB (worldenglish.bible): "a Public Domain (no copyright) Modern English translation," "based on the American Standard Version of the Holy Bible first published in 1901"; "'World English Bible' is a trademark. Permission is granted to use the name 'World English Bible' and its logo only to identify faithful copies."

KJV: public domain in the US; Crown patent in the UK via Cambridge University Press (unverified). ASV 1901: public domain (unverified).

Open English Bible: "under a Creative Commons Zero licence," but Release 2025.6 covers "the New Testament, Psalms and some Old Testament books" and Proverbs is not listed.

Free Bible Version: "Creative Commons Attribution-Share Alike (BY-SA) 4.0 International license"; all 39 OT books; "contemporary English without using slang or colloquialisms." unfoldingWord ULT: "Creative Commons Attribution-ShareAlike 4.0 International License," an updated ASV for translators that prioritizes literal form over readability. Share-alike could reach the app's own derived passages.

### Aggregator APIs

API.Bible: "Projects that generate revenue or support a revenue model are considered commercial," with examples "Bible apps with ads and/or in-app purchases" and "Subscription services that includes Scripture." Starter is free: "Strictly non-commercial use. No ads, fees, freemium models or upsells allowed," "up to 3 licensed Bibles," "5,000 API calls per month." "Pro (Commercial) — Starts at $29 USD/month plus licensing fees based on monthly active users and selected translations," 150,000 calls/month; homepage lists commercial licensing from "$10/mon per translation." Licensed versions shown: NIV, NKJV, NASB, The Message, CSB, NLT, Amplified, GNT, KJV, plus open-access Bibles. ESV is not on the platform; NIV has no commercial option there. "Cached content must be refreshed every 30 days to remain compliant with publisher licensing requirements," which rules out a permanently offline licensed Proverbs. "You are strictly prohibited from altering the content itself." FUMS tracking required for web apps; store apps exempt.

YouVersion Platform: terms page unreadable. Secondary sources (unverified): public beta December 2025, launch spring 2026, REST API plus Swift/Kotlin/React SDKs, ~1,474 Bibles, "free for non-commercial use," and "Future paywalls, ads, or paid tiers revoke API access." Not usable for a subscription app.

bible-api.com: WEB, KJV, ASV and others, "public domain or freely-licensed"; "rate limited to 15 requests every 30 seconds"; "Do not use this API to download an entire bible; instead, get the data from the source" (github.com/seven1m/open-bibles). Bolls and getbible not fetched.

## AI and derivative use

Biblica (unverified snippet): "Any use of Biblica content in connection with artificial intelligence, machine learning, large language models, chatbots, or similar technologies requires a valid license from Biblica expressly permitting such use," governed by a "Publisher AI Policy, which establishes requirements relating to intellectual property protection, theological integrity, security safeguards, human oversight, permissible functionality." Express Licensing excludes "artificial intelligence or machine learning features or functionality."

LSB: AI systems are "permitted to quote up to 1,000 verses in a single response which may constitute up to 100% of that response," not amounting to an entire book, with (LSB) and links requested over 10 verses.

API.Bible: "Using API.Bible content to train or fine-tune AI models" is prohibited; nothing found on inference or prompting.

Crossway, Lockman (NASB), Holman, Tyndale, Thomas Nelson, NET: no AI clause found on fetched pages; Crossway's Creative Commons ban is the nearest derivative-use restriction. CC0/public-domain texts carry no restriction on sending text to a model or paraphrasing; BY-SA texts require share-alike on adaptations.

## Attribution

ESV: "Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), © 2001 by Crossway, a publishing ministry of Good News Publishers. ESV Text Edition: 2025. Used by permission. All rights reserved." "ESV" and "English Standard Version" are registered trademarks: "Use of either trademark requires the permission of Crossway," so an app name or listing using "ESV" needs permission.

NIV (unverified): "Scripture quotations taken from The Holy Bible, New International Version® NIV® Copyright © 1973 1978 1984 2011 by Biblica, Inc." NIV is a Biblica trademark (unverified).

NASB: "Scripture quotations taken from the (NASB®) New American Standard Bible®, Copyright © 1960, 1971, 1977, 1995, 2020 by The Lockman Foundation. Used by permission. All rights reserved. www.Lockman.org"

LSB: "Scripture quotations taken from the (LSB®) Legacy Standard Bible®, Copyright © 2021 by The Lockman Foundation. Used by permission. All rights reserved. Managed in partnership with Three Sixteen Publishing Inc."

CSB: "Scripture quotations marked CSB have been taken from the Christian Standard Bible®, Copyright © 2017 by Holman Bible Publishers. Used by permission. Christian Standard Bible® and CSB® are federally registered trademarks of Holman Bible Publishers."

NLT: "Scripture quotations are taken from the Holy Bible, New Living Translation, copyright ©1996, 2004, 2015 by Tyndale House Foundation. Used by permission of Tyndale House Publishers, Carol Stream, Illinois 60188. All rights reserved."

NET: "Scripture quoted by permission. Quotations designated (NET) are from the NET Bible® copyright ©1996, 2019 by Biblical Studies Press, L.L.C. All rights reserved"; "(NET)" after each quotation, linked to netbible.org when online.

BSB: none required; courtesy credit to Bible Hub, Discovery Bible, OpenBible.com and the Berean Bible Translation Committee. WEB: none required; name only for faithful copies. API.Bible licensed texts: notice on the About/Settings page plus abbreviation after each quotation.

## Sources

- https://www.crossway.org/permissions/
- https://api.esv.org/
- https://www.biblica.com/permissions/ (blocked; snippets only)
- https://www.lockman.org/permission-to-quote/
- https://lsbible.org/permission-to-quote-the-lsb/
- https://csbible.com/permissions/
- https://www.tyndale.com/permissions
- https://www.thomasnelson.com/about-us/permissions/ (blocked)
- https://www.blueletterbible.org/versions.cfm
- https://netbible.com/copyright/
- https://berean.bible/terms.htm
- https://worldenglish.bible/
- https://openenglishbible.org/
- https://www.freebibleversion.org/
- https://www.unfoldingword.org/ult
- https://api.bible/
- https://docs.api.bible/quick-start/licensing-and-access
- https://care.api.bible/article/405-express-licensing-faqs
- https://blog.youversion.com/2026/04/introducing-the-youversion-platform/
- https://dev.to/arvavit/4-footguns-integrating-youversions-new-platform-api-and-a-clean-verse-of-the-day-2087
- https://bible-api.com/
- https://www.crosswire.org/pipermail/sword-devel/2019-June/047095.html (unverified)

## Relevant To

- [[Applying Proverbs]] — the text-version decision is this idea's first dependency
- [[Idea Backlog]] — Text section
