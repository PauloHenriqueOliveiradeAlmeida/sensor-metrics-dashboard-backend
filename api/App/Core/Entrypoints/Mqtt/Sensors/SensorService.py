from App.Core.Entrypoints.Mqtt.Sensors.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsEventPayloadDto,
)
from App.Core.Shared.Events.UpdateSensorMetrics.UpdateSensorMetricsEventDispatcher import (
    UpdateSensorMetricsEventDispatcher,
)
from App.Core.Shared.Repositories.Cache.ICacheRepository import ICacheRepository
import numpy


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

        temperature_standard_deviation = numpy.std([
            metric for metric in temperature_sensor_metrics if metric != 0
        ])
        humidity_standard_deviation = numpy.std([
            metric for metric in temperature_sensor_metrics if metric != 0
        ])

        min_length = min(len(temperature_sensor_metrics), len(humidity_sensor_metrics))
        correlation = numpy.corrcoef(
            temperature_sensor_metrics[:min_length],
            humidity_sensor_metrics[:min_length],
        )
        self.update_sensor_metrics_event_dispatcher.dispatch(
            UpdateSensorMetricsEventPayloadDto(
                temperature_metrics=temperature_sensor_metrics,
                humidity_metrics=humidity_sensor_metrics,
                temperature_standard_deviation=temperature_standard_deviation.__float__(),
                humidity_standard_deviation=humidity_standard_deviation.__float__(),
                correlation=correlation[0, 1],
            )
        )
