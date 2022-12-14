from fastapi import FastAPI

import random
import requests

app = FastAPI()
db = "http://127.0.0.1:8000" # URL de la base de datos

# Obtener clave aleatoria de 8 digitos
@app.post("/get-key")
def home(name: str):
    key: str = lookup_key(name)
    if key:
        return {"key": key}
    else:
        random.seed()
        key: str = f'{random.randrange(100000000):08d}'
        if register_key(name, key):
            return {"key": key}

# Buscar clave dado un nombre
def lookup_key(name: str):
    r = requests.get(f"{db}/get-key/?name={name}")
    if r.json().get("response"):
        return None
    else:
        return r.json().get("key")

# Enviar clave a base de datos
def register_key(name: str, key: str):
    r = requests.post(f"{db}/log-key/?key={key}&name={name}")
    if r.text == "true":
        return True
    return False
