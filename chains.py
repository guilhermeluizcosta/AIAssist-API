from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def get_resume_chain(model):
    prompt = ChatPromptTemplate.from_template(
        """
        Você é um assistente especialista em resumo de textos. 
        Resuma o texto abaixo de forma objetiva, clara e mantendo as informações mais importantes.
        Não inclua comentários ou explicações além do resumo.

        Texto:
        {texto}

        Resumo:
        """
    )
    chain = (
            prompt
            | model
            | StrOutputParser()
            | (lambda x: x.replace("\n", " ").strip())
    )

    return chain

def get_explain_chain(model):
    prompt = ChatPromptTemplate.from_template(
        """
        Você é um assistente de programação. Receberá um código e deve explicar de forma clara e didática 
        o que ele faz, linha por linha ou por blocos se fizer mais sentido.
        Não inclua informações além da explicação do código.

        Código:
        {codigo}

        Explicação:
        """
    )

    chain = (
            prompt
            | model
            | StrOutputParser()
            | (lambda x: x.replace("\n", " ").strip())
    )
    return chain

def get_translate_chain(model):
    prompt = ChatPromptTemplate.from_template(
        """
        Traduza APENAS o texto abaixo para o idioma {lingua}, sem adicionar comentários, explicações, formatações, quebras de linha ou qualquer outra informação. 
        Responda SOMENTE com a tradução exata.

        Texto:
        {texto}

        Tradução:
        """
    )
    chain = (
            prompt
            | model
            | StrOutputParser()
            | (lambda x: x.replace("\n", " ").strip())
    )
    return chain