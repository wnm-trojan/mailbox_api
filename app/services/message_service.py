"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12
Email: warunanissanka44@gmail.com
Description: 
"""

from app.kafka.producer import send_message_to_kafka
from app.kafka.topics import MESSAGE_TOPIC
from app.schemas.message_schema import MessageCreate

def send_message(message: MessageCreate):
    # Convert Pydantic model to dict
    message_data = message.dict()
    send_message_to_kafka(MESSAGE_TOPIC, message_data)
