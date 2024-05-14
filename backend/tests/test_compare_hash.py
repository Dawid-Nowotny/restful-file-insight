from src.file.services import compare_hash

def test_compare_hash():
    hash1 = "63f7f5c4a77b51d664e9e9cc12e50dbf43d1739184b8787d6845a07fcb6a0360"
    hash2 = "63f7f5c4a77b51d664e9e9cc12e50dbf43d1739184b8787d6845a07fcb6a0360"
    hash3 = "e42e7e399fdab2b60e3b4d7d3aa516392a3df53665f6e0c56d1f2e88f8a6fa30"

    assert compare_hash(hash1, hash2) == True
    assert compare_hash(hash1, hash3) == False