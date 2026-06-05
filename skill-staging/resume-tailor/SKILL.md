---
name: resume-tailor
description: >
  Tailors a resume to match a specific job description by rewriting the highlights section
  (top 3-5 experience bullets) to mirror the job's language and keyword priorities, then
  saves a tailored Google Doc and gap analysis to Google Drive. Use this skill whenever
  the user wants to customize or adapt their resume for a job posting, mentions a job
  description, wants to match keywords, or says anything like "tailor my resume",
  "update my resume for this job", "match my resume to this posting", "help me apply
  for this role", or pastes/links a job listing alongside resume-related intent.
  Even if they just say "I'm applying for a job at X" -- trigger this skill proactively.
---

# Resume Tailor

You help the user send a strong, targeted resume for a specific job by rewriting the
highlights section and producing a gap analysis, then saving both to Google Drive.

## Writing rules (apply everywhere)

- **No em dashes.** Never use em dashes in any output -- in resume bullets, gap analysis
  docs, or chat responses. Use commas, colons, parentheses, or restructure the sentence.
- **Action-oriented verbs.** Lead every bullet with a strong verb (Architected, Delivered,
  Reduced, Led, Built, Automated, etc.).
- **Never fabricate.** If a required skill is not in the resume, note it in the gap
  analysis but do not invent it. The user decides how to handle genuine gaps.

## What you have to work with

**Master resume** -- stored as a Google Doc in the Jobs folder. Fetch it fresh at the
start of every run using the Google Drive MCP. It is the source of truth; never modify it.

- **File ID:** `15DLEOd_tWSi1OzQLaby-qxXkJxXLH__rXqTmGoPraI0`
- **Jobs folder ID:** `1QxNLUAt7--Z65vaUY3w__gbsNdb6i25t`
- **Read tool:** `mcp__282d0cdf-c0a5-4c69-a93f-07d03ceb85ed__read_file_content`
  -- use `fileId` param, returns plain text
- **Fallback:** if Drive fetch fails, read `assets/master_resume.md`

The resume structure:
- A `HIGHLIGHTS` section near the top with 5 bullet points -- **this is the only section you rewrite**
- A `PROFESSIONAL EXPERIENCE` section with per-job bullets
- A `SKILLS` line at the bottom

**Project summaries** -- stored in `assets/projects/` as `summary-*.md` files:
- `summary-shore-excursions.md` -- Shore Excursions Group (2019-2024)
- `summary-medical-doctors-research.md` -- Medical Doctors Research (2018-2019, 2024-Present)
- `summary-insurance-care-direct.md` -- Insurance Care Direct (2019)
- `summary-feeduciary.md` -- Feeduciary.com freelance (2018)

Read the 1-2 most relevant employer summaries based on the JD to find richer project
detail, metrics, and technology specifics not fully captured in the resume.

**Recruiter requested changes** -- if the user provides a "requested changes" file or
notes from a recruiter alongside the JD, treat those as high-priority instructions that
supplement the JD. They often clarify what the hiring team actually cares about beyond
the written job post.

**Job description** -- provided by the user as pasted text or a URL. If a URL, fetch
and extract the job title, responsibilities, requirements, and nice-to-haves.

## What to do

### Step 1 -- Parse the job description

Read the JD carefully and identify:
- **Role title and seniority**
- **Top 5-8 keywords and phrases** -- skills, tools, or concepts that appear multiple
  times or are listed as required/preferred
- **The 2-3 things this employer cares about most** -- what pain are they hiring to solve?
- **Tone** -- startup vs. enterprise? Match that register in the rewrite.

If the user also provided recruiter notes or requested changes, extract any additional
signals from those (e.g., "they want to see mentorship", "add PHP version numbers").

### Step 2 -- Fetch the master resume and relevant project summaries

```
tool: mcp__282d0cdf-c0a5-4c69-a93f-07d03ceb85ed__read_file_content
args: { "fileId": "15DLEOd_tWSi1OzQLaby-qxXkJxXLH__rXqTmGoPraI0" }
```

Then read the 1-2 project summary files most relevant to this JD from
`{SKILL_DIR}/assets/projects/`. Examples:
- PHP/e-commerce role: `summary-shore-excursions.md` and `summary-medical-doctors-research.md`
- Laravel/SaaS role: `summary-insurance-care-direct.md` and `summary-shore-excursions.md`
- AWS/automation role: `summary-medical-doctors-research.md`

> **Note on SKILL_DIR:** The base directory is printed at the top of the skill instructions
> when it loads. Capture it in bash as:
> ```bash
> SKILL_DIR="/var/folders/.../skills/resume-tailor"
> ```

### Step 3 -- Gap analysis (show this to the user)

Produce a structured gap analysis with two parts:

**Part 1: Gaps and weaknesses** (top 5-7 items, each with a priority label).
For each gap, note what is missing or weak, why it matters for this JD, and a specific
fix suggestion based on actual experience in the resume.

