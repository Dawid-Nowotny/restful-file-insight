from fastapi import APIRouter, UploadFile, File, Response, status

from .services import *

import json

router = APIRouter()

@router.post("/check-magic-numbers")
async def check_magic_numbers(file: UploadFile = File(...)):
    extension = await get_extension(file)

    return Response(
        content=json.dumps({"extension": extension}),
        media_type="application/json",
        status_code=status.HTTP_200_OK,
    )

@router.post("/scan")
async def scan_file(file: UploadFile = File(...)):
    result = await get_analysis(file)
    return result

@router.post("/compare_files/")
def compare_files(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    hash1 = generate_file_hash(file1)
    hash2 = generate_file_hash(file2)

    if compare_hash(hash1, hash2):
        return Response(
        content=json.dumps({"message": "Pliki są identyczne."}),
        media_type="application/json",
        status_code=status.HTTP_200_OK,
        )
    
    check_file_extensions(file1, file2)

    return Response(
        content=json.dumps({"message": "Pliki różnią się od siebie"}),
        media_type="application/json",
        status_code=status.HTTP_200_OK,
    )