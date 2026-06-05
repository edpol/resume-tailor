# Resume Tailoring Instructions for Next Job Application

## Quick Start

1. **Get the job description** (copy/paste or save as text file)
2. **Invoke the skill**: Type `/resume-tailor` and provide the job description
3. **Review the output**:
   - Gap analysis (what skills align, what's missing)
   - 5 new highlights tailored to the job
4. **Files created automatically**:
   - Tailored resume (.docx) in `/applications/{Company}/`
   - Gap analysis for interview prep
   - Job description copy for reference

## What the Skill Does

- Parses the job description for key requirements and keywords
- Compares against your master resume and project experience
- Produces a gap analysis showing strengths and any missing skills
- Rewrites your 5 HIGHLIGHTS to match the job (only section that changes)
- Generates a clean Word document ready to submit

## Important Constraints

✓ **Never fabricates** — Only uses your actual experience  
✓ **Action verbs** — Every bullet starts with a strong verb (Led, Built, Designed, etc.)  
✓ **ATS-friendly** — Clean formatting, no em-dashes, parseable by resume scanners  
✓ **Natural tone** — Relaxed, conversational (not overly corporate)  

## Master Resume Location

```
/Users/edpol/Documents/Claude/Projects/Resume/skill-staging/resume-tailor/assets/master_resume.docx
```

This is your complete, unedited resume template with placeholder highlights {{HIGHLIGHT_1}} through {{HIGHLIGHT_5}}.

## Output Structure

Each job application gets its own folder:

```
/Applications/{Company}/
├── Edward_Pol_Resume_{Company}.docx      ← Ready to submit
├── {company}-gap-analysis.txt             ← Interview prep
└── Job Description -- {Company}.txt       ← Original JD
```

## Customization

After the skill generates highlights, you can:
- Review for accuracy (all claims must be truthful)
- Request tone adjustments ("more formal," "shorter," "more emphasis on X")
- Add specific metrics or results from your experience
- Request rewrites if highlights don't feel natural

## Questions to Ask When Tailoring

1. Does this job emphasize **team leadership** or **individual contribution**?
2. What **technologies** are they most focused on?
3. What **problem** are they hiring to solve?
4. What **tone** do they use (startup vs. enterprise)?

Answer these and the skill will tailor more effectively.
