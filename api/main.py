from fastapi import FastAPI
from App.Core.Entrypoints.Mqtt.Sensors.SensorGateway import mqttLifespan
from App.Core.Entrypoints.Websocket.Notifiers.NotifierGateway import websocket_client

app = FastAPI(lifespan=mqttLifespan)
app.include_router(websocket_client)
