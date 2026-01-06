import os
import sys
import platform
import argparse
import json
import datetime
from pathlib import Path

"""
NEURO AI Assistant (Offline JARVIS)
- Safe config loading
- Optional offline LLM (llama.cpp)
"""

# =====================
# Config (SAFE)
# =====================

def load_config():
    config_path = Path(__file__).parent / "config" / "settings.json"

    default_config = {
        "assistant_name": "NEURO",
        "user_name": "User",
        "tts": False,
        "use_llm": False,
        "llm_model": "tinyllama-1.1b-chat-v1.0-q4_k_m.gguf",
        "model": "tinyllama-1.1b-chat-v1.0-q4_k_m.gguf",
        "context_size": 2048
    }

    if not config_path.exists():
        config_path.parent.mkdir(exist_ok=True)
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config

    with open(config_path, "r") as f:
        user_config = json.load(f)

    # Merge defaults to prevent KeyError
    for k, v in default_config.items():
        user_config.setdefault(k, v)

    return user_config

# =====================
# Optional TTS
# =====================

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

class Speaker:
    def __init__(self, enabled=False):
        self.enabled = enabled and TTS_AVAILABLE
        if self.enabled:
            self.engine = pyttsx3.init()

    def say(self, text):
        print(text)
        if self.enabled:
            self.engine.say(text)
            self.engine.runAndWait()

# =====================
# Offline LLM
# =====================

USE_LLM = False
LLM = None

def load_llm(config):
    global USE_LLM, LLM

    if not config.get("use_llm"):
        return

    try:
        from llama_cpp import Llama
        model_path = Path(__file__).parent / "models" / config["llm_model"]

        if not model_path.exists():
            print("[LLM] Model not found:", model_path)
            return

        LLM = Llama(
            model_path=str(model_path),
            n_ctx=config.get("context_size", 2048),
            n_threads=os.cpu_count()
        )
        USE_LLM = True
        print("[LLM] Offline model loaded")

    except ImportError:
        print("[LLM] llama-cpp-python not installed")

# =====================
# Brain
# =====================

def generate_response(text, config):
    text = text.strip()

    # ---- LLM ----
    if USE_LLM and LLM:
        prompt = (
            f"You are an offline AI assistant named {config['assistant_name']}.\n"
            f"User: {text}\nAssistant:"
        )
        result = LLM(prompt, max_tokens=256, stop=["User:"])
        return result["choices"][0]["text"].strip()

    # ---- Rules ----
    lower = text.lower()

    if lower in ["hi", "hello", "hey"]:
        return f"Hello {config['user_name']}. How can I help?"

    if "time" in lower:
        return datetime.datetime.now().strftime("%H:%M:%S")

    if "date" in lower:
        return datetime.date.today().isoformat()

    if "system" in lower or "os" in lower:
        return f"{platform.system()} {platform.release()}"

    if "your name" in lower:
        return f"My name is {config['assistant_name']}"

    if "help" in lower:
        return "Commands: time, date, system, your name, exit"
    
    if "what can you do?" in lower:
        return "Commands: time, date, system, your name, exit"

    return "Offline mode active. Enable LLM for free chat."

# =====================
# CLI
# =====================

def run_cli(config):
    speaker = Speaker(enabled=config.get("tts", False))

    speaker.say(f"{config['assistant_name']} online.")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                speaker.say("Goodbye.")
                break

            response = generate_response(user_input, config)
            speaker.say(f"{config['assistant_name']}: {response}")

        except (KeyboardInterrupt, EOFError):
            speaker.say("Shutting down.")
            break

# =====================
# Main
# =====================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", action="store_true")
    args = parser.parse_args()

    config = load_config()
    load_llm(config)
    run_cli(config)

if __name__ == "__main__":
    main()
