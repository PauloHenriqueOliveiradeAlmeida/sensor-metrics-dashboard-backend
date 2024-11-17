from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from App.Core.Entrypoints.Websocket.Notifiers.NotifierService import NotifierService


websocket_client = APIRouter()
notifier_service = NotifierService()


@websocket_client.websocket("/notifier")
async def notifier(websocket: WebSocket):
    try:
        await notifier_service.subscribe(websocket)
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await notifier_service.subscribe(websocket)
