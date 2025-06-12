"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12
Email: warunanissanka44@gmail.com
Description: 
"""

from fastapi import APIRouter, status
from app.schemas.message_schema import MessageCreate
from app.services.message_service import send_message

router = APIRouter()

@router.post("/send", status_code=status.HTTP_202_ACCEPTED)
def send_mail(message: MessageCreate):
    send_message(message)
    return {"message": "Message sent to Kafka queue"}
