from fastapi import WebSocket
from typing import List

class Notifier:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def notify_all(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

notifier = Notifier()
