import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException, status

from src.file.services import get_analysis

@pytest.mark.asyncio
async def test_get_analysis():
    mock_client = MagicMock()
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.__exit__.return_value = None
    mock_client.scan_file_async.return_value = MagicMock(id="123")
    mock_client.get_object_async.return_value = MagicMock(to_dict=lambda: {"result": "analysis"})

    with pytest.raises(HTTPException) as exc_info:
        await get_analysis(mock_file)

    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR