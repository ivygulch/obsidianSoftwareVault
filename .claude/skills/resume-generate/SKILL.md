---
name: resume-generate
description: Generate application materials for a job or contract description, grounded in the Resume vault — a markdown file under Resume/Generated/ (JD, cover letter, ATS resume, focused resume, flags), an ATS resume docx under Resume/Archive/, and a cover letter txt under Resume/coverletters/, each modeled on the most recently edited docx and letter. Use when the user provides a JD and wants tailored application materials saved for later use.
allowed-tools: Read Bash Grep Glob Write
disable-model-invocation: true
arguments: [job_description]
---

# Resume Generation

You are generating application materials for Douglas Sjoquist, grounded in the career database under `Resume/`. The output is three files: a **single markdown file written to `Resume/Generated/`** (JD, cover letter, ATS resume, focused resume, flags), an **ATS resume `.docx` in `Resume/Archive/`** built from it by `generate_docx.py` (in this skill's directory), and the **cover letter as plain text in `Resume/coverletters/`**. The focused resume stays markdown only. The markdown file also preserves the original JD for later reference.

**Templates are always the latest hand-edited outputs.** The most recently modified resume docx in `Resume/Archive/` is the template for the ATS resume (formatting and content baseline), and the most recently modified `CoverLetter_*.txt` in `Resume/coverletters/` is the template for the cover letter (structure, voice, conventions). Doug's edits land in those files, so each generation inherits them without anyone updating a rule.

## Binding policy

Before drafting anything, read these files in full. They are binding for this task — if anything below conflicts with them, they win:

1. `Resume/Philosophy.md` — core principles, schema conventions, editorial policies. The "Target output" section defines what you produce.
2. `Resume/Career Preferences.md` — targeting policy. Role content, contract structure, what to emphasize and avoid.

## Inputs

**Job or contract description** (pasted inline):

$ARGUMENTS

**Vault contents to read**:

- `Resume/Engagements/*.md` — source of truth for all resume bullets. Read all.
- `Resume/Framing/*.md` — editorial narrative pieces (Summary, Pillars, Conference Talks, Earlier Career).
- `Resume/Companies/*.md` — entity metadata for context.
- `Resume/Education.md` — degree entry.

Use Glob or Bash `ls` to list directory contents; Read to pull individual files.

## Process

1. **Read** `Resume/Philosophy.md` and `Resume/Career Preferences.md` in full. Internalize the rules before drafting.

2. **Scan** engagement and framing files. Pay attention to:
   - Engagement frontmatter: `industry`, `tech`, `practices`, `themes`, `employment`, `start`, `end`, `status`.
   - Achievement bullets with inline hashtags (these feed pillar pulls).
   - Framing Pillar `pull_bullet_tags` lists (they define which bullets each pillar pulls by tag).
   - Private Notes sections — read for context, but NEVER include their content in any output.

3. **Analyze the JD** for:
   - **Company name** and **job title** — extract for filename and heading.
   - Explicit requirements (must-haves).
   - Keyword emphasis (what the ATS will match on).
   - Specific questions asked in the posting (cover letter must address each directly).
   - Red flags relative to Career Preferences (e.g., weighted toward non-iOS platforms, hourly T&M staff aug structure).

4. **Match** engagement content to JD requirements. Select:
   - Which engagements belong in the Experience block. Include all relevant engagements with `status != archive` plus select `status: archive` entries for deep-history signals when the JD values them.
   - Which pillars to foreground in the focused resume.
   - Which specific bullets to emphasize under each engagement.

5. **Determine the output filename**:
   - Format: `yyyy-mm-dd hhmm <company>.md` — no colon in the time, no dash separator before the company name; a single space separates date, time, and company.
   - Use current local timestamp — run `date "+%Y-%m-%d %H%M"` via Bash to get the `yyyy-mm-dd hhmm` portion.
   - Company name: taken from the JD. Trim whitespace. Keep spaces as spaces. If the JD has no clear company name, use `unknown-company` and flag this in the Notes / Flags section.
   - Example: `2026-04-23 1745 BeatStars.md`

6. **Compose the single-file output** per the structure below and **write it** to `Resume/Generated/<filename>` using the Write tool.
   - **The content baseline is the most recently created or edited resume docx in `Resume/Archive/`** (newest `Resume*.docx` by modification time). Doug's latest hand edits live there, and they may postdate the transcription in `Resume/Framing/Reference Resume.md`. Find it with `ls -t /Users/dwsjoquist/ivygulch/vault/Resume/Archive/Resume*.docx | head -1`. If it is the docx named in the transcription's `source:` frontmatter and is not newer than that file, use the transcription verbatim. Otherwise extract it as a ready-to-paste block with `python3 /Users/dwsjoquist/ivygulch/vault/.claude/skills/resume-generate/generate_docx.py --dump <docx>` (prints the `## ATS Resume` section in the exact markdown structure the build step expects; it round-trips without text changes), use that as the baseline, and add a Notes / Flags item saying the reference transcription is stale and offering to promote the newer docx (transcribe it, record the hand edits in `Philosophy.md`).
   - **The ATS Resume block starts from that baseline verbatim.** Keep its summary, titles, bullet sets, bullet order, and Skills lines as they are. Permitted JD-driven changes are additive only: new Experience entries the target calls for (placed reverse-chronologically), and keywords appended to existing Skills lines. Do not rewrite the summary, and do not reintroduce bullets the reference cut; list any such candidates under "Suggested additions and reintroductions" in Notes / Flags instead.
   - **The cover letter template is the most recently modified `CoverLetter_*.txt` in `Resume/coverletters/`.** Find it with `ls -t /Users/dwsjoquist/ivygulch/vault/Resume/coverletters/CoverLetter_*.txt | head -1` and read it in full before drafting. Match its structure (greeting; opening fit paragraph anchored on the target's actual product; requirement-by-requirement mapping; a direct paragraph for gaps that pairs each gap with the nearest real experience; level and location or hybrid paragraph when relevant; one-sentence closing ask; signature "Doug Sjoquist" with no contact block), its voice, and any conventions Doug's edits introduced. Reuse its phrasing for recurring facts (the Walmart scope sentence, the CLEAR and fire-department sentences, the AI-tools sentence, the hybrid sentence) when the JD calls for the same point; rewrite everything target-specific. If the newest letter contains facts not yet in the vault (Doug adds these by hand), use them and add a Notes / Flags item offering to record them in the engagement files.

7. **Update the Generated MOC** at `Resume/Generated/_Generated MOC.md`:
   - Read the MOC.
   - Under the `## Targets` section, look for an existing line matching this company. Match format is `- **<Company>** — …` with the company name between the `**` bold markers (exact string match on the company name as extracted from the JD).
   - If an existing line is found: replace that entire line with the new line (updated date + new filename link).
   - If no existing line is found: append a new line to the `## Targets` section.
   - Line format: `- **<Company>** — yyyy-mm-dd hhmm — [[<filename-without-.md>]]`
     Example: `- **BeatStars** — 2026-04-23 1745 — [[2026-04-23 1745 BeatStars]]`
   - Keep the `## Targets` list alphabetized by company name (reorder if the new entry changes sort position).
   - Write the updated MOC back.
   - If `_Generated MOC.md` is missing for any reason, create it with this header and an empty `## Targets` section:

     ```
     ---
     type: moc
     created: <today>
     updated: <today>
     ---

     # Generated MOC

     Index of application materials generated by the `/resume-generate` skill. One entry per target company. The date reflects the most recent generation for that company, and the wikilink opens the generated file.

     ## Targets
     ```

8. **Generate the ATS resume docx** by running the script that ships with this skill, via absolute path:

   ```
   python3 /Users/dwsjoquist/ivygulch/vault/.claude/skills/resume-generate/generate_docx.py "/Users/dwsjoquist/ivygulch/vault/Resume/Generated/<filename>"
   ```

   - It reads only the `## ATS Resume` section, so that section must follow the structure below exactly: name line, contact line(s), then `### Summary`, `### Experience` (`**Title**` line, `Company  |  dates` line, `- ` bullets), `### Education`, `### Skills` (`- **Category**: items`). The script exits with an error naming what it could not parse; fix the markdown, then rerun.
   - Output lands at `Resume/Archive/Resume<yyyy>_<mm>_<dd>_<companyslug>.docx` (date from the markdown filename, slug = company lowercased with non-alphanumerics removed). It refuses to overwrite an existing file; pass `--force` only when regenerating the same target on the same day.
   - Styles and page setup are cloned from the template docx. By default the script uses the most recently modified `Resume*.docx` in `Resume/Archive/` (excluding the file it is about to write), so Doug's latest hand-edited docx is always the template with no configuration; the script prints which file it used. Override with `--template` only when asked.
   - Validate the result with pandoc before reporting it (`pandoc <out.docx> -t plain | head`); a parse failure or missing section means the markdown structure drifted.
   - Do not generate a docx for the cover letter or focused resume; those remain markdown.

9. **Write the cover letter as plain text** to `Resume/coverletters/CoverLetter_<yyyy-mm-dd>_<companyslug>.txt`, where the date is the generation date and the slug is the company name lowercased with non-alphanumerics removed (the same slug the docx uses, e.g. `CoverLetter_2026-09-12_weightwatchers.txt`). The content is the `## Cover letter` section of the markdown file, verbatim, with no markdown markup (the letters carry none). Do not overwrite an existing file for the same company and date; if one exists, Doug has edited it, so leave it and say so in chat. Extract it with:

   ```
   python3 - <<'EOF'
   import pathlib
   md = pathlib.Path("/Users/dwsjoquist/ivygulch/vault/Resume/Generated/<filename>").read_text()
   cl = md.split("## Cover letter\n")[1].split("## ATS Resume")[0].strip() + "\n"
   out = pathlib.Path("/Users/dwsjoquist/ivygulch/vault/Resume/coverletters/CoverLetter_<yyyy-mm-dd>_<companyslug>.txt")
   assert not out.exists(), "cover letter already exists; leave it"
   out.write_text(cl)
   EOF
   ```

10. **Confirm in chat** with the full file path plus a short summary:
   - Engagements included in the Experience block.
   - Pillars used in the focused resume.
   - Count of items in the Notes / Flags section (so the user knows whether to prioritize reading those).
   - Count of suggested additions/reintroductions, if any.
   - Whether the MOC got a new line or an existing line updated.
   - The docx path, or the parse error if generation failed.
   - The cover letter txt path, and which letter served as its template.
   Keep the chat confirmation short — the file is the output; the chat is a receipt.

## Output file structure

The generated file contains six sections in this exact order. Use `##` headings so they're easy to jump to.

### 1. Heading block (top of file, above any `##`)

```markdown
# <Company> — <Job title>

- **Generated**: yyyy-mm-dd hh:mm
- **Company**: <Company>
- **Job title**: <Job title>
```

### 2. `## Job description`

The entire pasted JD text, verbatim. Preserve line breaks exactly. This anchors the file so the user can re-read the original later without digging for it.

### 3. `## Cover letter`

Plain-prose cover letter (no markdown markup, since it is also written out as a .txt). Modeled on the newest `CoverLetter_*.txt` per step 6. Addressed to the company / role; opens with a specific fit statement tied to the target (not a generic "I'm excited"); directly addresses each specific requirement or question the JD asks; grounds claims in concrete engagements from the vault ("at Walmart, I led…"; "for FirefighterSpot, I…"); respects `Career Preferences.md` on role content and contract shape — if the target is out-of-preference, say so honestly or adapt accordingly; closes with a concrete next step.

### 4. `## ATS Resume`

Reverse-chronological experience. Plain markdown — no tables, no horizontal rules, no fancy formatting. Structure: Summary → Experience (company + role + dates + bullets) → Skills (consolidated from relevant engagement `tech` + `practices`) → Education. ATS-canonical casing per `Philosophy.md`. Strip inline hashtags from bullets. Summary pulled from `Framing/Summary - iOS.md`; do not add level-positioning. Include engagements that clear a relevance bar for the target; archive-tier engagements go in only if they add a specific signal the JD calls for.

### 5. `## Focused Resume`

Pillar-forward narrative. Structure: Summary → Core Focus Areas (relevant pillars from `Framing/Pillar - *.md`) → Selected Engagements (curated subset, reverse-chronological) → Conference Talks and Teaching (optional) → Earlier Career Summary (optional) → Education. Tables allowed. Include only the pillars most relevant to the JD. For each included pillar, include the narrative as written in `Framing/Pillar - *.md`, then pull the relevant engagement bullets matching `pull_bullet_tags`.

### 6. `## Notes / Flags`

- **Suggested additions and reintroductions.** Content pertinent to this JD that the ATS block does not carry because the reference docx cut it or never had it. Check three sources: (1) bullets present in earlier reference docx files under `Resume/Archive/` or earlier dated "Copy style additions" lists in `Philosophy.md` but absent from the current reference (e.g., the Builder.io, App Store rating, or accessibility-teaching bullets); (2) engagement bullets in `Resume/Engagements/` that match the JD's keywords but are not in the reference; (3) summary keywords the JD emphasizes that the reference summary omits. For each, give the exact bullet or phrase, where it would go, and the JD line it answers, so Doug can paste it in or ignore it. This is the only place such content appears; the ATS block itself stays additive-only per step 6.
- **JD requirements the vault doesn't obviously address.** Things the JD asks for where the vault doesn't show clear evidence — call these out so the user can decide whether to supplement from memory.
- **Career Preferences mismatches.** JD aspects that fall outside the user's preferred role content.
- **Unverified metrics.** Claims the vault flags as unverified (per Private Notes caveats) where a number was used or softened. Name the specific numbers to double-check.
- **Omissions.** Anything from the JD that couldn't be addressed.
- **Filename fallback** noted if the company name couldn't be extracted cleanly from the JD.

## Editorial rules (non-negotiable)

- **Never** include Private Notes content in any output.
- **Never** fabricate metrics, dates, or engagement details. If a claim isn't in the vault, don't make it. If the vault flags a metric as unverified, soften or omit it and call it out in Notes / Flags.
- **Cover letter vs resume blocks**: the cover letter references engagements and achievements; it doesn't restate resume bullets verbatim. A recipient may see both the cover letter and one resume, so that separation matters.
- **ATS Resume and Focused Resume can share bullets freely.** Only one resume variant is sent per target — never both — so verbatim overlap between the two is fine and expected. Tailor each to its format (ATS keyword-dense and flat; Focused pillar-forward and narrative), but don't burn editing effort rewriting the same underlying bullet two different ways.
- **Keep** the Summary title-agnostic. Not "Principal iOS engineer" at the opening. Level framing is negotiated elsewhere per `Career Preferences.md`.
- **Respect** the ATS vs focused distinction — ATS is keyword-dense and flat; focused is pillar-forward narrative.
- **Write** exactly one markdown file per invocation into `Resume/Generated/`, one docx into `Resume/Archive/`, and one cover-letter txt into `Resume/coverletters/`. Don't modify other vault files.
