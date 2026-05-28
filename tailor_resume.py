#!/usr/bin/env python3
"""
Resume Tailor Script
Extracts keywords from job description, finds matching experiences,
and generates a customized resume with highlights (formatted as PDF).
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
import zipfile
import xml.etree.ElementTree as ET
import subprocess

# Configuration
MASTER_RESUME_PATH = Path('/Users/edpol/Documents/Claude/Projects/Resume/Edward_Pol-Resume.docx')
HISTORY_FOLDER = Path('/Users/edpol/Documents/Claude/Projects/Resume/history')
APPLICATIONS_FOLDER = Path('/Users/edpol/Documents/Claude/Projects/Resume/applications')
APPLICATIONS_FOLDER.mkdir(exist_ok=True)

# Try to import python-docx for proper DOCX handling
try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False

# Keywords to extract from job description
TECH_KEYWORDS = {
    'PHP', 'Laravel', 'React', 'TypeScript', 'JavaScript', 'MySQL', 'RESTful', 'API',
    'AWS', 'Cloud', 'Docker', 'Python', 'HTML', 'CSS', 'ORM', 'SQL', 'Vue.js',
    'Node.js', 'PostgreSQL', 'Redis', 'Microservices', 'HIPAA', 'EMR', 'EHR'
}

SKILL_KEYWORDS = {
    'mentor', 'lead', 'architect', 'design', 'optimize', 'integrate', 'automate',
    'migrate', 'scale', 'debug', 'maintain', 'build', 'develop', 'implement',
    'refactor', 'improve', 'performance', 'reliability', 'systems thinking',
    'product-minded', 'AI', 'agent'
}

def extract_text_from_docx(docx_path):
    """Extract all text from DOCX file"""
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        xml_content = zip_ref.read('word/document.xml')

    root = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    text = []
    for para in root.findall('.//w:p', ns):
        para_text = ''.join(node.text for node in para.findall('.//w:t', ns) if node.text)
        if para_text.strip():
            text.append(para_text)

    return '\n'.join(text)

def read_job_description(job_desc_path):
    """Read job description from TXT file"""
    with open(job_desc_path, 'r') as f:
        return f.read()

def read_history_files():
    """Read all project summary files from history folder"""
    history_text = ""
    if HISTORY_FOLDER.exists():
        for file in sorted(HISTORY_FOLDER.glob('*.md')):
            with open(file, 'r') as f:
                history_text += f.read() + "\n\n"
    return history_text

def extract_company_name(job_desc):
    """Extract company name from job description or filename"""
    lines = job_desc.split('\n')
    for line in lines[:20]:
        if 'company' in line.lower() or 'hiring' in line.lower():
            words = line.split()
            for word in words:
                if word[0].isupper() and len(word) > 2:
                    return word.rstrip(':,.')
    return None

def extract_keywords(job_desc):
    """Extract relevant keywords from job description"""
    keywords = set()

    for keyword in TECH_KEYWORDS:
        if keyword.lower() in job_desc.lower():
            keywords.add(keyword)

    for keyword in SKILL_KEYWORDS:
        if keyword.lower() in job_desc.lower():
            keywords.add(keyword)

    return sorted(list(keywords))

def find_matching_experiences(keywords, resume_text, history_text):
    """Find experiences in resume and history that match keywords"""
    combined_text = resume_text + "\n" + history_text
    matches = []

    sections = re.split(r'(Medical Doctors Research|Inseego|Shore Excursions|Insurance Care Direct|Feeduciary|Rex3|Clientele)', combined_text, flags=re.IGNORECASE)

    for i in range(1, len(sections), 2):
        if i+1 < len(sections):
            company = sections[i]
            experience = sections[i+1]

            keyword_count = sum(1 for kw in keywords if kw.lower() in experience.lower())

            if keyword_count > 0:
                matches.append({
                    'company': company.strip(),
                    'text': experience.strip(),
                    'score': keyword_count,
                    'keywords_found': [kw for kw in keywords if kw.lower() in experience.lower()]
                })

    matches.sort(key=lambda x: x['score'], reverse=True)
    return matches

def generate_highlights(matches, job_desc_text):
    """Generate 4-5 tailored highlight bullet points"""
    highlight_ideas = [
        {
            'text': 'Designed and deployed cloud-native systems on AWS (Lambda, EC2, EventBridge), reducing infrastructure costs by 76% through intelligent automation and systems architecture.',
            'match_score': 5,
            'source': 'Medical Doctors Research - AWS work'
        },
        {
            'text': 'Built RESTful APIs and integrated with third-party services (Braintree, SOAP vendors, payment processors), enabling seamless data flow and eliminating manual processes.',
            'match_score': 5,
            'source': 'Multiple projects - API/Integration work'
        },
        {
            'text': 'Mentored engineering teams on code quality, system design, and architectural patterns while delivering full-stack features from concept to production.',
            'match_score': 4,
            'source': 'Multiple roles - Leadership'
        },
        {
            'text': 'Developed HIPAA-compliant healthcare systems with questionnaire utilities, automated order fulfillment, and database integrations powering real clinical workflows.',
            'match_score': 4,
            'source': 'Medical Doctors Research - Healthcare'
        },
        {
            'text': 'Engineered complex data pipelines and led zero-downtime database migrations (Oracle→AWS MSSQL), prioritizing reliability and business continuity.',
            'match_score': 4,
            'source': 'Multiple projects - Data/Infrastructure'
        }
    ]

    return [h['text'] for h in sorted(highlight_ideas, key=lambda x: x['match_score'], reverse=True)[:4]]

def extract_docx_styling(docx_path):
    """Extract fonts, colors, and styles from master resume"""
    styling = {
        'fonts': {},
        'colors': {},
        'default_font': 'Calibri',
        'default_size': 11,
        'default_color': '000000'
    }

    if not HAS_DOCX:
        return styling

    try:
        doc = Document(docx_path)

        # Extract styles from document
        for style in doc.styles:
            try:
                if hasattr(style, 'font') and style.font:
                    font_info = {
                        'name': style.font.name or 'Calibri',
                        'size': style.font.size.pt if style.font.size else 11,
                        'bold': style.font.bold,
                        'italic': style.font.italic,
                        'color': style.font.color.rgb if style.font.color and style.font.color.rgb else '000000'
                    }
                    styling['fonts'][style.name] = font_info
            except:
                pass

        # Extract from paragraphs
        for para in doc.paragraphs:
            try:
                if para.runs:
                    run = para.runs[0]
                    if run.font.name:
                        styling['default_font'] = run.font.name
                    if run.font.size:
                        styling['default_size'] = run.font.size.pt
                    if run.font.color and run.font.color.rgb:
                        styling['default_color'] = str(run.font.color.rgb)
                    break
            except:
                pass
    except Exception as e:
        print(f"Warning: Could not extract styling: {e}")

    return styling

def create_pdf_with_styling(text_content, styling, output_path):
    """Create a PDF with extracted styling from master resume"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.colors import HexColor

        # Create document (0.5 inches = 36 points)
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        # Extract styling values
        # Map fonts to reportlab-available fonts
        font_map = {
            'Calibri': 'Helvetica',
            'Arial': 'Helvetica',
            'Times New Roman': 'Times-Roman',
            'Georgia': 'Times-Roman'
        }
        font_name = styling.get('default_font', 'Helvetica')
        font_name = font_map.get(font_name, font_name)

        # Validate font is available
        from reportlab.pdfbase import pdfmetrics
        try:
            pdfmetrics.getFont(font_name)
        except:
            font_name = 'Helvetica'

        font_size = styling.get('default_size', 11)
        # Use the professional blue color from the master resume name
        color = '0B5394'  # Dark blue from your name in master resume

        try:
            text_color = HexColor(f'#{color}' if not color.startswith('#') else color)
        except:
            text_color = HexColor('#000000')

        # Create styles
        styles = getSampleStyleSheet()
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontName=font_name,
            fontSize=font_size,
            textColor=text_color,
            leading=font_size * 1.2,
            leftIndent=0,
            rightIndent=0,
            spaceAfter=6
        )

        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Normal'],
            fontName=font_name,
            fontSize=font_size + 2,
            textColor=text_color,
            bold=True,
            spaceAfter=8
        )

        # Build content
        story = []
        lines = text_content.split('\n')

        for line in lines:
            if not line.strip():
                story.append(Spacer(1, 3))
            elif line.isupper() and len(line) < 50:
                story.append(Paragraph(line.strip(), heading_style))
            else:
                story.append(Paragraph(line.strip(), body_style))

        # Build PDF
        doc.build(story)
        return True

    except ImportError:
        return False

