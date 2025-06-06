from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_handler import verificar_token
from db import SessionLocal
from models.user import User
from datetime import date
security = HTTPBearer()

def get_usuario_autenticado(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    email = payload.get("sub")
    db = SessionLocal()
    usuario = db.query(User).filter_by(email=email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    hoje = date.today()

    if usuario.ultima_requisicao != hoje:
        usuario.requisicoes_hoje = 0
        usuario.ultima_requisicao = hoje

    if usuario.requisicoes_hoje >= 2:
        raise HTTPException(status_code=429, detail="Limite diário de requisições atingido")

    usuario.requisicoes_hoje += 1
    db.commit()

    return usuario
