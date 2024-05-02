from fastapi import UploadFile, HTTPException, status
import vt

import tempfile
import os

from .constants import MAGIC_NUMBERS
from .api_key import VT_API_KEY

client = vt.Client(VT_API_KEY)

async def get_extension(file: UploadFile) -> str:
    header = await file.read(4)
    hex_signature = header.hex().lower()
    
    for extension, magic_number in MAGIC_NUMBERS.items():
        if hex_signature.startswith(magic_number):
            return extension
    
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Magic number not found for this file.")

async def get_analysis(file):
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_file_path = os.path.join(tmp_dir, file.filename)
            
            with open(tmp_file_path, "wb") as tmp_file:
                tmp_file.write(await file.read())
                
            with open(tmp_file_path, "rb") as tmp_file:
                analysis = await client.scan_file_async(tmp_file, wait_for_completion=True)
            
            analysis = await client.get_object_async(f"/analyses/{analysis.id}")
            return analysis.to_dict()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error occurred during analysis")