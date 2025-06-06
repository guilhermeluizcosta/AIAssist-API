from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from chains import get_explain_chain
from config import model
from dependencies.auth import get_usuario_autenticado

router = APIRouter()

# Entrada de dados do Explicar
class ExplicarInput(BaseModel):
    codigo: str


@router.post("/explicar")
async def explicar(input: ExplicarInput,usuario=Depends(get_usuario_autenticado)):
    try:
        output = get_explain_chain(model).invoke(input.dict())
        return {"explanation": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
