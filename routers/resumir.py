from fastapi import APIRouter, HTTPException,Depends
from pydantic import BaseModel
from chains import get_resume_chain
from config import model
from dependencies.auth import get_usuario_autenticado

router = APIRouter()

# Entrada de dados do Resumir
class ResumirInput(BaseModel):
    texto: str


@router.post("/resumir")
async def resumir(input: ResumirInput,usuario=Depends(get_usuario_autenticado)):
    try:
        output = get_resume_chain(model).invoke(input.dict())
        return {"resume": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
