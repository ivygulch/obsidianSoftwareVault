---
type: research
confidence: verified
tags: [proverbs, app-idea, commentaries, public-domain, licensing]
created: 2026-10-03
updated: 2026-10-03
---

# Public-Domain Proverbs Commentaries

> Sourcing and license survey for a commentary layer in [[Applying Proverbs]]. Researched 2026-10-03; license lines are quoted from fetched pages or SWORD module `.conf` files, and items marked (unverified) could not be confirmed before the search budget ran out (the six-volume JFB digitization, a Toy and a Lange sample sentence, the Gill module's license line).

## Summary

Usable as-is (verse-aligned, machine-readable, explicit license line in the SWORD `.conf`): Matthew Henry Concise (`MHCC`, "Public Domain--Copy Freely"), Henry Complete (`MHC`, same license, text prepared from CCEL), Clarke, JFB one-volume, Keil & Delitzsch (Easton's English), Wesley's Notes, Treasury of Scripture Knowledge (all "Public Domain"), OpenBible.info cross-refs (CC BY), and unfoldingWord Translation Notes `tn_PRO.tsv` (CC BY-SA 4.0).

Needs cleanup or has provenance caveats: Gill (SWORD module is in the Xiphos repo; license line not verified), Poole, Trapp, Geneva notes (SWORD license field `null`), Pulpit, Cambridge (Perowne), Ellicott (Nutt), "Barnes" on Proverbs (actually Plumptre, Speaker's Commentary — PD regardless), Benson. Clean HTML exists on BibleHub and in community e-Sword/JSON dumps, but no host grants a redistribution license for its markup, so you scrape and own the cleanup or take a GitHub dump and verify its chain. Bridges, Arnot, Toy (ICC), Lange/Zöckler, Horton and Thomas Scott are PD but exist as Archive.org OCR or Gutenberg/CCEL prose; Bridges is the only one of these that is verse-by-verse and worth the alignment effort for a lay app.

Off the table: NET Bible notes (copyrighted; no bundling in a sold product), Kidner (IVP 1964), modernized/abridged Henry, Gill or Bridges editions (Hendrickson 1991, Zondervan NIV Henry 1992, Crossway Classic Bridges — new editorial copyright), Barclay, and BibleHub's Berean Study Bible notes/outlines (the 2023 dedication names only the BSB and Majority Bible *texts*).

## Comparison table

| Work | Date | Approach | Length on Prov. (est.) | Readability | PD status | Best machine-readable source | Source caveats |
|---|---|---|---|---|---|---|---|
| Henry, Complete | 1710 | Section-by-section, practical/devotional | ~150–200k words | Good; long sentences, 18th-c. diction | PD | SWORD `MHC` v2.2 | Text derived from CCEL; CCEL asks permission for commercial use |
| Henry, Concise | 1710 / abridged 19th c. | Paragraph per section | ~25–35k | Easiest of the classics | PD | SWORD `MHCC` v2.0 | Based on Moody Press printing, "no Copyright displayed" |
| Gill | 1746–63 | Verse-by-verse, exhaustive, rabbinic citations | ~250k+ | Dense; readable but long | PD | Xiphos-repo SWORD `Gill`; BibleHub HTML | Module license not fetched (unverified); modernized "New Gill" editions carry claims |
| Clarke | 1810–26 | Verse-by-verse, philological | ~60–80k | Good; numbered points | PD | SWORD `Clarke` v2.0 | Hebrew inline |
| JFB one-vol | 1871 | Verse phrase glosses | ~50–60k | Terse, telegraphic | PD | SWORD `JFB` v3.0 | 6-vol. Critical & Experimental (1866–71) is PD but scans only |
| "Barnes" (= Plumptre, Speaker's Comm.) | 1873 | Verse-by-verse, brief | ~40k | Good | PD | BibleHub HTML; e-Sword | SWORD `Barnes` is NT-only |
| Keil & Delitzsch (Easton tr.) | 1874–75 | Verse-by-verse, philological | ~250k | Hard; 15–20% Hebrew/transliteration | PD | SWORD `KD` v2.0; BibleHub `kad` | Built from BibleWorks user module |
| Bridges | 1846 | Verse-by-verse, pastoral | ~250k | Good; Victorian evangelical | PD | Archive.org; Gordon College HTML; Monergism ePub | No verse-aligned structured file found; Crossway abridgment is © |
| Arnot | 1857–58 | ~100 topical essays on selected verses | ~200k | Good prose; not systematic | PD | Archive.org; biblicalelearning HTML | Covers maybe a third of the verses |
| Pulpit (Deane, Taylor-Taswell; homiletics Adeney et al.) | 1891 | Verse-by-verse exposition + homiletics | ~400k+ (ch. 1 ≈ 18–20k) | Dense | PD | BibleHub HTML; e-Sword | Hebrew transliterations |
| Cambridge (T. T. Perowne) | 1899 | Brief verse notes on RV | ~40k | Good, scholarly-concise | PD | BibleHub HTML; Archive.org | — |
| Expositor's Bible (Horton) | 1891 | 31 topical lectures | ~110k | Good essay prose | PD | Gutenberg #42189; CCEL | Not verse-aligned |
| Lange (Zöckler, Schaff ed.) | 1870 | Critical + doctrinal + homiletical blocks | ~200k | Hard, academic | PD | Archive.org chOCR; StudyLight | OCR; StudyLight blocks fetchers |
| Ellicott (J. W. Nutt) | 1884 | Brief verse notes | ~35k | Good | PD | BibleHub HTML | — |
| Poole | 1683–85 | Verse glosses | ~60k | Readable, 17th-c. | PD | BibleHub; samueldotj JSON; e-Sword | — |
| Trapp | 1647–56 | Verse glosses, witty | ~60k | Archaic | PD | sermonindex HTML; samueldotj JSON | sermonindex copying policy is non-commercial |
| Geneva notes | 1599 | Marginal notes, sparse | ~8k | Short, archaic | PD | SWORD `Geneva` v1.1 | `.conf` license field is `null` |
| Wesley Notes | 1765 | Brief verse notes (mostly Henry/Poole digests) | ~20k | Easy | PD | SWORD `Wesley` v1.1 | nnu.edu edition claims site © |
| Thomas Scott | 1788–92 | Section notes + "practical observations" | ~100k | Readable | PD | StudyLight only (unverified); Archive.org scans | No open dump found |
| TSK | 1830s / ~1880 | Cross-references, no prose | 100% verse coverage | n/a | PD | SWORD `TSK` v1.4; OpenBible.info (CC BY); CrossReferences-org (CC BY 4.0) | — |
| Toy, ICC | 1899 | Critical, own translation, textual notes | ~250k | Hard; critical scholarship | PD | Archive.org OCR | No verse-aligned text found |
| Spurgeon sermons / Salt-Cellars | 1855–92 / 1889 | Sermon per verse / English proverbs A–Z | 12 sermons ≈ 60k | Very good | PD | CCEL; spurgeongems PDFs; godrules.net | Not commentaries; Salt-Cellars is not about biblical Proverbs |
| Benson | 1811–18 | Verse notes, Wesleyan | ~70k | Good | PD | BibleHub HTML | — |

Lengths are estimates extrapolated from fetched chapter pages; treat as ±40%.

## Details

### Matthew Henry (Complete and Concise)
Henry wrote the Proverbs volume himself. Complete: sections per chapter (ch. 3: vv. 1–6, 7–12, 13–20, 21–26, 27–35). Sample (3:5, CCEL): "We must repose an entire confidence in the wisdom, power, and goodness of God, assuring ourselves of the extent of his providence to all the creatures and all their actions." Concise sample: "In the way of believing obedience to God's commandments health and peace may commonly be enjoyed." SWORD `MHC` v2.2: "This text was prepared from the Christian Classics Ethereal Library located at www.ccel.org. Thanks also to Logos Research, Inc. for providing CCEL with their text" — "Public Domain--Copy Freely." SWORD `MHCC` v2.0: "This text matches the printed edition as published by Moody Press, 28th printing, no Copyright displayed ... roughly 1200 errors corrected" — "Public Domain--Copy Freely." Hendrickson 1991, Zondervan NIV one-volume 1992 and "simpler terms" modernizations carry new copyright; stay on the 1710-text lineage.

### John Gill
Verse-by-verse, every verse of Proverbs 3 has an entry; heavy Talmud/Targum citation. Sample (3:5): "Trust in the Lord with all thine heart,.... Not in a creature, the best, the holiest, and the highest; not in any creature enjoyment, as riches, strength, and wisdom..." The SWORD module is in the Xiphos repository (ThML source, `BlockType=BOOK`, flagged on sword-devel as a mobile memory problem); its `.conf` license line is (unverified). PD by date (1763). Avoid "The New John Gill Exposition" (Online Bible modernization) — editorial claims apply (unverified).

### Adam Clarke
Sample (3:5): "Trust in the Lord with all thine heart - This is a most important precept: 1. God is the Fountain of all good. 2. He has made his intelligent creatures dependent upon himself..." SWORD `Clarke` v2.0 (2021-10-19), "Public Domain." Chapter 3 ≈ 4,200–4,500 words.

### Jamieson-Fausset-Brown
One-volume (1871) sample (3:6): "acknowledge—by seeking His wise aid (Pr 16:3; Ps 37:5; Jer 9:23, 24)." SWORD `JFB` v3.0, "Public Domain." The six-volume Critical and Experimental edition (Fausset on Proverbs) is PD by date; only scans surfaced (unverified beyond that).

### "Barnes' Notes" on Proverbs
BibleHub labels it "Notes on the Bible by Albert Barnes [1834]," but Barnes wrote no Proverbs volume; Baker's "Barnes' Notes on the Old Testament" filled gaps from the Speaker's Commentary, whose Proverbs is E. H. Plumptre (1873) (prior knowledge, not confirmed on the fetched page). Sample (1:7): "The beginning of wisdom is found in the temper of reverence and awe. The fear of the finite in the presence of the Infinite, of the sinful in the presence of the Holy (compare Job 42:5-6), this for the Israelite was the starting-point of all true wisdom." PD either way. SWORD `Barnes` v1.1 is NT only.

### Keil & Delitzsch
Franz Delitzsch, *Biblical Commentary on the Proverbs of Solomon*, tr. M. G. Easton, T&T Clark 1874–75; Archive.org `biblicalcommentary01deli` marked NOT_IN_COPYRIGHT. Sample (3:5–6): "From God alone comes true prosperity, true help. He knows the right way to the right ends." SWORD `KD` v2.0: "based on the BibleWorks 8 user-created module by Willem Swanepoel" — "Public Domain." Chapter 3 ≈ 8,500–9,000 words with substantial Hebrew; an "advanced" toggle, not a lay default.

### Charles Bridges
*An Exposition of the Book of Proverbs* (1846; US ed. 1847). Verse-by-verse, warm, cross-reference dense. Sample (3:5–6, secondary quotation, unverified against the page): "Self-dependence is folly (Chapter 28:26), rebellion (Jeremiah 2:13; 9:23), ruin." Archive.org scans, Gordon College HTML (Hildebrandt), Monergism ePub/PDF, Chapel Library PDF, StudyLight `cbp`. No verse-keyed file found; the Gordon HTML is the cheapest alignment start. Banner of Truth facsimile = PD text; Crossway Classic abridgment is copyrighted.

### William Arnot
*Laws from Heaven for Life on Earth* (T. Nelson, 1857–58, two series). Fifty numbered essays per volume on chosen verses ("The All-Seeing," "A Wholesome Tongue"). Sample (15:4): "The tongue, when it is whole and wholesome, 'is a tree of life'." Archive.org; biblicalelearning.org HTML. Partial coverage; per-passage essays, not a verse layer.

### Pulpit Commentary
Vol. 9 (1891), exposition by W. J. Deane and S. T. Taylor-Taswell, homiletics by W. F. Adeney and others. Sample (1:7): "This proposition is by some commentators regarded as the motto, symbol, or device of the book." Chapter 1 page ≈ 18–20k words. BibleHub HTML; Archive.org; e-Sword.

### Cambridge Bible for Schools and Colleges
T. T. Perowne, *The Proverbs* (CUP 1899, 196 pp.). Sample (1:7): "This verse stands out as the motto, or key-note, both of the whole Book, and of the whole subject of which the Book treats." BibleHub HTML; Archive.org.

### Expositor's Bible (Horton)
R. F. Horton, *The Book of Proverbs* (1891). 31 lectures ("The Beginning of Wisdom," i. 7, ix. 10; "Wisdom as the Guide of Conduct," ii. 12–16). Gutenberg #42189; CCEL. Essays map to passages, not verses.

### Lange (Zöckler)
*The Proverbs of Solomon, Theologically and Homiletically Expounded* (Schaff ed., 1870). Archive.org Lange set has chOCR HTML of vol. 10; StudyLight `lcc` (403). No sample fetched. Academic; low lay value.

### Ellicott's Commentary for English Readers
Proverbs by "Rev. J. W. Nutt, M.A., Late Fellow of All Souls' College, Oxford" (1884). Sample (1:7): "This expression, 'the fear of the Lord,' occurs thirteen times in the Proverbs, and plays a prominent part throughout the Old Testament." BibleHub HTML.

### Matthew Poole
*Annotations* (1683–85). Sample (3:5): "Trust in the Lord; wholly and securely rely upon God's promises and providence for help and relief in all thine affairs and dangers." BibleHub; samueldotj JSON (from BibleSupport e-Sword files); BibleSupport module (79 MB).

### John Trapp
(1647–56). Sample (3:5): "To trust in God is to be unbottomed of thyself, and of every creature, and so to lean upon God, that if he fail thee thou sinkest." sermonindex.net HTML ("Copying Permissions" = non-commercial); BibleSupport `.cmti`; samueldotj JSON.

### Geneva Bible notes
1599 marginal notes; sparse on Proverbs. SWORD `Geneva` v1.1 — DistributionLicense field empty ("null"); PD by date. No sample fetched (no BibleHub path; biblestudytools paywalls it).

### John Wesley's Explanatory Notes
1765; OT notes mostly digest Henry and Poole. Sample (3:5): "Trust - Wholly rely upon God's promises and providences. Lean not - Under this one kind of carnal confidence, he understands all other confidence in bodily strength, wealth, or friends." ~23 of 35 verses in ch. 3 annotated. SWORD `Wesley` v1.1, "Public Domain." The wesley.nnu.edu copy asserts "Copyright © 1993-2011. Wesley Center for Applied Theology" — use the SWORD text.

### Thomas Scott
(1788–92; 5 vols.) PD. Only StudyLight and Archive.org scans surfaced; no open structured dump (unverified).

### Treasury of Scripture Knowledge
SWORD `TSK` v1.4: "five-hundred thousand scripture references and parallel passages by Canne, Browne, Blayney, Scott, and others about 1880" — "Public Domain." OpenBible.info: "About 340,000 cross references" ... "Unless otherwise indicated, all content is licensed under a Creative Commons Attribution License," 2 MB zip. CrossReferences-org on GitHub: TSK with phrase-level anchors for KJV and BSB, JSON/TSV, CC BY 4.0.

### Crawford Toy, ICC
*A Critical and Exegetical Commentary on the Book of Proverbs* (T&T Clark 1899, 554 pp.). Archive.org `criticalexegetic00toyc` NOT_IN_COPYRIGHT; biblicalstudies.org.uk PDF (403). Own translation with critical notes; OCR clean on English, lossy on Hebrew. Not a lay layer.

### Spurgeon
CCEL *Sermons on Proverbs* = "twelve of Spurgeon's most famous sermons from the Book of Proverbs." The full Metropolitan Tabernacle Pulpit (sermons 348–3561) is PD (Archive.org volumes carry Public Domain Mark 1.0); spurgeongems.org PDFs are indexed by number, so a Proverbs text index must be built. *The Salt-Cellars* (1889) is an A–Z collection of English proverbs with Spurgeon's "homely notes" — not Scripture commentary.

### Benson (bonus)
Joseph Benson (1811–18), on BibleHub. Sample (3:5): "Wholly and securely rely upon God's wisdom, power, and goodness, and upon his providence and promises." Clear and short; a good lay candidate.

## Data sources and formats

- **CrossWire SWORD** (crosswire.org/sword/modules). Each module ships `mods.d/<name>.conf` with a `DistributionLicense` line — the authoritative grant. Dump zCom modules with libsword `diatheke`/`mod2imp` or Python `pysword`. Main repo: Clarke, JFB, KD, MHC, MHCC, TSK, Wesley, Geneva, Barnes (NT), NETnotesfree; Gill is in the Xiphos repo. GPL covers the library, not the data.
- **CCEL** (ccel.org). ThML/XML downloads. "These books may be used for personal, educational, or non-profit purposes" ... "Contact us for permission to republish CCEL works or to use them commercially." A paid app is commercial; prefer SWORD or Gutenberg lineages for Henry and Horton, or ask CCEL.
- **BibleHub** (biblehub.com/commentaries). Best HTML reference copy of Pulpit, Cambridge, Ellicott, Poole, Benson, "Barnes," Gill, KD, JFB, Henry. Its terms page is a user-conduct ToS; its copyright FAQ says PD commentaries "may be quoted freely." No bulk download; a scrape is unlicensed site use — verify text there, source it elsewhere. BSB text: "officially dedicated to the public domain as of April 30, 2023 ... All uses are freely permitted"; the page "does not specifically clarify whether footnotes, cross-references, or commentaries are included," and bereanbibles.com still shows "BSB Copyright ©2016, 2018 by Bible Hub ... All Rights Reserved" for the Study Bible edition (unverified beyond snippet). Treat BSB notes/outlines as not PD.
- **StudyLight** (studylight.org). Largest catalog (Bridges `cbp`, Lange `lcc`, Pulpit `tpc`, Barnes `bnb`, Scott, Trapp), per-work copyright pages, but 403 to automated fetches and asserts site copyright on its editions (unverified). Reference only.
- **sermonindex.net**: Gill, Trapp, Church Fathers; "Copying Permissions" is non-commercial.
- **Project Gutenberg**: Horton only. Once the PG header and trademark are stripped, "You can do anything you want with that text in the United States and most of the rest of the world."
- **Internet Archive**: scans + `_djvu.txt` OCR for Bridges, Arnot, Toy, Lange, Perowne, Delitzsch, Pulpit, JFB 6-vol., all NOT_IN_COPYRIGHT. OCR cleanup and verse segmentation is the labor.
- **e-Sword / BibleSupport**: `.cmti`/`.cmtx` are SQLite files (Poole, Trapp, Pulpit, Barnes OT, Bridges). Module builders sometimes add "do not redistribute" notes; check each download page (unverified).
- **GitHub dumps**: `samueldotj/bible-commentaries` (Geneva, Henry, Poole, Trapp, Church Fathers; one JSON per chapter; per-source `SOURCE.md` records origin and license; Gill "set aside"). `tradewithadam/apparatus` (SQLite of Henry, JFB, Barnes, Gill, Clarke, Wesley, KD, Catena from SWORD; code license unstated). `eve-coda/open-christian-data` (34 commentaries as JSON, but "Everything else (code, schemas, intermediate data, tooling): CC BY-NC 4.0" — regenerate from SWORD instead). `lisasdungeon/the-gift` (20 SWORD modules; "A couple of items ... are copyrighted but distributed with the rights-holder's permission for free non-commercial use"). `HistoricalChristianFaith/Commentaries-Database` (patristic, PD, CSV/SQLite/JSON; thin on Proverbs).

## Openly licensed modern material

- **unfoldingWord Translation Notes** — `tn_PRO.tsv` in git.door43.org/unfoldingWord/en_tn; "Except where otherwise noted, content on DCS is licensed under a CC BY-SA 4.0 License." TSV columns: Book, Chapter, Verse, ID, SupportReference, OrigQuote, Occurrence, GLQuote, OccurrenceNote (Markdown). Translator-facing (figures of speech, cultural notes), not devotional; share-alike reaches derivatives of the notes, not the app if kept as a separate data file (own reading, not legal advice). `en_tq` Translation Questions, same license.
- **NET Bible notes** — "THE NET BIBLE®, New English Translation COPYRIGHT (c) 1996 BY BIBLICAL STUDIES PRESS, L.L.C."; "The NET Bible® Scripture text (without the NET Bible notes) may be quoted in any form ... without written permission"; free copies must be given away and "cannot be bundled with anything sold." SWORD `NETnotesfree` is "Copyrighted," limited notes. Not usable in a paid app without a license.
- **BSB text** — PD since 2023-04-30; usable as display text or alignment anchors (CrossReferences-org has BSB phrase anchors).
- **Not open**: Kidner (IVP 1964), Barclay, Waltke, Longman, ESV/NIV study notes.

## Sources

- CrossWire module pages: http://crosswire.org/sword/modules/ModInfo.jsp?modName=MHCC (also MHC, JFB, Clarke, KD, Wesley, TSK, Geneva, Barnes, NETnotesfree); Gill in Xiphos repo: https://www.mail-archive.com/sword-devel@crosswire.org/msg22586.html
- CCEL: https://www.ccel.org/about/copyright.html · https://www.ccel.org/ccel/henry/mhc3.Prov.iv.html · https://www.ccel.org/ccel/spurgeon/proverbs.html
- BibleHub: https://biblehub.com/terms.htm · https://biblehub.com/q/bible_copyright_details.htm · https://biblehub.com/commentaries/proverbs/3-5.htm (and `/commentaries/<work>/proverbs/<ch>.htm` for barnes, ellicott, pulpit, cambridge, poole, mhc, clarke, gill, jfb, kad)
- Berean: https://berean.bible/terms.htm · https://bereanbibles.com/terms-and-conditions/
- Cross-refs: https://www.openbible.info/labs/cross-references/ · https://github.com/CrossReferences-org/bible-cross-references
- NET: https://thebible.org/gt/notices/net.html · unfoldingWord: https://git.door43.org/unfoldingWord/en_tn
- Gutenberg: https://www.gutenberg.org/ebooks/42189 · https://www.gutenberg.org/policy/license.html
- Archive.org items: anexpositionboo00bridgoog, expositionprover00briduoft (Bridges); lawsfromheavenf01arnogoog/02 (Arnot); criticalexegetic00toyc (Toy); biblicalcommentary01deli (Delitzsch); proverbswithintr00pero (Perowne); pulpitcommentary0014spen; CommentaryOnTheHolyScripturesCriticalDoctrinalAndHomilectical.Lange
- Bridges: http://faculty.gordon.edu/hu/bi/ted_hildebrandt/OTeSources/20-Proverbs/Text/Books/Bridges-ProverbsCommentary/Bridges-Proverbs.htm · https://www.monergism.com/exposition-book-proverbs-ebook
- Arnot: https://biblicalelearning.org/wp-content/uploads/2022/01/Arnot_Proverbs_Vol2.htm · Trapp: https://www.sermonindex.net/commentary/trapp/PRO/3/ · Wesley: https://wesley.nnu.edu/john-wesley/john-wesleys-notes-on-the-bible/notes-on-the-book-of-proverbs/ · Salt-Cellars: https://godrules.net/library/spurgeon/NEW10spurgeon_b9.htm
- GitHub: github.com/samueldotj/bible-commentaries · tradewithadam/apparatus · eve-coda/open-christian-data · lisasdungeon/the-gift · HistoricalChristianFaith/Commentaries-Database
- e-Sword: http://www.biblesupport.com/e-sword-downloads/file/7101-trapp-john-complete-commentary-5-vols/ · StudyLight (403): https://www.studylight.org/commentaries.html · Toy PDF: https://www.biblicalstudies.org.uk/book_proverbs-icc_toy.html

## Relevant To

- [[Applying Proverbs]]
- [[Bible Text Licensing & APIs]] — the same license questions for the scripture text itself
- [[Text Version Comparison]]
