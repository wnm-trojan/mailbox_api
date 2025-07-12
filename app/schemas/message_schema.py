"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12
Email: warunanissanka44@gmail.com
Description: 
"""

from pydantic import BaseModel, ConfigDict
from typing import Optional

class MessageCreate(BaseModel):
    sender: str
    receiver: str
    subject: Optional[str] = None
    body: str

class MessageOut(BaseModel):
    sender: str
    receiver: str
    subject: str | None
    body: str

    model_config = ConfigDict(from_attributes=True)
