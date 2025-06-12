import os
import json
import pathlib
from fastapi import Request
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from app.config import settings

CLIENT_SECRET_FILE = str(pathlib.Path(__file__).parent / "../config/client_secret.json")
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_auth_flow():
    return Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri="http://localhost:8000/gmail/callback"
    )

def fetch_messages_from_gmail(credentials):
    service = build('gmail', 'v1', credentials=credentials)
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])
    return messages
