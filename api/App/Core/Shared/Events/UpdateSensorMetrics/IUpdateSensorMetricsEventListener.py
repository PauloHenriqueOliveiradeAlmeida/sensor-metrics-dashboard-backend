from typing import Protocol

from App.Core.Shared.Events.UpdateSensorMetrics.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsEventPayloadDto,
)


class IUpdateSensorMetricsEventListener(Protocol):
    def onUpdateSensorMetrics(self, payload: UpdateSensorMetricsEventPayloadDto):
        pass
