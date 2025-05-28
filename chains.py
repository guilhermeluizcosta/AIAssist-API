from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


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

def get_translate_chain(model):
    translate_prompt = ChatPromptTemplate.from_template(
        'Você é um assistente de tradução. Traduza o texto a seguir para o idioma {lingua}: {texto}'
    )
    translate_chain = translate_prompt | model | StrOutputParser()
    return translate_chain
