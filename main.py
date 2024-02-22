from fastapi import FastAPI
import datetime
import socket

app = FastAPI()


@app.get("/{nome}")
async def root(nome: str):
    return {"message": f"Hello {nome}"}


@app.get("/date")
async def date():
    return {"date": datetime.date.today()}

@app.get("/ip")
async def ip():
    return {"ip": socket.gethostbyname(socket.gethostname()) }

@app.get("/conversordolar/{valor}")
async def converter(valor: float):
    return {"valor": valor * 4.80}

@app.get("/conversortemperatura/{tipo}/{valor}")
async def converterTemperatura(tipo: str, valor: float):
        if tipo == "f":
            return {"valor_fahrenheit": valor * 9/5 + 32}
        elif tipo == "k":
            return {"valor_kelvin": valor + 273.15}
    