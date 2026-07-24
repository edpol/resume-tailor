# Resume Tailor Project

## Skills

### resume-tailor
**Location**: `./skill-staging/resume-tailor`

A skill for tailoring your resume to match specific job descriptions.

## Resume Writing Rules

### Fabrication audit -- mandatory before producing any resume output

Every highlight bullet must trace to a source sentence in the master resume or a
project summary file. Before finalizing any bullet:

1. **Scale/volume claims** -- user counts, request volumes, concurrent users,
   transactions per second MUST appear verbatim in the source. If not, DELETE IT.

2. **Architecture labels** -- "enterprise-scale", "high-availability", "distributed",
   "event-driven" require explicit support in the source. Do not infer scale.

3. **Banned phrases** (unless word-for-word in source resume):
    - "thousands of users" / "1000s of users" / "millions of requests"
    - "high availability" / "99.9% uptime" / "enterprise-scale"
    - "concurrent users" / "concurrent requests" / "real-time at scale"
    - Any SLA percentage not cited in the source

4. **Self-citation check** -- for every metric, identify the exact source sentence.
   If you cannot find it, remove the metric from the bullet.

A weaker but honest bullet is always better than a strong fabricated one.

**⚠️ MANDATORY PRE-FLIGHT CHECKLIST**

**DO NOT RUN THIS SKILL WITHOUT COMPLETING THIS CHECKLIST FIRST AND SHOWING IT TO THE USER.**

Before running `/resume-tailor`, you must:
- [ ] Have read `/Users/edpol/.claude/projects/-Users-edpol-Documents-Claude-Projects-Resume/memory/resume_format_critical.md` in this conversation
- [ ] Confirm: Master resume is a Google Doc (File ID: 1pX1y3G0RdJ6JNjjHt9EQmcCX4IoDl7e290znPbPJf2c)
- [ ] Confirm: Formatting template is Resume-Template.docx from Google Drive
- [ ] Confirm: You will use findAndReplaceInDoc to update only the {{HIGHLIGHT_X}} placeholders, preserving all formatting
- [ ] Confirm: You will show this completed checklist to the user before proceeding with the skill

**If you cannot complete all items above, STOP and ask the user for clarification.**

This error has occurred 10+ times. This checklist prevents it from happening again.

---

**What this skill does:**
- Parses job descriptions to identify key requirements and keywords
- Reads your master resume from Google Drive (Resume-Master.md)
- Reads relevant project summaries for contextual details
- Produces a gap analysis showing strengths and areas to address
- Rewrites the HIGHLIGHTS section using the XYZ formula to better match the job
- Saves the tailored resume, gap analysis, and job description to Google Drive

**When to use**: Mention a job description, say you're applying for a role, or ask to tailor your resume for a specific position. The skill can be invoked with `/resume-tailor`.

**Output Naming Convention**:
- Tailored resume: `Edward_Pol-<CompanyName>.docx` (e.g., `Edward_Pol-Credify.docx`)
- Gap analysis: `Gap_Analysis-<CompanyName>-<RoleTitle>.doc`
- Job description: `Job_Description-<CompanyName>-<RoleTitle>.txt`

**Key features**:
- No em-dashes in output (uses commas and colons instead)
- Action-oriented bullet points with strong verbs
- Never fabricates experience—gaps are noted honestly
- All output saved to Google Drive for easy access
- Preserves your original resume; only updates HIGHLIGHTS section
- **CRITICAL: Must use `findAndReplaceInDoc` to preserve all formatting—this is non-negotiable**

## Google Drive Output
- **Jobs Folder ID**: `1QxNLUAt7--Z65vaUY3w__gbsNdb6i25t` — Where tailored resumes and gap analyses are saved

## Google Drive Files
- **Resume-Master** (File ID: `1pX1y3G0RdJ6JNjjHt9EQmcCX4IoDl7e290znPbPJf2c`) — Master resume content (Google Doc)
- **Resume-Template.docx** (File ID: `1nJgFTIaWUArZnnGltD92JNx8_p8wDDcw`) — Official formatting template for ALL tailored resumes

## Local Asset Files
- `projects/summary-*.md` — Detailed project context for different employers
- `Skills.csv` — Your technical skills inventory
- `Recommendations_Received.csv` — Recommendations and social proof
