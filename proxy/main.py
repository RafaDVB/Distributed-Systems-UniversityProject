from fastapi import FastAPI

import requests

app = FastAPI()
# URL de servidor para autenticacion y clave respectivamente
auth = "http://127.0.0.1:8001"
keyServer = "http://127.0.0.1:8002"

# Obtener peticion y redirigir
@app.post("/service")
def process_request(type: str, name: str, key: str = None):
    match type:
        case "FIRMAR":
            r = requests.post(f"{keyServer}/get-key/?name={name}")
            return r.json()
        case "AUTENTICAR":
            r = requests.get(f"{auth}/auth/?key={key}&name={name}")
            return r.json()