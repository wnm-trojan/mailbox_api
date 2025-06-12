"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-11
Email: warunanissanka44@gmail.com
Description: Main entry point for the FastAPI application.
"""

from fastapi import FastAPI
from app.api.v1 import auth, messages, gmail

app = FastAPI()

app.include_router(auth.router, prefix="/v1/auth", tags=["Authentication"])
app.include_router(messages.router, prefix="/v1/messages", tags=["Messages"])
app.include_router(gmail.router, prefix="/v1/gmail", tags=["Gmail"])
