"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12
Email: warunanissanka44@gmail.com
Description: 
"""

from pydantic import BaseModel
from typing import Optional

class MessageCreate(BaseModel):
    sender: str
    receiver: str
    subject: Optional[str] = None
    body: str

class MessageOut(BaseModel):
    id: int
    sender: str
    receiver: str
    subject: Optional[str]
    body: str

    class Config:
        orm_mode = True
