import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

model = ChatGroq(model="llama-3.3-70b-versatile")

app= FastAPI(
    title= "LlamaServe AI",
    version='0.1',
    description='API de Inteligência Artificial com FastAPI + LangChain + Groq',
)

add_routes(
    app,
    model,
    path='/groq',
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)