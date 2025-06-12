from fastapi import APIRouter, WebSocket
from app.core.notifier import notifier

router = APIRouter()

@router.websocket("/ws/notify")
async def notify_socket(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Just hold the connection
    except:
        notifier.disconnect(websocket)
