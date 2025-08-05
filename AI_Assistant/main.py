import os
import sys
import platform
import argparse
import json
from pathlib import Path

# Stubs for AI, Speech-to-Text, and TTS modules
def load_config():
    config_path = Path(__file__).parent / "config" / "settings.json"
    with open(config_path, "r") as f:
        return json.load(f)

def run_cli():
    print("=== Offline JARVIS AI Assistant (CLI Mode) ===")
    print("Say 'exit' or press Ctrl+C to quit.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower().strip() in ["exit", "quit"]:
                print("Goodbye!")
                break
            # TODO: Replace with actual LLM inference and TTS output
            print("JARVIS: [Simulated AI Response]")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

def main():
    parser = argparse.ArgumentParser(description="Offline JARVIS AI Assistant")
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode")
    parser.add_argument("--gui", action="store_true", help="Run in GUI mode (PySide6)")
    args = parser.parse_args()

    config = load_config()

    if args.cli or not args.gui:
        run_cli()
    else:
        print("GUI mode is not implemented yet. Try --cli.")

if __name__ == "__main__":
    main()