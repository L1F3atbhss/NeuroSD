# NeuroSD

## Overview

**NeuroSD** is a fully offline, cross-platform, voice-enabled personal AI inspired by Iron Man’s JARVIS.  
It could run entirely locally from an SD card or on your personal computer. No internet required. Supported on **Linux, Windows, and macOS**.

---

## Features

- Fully offline local LLM (GGUF via `llama.cpp`)
- Speech-to-text (Whisper.cpp – optional)
- Text-to-speech (pyttsx3)
- Wake word detection (Whisper – optional)
- CLI (stable) & GUI (PySide6)
- Offline knowledge base (RAG-ready)
- Auto-launch on SD card insertion

---

## Folder Structure

```text
models/        # LLM GGUF files
voices/        # TTS voice models
config/        # settings.json
AI_Assistant/  # Core assistant logic
```
---
# Requirements

Python
	•	Python 3.10 – 3.12 (64-bit required)
	•	Windows: ensure Python is added to PATH

# Core Dependencies

```Bash
pip install -r requirements.txt
pip install llama-cpp-python
```
Optional (voice support):
```
pip install pyttsx3
```
---

# Downloading an Offline LLM (GGUF)

Download GGUF models and place them in the /models folder.

## Recommended Models

TinyLLaMA (Fast, low RAM – recommended starter)

`tinyllama-1.1b-chat.Q4_K_M.gguf`


LLaMA 3 (Higher quality, more RAM required)

`https://huggingface.co/TheBloke/Meta-Llama-3-8B-GGUF`

Gemma

`https://huggingface.co/TheBloke/Gemma-GGUF`

Example:
```
models/
└── tinyllama-1.1b-chat.Q4_K_M.gguf
```

Enable in config/settings.json:
```
{
  "use_llm": true,
  "llm_model": "tinyllama-1.1b-chat.Q4_K_M.gguf",
  "context_size": 2048
}
```
---
Setup & Run
	1.	Install dependencies
	2.	Add LLM models to /models
	3.	Run the assistant

---
#Auto-Launch on SD Card Insert

Linux:
```Bash
sudo cp udev/99-aiassistant.rules /etc/udev/rules.d/
```

Windows:
Uses autorun.inf

MacOS:

```
macos/com.jarvis.aiautostart.plist
```
To:
```
~/Library/LaunchAgents/
```
---

#Building Launchers:
Windows:
```
pyinstaller --onefile bin/win_launcher.py --name win_launcher.exe
```

MacOS:
```
pyinstaller --onefile bin/mac_launcher.py --name mac_launcher.app
```
---
# Extending NeuroSD

	•	rag/rag.py – Offline retrieval (RAG)
	•	wakeword/wakeword.py – Wake word detection
	•	GUI logic with PySide6
	•	Swap GGUF models freely
	•	Add new voices under /voices
