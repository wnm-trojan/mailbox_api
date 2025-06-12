from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.inbox_service import get_user_inbox

router = APIRouter()

@router.get("/{email}")
def inbox(email: str, db: Session = Depends(get_db)):
    return get_user_inbox(email, db)
