# Resume Tailor Skill Setup

Your resume tailoring skill is ready to use! Here's how to set it up and use it.

## Quick Start

### Option 1: Run from Terminal
```bash
/Users/edpol/Documents/Claude/Projects/Resume/tailor-resume <path-to-job-description.txt>
```

**Example:**
```bash
/Users/edpol/Documents/Claude/Projects/Resume/tailor-resume "/Users/edpol/Desktop/AxisCare\ Job\ Description.txt"
```

### Option 2: Interactive Mode
```bash
/Users/edpol/Documents/Claude/Projects/Resume/tailor-resume
```
Then type the job description file path when prompted.

## What It Does

The skill automates your entire job application tailoring process:

1. **Extracts Keywords** — Identifies all technical and skill-related terms from the job description
2. **Analyzes Your Background** — Searches your resume and project history for matching experiences
3. **Generates Highlights** — Creates 4 customized, action-oriented bullet points that match the job
4. **Creates Folder Structure** — Makes a company-specific folder in `/applications`
5. **Customizes Resume** — Replaces `{{HIGHLIGHT_1}}` through `{{HIGHLIGHT_5}}` with new content
6. **Creates Gap Analysis** — Compares your skills against job requirements with a detailed report
7. **Saves Everything** — Organizes all files (resume, job description, gap analysis) in one place

## Output Files

For each application, you'll get:
- **Edward_Pol-Resume.txt** — Your customized resume with new highlights
- **Edward_Pol-Resume.pdf** — PDF version (if conversion tools available)
- **job_description.txt** — Copy of the job description
- **gap_analysis.md** — Skills assessment and alignment report

## Making It a `/tailor-resume` Skill in Claude Code

To use this as a custom `/tailor-resume` command in Claude Code, we can set up a hook or alias:

1. Open Claude Code settings (`.claude/settings.json`)
2. Add a hook to handle `/tailor-resume` commands
3. The skill will then be available as `/tailor-resume <file-path>`

**To set this up, run:**
```
/update-config
```

Then ask to "Add tailor-resume skill" — Claude Code can help configure it.

Alternatively, you can manually add to your settings.json:

```json
{
  "hooks": {
    "on_skill_invoke": {
      "tailor-resume": {
        "command": "/Users/edpol/Documents/Claude/Projects/Resume/tailor-resume"
      }
    }
  }
}
```

## Customization

The script is configured to:
- ✅ Extract real, verified keywords from job descriptions
- ✅ Generate action-oriented, natural-sounding highlights
- ✅ Never invent skills or experiences you don't have
- ✅ Match your actual background and project history
- ✅ Create ATS-friendly, clean resume formatting

To modify keyword detection or highlight generation, edit:
- `TECH_KEYWORDS` and `SKILL_KEYWORDS` in `tailor_resume.py`
- The `generate_highlights()` function to change how highlights are created

## Tips

1. **Keep job descriptions simple** — TXT format works best
2. **Company name detection** — The script looks for company name in the file name or description
3. **Five highlights available** — You have slots for `{{HIGHLIGHT_1}}` through `{{HIGHLIGHT_5}}` in your master resume
4. **Gap analysis is informative** — Use it to identify skills to emphasize in your cover letter
5. **Batch processing** — You can run this for multiple job descriptions in one session

## Troubleshooting

**"Python script not found"**
- Make sure you're using the full path to tailor-resume script

**"Job description file not found"**
- Check that the file path is correct and the file exists
- Use quotes around paths with spaces: `"/path/with spaces/file.txt"`

**"PDF not generating"**
- The script falls back to TXT format if PDF conversion tools aren't available
- You can manually convert TXT to PDF using your OS tools or online converters
- Or install `wkhtmltopdf` or `weasyprint` for automatic PDF generation

## Files Included

- `tailor_resume.py` — Main Python script (do not edit unless you know Python)
- `tailor-resume` — Bash wrapper script (makes it easy to run)
- `RESUME_TAILOR_SETUP.md` — This documentation
- `Edward_Pol-Resume.docx` — Your master resume with `{{HIGHLIGHT_*}}` placeholders

## Next Steps

1. Try it out with your first job application
2. Once working, consider setting it up as a `/tailor-resume` skill for quicker access
3. Adjust highlight generation if needed based on results
4. Build up your applications folder with each tailored version
