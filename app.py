import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
from fastapi_key_auth import AuthorizerMiddleware
from chains import get_explain_chain, get_resume_chain, get_translate_chain

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['X_API_KEY'] = config('X_API_KEY')

# Inicializa o modelo
model = ChatGroq(model="llama-3.3-70b-versatile")

# Inicializa a aplicação FastAPI
app= FastAPI(
    title= "LlamaServe AI",
    version='0.1',
    description='API de Inteligência Artificial com FastAPI + LangChain + Groq',
)

# Inicializa o middleware
app.add_middleware(
    middleware_class=AuthorizerMiddleware,
    public_paths=['/docs', '/redoc', '/openapi.json'],
    key_pattern='X_API_KEY',
)

# Endpoints
add_routes(
    app,
    get_resume_chain(model),
    path='/resumir',
)

add_routes(
    app,
    get_explain_chain(model),
    path='/explicar',
)

add_routes(
    app,
    get_translate_chain(model),
    path='/traduzir'
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)

