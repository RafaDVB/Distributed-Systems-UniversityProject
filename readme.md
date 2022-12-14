# Proyecto de Sistemas Distribuidos

## Dependencias

Instalar dependencias con `python3 pip install -r requirements.txt`. Se recomienda usar un ambiente virtual.

## Ejecucion

- Servidor Base de Datos
  - `cd db`
  - `uvicorn main:app --reload --port 8000`
- Servidor de Autenticacion
  - `cd auth`
  - `uvicorn main:app --reload --port 8001`
- Servidor de Claves
  - `cd key`
  - `uvicorn main:app --reload --port 8002`
- Proxy
  - `cd proxy`
  - `uvicorn main:app --reload --port 8003`
- Cliente
  - `cd client`
  - `python3 main.py -i <ARCHIVO DE ENTRADA>`
