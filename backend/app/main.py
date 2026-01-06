from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from app.speech_to_text import audio_to_text
from app.llm import generate_reply
from app.text_to_speech import text_to_speech
from app.utils.audio import save_audio

app = FastAPI(title="Voice AI Friend")

@app.post("/chat-audio")
async def chat_audio(audio: UploadFile = File(...)):
    audio_path = save_audio(audio)

    user_text = audio_to_text(audio_path)
    ai_text = generate_reply(user_text)
    ai_audio_path = text_to_speech(ai_text)

    return FileResponse(ai_audio_path, media_type="audio/wav")
