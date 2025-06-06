from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import  declarative_base
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    senha = Column(String)
    requisicoes_hoje = Column(Integer, default=0)
    ultima_requisicao = Column(Date, default=date.today)




