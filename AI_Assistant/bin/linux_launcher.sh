#!/bin/bash
# Linux launcher for offline JARVIS AI Assistant
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$DIR"
echo "Launching JARVIS AI Assistant (Linux)..."
python3 main.py --cli