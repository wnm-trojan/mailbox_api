from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from app.integrations.gmail import get_gmail_auth_flow, fetch_messages_from_gmail
from google.oauth2.credentials import Credentials

router = APIRouter()

# In-memory user sessions (use DB or Redis in prod)
user_sessions = {}

@router.get("/login")
def gmail_login():
    flow = get_gmail_auth_flow()
    auth_url, _ = flow.authorization_url(prompt="consent")
    return RedirectResponse(auth_url)

@router.get("/callback")
def gmail_callback(request: Request):
    flow = get_gmail_auth_flow()
    flow.fetch_token(authorization_response=str(request.url))
    credentials = flow.credentials

    # Save session temporarily
    user_sessions["user"] = credentials_to_dict(credentials)
    return {"message": "✅ Gmail connected!"}

@router.get("/messages")
def gmail_messages():
    cred_info = user_sessions.get("user")
    if not cred_info:
        return {"error": "Gmail not authorized"}

    credentials = Credentials(**cred_info)
    messages = fetch_messages_from_gmail(credentials)
    return {"messages": messages}

def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes
    }
