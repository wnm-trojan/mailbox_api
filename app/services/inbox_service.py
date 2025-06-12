import json
from sqlalchemy.orm import Session
from app.core.cache import cache_get, cache_set
from app.models.message import Message
from app.schemas.message_schema import MessageOut

def get_user_inbox(user_email: str, db: Session):
    cache_key = f"inbox:{user_email}"
    cached_data = cache_get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    messages = db.query(Message).filter_by(receiver=user_email).all()
    result = [MessageOut.from_orm(msg).dict() for msg in messages]

    cache_set(cache_key, json.dumps(result), ex=60)
    return result
