from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Curso, Aluno

# pip install jinja2 python-multipart

# inicializador o fastapi
app = FastAPI(title="Gestão escolar")

templates = Jinja2Templates(directory="templates")

# rodar api
# no terminal: python -m uvicorn main:app --reload

# rota 
# métodos http: GET,POST, PUT, DELETE

@app.get("/curso/cadastro")
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(

        request,
        "cadastrar_curso.html",
        {"request": request}
    )
    
# rota para cadastrar um curso

@app.post("/curso")
def criar_curso(
    nome: str = Form(...),
    carga_horaria: int = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    # cadastrar o curso no banco

    novo_curso = Curso(nome=nome, carga_horaria=carga_horaria, descricao=descricao)
    db.add(novo_curso)
    db.commit()

    return RedirectResponse(url="/", status_code=303)