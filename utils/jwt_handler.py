import os
from decouple import config
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 60

def criar_token(dados: dict):
    dados_para_token = dados.copy()
    exp = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    dados_para_token.update({"exp": exp})
    return jwt.encode(dados_para_token, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
