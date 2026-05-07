<div align="center">

# 🎧 Voice AI Friend

**Talk. Listen. Connect. — Your personal AI companion, powered by voice.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

*Voice AI Friend is a real-time audio-to-audio conversational AI app. Speak into your mic, and your AI friend speaks back — no typing, no waiting, just natural conversation.*

</div>

---

## ✨ Features

- 🎙️ **Voice Input** — Click a button, speak naturally, done.
- 🤖 **AI-Powered Replies** — Intelligent, context-aware conversation powered by an LLM.
- 🔊 **Voice Output** — AI responds in spoken audio using text-to-speech.
- ⚡ **Real-Time Pipeline** — End-to-end audio flow: mic → STT → LLM → TTS → speaker.
- 🌐 **Browser-Based UI** — Clean Streamlit frontend, no installation friction for users.
- 🔌 **Decoupled Architecture** — FastAPI backend is independent and easily extendable.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    STREAMLIT FRONTEND                    │
│                                                          │
│   User speaks → audio_recorder → WAV file recorded      │
│   WAV sent via HTTP POST → /chat-audio endpoint          │
│   AI WAV response received → played in browser           │
└───────────────────────┬──────────────────────────────────┘
                        │  HTTP (multipart/form-data)
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND                       │
│                                                          │
│   1. save_audio()       → saves uploaded WAV to disk     │
│   2. audio_to_text()    → Speech-to-Text (STT)           │
│   3. generate_reply()   → LLM generates response text    │
│   4. text_to_speech()   → TTS converts text to WAV       │
│   5. FileResponse       → streams WAV back to frontend   │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
voice-ai-friend/
│
├── frontend/
│   └── app.py                  # Streamlit UI (audio recorder + playback)
│
├── app/
│   ├── main.py                 # FastAPI app & /chat-audio endpoint
│   ├── speech_to_text.py       # STT: converts audio → text
│   ├── llm.py                  # LLM: generates AI reply text
│   ├── text_to_speech.py       # TTS: converts text → audio (pyttsx3)
│   └── utils/
│       └── audio.py            # Utility: saves uploaded audio to disk
│
├── temp_audio/                 # Temporary WAV files (auto-created)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A working microphone
- `pip` or a virtual environment manager

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-ai-friend.git
cd voice-ai-friend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `pyttsx3` requires a system TTS engine. On Linux, install `espeak`:
> ```bash
> sudo apt install espeak
> ```
> On macOS/Windows, the default system voices are used automatically.

---

### 4. Run the Backend (FastAPI)

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The API will be live at: `http://127.0.0.1:8000`
Interactive docs at: `http://127.0.0.1:8000/docs`

---

### 5. Run the Frontend (Streamlit)

In a **new terminal** (with venv activated):

```bash
streamlit run frontend/app.py
```

Open your browser at `http://localhost:8501` and start talking! 🎤

---

## 🔄 How It Works — Step by Step

| Step | Component | What Happens |
|------|-----------|--------------|
| 1 | **Frontend** | User clicks the mic button and speaks |
| 2 | **Frontend** | Audio is recorded and saved as `user.wav` |
| 3 | **Frontend → Backend** | WAV file is POST'd to `/chat-audio` |
| 4 | **Backend: STT** | `audio_to_text()` transcribes speech to text |
| 5 | **Backend: LLM** | `generate_reply()` sends text to the AI model |
| 6 | **Backend: TTS** | `text_to_speech()` converts reply to `ai.wav` |
| 7 | **Backend → Frontend** | WAV file is streamed back as `FileResponse` |
| 8 | **Frontend** | AI voice response is played in the browser |

---

## 🛠️ Configuration

| Variable | Location | Default | Description |
|----------|----------|---------|-------------|
| `BACKEND_URL` | `frontend/app.py` | `http://127.0.0.1:8000/chat-audio` | Backend endpoint URL |
| `TEMP_DIR` | `frontend/app.py` & `text_to_speech.py` | `temp_audio/` | Directory for temp WAV files |

To change the LLM or STT engine, edit `app/llm.py` and `app/speech_to_text.py` respectively.

---

## 📦 Dependencies

```txt
# Backend
fastapi
uvicorn
pyttsx3

# Frontend
streamlit
audio-recorder-streamlit
requests
```

Install all at once:
```bash
pip install fastapi uvicorn pyttsx3 streamlit audio-recorder-streamlit requests
```

---

## 🔧 Extending the Project

Voice AI Friend is designed to be modular. Here are some easy ways to extend it:

- **Swap the STT engine** — Replace the STT module with OpenAI Whisper, Deepgram, or AssemblyAI for higher accuracy.
- **Upgrade the LLM** — Plug in GPT-4, Claude, Mistral, or a local model via Ollama.
- **Improve TTS** — Replace `pyttsx3` with ElevenLabs or Google Cloud TTS for more natural voices.
- **Add memory** — Store conversation history per session to give the AI friend context across turns.
- **Deploy** — Dockerize the backend and deploy to Railway, Render, or any cloud provider.

---

## 🐛 Troubleshooting

**Mic not recording?**
- Make sure your browser has microphone permissions enabled.
- Try a different browser (Chrome recommended).

**Backend connection refused?**
- Confirm FastAPI is running on port `8000` before launching Streamlit.
- Check `BACKEND_URL` in `frontend/app.py` matches your backend address.

**No audio output / silent WAV?**
- On Linux, ensure `espeak` is installed: `sudo apt install espeak`
- Run `python -c "import pyttsx3; e = pyttsx3.init(); e.say('test'); e.runAndWait()"` to verify TTS works.

**Slow response?**
- Check your LLM API latency. For local models, consider quantized versions for faster inference.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and a lot of talking to robots

*If you find this useful, drop a ⭐ on GitHub!*

</div>
