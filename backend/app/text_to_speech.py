import pyttsx3
import uuid
import os

engine = pyttsx3.init()

def text_to_speech(text: str) -> str:
    filename = f"reply_{uuid.uuid4().hex}.wav"
    filepath = os.path.join("temp_audio", filename)

    engine.save_to_file(text, filepath)
    engine.runAndWait()

    return filepath
