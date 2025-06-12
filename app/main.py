"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-11
Email: warunanissanka44@gmail.com
Description: Main entry point for the FastAPI application.
"""

from fastapi import FastAPI
from app.api.v1 import auth, messages, gmail, inbox, ws_notify

app = FastAPI()

app.include_router(auth.router, prefix="/v1/auth", tags=["Authentication"])
app.include_router(messages.router, prefix="/v1/messages", tags=["Messages"])
app.include_router(gmail.router, prefix="/v1/gmail", tags=["Gmail"])
app.include_router(inbox.router, prefix="/v1/inbox", tags=["Inbox"])
app.include_router(ws_notify.router, prefix="/v1/notify", tags=["WebSocket Notifications"])
