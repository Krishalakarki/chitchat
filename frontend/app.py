import streamlit as st
import requests
import os
from audio_recorder_streamlit import audio_recorder

# ---------------- CONFIG ----------------
BACKEND_URL = "http://127.0.0.1:8000/chat-audio"  # backend endpoint
TEMP_DIR = "temp_audio"
os.makedirs(TEMP_DIR, exist_ok=True)

st.set_page_config(page_title="Voice AI Friend", page_icon="🎧")

# ---------------- UI ----------------
st.title("🎧 Voice AI Friend")
st.write("Talk to your AI friend using your microphone")

# 🎙️ Record audio
audio_bytes = audio_recorder(
    text="🎙️ Click and speak",
    recording_color="#ff4b4b",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="3x",
)

# ---------------- AUDIO HANDLING ----------------
if audio_bytes:
    user_audio_path = f"{TEMP_DIR}/user.wav"

    with open(user_audio_path, "wb") as f:
        f.write(audio_bytes)

    st.success("✅ Voice recorded")

    st.audio(user_audio_path, format="audio/wav")

    with st.spinner("🤖 AI is thinking..."):
        try:
            with open(user_audio_path, "rb") as f:
                response = requests.post(
                    BACKEND_URL,
                    files={"audio": f},
                    timeout=120
                )

            if response.status_code == 200:
                ai_audio_path = f"{TEMP_DIR}/ai.wav"

                with open(ai_audio_path, "wb") as f:
                    f.write(response.content)

                st.success("🗣️ AI replied")
                st.audio(ai_audio_path, format="audio/wav")

            else:
                st.error("❌ Backend error")

        except Exception as e:
            st.error(f"Error: {e}")
