from App.Core.Entrypoints.Mqtt.Sensors.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsEventPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.UpdateSensorMetricsEventDispatcher import (
    UpdateSensorMetricsEventDispatcher,
)
from App.Core.Shared.Filters.CorrelationFilter import CorrelationFilter
from App.Core.Shared.Filters.StandardDeviationFilter import StandardDeviationFilter
from App.Core.Shared.Repositories.Cache.ICacheRepository import ICacheRepository


class SensorService:
    update_sensor_metrics_event_dispatcher = UpdateSensorMetricsEventDispatcher()

    def __init__(self, chache_repository: ICacheRepository):
        self.chache_repository = chache_repository

    def updateSensorMetrics(self, payload: UpdateSensorMetricsPayloadDto):
        self.chache_repository.create(payload.sensor_name, payload.value)
        temperature_sensor_metrics = self.chache_repository.get("temperature")
        humidity_sensor_metrics = self.chache_repository.get("humidity")
        if not temperature_sensor_metrics or not humidity_sensor_metrics:
            return

        temperature_standard_deviation = StandardDeviationFilter().execute(
            temperature_sensor_metrics
        )
        humidity_standard_deviation = StandardDeviationFilter().execute(
            humidity_sensor_metrics
        )
        correlation = CorrelationFilter().execute(
            temperature_sensor_metrics, humidity_sensor_metrics
        )

        self.update_sensor_metrics_event_dispatcher.dispatch(
            UpdateSensorMetricsEventPayloadDto(
                temperature_metrics=temperature_sensor_metrics,
                humidity_metrics=humidity_sensor_metrics,
                temperature_standard_deviation=temperature_standard_deviation,
                humidity_standard_deviation=humidity_standard_deviation,
                correlation=correlation,
            )
        )
