from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0
    mqtt_broker: str = "mosquitto"
    mqtt_port: int = 1883


settings = Settings()
