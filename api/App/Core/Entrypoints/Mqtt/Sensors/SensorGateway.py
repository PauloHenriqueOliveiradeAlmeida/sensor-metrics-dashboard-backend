from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTClient, MQTTConfig

from App.Core.Entrypoints.Mqtt.Sensors.Dtos.UpdateSensorMetricsPayloadDto import (
    UpdateSensorMetricsPayloadDto,
)
from App.Core.Entrypoints.Mqtt.Sensors.SensorService import SensorService
from App.Infra.Cache.Redis.RedisRepository import RedisRepository
from settings import settings

mqtt_client = FastMQTT(
    config=MQTTConfig(host=settings.mqtt_broker, port=settings.mqtt_port)
)
cache_repository = RedisRepository()
sensor_service = SensorService(cache_repository)


@asynccontextmanager
async def mqttLifespan(_: FastAPI):
    await mqtt_client.mqtt_startup()
    yield
    await mqtt_client.mqtt_shutdown()


@mqtt_client.subscribe("update-sensor-metrics")
async def updateSensorMetrics(
    client: MQTTClient,
    topic: str,
    payload: bytes,
    qos: int,
    properties: int,
):
    sensor_service.updateSensorMetrics(UpdateSensorMetricsPayloadDto.serialize(payload))
