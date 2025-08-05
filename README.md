# NeuroSD

## Overview

A fully offline, cross-platform, voice-enabled personal AI, inspired by Iron Man's JARVIS, running from an SD card on Linux, Windows, and macOS.

## Features

- Local LLM (LLaMA 3, Gemma, etc.)
- Whisper.cpp for speech-to-text
- Coqui/Piper TTS for voice
- Wake word detection (Porcupine/Whisper)
- CLI & GUI (PySide6)
- Retrieval from offline knowledge base (RAG)
- Auto-launch on SD insertion

## Folder Structure

See project root for layout.

## Setup

1. **Install dependencies:**  
   `pip install -r requirements.txt`
2. **Add models to `/models` and voice to `/voices`.**
3. **Run the assistant:**
   - Linux: `bash bin/linux_launcher.sh`
   - Windows: Double-click `bin/win_launcher.exe` (build with pyinstaller)
   - macOS: Open `bin/mac_launcher.app` (build with pyinstaller)
4. **Auto-launch:**
   - Linux: Install `udev/99-aiassistant.rules` to `/etc/udev/rules.d/`
   - Windows: `autorun.inf` triggers on insert
   - macOS: Install `macos/com.jarvis.aiautostart.plist` to `~/Library/LaunchAgents/`

## Building Launchers

- **Windows:**  
  `pyinstaller --onefile bin/win_launcher.py --name win_launcher.exe`
- **macOS:**  
  `pyinstaller --onefile bin/mac_launcher.py --name mac_launcher.app`

## Extending

- Fill in `rag/rag.py`, `wakeword/wakeword.py`, and GUI logic.
- Integrate LLaMA.cpp, Whisper.cpp, Piper/Coqui TTS as needed.

---

**Enjoy your portable, offline JARVIS!**
