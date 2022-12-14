from fastapi import FastAPI

app = FastAPI()
db: list = []

# Leer base de datos
with open('db.txt') as f:
    key: str = ""
    name: str = ""
    for entry in f.readlines():
        entry = entry.strip() # Remover saltos de linea
        if "," not in entry:
            if entry == "0": break
            key = entry
        else:
            entry = entry.removesuffix(",")
            name = entry
            db.append({name: key})
f.close()

# Guardar base de datos en texto
def write_to_db():
    with open('db.txt', 'w') as f:
        for entry in db:
            key = list(entry.keys())[0]
            f.write(f"{key}\n{entry.get(key)},\n")
        f.write("0")
    f.close

# Escribir combinacion de nombre y clave
@app.post("/log-key")
def log_key(key: str, name: str) -> bool: 
    if {name: key} in db:
        return False
    else:
        db.append({name: key})
        write_to_db()
        return True

# Encontrar clave del nombre
@app.get("/get-key")
def get_key(name: str):
    for entry in db:
        if entry.get(name):
            return {"key": entry.get(name)}
    return {"response": "ERROR"}

# Consultar combinacion de nombre y clave
@app.get("/auth-key")
def auth_key(key: str, name: str) -> bool:
    if {name: key} in db:
        return True
    return False