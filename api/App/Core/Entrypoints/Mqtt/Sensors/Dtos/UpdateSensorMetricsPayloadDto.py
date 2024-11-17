from typing import Literal
from gmqtt.client import json
from pydantic import BaseModel


class UpdateSensorMetricsPayloadDto(BaseModel):
    sensor_name: Literal["temperature", "humidity"]
    value: float

    @classmethod
    def serialize(cls, value: bytes):
        payload = json.loads(value.decode("utf-8"))

        return cls(**payload)
