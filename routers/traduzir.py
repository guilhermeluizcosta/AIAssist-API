from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from chains import get_translate_chain
from config import model
from dependencies.auth import get_usuario_autenticado

router = APIRouter()

# Entrada de dados do Traduzir
class TraduzirInput(BaseModel):
    lingua: str
    texto: str

@router.post("/traduzir")
async def traduzir(input: TraduzirInput,usuario=Depends(get_usuario_autenticado)):
    try:
        output = get_translate_chain(model).invoke(input.dict())
        return {"translation": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
