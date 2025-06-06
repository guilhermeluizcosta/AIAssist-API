from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import secrets
from db import SessionLocal
from models.user import User, APIKey

router = APIRouter()

class RegisterInput(BaseModel):
    email: str
    nome: str
    senha: str

@router.post("/registrar")
def registrar(dados: RegisterInput):
    db = SessionLocal()
    if db.query(User).filter_by(email=dados.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    usuario = User(email=dados.email, nome=dados.nome, senha=dados.senha)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    chave = secrets.token_hex(16)
    api_key = APIKey(chave=chave, user_id=usuario.id)
    db.add(api_key)
    db.commit()

    return {"api_key": chave}
