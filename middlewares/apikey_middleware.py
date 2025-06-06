from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from db import SessionLocal
from models.user import APIKey

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        rotas_publicas = ["/docs", "/openapi.json", "/registrar", "/login"]

        if any(request.url.path.startswith(rota) for rota in rotas_publicas):
            return await call_next(request)

        api_key = request.headers.get("x-api-key")
        if not api_key:
            raise HTTPException(status_code=401, detail="API Key ausente")

        db = SessionLocal()
        try:
            key = db.query(APIKey).filter_by(chave=api_key).first()
            if not key:
                raise HTTPException(status_code=403, detail="API Key inválida")
            if key.usado >= key.limite:
                raise HTTPException(status_code=429, detail="Limite de requisições excedido")

            key.usado += 1
            db.commit()
        finally:
            db.close()

        return await call_next(request)
