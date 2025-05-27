import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
from chains import get_explain_chain, get_resume_chain

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# Inicializa o modelo
model = ChatGroq(model="llama-3.3-70b-versatile")

# Inicializa a aplicação FastAPI
app= FastAPI(
    title= "LlamaServe AI",
    version='0.1',
    description='API de Inteligência Artificial com FastAPI + LangChain + Groq',
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

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)