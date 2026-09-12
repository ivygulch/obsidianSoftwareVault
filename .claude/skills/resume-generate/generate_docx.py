#!/usr/bin/env python3
"""Build an ATS resume .docx from a generated markdown file.

Reads the `## ATS Resume` section of a `Resume/Generated/<file>.md` produced by the
resume-generate skill, and writes a .docx that reuses the paragraph styles and page
setup of an existing hand-edited resume (the template). No third-party packages:
the template's document.xml is rewritten with cloned paragraph properties.

Usage:
    generate_docx.py <generated-markdown> [--template <docx>] [--out <docx>] [--force]
    generate_docx.py --dump <docx>

--dump prints the docx back as an `## ATS Resume` markdown block (the inverse of the
build), so a hand-edited docx can serve as the verbatim content baseline for the
next generation.

Defaults:
    --template  the most recently modified Resume*.docx in Resume/Archive/ (the output
                file itself is excluded, so regenerating with --force does not pick
                the file being replaced). Pass a path to override.
    --out       Resume/Archive/Resume<yyyy>_<mm>_<dd>_<companyslug>.docx, where the date
                comes from the markdown filename and the slug is the company name
                lowercased with non-alphanumerics removed (e.g. "The Home Depot" ->
                "thehomedepot").

The script refuses to overwrite an existing output file unless --force is given.
"""

import argparse
import html
import re
import shutil
import sys
import zipfile
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[3]
ARCHIVE_DIR = VAULT_ROOT / "Resume" / "Archive"


# ---------------------------------------------------------------- markdown parsing


