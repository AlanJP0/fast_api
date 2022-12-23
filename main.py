
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cliente")
def read_usuario():
    return {"cliente_id": 10, "cliente": "ALan"}

@app.put("/cliente")
def save_cliente(cliente_id: int, cliente: str):
    cliente = {"cliente_id": cliente_id, "cliente": cliente}
    return cliente

lista_user = [{"usermane": "Alan_juca"}] 

@app.get("/usuarios")
def read_usuarios():
    return lista_user

@app.post("/usuario")
def read_usuario(username: str):
    return lista_user.append({"usermane": username}) 