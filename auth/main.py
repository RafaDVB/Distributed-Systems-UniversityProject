from fastapi import FastAPI

import requests

app = FastAPI()
db = "http://127.0.0.1:8000" # URL de la base de datos

# Validar un par clave/nombre
@app.get("/auth")
def authenticate(key: str, name: str):
    r = requests.get(f"{db}/auth-key/?key={key}&name={name}")
    if r.text == "true":
        return {"response": "VALIDA"}
    return {"response": "INVALIDA"}
