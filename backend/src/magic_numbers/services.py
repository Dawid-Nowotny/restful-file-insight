from fastapi import UploadFile, HTTPException, status

from .constants import MAGIC_NUMBERS

async def get_extension(file: UploadFile) -> str:
    header = await file.read(4)
    hex_signature = header.hex().lower()
    
    for extension, magic_number in MAGIC_NUMBERS.items():
        if hex_signature.startswith(magic_number):
            return extension
    
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Magic number not found for this file.")