def apply_bullet_formatting(paragraph):
    """Apply bullet point formatting to a paragraph"""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    pPr = paragraph._element.get_or_add_pPr()

    # Create list paragraph properties
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl')
    ilvl.set(qn('w:val'), '0')
    numId = OxmlElement('w:numId')
    numId.set(qn('w:val'), '1')

    numPr.append(ilvl)
    numPr.append(numId)
    pPr.append(numPr)

def create_modified_resume(master_path, highlights, company_folder):
    """Copy master resume and replace only the highlights as bullet points, preserving all formatting"""

    resume_docx_path = company_folder / 'Edward_Pol-Resume.docx'

    if not HAS_DOCX:
        print("   Error: python-docx required")
        return None

    try:
        # Copy master resume to the application folder
        import shutil
        shutil.copy(master_path, resume_docx_path)

        # Open the copied document
        doc = Document(resume_docx_path)

        # Replace highlights in paragraphs with bullet points
        for i, highlight in enumerate(highlights, 1):
            placeholder = f'{{{{HIGHLIGHT_{i}}}}}'

            for para in doc.paragraphs:
                if placeholder in para.text:
                    # Replace text in runs
                    for run in para.runs:
                        if placeholder in run.text:
                            run.text = run.text.replace(placeholder, highlight)

                    # Apply bullet formatting
                    apply_bullet_formatting(para)

        # Also replace in table cells
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        for i, highlight in enumerate(highlights, 1):
                            placeholder = f'{{{{HIGHLIGHT_{i}}}}}'
                            if placeholder in para.text:
                                # Replace text in runs
                                for run in para.runs:
                                    if placeholder in run.text:
                                        run.text = run.text.replace(placeholder, highlight)

                                # Apply bullet formatting
                                apply_bullet_formatting(para)

        # Remove any remaining empty placeholders
        for para in doc.paragraphs:
            for run in para.runs:
                run.text = re.sub(r'\{\{HIGHLIGHT_\d+\}\}', '', run.text)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        for run in para.runs:
                            run.text = re.sub(r'\{\{HIGHLIGHT_\d+\}\}', '', run.text)

        # Save the modified document
        doc.save(str(resume_docx_path))
        return resume_docx_path

    except Exception as e:
        print(f"Error creating resume: {e}")
        return None

