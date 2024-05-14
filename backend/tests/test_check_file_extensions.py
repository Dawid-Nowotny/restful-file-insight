import pytest
from unittest.mock import MagicMock
from fastapi import UploadFile, HTTPException, status

from src.file.services import check_file_extensions

def test_check_file_extensions():
    mock_file1_same_ext = MagicMock(spec=UploadFile, filename="file1.txt")
    mock_file2_same_ext = MagicMock(spec=UploadFile, filename="file2.txt")

    check_file_extensions(mock_file1_same_ext, mock_file2_same_ext)

    mock_file1_diff_ext = MagicMock(spec=UploadFile, filename="file1.txt")
    mock_file2_diff_ext = MagicMock(spec=UploadFile, filename="file2.jpg")

    with pytest.raises(HTTPException) as exc_info:
        check_file_extensions(mock_file1_diff_ext, mock_file2_diff_ext)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
