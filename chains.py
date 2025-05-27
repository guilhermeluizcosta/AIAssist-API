import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

def get_resume_chain(model):

    prompt = ChatPromptTemplate.from_template(
        """
        Você é um assistente especialista em resumo de textos.
        Resuma o texto a seguir de forma clara, objetiva e mantendo as informações principais:

        Texto:
        {texto}

        Resumo:
        """
    )
    chain = prompt | model | StrOutputParser()

    return chain

def get_explain_chain(model):
    prompt = ChatPromptTemplate.from_template(
        """
        Você é um assistente de programação. Receberá um código e deve explicar de forma clara e didática
        o que ele faz, linha por linha ou por blocos se fizer mais sentido.

        Código:
        {codigo}

        Explique:
        """
    )

    chain = prompt | model | StrOutputParser()
    return chain
