import os
from fastapi import UploadFile

TEMP_DIR = "temp_audio"

os.makedirs(TEMP_DIR, exist_ok=True)

def save_audio(file: UploadFile) -> str:
    path = os.path.join(TEMP_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return path
