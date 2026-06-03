import asyncio
import time

from fastapi import FastAPI, BackgroundTasks, WebSocket, WebSocketDisconnect

app = FastAPI(title="Demo")

processed = 0


@app.get("/slow-sync")
def slow_sync():
    time.sleep(5)
    return {"mode": "sync"}


@app.get("/slow-async")
async def slow_async():
    await asyncio.sleep(5)
    return {"mode": "async"}


@app.post("/submit", status_code=202)
async def submit(background_tasks: BackgroundTasks):
    async def simulate_processing():
        global processed
        await asyncio.sleep(3)
        processed += 1

    background_tasks.add_task(simulate_processing)
    return {"status": "accepted"}


@app.get("/status")
async def status():
    return {"processed": processed}


@app.websocket("/ws/echo")
async def ws_echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"echo: {data}")
    except WebSocketDisconnect:
        pass
