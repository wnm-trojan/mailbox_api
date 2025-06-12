"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-11
Email: warunanissanka44@gmail.com
Description: 
"""

from app.db.database import Base, engine
from app.models import user, message

def init():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created.")

if __name__ == "__main__":
    init()
