from fastapi import FastAPI
from config import model
from routers.traduzir import router as traduzir_router
from routers.explicar import router as explicar_router
from routers.resumir import router as resumir_router
from routers.auth import router as auth_router
from db import init_db

app = FastAPI(
    title="LlamaServe AI",
    version='0.2',
    description='API de Inteligência Artificial com FastAPI + LangChain + Groq',
)

# Inicializa o banco
init_db()

# Rotas
app.include_router(auth_router)
app.include_router(traduzir_router)
app.include_router(explicar_router)
app.include_router(resumir_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
