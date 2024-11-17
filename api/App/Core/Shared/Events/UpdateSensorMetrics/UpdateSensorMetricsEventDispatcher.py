from typing import List
from App.Core.Shared.Events.UpdateSensorMetrics.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsEventPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.IUpdateSensorMetricsEventListener import (
    IUpdateSensorMetricsEventListener,
)


class UpdateSensorMetricsEventDispatcher:
    listeners: List[IUpdateSensorMetricsEventListener] = []

    def subscribe(self, listener: IUpdateSensorMetricsEventListener):
        self.listeners.append(listener)

    def dispatch(self, payload: UpdateSensorMetricsEventPayloadDto):
        for listener in self.listeners:
            listener.onUpdateSensorMetrics(payload)
