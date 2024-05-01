from fastapi import APIRouter, UploadFile, File, Response

from .services import *

import json

router = APIRouter()

@router.post("check-magic-numbers")
async def check_magic_numbers(file: UploadFile = File(...)):
    extension = await get_extension(file)

    return Response(
        content=json.dumps({"extension": extension}),
        media_type="application/json",
        status_code=200,
    )