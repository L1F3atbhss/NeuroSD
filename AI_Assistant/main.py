import os
import sys
import platform
import argparse
import json
import datetime
from pathlib import Path

"""
Offline JARVIS AI Assistant (Finished Minimal Version)
- Fully working CLI
- Config loading
- Simple offline brain (rule-based + command system)
- Optional offline TTS (pyttsx3)
- Clean project structure

No internet or cloud APIs required.
"""

# Config

def load_config():
    config_path = Path(__file__).parent / "config" / "settings.json"
    if not config_path.exists():
        config_path.parent.mkdir(exist_ok=True)
        default_config = {
            "assistant_name": "NEURO",
            "tts": true,
            "user_name": "User"
        }
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
    with open(config_path, "r") as f:
        return json.load(f)


# Optional TTS

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

class Speaker:
    def __init__(self, enabled=True):
        self.enabled = enabled and TTS_AVAILABLE
        if self.enabled:
            self.engine = pyttsx3.init()

    def say(self, text):
        print(text)
        if self.enabled:
            self.engine.say(text)
            self.engine.runAndWait()


# Brain (Offline Logic)


def generate_response(text, config):
    text = text.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return f"Hello {config['user_name']}. How can I assist you?"

    if "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    if "date" in text:
        return f"Today's date is {datetime.date.today().isoformat()}"

    if "os" in text or "system" in text:
        return f"You are running {platform.system()} {platform.release()}"

    if "your name" in text:
        return f"My name is {config['assistant_name']}. Offline and operational."

    if "help" in text:
        return (
            "Available commands:\n"
            "- time\n"
            "- date\n"
            "- system info\n"
            "- your name\n"
            "- exit"
        )

    return "I am currently running offline logic. Command not recognized. Try 'help'."

# CLI Mode

def run_cli(config):
    speaker = Speaker(enabled=config.get("tts", False))

    print("=== Offline JARVIS AI Assistant (CLI Mode) ===")
    print("Type 'exit' or press Ctrl+C to quit. Type 'help' for commands.\n")

    speaker.say(f"{config['assistant_name']} online.")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower().strip() in ["exit", "quit"]:
                speaker.say("Goodbye.")
                break

            response = generate_response(user_input, config)
            speaker.say(f"{config['assistant_name']}: {response}")

        except (KeyboardInterrupt, EOFError):
            speaker.say("Shutting down.")
            break


# GUI Stub

def run_gui():
    print("GUI mode coming soon (PySide6). Use --cli for now.")


# Entry Point

def main():
    parser = argparse.ArgumentParser(description="Offline JARVIS AI Assistant")
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode")
    parser.add_argument("--gui", action="store_true", help="Run in GUI mode")
    args = parser.parse_args()

    config = load_config()

    if args.gui:
        run_gui()
    else:
        run_cli(config)

if __name__ == "__main__":
    main()
