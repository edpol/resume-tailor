# Enable PDF Output for Resume Tailor

Your resume tailor now creates **DOCX files with full formatting preserved**. To enable automatic PDF conversion, install LibreOffice.

## Current Status

✅ **Installed:**
- `python-docx` — Preserves original resume formatting
- Resume tailor script — Creates properly formatted DOCX files

❌ **Optional (for PDF):**
- `LibreOffice` — Converts DOCX to PDF automatically

## Install LibreOffice (macOS)

### Option 1: Using Homebrew (Recommended)

```bash
brew install libreoffice
```

Then test:
```bash
which libreoffice
```

### Option 2: Download & Install Directly

1. Visit: https://www.libreoffice.org/download/download/
2. Download LibreOffice for macOS
3. Open the DMG and drag to Applications
4. Verify installation:
   ```bash
   /Applications/LibreOffice.app/Contents/MacOS/soffice --version
   ```

## After Installing LibreOffice

Your resume tailor will automatically:
1. Create a DOCX file with your original resume formatting
2. Convert it to PDF with the same professional look
3. Save both versions in the application folder

**Test it:**
```bash
tailor-resume "/Users/edpol/Desktop/AxisCare\ Job\ Description.txt"
```

You should see:
```
📄 Creating customized resume...
   Resume saved: .../Edward_Pol-Resume.pdf
```

## File Format Options

The script intelligently selects formats based on what's available:

| Scenario | Output | Format Quality |
|----------|--------|---|
| All tools installed | PDF + DOCX | ⭐⭐⭐⭐⭐ Professional |
| python-docx only | DOCX | ⭐⭐⭐⭐ Professional |
| No tools | TXT | ⭐⭐ Plain text |

## Troubleshooting

**LibreOffice installed but PDF still not generating?**

Try this command manually:
```bash
libreoffice --headless --convert-to pdf \
  --outdir /tmp \
  "/path/to/resume.docx"
```

If that works, the script should too. If not, check:
- LibreOffice is in your PATH: `which libreoffice`
- No LibreOffice processes are running: `killall soffice`

**PDF comes out with wrong formatting?**

This shouldn't happen — LibreOffice uses the exact DOCX file you edited. If it looks wrong:
1. Check the master resume opens correctly in Word/Pages
2. Verify python-docx preserves the formatting (open the generated DOCX)
3. Test LibreOffice conversion manually on the DOCX file

## What Gets Converted

When you run `tailor-resume`:

```
applications/CompanyName/
├── Edward_Pol-Resume.pdf       ← Converted from DOCX
├── Edward_Pol-Resume.docx      ← Modified with your highlights
├── job_description.txt
└── gap_analysis.md
```

The PDF is an exact visual representation of your customized DOCX, preserving:
- ✅ Original formatting and fonts
- ✅ Section layout and spacing
- ✅ All text styling (bold, etc.)
- ✅ Professional appearance

---

**Next steps:**
1. Install LibreOffice: `brew install libreoffice`
2. Test with: `tailor-resume "/path/to/job/description.txt"`
3. Check the output folder for both DOCX and PDF
