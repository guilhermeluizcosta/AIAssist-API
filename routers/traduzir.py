from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chains import get_translate_chain
from config import model

router = APIRouter()

class TraduzirInput(BaseModel):
    lingua: str
    texto: str

@router.post("/traduzir")
async def traduzir(input: TraduzirInput):
    try:
        output = get_translate_chain(model).invoke(input.dict())
        return {"translation": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
