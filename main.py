from fastapi import FastAPI

# inicializador o fastapi
app = FastAPI(title="Gestão escolar")

# rodar api
# no terminal: python -m uvicorn main:app --reload

# rota 
# métodos http: GET,POST, PUT, DELETE
@app.get("/")
def tela_inicial():
    return {"mensagem": "Bem-vindo ao sistema de gestão escolar"}

# banco de dados
alunos = {
    1: {"nome": "Iago", "idade": 18},
    2: {"nome": "Gabriel", "idade": 28},
    3: {"nome": "Gomes", "idade": 17},
}

@app.get("/alunos")
def listar_alunos():
    return {"alunos": alunos}