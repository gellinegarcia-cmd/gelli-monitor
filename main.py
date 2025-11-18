from fastapi import FastAPI, Request
from datetime import datetime
import csv
import os

app = FastAPI()

# Crear archivo CSV si no existe
FILE = "registros.csv"
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "imei", "hr", "spo2", "temp", "bp", "battery", "lat", "lng"])

@app.post("/data")
async def recibir_datos(request: Request):
    data = await request.json()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [
        timestamp,
        data.get("imei"),
        data.get("hr"),
        data.get("spo2"),
        data.get("temp"),
        data.get("bp"),
        data.get("battery"),
        data.get("lat"),
        data.get("lng")
    ]

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    return {"status": "OK", "received": row}

@app.get("/")
def home():
    return {"status": "Servidor funcionando", "msg": "Gelline monitor activo"}