def extract_section(md: str, heading: str) -> str:
    """Return the body of a `## <heading>` section (up to the next `## `)."""
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.M)
    m = pattern.search(md)
    if not m:
        sys.exit(f"error: section '## {heading}' not found in markdown")
    rest = md[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def parse_ats(section: str) -> dict:
    """Parse the ATS Resume markdown into a simple structure."""
    lines = [l.rstrip() for l in section.strip("\n").split("\n")]
    doc = {"name": None, "contact": [], "summary": [], "experience": [], "education": [], "skills": []}

    # Preamble: name + contact lines before the first ### heading
    i = 0
    while i < len(lines) and not lines[i].startswith("### "):
        line = lines[i].strip()
        if line:
            if doc["name"] is None:
                doc["name"] = line
            else:
                doc["contact"].append(line)
        i += 1

    current = None
    entry = None
    for line in lines[i:]:
        stripped = line.strip()
        if stripped.startswith("### "):
            current = stripped[4:].strip().lower()
            entry = None
            continue
        if not stripped:
            continue
        if current == "summary":
            doc["summary"].append(stripped)
        elif current == "experience":
            m = re.fullmatch(r"\*\*(.+?)\*\*", stripped)
            if m:
                entry = {"title": m.group(1), "company": None, "bullets": []}
                doc["experience"].append(entry)
            elif stripped.startswith("- "):
                if entry is None:
                    sys.exit("error: bullet before any job title in Experience")
                entry["bullets"].append(stripped[2:].strip())
            else:
                if entry is None:
                    sys.exit("error: company line before any job title in Experience")
                entry["company"] = stripped
        elif current == "education":
            doc["education"].append(stripped)
        elif current == "skills":
            if stripped.startswith("- "):
                stripped = stripped[2:].strip()
            m = re.fullmatch(r"\*\*(.+?)\*\*:\s*(.*)", stripped)
            if m:
                doc["skills"].append((m.group(1) + ": ", m.group(2)))
            else:
                doc["skills"].append(("", stripped))
        else:
            sys.exit(f"error: unexpected content under '### {current}': {stripped}")

    missing = [k for k in ("name", "summary", "experience", "education", "skills") if not doc[k]]
    if missing:
        sys.exit(f"error: ATS Resume section is missing: {', '.join(missing)}")
    return doc


def strip_inline_markdown(text: str) -> str:
    """Remove bold/italic markers; the docx bullets and prose are plain runs."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text)
    return text


# ---------------------------------------------------------------- docx building


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def run(text: str, rpr: str = "") -> str:
    rpr_xml = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return f'<w:r>{rpr_xml}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def para(ppr: str, runs: str) -> str:
    ppr_xml = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
    return f"<w:p>{ppr_xml}{runs}</w:p>"


SZ18 = '<w:sz w:val="18"/><w:szCs w:val="18"/>'
SZ19 = '<w:sz w:val="19"/><w:szCs w:val="19"/>'
BOLD19 = "<w:b/><w:bCs/>" + SZ19


class Template:
    """Paragraph properties harvested from the template docx, keyed by role."""

    def __init__(self, path: Path):
        with zipfile.ZipFile(path) as z:
            self.document_xml = z.read("word/document.xml").decode("utf-8")
        body = re.search(r"<w:body>(.*)</w:body>", self.document_xml, re.S)
        if not body:
            sys.exit("error: template has no <w:body>")
        self.body_xml = body.group(1)
        sect = re.search(r"<w:sectPr.*?</w:sectPr>", self.body_xml, re.S)
        self.sect_pr = sect.group(0) if sect else ""
        paras = re.findall(r"<w:p[ >].*?</w:p>", self.body_xml, re.S)
        self.ppr = {}
        self._harvest(paras)

    @staticmethod
    def _style(p: str):
        m = re.search(r'w:pStyle w:val="([^"]*)"', p)
        return m.group(1) if m else None

    @staticmethod
    def _ppr(p: str) -> str:
        m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
        return m.group(1) if m else ""

    @staticmethod
    def _text(p: str) -> str:
        return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

    def _harvest(self, paras):
        prev_header = None
        for idx, p in enumerate(paras):
            style = self._style(p)
            text = self._text(p).strip().upper()
            if style == "Name":
                self.ppr.setdefault("name", self._ppr(p))
                if idx + 1 < len(paras) and self._style(paras[idx + 1]) is None:
                    self.ppr.setdefault("contact", self._ppr(paras[idx + 1]))
            elif style == "SectionHeader":
                self.ppr.setdefault("section", self._ppr(p))
                prev_header = text
                continue
            elif style == "JobTitle":
                self.ppr.setdefault("title", self._ppr(p))
            elif style == "CompanyLine":
                self.ppr.setdefault("company", self._ppr(p))
            elif style == "ListParagraph":
                self.ppr.setdefault("bullet", self._ppr(p))
            elif style is None and prev_header == "SUMMARY":
                self.ppr.setdefault("summary", self._ppr(p))
            elif style is None and prev_header == "EDUCATION":
                self.ppr.setdefault("education", self._ppr(p))
            elif style is None and prev_header == "SKILLS":
                self.ppr.setdefault("skills", self._ppr(p))
            prev_header = prev_header if style is None else None
        needed = ["name", "contact", "section", "summary", "title", "company", "bullet", "education", "skills"]
        missing = [k for k in needed if k not in self.ppr]
        if missing:
            sys.exit(f"error: template is missing paragraph roles: {', '.join(missing)}")


def build_body(doc: dict, tpl: Template) -> str:
    out = []
    out.append(para(tpl.ppr["name"], run(doc["name"])))
    for line in doc["contact"]:
        out.append(para(tpl.ppr["contact"], run(line, SZ18)))

    out.append(para(tpl.ppr["section"], run("SUMMARY")))
    for text in doc["summary"]:
        out.append(para(tpl.ppr["summary"], run(strip_inline_markdown(text))))

    out.append(para(tpl.ppr["section"], run("EXPERIENCE")))
    for entry in doc["experience"]:
        out.append(para(tpl.ppr["title"], run(entry["title"])))
        if entry["company"]:
            out.append(para(tpl.ppr["company"], run(entry["company"])))
        for b in entry["bullets"]:
            out.append(para(tpl.ppr["bullet"], run(strip_inline_markdown(b), SZ19)))

    out.append(para(tpl.ppr["section"], run("EDUCATION")))
    for line in doc["education"]:
        out.append(para(tpl.ppr["education"], run(strip_inline_markdown(line))))

    out.append(para(tpl.ppr["section"], run("SKILLS")))
    for label, body in doc["skills"]:
        runs = (run(label, BOLD19) if label else "") + run(strip_inline_markdown(body), SZ19)
        out.append(para(tpl.ppr["skills"], runs))

    return "".join(out) + tpl.sect_pr


def write_docx(template: Path, out: Path, body_xml: str, tpl: Template):
    new_document = re.sub(
        r"<w:body>.*</w:body>", lambda _: f"<w:body>{body_xml}</w:body>", tpl.document_xml, count=1, flags=re.S
    )
    tmp = out.with_suffix(".docx.tmp")
    with zipfile.ZipFile(template) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = new_document.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, out)


# ---------------------------------------------------------------- docx -> markdown


def dump_ats(path: Path) -> str:
    """Render a resume docx as the `## ATS Resume` markdown block."""
    with zipfile.ZipFile(path) as z:
        doc = z.read("word/document.xml").decode("utf-8")
    body = re.search(r"<w:body>(.*)</w:body>", doc, re.S).group(1)
    out = ["## ATS Resume", ""]
    section = None
    prev = None
    for p in re.findall(r"<w:p[ >].*?</w:p>", body, re.S):
        st = Template._style(p)
        runs = re.findall(r"<w:r[ >].*?</w:r>", p, re.S)
        parts = [("B" if "<w:b/>" in r else "N", html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", r)))) for r in runs]
        text = "".join(t for _, t in parts).strip()
        if not text:
            continue
        if st == "Name":
            out += [text, ""]
        elif st == "SectionHeader":
            section = text.upper()
            if prev == "bullet":
                out.append("")
            out += [f"### {text.title()}", ""]
        elif st == "JobTitle":
            if prev == "bullet":
                out.append("")
            out.append(f"**{text}**")
        elif st == "CompanyLine":
            out += [text, ""]
        elif st == "ListParagraph":
            out.append(f"- {text}")
        elif section == "SKILLS" and parts and parts[0][0] == "B":
            label = "".join(t for k, t in parts if k == "B").strip().rstrip(":")
            rest = "".join(t for k, t in parts if k == "N").strip()
            out.append(f"- **{label}**: {rest}")
        else:
            out += [text, ""]
        prev = "bullet" if st == "ListParagraph" or (section == "SKILLS" and st is None) else "other"
    return "\n".join(out).rstrip("\n") + "\n"


# ---------------------------------------------------------------- template selection


def latest_template(exclude: Path) -> Path:
    """Most recently modified Resume*.docx in the archive, excluding the output path."""
    candidates = [
        f for f in ARCHIVE_DIR.glob("Resume*.docx")
        if f.resolve() != exclude.resolve() and not f.name.startswith("~$")
    ]
    if not candidates:
        sys.exit(f"error: no Resume*.docx found in {ARCHIVE_DIR} to use as a template; pass --template")
    return max(candidates, key=lambda f: f.stat().st_mtime)


# ---------------------------------------------------------------- naming


def default_output(md_path: Path, company: str) -> Path:
    m = re.match(r"(\d{4})-(\d{2})-(\d{2}) \d{4} ", md_path.name)
    if not m:
        sys.exit("error: markdown filename must start with 'yyyy-mm-dd hhmm ' to derive the output name; pass --out")
    slug = re.sub(r"[^a-z0-9]", "", company.lower())
    return ARCHIVE_DIR / f"Resume{m.group(1)}_{m.group(2)}_{m.group(3)}_{slug}.docx"


def company_from_md(md: str, md_path: Path) -> str:
    m = re.search(r"^- \*\*Company\*\*:\s*(.+?)\s*$", md, re.M)
    if m:
        return m.group(1)
    m = re.match(r"\d{4}-\d{2}-\d{2} \d{4} (.+)\.md", md_path.name)
    return m.group(1) if m else "unknown-company"


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("markdown", type=Path, nargs="?", help="generated markdown file (Resume/Generated/...)")
    ap.add_argument("--dump", type=Path, default=None, help="print a docx back as an ATS Resume markdown block and exit")
    ap.add_argument("--template", type=Path, default=None, help="reference .docx whose styles to reuse (default: newest Resume*.docx in the archive)")
    ap.add_argument("--out", type=Path, default=None, help="output .docx path")
    ap.add_argument("--force", action="store_true", help="overwrite an existing output file")
    args = ap.parse_args()

    if args.dump:
        if not args.dump.exists():
            sys.exit(f"error: docx not found: {args.dump}")
        sys.stdout.write(dump_ats(args.dump))
        return
    if not args.markdown:
        ap.error("markdown path is required unless --dump is given")

    md_path = args.markdown.resolve()
    if not md_path.exists():
        sys.exit(f"error: markdown not found: {md_path}")
    md = md_path.read_text(encoding="utf-8")
    doc = parse_ats(extract_section(md, "ATS Resume"))
    out = args.out.resolve() if args.out else default_output(md_path, company_from_md(md, md_path))
    if out.exists() and not args.force:
        sys.exit(f"error: output exists, pass --force to overwrite: {out}")

    template = args.template if args.template else latest_template(out)
    if not template.exists():
        sys.exit(f"error: template not found: {template}")

    tpl = Template(template)
    write_docx(template, out, build_body(doc, tpl), tpl)

    n_bullets = sum(len(e["bullets"]) for e in doc["experience"])
    print(f"wrote {out}")
    print(f"  {len(doc['experience'])} roles, {n_bullets} bullets, {len(doc['skills'])} skills lines, template {template.name}")


if __name__ == "__main__":
    main()
