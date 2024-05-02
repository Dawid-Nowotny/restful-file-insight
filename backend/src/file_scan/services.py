from fastapi import HTTPException, status
import vt

import tempfile
import os

from .api_key import VT_API_KEY

client = vt.Client(VT_API_KEY)

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