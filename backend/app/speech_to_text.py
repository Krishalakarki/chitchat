import whisper
import torch

model = whisper.load_model("tiny")
model = model.to("cpu").to(torch.float32)

def audio_to_text(audio_path: str) -> str:

    result = model.transcribe(audio_path)
    return result["text"]