import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
from chains import resumidor_chain, explicar_codigo_chain

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# Inicializa o modelo
model = ChatGroq(model="llama-3.3-70b-versatile")

# Inicializa a aplicação FastAPI
app= FastAPI(
    title= "LlamaServe AI",
    version='0.1',
    description='API de Inteligência Artificial com FastAPI + LangChain + Groq',
)

# Inicializa as chains
resumo_chain = resumidor_chain(model)
explicar_chain = explicar_codigo_chain(model)


# Endpoints
add_routes(
    app,
    model,
    path='/groq',
)


add_routes(
    app,
    resumo_chain,
    path='/resumir',
)

add_routes(
    app,
    explicar_chain,
    path='/explicar',
)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)