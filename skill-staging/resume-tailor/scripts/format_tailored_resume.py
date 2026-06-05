#!/usr/bin/env python3
"""
Formats a tailored resume by replacing only the HIGHLIGHTS section
while preserving the exact structure and formatting of the master resume.

Usage:
    python format_tailored_resume.py <master_resume_path> <new_highlights> <output_path>

Where new_highlights is a list of 5 bullet points (one per line).
"""

import sys
from pathlib import Path
from typing import List, Tuple


def parse_highlights_from_text(text: str) -> List[str]:
    """Extract the 5 highlights from formatted text."""
    lines = text.strip().split('\n')
    highlights = []
    in_highlights = False

    for line in lines:
        if line.strip().startswith('**HIGHLIGHTS**'):
            in_highlights = True
            continue
        if in_highlights:
            if line.strip().startswith('**PROFESSIONAL EXPERIENCE**'):
                break
            if line.strip().startswith('*') and line.strip() != '*':
                # Clean up the line
                clean_line = line.strip().lstrip('* ').strip()
                if clean_line:
                    highlights.append(clean_line)

    return highlights


def format_tailored_resume(master_resume_path: str, new_highlights: List[str], output_path: str) -> bool:
    """
    Replace HIGHLIGHTS section in master resume with new highlights.

    Args:
        master_resume_path: Path to master resume file
        new_highlights: List of 5 new highlight bullet points
        output_path: Where to save the tailored resume

    Returns:
        True if successful, False otherwise
    """
    try:
        # Read master resume
        master_path = Path(master_resume_path)
        if not master_path.exists():
            print(f"❌ Master resume not found: {master_resume_path}")
            return False

        with open(master_path, 'r') as f:
            content = f.read()

        # Find HIGHLIGHTS section boundaries
        highlights_start = content.find('**HIGHLIGHTS**')
        if highlights_start == -1:
            print("❌ Could not find HIGHLIGHTS section in master resume")
            return False

        prof_exp_start = content.find('**PROFESSIONAL EXPERIENCE**', highlights_start)
        if prof_exp_start == -1:
            print("❌ Could not find PROFESSIONAL EXPERIENCE section")
            return False

        # Get everything before HIGHLIGHTS and from PROFESSIONAL EXPERIENCE onward
        before_highlights = content[:highlights_start]
        after_highlights = content[prof_exp_start:]

        # Build new HIGHLIGHTS section with proper formatting
        new_highlights_section = '**HIGHLIGHTS**\n\n'
        for highlight in new_highlights:
            # Ensure each bullet starts with * and is properly formatted
            highlight = highlight.strip()
            if not highlight.startswith('*'):
                highlight = '* ' + highlight
            new_highlights_section += highlight + '\n'

        # Combine with proper spacing
        new_content = before_highlights + new_highlights_section + '\n' + after_highlights

        # Write tailored resume
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w') as f:
            f.write(new_content)

        print(f"✅ Tailored resume created: {output_path}")
        return True

    except Exception as e:
        print(f"❌ Error formatting resume: {e}")
        return False


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: format_tailored_resume.py <master_resume_path> <output_path> <highlight_1> [highlight_2] ... [highlight_5]")
        print("\nExample:")
        print('  format_tailored_resume.py master.md output.md "Highlight 1 text" "Highlight 2 text" ...')
        sys.exit(1)

    master_path = sys.argv[1]
    output_path = sys.argv[2]
    highlights = sys.argv[3:]

    if len(highlights) != 5:
        print(f"❌ Expected 5 highlights, got {len(highlights)}")
        sys.exit(1)

    success = format_tailored_resume(master_path, highlights, output_path)
    sys.exit(0 if success else 1)
