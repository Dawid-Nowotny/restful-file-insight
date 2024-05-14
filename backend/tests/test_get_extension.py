import pytest
from unittest.mock import MagicMock
from fastapi import UploadFile, HTTPException, status

from src.file.services import get_extension

@pytest.mark.asyncio
async def test_get_extension():
    mock_file_with_magic_number = MagicMock(spec=UploadFile)
    mock_file_with_magic_number.read.return_value = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

    extension = await get_extension(mock_file_with_magic_number)
    assert extension == "PNG"

    mock_file_without_magic_number = MagicMock(spec=UploadFile)
    mock_file_without_magic_number.read.return_value = b'random_bytes'

    with pytest.raises(HTTPException) as exc_info:
        await get_extension(mock_file_without_magic_number)

    assert exc_info.value.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY