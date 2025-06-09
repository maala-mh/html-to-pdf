from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/hc")
def execute():
    return {"message": "OK"}
