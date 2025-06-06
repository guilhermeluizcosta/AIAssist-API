from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db
from models.user import User
from utils.jwt_handler import criar_token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Entrada de dados
class RegisterInput(BaseModel):
    email: str
    nome: str
    senha: str

class LoginInput(BaseModel):
    email: str
    senha: str

# Registro de usuário
@router.post("/registrar")
def registrar(dados: RegisterInput, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=dados.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    senha_hash = pwd_context.hash(dados.senha)
    usuario = User(email=dados.email, nome=dados.nome, senha=senha_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

# Login
@router.post("/login")
def login(dados: LoginInput, db: Session = Depends(get_db)):
    usuario = db.query(User).filter_by(email=dados.email).first()
    if not usuario or not pwd_context.verify(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
