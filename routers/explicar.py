from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chains import get_explain_chain
from config import model

router = APIRouter()

class ExplicarInput(BaseModel):
    codigo: str


@router.post("/explicar")
async def explicar(input: ExplicarInput):
    try:
        output = get_explain_chain(model).invoke(input.dict())
        return {"explanation": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
