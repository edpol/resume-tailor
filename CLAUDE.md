# Resume Tailor Project

## Skills

### resume-tailor
**Location**: `./skill-staging/resume-tailor`

A skill for tailoring your resume to match specific job descriptions. This skill:
- Parses job descriptions to identify key requirements and keywords
- Fetches your master resume from Google Drive (or local fallback)
- Reads relevant project summaries for contextual details
- Produces a gap analysis showing strengths and areas to address
- Rewrites the HIGHLIGHTS section using the XYZ formula to better match the job
- Saves the tailored resume, gap analysis, and job description to Google Drive

**When to use**: Mention a job description, say you're applying for a role, or ask to tailor your resume for a specific position. The skill can be invoked with `/resume-tailor`.

**Key features**:
- No em-dashes in output (uses commas and colons instead)
- Action-oriented bullet points with strong verbs
- Never fabricates experience—gaps are noted honestly
- All output saved to Google Drive for easy access
- Preserves your original resume; only updates HIGHLIGHTS section

## Google Drive Integration
- **Master Resume File ID**: `15DLEOd_tWSi1OzQLaby-qxXkJxXLH__rXqTmGoPraI0`
- **Jobs Folder ID**: `1QxNLUAt7--Z65vaUY3w__gbsNdb6i25t`

## Asset Files
- `master_resume.md` — Your complete resume (local fallback)
- `projects/summary-*.md` — Detailed project context for different employers
- `Skills.csv` — Your technical skills inventory
- `Recommendations_Received.csv` — Recommendations and social proof
