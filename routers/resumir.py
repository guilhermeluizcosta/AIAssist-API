from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chains import get_resume_chain
from config import model

router = APIRouter()

class ResumirInput(BaseModel):
    texto: str


@router.post("/resumir")
async def resumir(input: ResumirInput):
    try:
        output = get_resume_chain(model).invoke(input.dict())
        return {"resume": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
