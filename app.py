from fastapi import FastAPI, Request
import datetime

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    print("Datos recibidos:", data)
    
    return {"status": "ok"}
