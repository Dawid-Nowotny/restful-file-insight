from fastapi import APIRouter, UploadFile, File, Response

from .services import *

router = APIRouter()

@router.post("/scan-file")
async def scan_file(file: UploadFile = File(...)):
    result = await get_analysis(file)
    return result