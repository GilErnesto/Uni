import asyncio
import random
import time
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Header, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

SECRET_TOKEN = "secret-token"
STATIONS = ["aveiro", "lisboa", "porto", "coimbra"]

history: dict[str, list[dict]] = {s: [] for s in STATIONS}
connections: dict[str, list[WebSocket]] = {s: [] for s in STATIONS}
connections["*"] = []


def generate_reading(station: str) -> dict:
    return {
        "station": station,
        "timestamp": time.strftime("%H:%M:%S"),
        "aqi": random.randint(10, 150),
        "temperature": round(random.uniform(10.0, 35.0), 1),
        "humidity": random.randint(30, 90),
    }


async def push_readings():
    while True:
        await asyncio.sleep(3)
        for station in STATIONS:
            reading = generate_reading(station)
            history[station].append(reading)
            if len(history[station]) > 20:
                history[station].pop(0)
            for ws in list(connections[station]):
                try:
                    await ws.send_json(reading)
                except Exception:
                    connections[station].remove(ws)
            for ws in list(connections["*"]):
                try:
                    await ws.send_json(reading)
                except Exception:
                    connections["*"].remove(ws)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(push_readings())
    yield
    task.cancel()


app = FastAPI(title="Air Quality Monitor", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stations")
async def list_stations():
    return [
        {"station": s, "latest": history[s][-1] if history[s] else None}
        for s in STATIONS
    ]


@app.get("/stations/{station}")
async def get_station(station: str):
    if station not in STATIONS:
        raise HTTPException(status_code=404, detail="Station not found")
    return {"station": station, "history": history[station]}


@app.post("/stations/{station}/alert", status_code=202)
async def trigger_alert(
    station: str, authorization: Optional[str] = Header(default=None)
):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    if station not in STATIONS:
        raise HTTPException(status_code=404, detail="Station not found")
    return {"status": "alert queued", "station": station}


@app.websocket("/ws/{station}")
async def ws_station(websocket: WebSocket, station: str):
    if station not in STATIONS:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    connections[station].append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connections[station].remove(websocket)


@app.websocket("/ws")
async def ws_all(websocket: WebSocket):
    await websocket.accept()
    connections["*"].append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connections["*"].remove(websocket)
