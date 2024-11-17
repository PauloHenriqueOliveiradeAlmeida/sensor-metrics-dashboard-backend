from typing import List
from pydantic import BaseModel


class UpdateSensorMetricsResponseDto(BaseModel):
    temperature_metrics: List[float]
    humidity_metrics: List[float]
    temperature_standard_deviation: float
    humidity_standard_deviation: float
    correlation: float
