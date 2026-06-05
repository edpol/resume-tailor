#!/usr/bin/env python3
"""
Format tailored resume by replacing HIGHLIGHTS in master .docx file.
Preserves all formatting, styling, and layout from the master resume.

Usage:
    python format_tailored_resume_docx.py <master_docx> <output_docx> <highlight_1> ... <highlight_5>
"""

import sys
from pathlib import Path
from typing import List

try:
    from docx import Document
    from docx.shared import Pt, RGBColor
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False


def format_tailored_resume_docx(master_docx_path: str, output_docx_path: str, new_highlights: List[str]) -> bool:
    """
    Replace HIGHLIGHTS placeholders in master .docx with new highlights.
    Master template uses {{HIGHLIGHT_1}} through {{HIGHLIGHT_5}}.

    Args:
        master_docx_path: Path to master resume .docx (with placeholders)
        output_docx_path: Where to save the tailored resume .docx
        new_highlights: List of 5 new highlight bullet points

    Returns:
        True if successful, False otherwise
    """
    if not HAS_DOCX:
        print("❌ python-docx not installed.")
        print("Install with: pip install python-docx")
        return False

    try:
        # Load master resume
        master_path = Path(master_docx_path)
        if not master_path.exists():
            print(f"❌ Master resume not found: {master_docx_path}")
            return False

        doc = Document(master_path)

        # Replace {{HIGHLIGHT_N}} placeholders with new highlights
        placeholder_map = {
            '{{HIGHLIGHT_1}}': new_highlights[0],
            '{{HIGHLIGHT_2}}': new_highlights[1],
            '{{HIGHLIGHT_3}}': new_highlights[2],
            '{{HIGHLIGHT_4}}': new_highlights[3],
            '{{HIGHLIGHT_5}}': new_highlights[4],
        }

        found_any = False
        for i, para in enumerate(doc.paragraphs):
            for placeholder, highlight_text in placeholder_map.items():
                if placeholder in para.text:
                    # Replace placeholder with new highlight
                    para.text = highlight_text.strip()
                    found_any = True
                    print(f"✓ Replaced {placeholder}")
                    break

        if not found_any:
            print("❌ Could not find any {{HIGHLIGHT_N}} placeholders in master resume")
            return False

        # Save tailored resume
        output_file = Path(output_docx_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output_file)

        print(f"✅ Tailored resume created: {output_docx_path}")
        return True

    except Exception as e:
        print(f"❌ Error formatting resume: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: format_tailored_resume_docx.py <master_docx> <output_docx> <highlight_1> ... <highlight_5>")
        print("\nExample:")
        print('  format_tailored_resume_docx.py master.docx output.docx "Highlight 1" "Highlight 2" ...')
        sys.exit(1)

    master_path = sys.argv[1]
    output_path = sys.argv[2]
    highlights = sys.argv[3:]

    if len(highlights) != 5:
        print(f"❌ Expected 5 highlights, got {len(highlights)}")
        sys.exit(1)

    success = format_tailored_resume_docx(master_path, output_path, highlights)
    sys.exit(0 if success else 1)
