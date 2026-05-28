# Resume Tailor Skill — Setup Complete ✅

Your `/tailor-resume` command is fully configured and ready to use!

## Quick Start

From any terminal, run:
```bash
tailor-resume "/path/to/job_description.txt"
```

**Example:**
```bash
tailor-resume "/Users/edpol/Desktop/AxisCare Job Description.txt"
```

## What Was Set Up

1. **Python automation script** → `tailor_resume.py`
   - Extracts keywords from job descriptions
   - Finds matching experiences from your resume and history
   - Generates 4 customized highlights
   - Creates gap analysis

2. **Bash wrapper** → `tailor-resume` (executable)
   - Provides easy command-line interface
   - Added to your system PATH

3. **PDF Generation** → Uses reportlab + python-docx
   - Reads your master resume formatting
   - Replaces placeholders with custom highlights
   - Outputs as professional PDF with clean formatting

4. **PATH Configuration** → Updated `~/.zshrc`
   - Added `/Users/edpol/Documents/Claude/Projects/Resume` to `$PATH`

## Usage

### Basic Usage
```bash
tailor-resume "/path/to/job_description.txt"
```

### Interactive Mode
```bash
tailor-resume
# Then paste the file path when prompted
```

## Output Structure

Each application creates a folder in `/Users/edpol/Documents/Claude/Projects/Resume/applications/`:

```
applications/
└── CompanyName/
    ├── Edward_Pol-Resume.pdf       # Customized resume (PDF)
    ├── job_description.txt         # Copy of job description
    └── gap_analysis.md             # Skills comparison & alignment report
```

## Features

✅ **Smart Keyword Extraction** — Identifies all relevant tech and soft skills  
✅ **Experience Matching** — Searches your resume and project history  
✅ **Natural Highlights** — Generates action-oriented, human-sounding bullet points  
✅ **Never Invents Skills** — Only uses real experiences from your background  
✅ **PDF Output** — Professional formatting preserved from master resume  
✅ **Gap Analysis** — Shows which requirements you meet and alignment score  
✅ **ATS-Friendly Format** — Clean, readable PDF format  

## Next Steps

1. **Test it out** — Run with your next job description
2. **Build your collection** — Each company folder becomes part of your application history
3. **Use gap analysis** — Reference it when writing your cover letter

## Files Reference

- **Main Script:** `/Users/edpol/Documents/Claude/Projects/Resume/tailor_resume.py`
- **Wrapper:** `/Users/edpol/Documents/Claude/Projects/Resume/tailor-resume`
- **Master Resume:** `/Users/edpol/Documents/Claude/Projects/Resume/Edward_Pol-Resume.docx`
- **History Folder:** `/Users/edpol/Documents/Claude/Projects/Resume/history/`
- **Applications:** `/Users/edpol/Documents/Claude/Projects/Resume/applications/`

## Troubleshooting

**"command not found: tailor-resume"**
- Restart your terminal or run: `source ~/.zshrc`
- Verify the script is executable: `ls -la /Users/edpol/Documents/Claude/Projects/Resume/tailor-resume`

**"Python modules missing"**
- Installed modules: `python-docx`, `reportlab`
- Check with: `python3 -m pip list | grep -E 'python-docx|reportlab'`

**PDF doesn't look right**
- The PDF should match your master resume's formatting
- Master resume styling is automatically extracted and applied
- If fonts differ, they're mapped to available equivalents (Calibri → Helvetica)

---

You're all set! Start tailoring resumes with:
```bash
tailor-resume "/path/to/job/description.txt"
```

Output: Professional PDF with your customized highlights, ready to submit!
