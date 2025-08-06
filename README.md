# 🦙 LlamaServe AI - API de Inteligência Artificial

API REST criada com **FastAPI + LangChain + Groq (Llama 3.3)**, oferecendo funcionalidades de:

- 📝 **Resumo de textos**
- 💡 **Explicação de códigos**
- 🌐 **Tradução de textos**

---

## **Documentação pública:**

👉 [https://aiassist-api.onrender.com/docs](https://aiassist-api.onrender.com/docs)

---

## **Autenticação:**

Embora a documentação `/docs` seja pública, **todas as rotas da API são protegidas com autenticação via API Key**.

### Se quiser realizar uma requisição:
- Cadastre-se utilizando o endpoint:
`POST /registrar`
```json
{
  "email": "string",
  "nome": "string",
  "senha": "string"
}
```
- Ou faça o login utilizando o endpoint:
`POST /login`
```json
{
  "email": "string",
  "senha": "string"
}
``` 

---
## **Tecnologias usadas**
- Python (Versão 3.10)

- FastAPI

- LangChain

- Groq (Llama 3.3)

- FastAPI Key Auth

- Render (Deploy)
---
##  **Endpoints disponíveis**

### Resumir Texto
`POST /resumir/invoke`

**Body:**
```json
{
  "input": {
    "texto": "Seu texto aqui"
  }
}
```

### Explicar Código
`POST /explicar/invoke`
```json
{
  "input": {
    "codigo": "Seu código aqui"
  }
}
```
### Traduzir Texto
`POST /traduzir/invoke`
```json
{
  "input": {
    "texto": "Texto para traduzir",
    "lingua": "Idioma destino (ex: English, Spanish, French)"
  }
}
```

## **Como rodar localmente**

### Clone o Projeto
```
git clone https://github.com/guilhermeluizcosta/AIAssist-API.git
cd AIAssist-API
```
### Instale as dependências (sse-starlette deve ser instalado depois)
```
pip install -r requirements.txt
pip install sse-starlette
```
### Crie uma conta no site do Groq
👉 https://console.groq.com/

### Crie um arquivo .env
```
GROQ_API_KEY=suachavegroq
X_API_KEY=suaapikeyprivada
ENABLE_AUTH=True
```
### Execute
```
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Acesse: http://localhost:8000/docs