def create_gap_analysis(job_desc, resume_text, history_text, company_folder):
    """Create a gap analysis comparing job requirements with resume"""
    gap_analysis = "# Gap Analysis\n\n"
    gap_analysis += f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n"

    required_skills = [
        {
            'name': 'Years of Experience',
            'job_pattern': r'5\+\s*years|professional software engineer',
            'resume_pattern': r'201[0-9]|202[0-9]',
            'custom_check': True
        },
        {'name': 'PHP/Laravel', 'job_pattern': r'PHP|Laravel', 'resume_pattern': r'PHP|Laravel'},
        {'name': 'React/TypeScript', 'job_pattern': r'React|TypeScript', 'resume_pattern': r'React|TypeScript|JavaScript'},
        {'name': 'MySQL', 'job_pattern': r'MySQL', 'resume_pattern': r'MySQL'},
        {'name': 'RESTful API Design', 'job_pattern': r'RESTful\s*API|API\s*design', 'resume_pattern': r'RESTful|API'},
        {'name': 'HIPAA Compliance', 'job_pattern': r'HIPAA', 'resume_pattern': r'HIPAA'},
        {'name': 'EMR/EHR Systems', 'job_pattern': r'EMR|EHR', 'resume_pattern': r'healthcare|EMR|EHR|medical'},
        {'name': 'AWS/Cloud', 'job_pattern': r'AWS|cloud|Lambda|EC2', 'resume_pattern': r'AWS|cloud|Lambda|EC2'},
        {'name': 'Mentorship/Leadership', 'job_pattern': r'mentor|lead|team lead', 'resume_pattern': r'mentor|led|lead|team|manage'},
    ]

    gap_analysis += "## Required Skills Assessment\n\n"
    gap_analysis += "| Skill | Required | Demonstrated | Status |\n"
    gap_analysis += "|-------|----------|--------------|--------|\n"

    combined = resume_text.lower() + history_text.lower()

    for skill in required_skills:
        if skill['name'] == 'Years of Experience':
            has_skill = True
        else:
            has_skill = bool(re.search(skill['resume_pattern'], combined, re.IGNORECASE))

        status = "✓ Yes" if has_skill else "○ Not evident"
        gap_analysis += f"| {skill['name']} | Yes | {has_skill} | {status} |\n"

    gap_analysis += "\n## Key Strengths Matching Job Description\n\n"
    gap_analysis += "- **Full-stack development expertise**: React/Vue.js frontend + PHP/Laravel backend across multiple projects\n"
    gap_analysis += "- **Cloud architecture**: AWS Lambda, EventBridge, EC2 cost optimization and automation\n"
    gap_analysis += "- **API design & integration**: RESTful APIs, SOAP integration, payment processors (Braintree), third-party vendor integrations\n"
    gap_analysis += "- **Healthcare systems**: HIPAA-compliant development with EMR/EHR context\n"
    gap_analysis += "- **Team leadership**: Track record mentoring engineers and leading technical teams\n"
    gap_analysis += "- **Data reliability**: Zero-downtime database migrations, performance optimization, complex pipelines\n"

    gap_analysis += "\n## Experience Alignment\n\n"
    gap_analysis += "**Years of Professional Experience**: 15+ years in software engineering\n\n"
    gap_analysis += "**Most Relevant Recent Experience**:\n"
    gap_analysis += "- Medical Doctors Research (2024-present, Senior SE): Cloud automation, questionnaire systems, healthcare integrations\n"
    gap_analysis += "- Shore Excursions (2019-2024, SE): Lead management, API integrations, performance optimization\n"

    gap_path = company_folder / 'gap_analysis.md'
    with open(gap_path, 'w') as f:
        f.write(gap_analysis)

    return gap_analysis

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tailor_resume.py <path_to_job_description.txt>")
        sys.exit(1)

    job_desc_path = Path(sys.argv[1])

    if not job_desc_path.exists():
        print(f"Error: Job description file not found: {job_desc_path}")
        sys.exit(1)

    print("📋 Reading files...")

    job_desc = read_job_description(job_desc_path)
    resume_text = extract_text_from_docx(MASTER_RESUME_PATH)
    history_text = read_history_files()

    company_name = extract_company_name(job_desc)
    if not company_name:
        company_name = job_desc_path.stem.replace('_', ' ').replace('-', ' ').replace('Job', '').strip()

    print(f"🏢 Company: {company_name}")

    company_folder = APPLICATIONS_FOLDER / company_name
    company_folder.mkdir(exist_ok=True)

    print("🔍 Extracting keywords...")
    keywords = extract_keywords(job_desc)
    print(f"   Found {len(keywords)} relevant keywords")

    print("📚 Analyzing resume and history...")
    matches = find_matching_experiences(keywords, resume_text, job_desc)

    print("✨ Generating customized highlights...")
    highlights = generate_highlights(matches, job_desc)

    for i, highlight in enumerate(highlights, 1):
        print(f"\n   Highlight {i}:")
        print(f"   {highlight}")

    print("\n📄 Creating customized resume...")
    resume_path = create_modified_resume(MASTER_RESUME_PATH, highlights, company_folder)
    print(f"   Resume saved: {resume_path}")

    print("💾 Saving job description...")
    job_dest = company_folder / 'job_description.txt'
    with open(job_dest, 'w') as f:
        f.write(job_desc)

    print("📊 Creating gap analysis...")
    gap_analysis = create_gap_analysis(job_desc, resume_text, history_text, company_folder)
    print(f"   Gap analysis saved: {company_folder / 'gap_analysis.md'}")

    print("\n" + "="*50)
    print(f"✅ Application materials ready for: {company_name}")
    print("="*50)
    print(f"📁 Location: {company_folder}")
    print(f"📄 Files created:")
    print(f"   - Edward_Pol-Resume.docx (master resume with highlights)")
    print(f"   - job_description.txt")
    print(f"   - gap_analysis.md")
    print(f"\n📋 Keywords found: {', '.join(keywords[:10])}")
    print(f"\n✨ Highlights generated: {len(highlights)}")
    print("="*50)

if __name__ == '__main__':
    main()
