"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12
Email: warunanissanka44@gmail.com
Description: 
"""

from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, index=True)
    receiver = Column(String, index=True)
    subject = Column(String, nullable=True)
    body = Column(Text)
