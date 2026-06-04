#!/usr/bin/env python3
"""
Google Drive uploader for resume tailoring skill.
Handles authentication and uploads resume files to Google Drive.
"""

import os
import sys
import json
from pathlib import Path
from typing import Optional, Tuple

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    HAS_GOOGLE_LIBS = True
except ImportError:
    HAS_GOOGLE_LIBS = False

# Google Drive API scope
SCOPES = ['https://www.googleapis.com/auth/drive']

# File IDs from CLAUDE.md
JOBS_FOLDER_ID = '1QxNLUAt7--Z65vaUY3w__gbsNdb6i25t'

# Credentials cache location
CREDS_DIR = Path.home() / '.claude' / 'mcp-credentials'
TOKEN_FILE = CREDS_DIR / 'google_drive_token.json'
CREDENTIALS_FILE = CREDS_DIR / 'credentials.json'

def ensure_credentials_exist():
    """Check if credentials.json exists, guide user if not."""
    if not CREDENTIALS_FILE.exists():
        print("❌ Google Drive credentials not found.")
        print("\nTo set up Google Drive uploads:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project or select existing")
        print("3. Enable Google Drive API")
        print("4. Create OAuth 2.0 Desktop credentials")
        print("5. Download credentials.json")
        print(f"6. Save to: {CREDENTIALS_FILE}")
        print("\nThen run this skill again.")
        return False
    return True

def authenticate():
    """Authenticate with Google Drive API."""
    creds = None

    # Try to load existing token
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid credentials, get new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not ensure_credentials_exist():
                return None

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save token for future use
        CREDS_DIR.mkdir(parents=True, exist_ok=True)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds

def find_or_create_folder(service, folder_name: str, parent_id: str = JOBS_FOLDER_ID) -> str:
    """Find or create a folder in Google Drive.

    Args:
        service: Google Drive service instance
        folder_name: Name of the folder to find/create
        parent_id: Parent folder ID

    Returns:
        Folder ID
    """
    # Search for existing folder
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
    results = service.files().list(
        q=query,
        spaces='drive',
        fields='files(id, name)',
        pageSize=1
    ).execute()

    files = results.get('files', [])
    if files:
        return files[0]['id']

    # Create new folder
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')

def upload_file(service, file_path: str, folder_id: str, file_name: Optional[str] = None) -> Tuple[bool, str]:
    """Upload a file to Google Drive.

    Args:
        service: Google Drive service instance
        file_path: Local file path
        folder_id: Destination folder ID
        file_name: Optional custom file name

    Returns:
        Tuple of (success: bool, file_id: str)
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return False, f"File not found: {file_path}"

    if file_name is None:
        file_name = file_path.name

    # Determine MIME type
    mime_types = {
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.md': 'text/plain',
        '.txt': 'text/plain',
        '.pdf': 'application/pdf'
    }
    mime_type = mime_types.get(file_path.suffix, 'application/octet-stream')

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload(str(file_path), mimetype=mime_type)

    try:
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        return True, file.get('id')
    except Exception as e:
        return False, str(e)

def upload_resume_files(company_name: str, resume_path: str, gap_analysis_path: str, job_desc_path: str) -> bool:
    """Upload resume files to Google Drive.

    Args:
        company_name: Company name for folder
        resume_path: Path to tailored resume .docx
        gap_analysis_path: Path to gap analysis .md
        job_desc_path: Path to job description .txt

    Returns:
        True if successful, False otherwise
    """
    if not HAS_GOOGLE_LIBS:
        print("❌ Google Drive libraries not installed.")
        print("Install with: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
        return False

    # Authenticate
    print("🔐 Authenticating with Google Drive...")
    creds = authenticate()
    if not creds:
        return False

    try:
        service = build('drive', 'v3', credentials=creds)

        # Create/find company folder
        print(f"📁 Creating/finding folder: {company_name}")
        folder_id = find_or_create_folder(service, company_name)
        print(f"✓ Folder ready: {folder_id}")

        # Upload files
        files_to_upload = [
            (resume_path, f"Edward Pol Resume -- {company_name} (Tailored).docx"),
            (gap_analysis_path, f"Gap Analysis -- {company_name}.md"),
            (job_desc_path, f"Job Description -- {company_name}.txt")
        ]

        for local_path, drive_name in files_to_upload:
            if not Path(local_path).exists():
                print(f"⚠️  File not found: {local_path}")
                continue

            print(f"📤 Uploading: {drive_name}")
            success, result = upload_file(service, local_path, folder_id, drive_name)
            if success:
                print(f"✓ Uploaded: {drive_name}")
            else:
                print(f"❌ Failed to upload {drive_name}: {result}")
                return False

        print(f"\n✅ All files uploaded to Google Drive!")
        print(f"📁 Folder: https://drive.google.com/drive/folders/{folder_id}")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: google_drive_upload.py <company_name> <resume_path> <gap_analysis_path> <job_desc_path>")
        sys.exit(1)

    company_name = sys.argv[1]
    resume_path = sys.argv[2]
    gap_analysis_path = sys.argv[3]
    job_desc_path = sys.argv[4]

    success = upload_resume_files(company_name, resume_path, gap_analysis_path, job_desc_path)
    sys.exit(0 if success else 1)
