from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from app.config import MAX_RESPONSE_TOKENS

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

# Load model (CPU safe)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-small"
)

# Put model in evaluation mode
model.eval()


SYSTEM_PROMPT = """
You are a friendly, calm, and helpful AI assistant.
Give short, clear, and safe answers.
If the question is inappropriate or unsafe,
respond with "I'm sorry, I can't assist with that."
"""

def generate_reply(user_text: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nQuestion: {user_text}\nAnswer:"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    with torch.no_grad():  # saves memory
        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_RESPONSE_TOKENS
        )

    reply = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return reply.strip()
