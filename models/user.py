from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    senha = Column(String)  

    api_key = relationship("APIKey", back_populates="user", uselist=False)


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    chave = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    usado = Column(Integer, default=0)
    limite = Column(Integer, default=1000)
    criado_em = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="api_key")
