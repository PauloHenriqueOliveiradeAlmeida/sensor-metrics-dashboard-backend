from typing import List
import asyncio
from fastapi import WebSocket

from App.Core.Entrypoints.Websocket.Notifiers.Dtos.Response.UpdateSensorMetricsResponseDto import (
    UpdateSensorMetricsResponseDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsEventPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.IUpdateSensorMetricsEventListener import (
    IUpdateSensorMetricsEventListener,
)
from App.Core.Shared.Events.UpdateSensorMetrics.UpdateSensorMetricsEventDispatcher import (
    UpdateSensorMetricsEventDispatcher,
)


class NotifierService(IUpdateSensorMetricsEventListener):
    clients: List[WebSocket] = []

    def __init__(self):
        UpdateSensorMetricsEventDispatcher().subscribe(self)

    async def subscribe(self, client: WebSocket):
        await client.accept()
        self.clients.append(client)

    async def unsubscribe(self, client: WebSocket):
        self.clients.remove(client)

    async def notify(self, client: WebSocket, payload: UpdateSensorMetricsResponseDto):
        await client.send_json(payload.__dict__)

    def onUpdateSensorMetrics(self, payload: UpdateSensorMetricsEventPayloadDto):
        for client in self.clients:
            asyncio.create_task(
                self.notify(client, UpdateSensorMetricsResponseDto(**payload.__dict__))
            )
