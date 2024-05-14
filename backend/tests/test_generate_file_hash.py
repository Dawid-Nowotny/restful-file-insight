from unittest.mock import MagicMock
from fastapi import UploadFile

from src.file.services import generate_file_hash

def test_generate_file_hash():
    mock_file = MagicMock(spec=UploadFile)
    mock_file.file = MagicMock()
    mock_file.file.read.return_value = b'This is a file content'

    file_hash = generate_file_hash(mock_file)
    assert file_hash == "3e4aaf08762ea9b9131fb5b4424f2f98b33c2168feae715e9a94e1caba9d9000"