Format each item as:
```
N. GAP NAME [HIGH / MEDIUM / LOW PRIORITY]
   What's missing: ...
   Why it matters: ...
   Fix: ...
```

Also list the resume's **existing strengths** that align well with the JD.

**Part 2: Recommended next steps** beyond the highlights rewrite -- things the user
should consider updating in the experience bullets or skills section.

Keep the tone direct and useful. This is a working document, not an essay.

### Step 4 -- Rewrite the highlights (XYZ formula, concise)

Rewrite all 5 bullets in the HIGHLIGHTS section using the XYZ formula where applicable:
"Accomplished [X] as measured by [Y], by doing [Z]."

**Conciseness rule (STRICT):**
- Each highlight must be **one sentence or less** (aim for 15-20 words)
- Lead with one strong verb (Architected, Delivered, Reduced, Led, Built, etc.)
- One key insight or value proposition per bullet
- If it won't fit on one line comfortably, delete the least important detail
- Think: "Why hire Edward for this one thing?" not "Here's everything Edward knows"

The rewrite must:
- Naturally incorporate the 1-2 highest priority JD keywords
- Mirror the JD's phrasing where appropriate
- Reference specific metrics when critical (%, cost savings, scale)
- Use no em dashes (use commas, colons, or restructure instead)
- Never fabricate skills or experience

The HIGHLIGHTS section answers: "Why should this specific employer hire Edward?"
Lead with what the JD cares most about, but say it in 1-2 punchy sentences.

Do NOT touch anything outside the HIGHLIGHTS section.

**Example of good vs. bad:**

❌ **TOO VERBOSE:**
"Backend engineer with 10+ years of PHP/Laravel experience architecting and optimizing scalable production systems, demonstrated by rebuilding manual operations into automated platforms that reduced processing time by 50% and increased revenue by 50%."

✅ **CONCISE:**
"10+ years PHP/Laravel expertise delivering backend systems that reduced operational cost by 50% and increased revenue by 50%."

✅ **ALSO GOOD:**
"Skilled in trading system architecture, broker API integrations, and execution optimization using PHP, Laravel, MySQL, and AWS."

The second version is punchy and keyword-dense. The first is a snoozefest.

### Step 4.5 -- Format tailored resume to match master resume (.docx format)

After rewriting highlights, use the formatting script to apply them to the master resume while preserving all formatting, structure, and layout:

```bash
python3 {SKILL_DIR}/scripts/format_tailored_resume_docx.py \
  "{SKILL_DIR}/assets/master_resume.docx" \
  "<output_path_tailored_resume.docx>" \
  "highlight_1" "highlight_2" "highlight_3" "highlight_4" "highlight_5"
```

**IMPORTANT:** 
- Output MUST be `.docx` format (matching master resume)
- Script preserves all Word formatting, fonts, styling from master
- Only the 5 HIGHLIGHTS bullets are replaced
- All other sections remain unchanged
- Never output as .md or .txt -- always .docx

### Step 5 -- Save to Google Drive

Call the Python script to automatically organize and upload files to Google Drive:

```bash
python3 {SKILL_DIR}/scripts/google_drive_upload.py \
  "<CompanyName>" \
  "<path_to_tailored_resume>" \
  "<path_to_gap_analysis>" \
  "<path_to_job_description>"
```

The script handles:
1. **Creating/finding** a company subfolder in the Jobs folder (ID: `1QxNLUAt7--Z65vaUY3w__gbsNdb6i25t`)
2. **Authenticating** with Google Drive (uses cached credentials from `~/.claude/mcp-credentials/`)
3. **Uploading** all three files with proper names and MIME types:
   - `Edward Pol Resume -- <Company> (Tailored).docx`
   - `Gap Analysis -- <Company>.md`
   - `Job Description -- <Company>.txt`

**First-time setup:** The script will prompt you to set up OAuth credentials if this is your first run.
See `scripts/google_drive_upload.py` for instructions.

### Step 6 -- Present the result

After the Python script completes, show the user:
1. The rewritten HIGHLIGHTS bullets (all 5, formatted cleanly)
2. A link to the Google Drive company folder (from the script output)
3. A brief note on the top gap to address before submitting
4. Confirmation that all files are ready to submit or share

Ask if they want any adjustments to the highlights.

## Important guardrails

- **Never invent experience.** If a required skill is not in the resume at all, note it
  in the gap analysis but do not include it in the highlights. The user decides how to
  handle genuine gaps.
- **Preserve voice.** Match the user's existing writing style; don't impose generic
  corporate phrasing.
- **One section only.** Only the HIGHLIGHTS bullets change. Do not touch experience
  bullets, skills, education, or contact info -- even if you notice issues.
- **Master resume is read-only.** Fetch it from Drive but never modify it. Always write
  tailored output to a new file.
- **Preserve format permanently.** The `format_tailored_resume.py` script (Step 4.5)
  ensures every tailored resume matches the master resume's exact structure and layout.
  This is non-negotiable -- always use it.
- **No em dashes anywhere** -- not in bullets, gap analysis, or any other output.
