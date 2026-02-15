#!/bin/bash

# Activate venv (create if doesn't exist)
if [ ! -d "venv" ]; then
    echo "🔧 First-time setup: Creating venv and installing packages..."
    python3.12 -m venv venv
    source venv/bin/activate
    pip install -q anthropic python-dotenv
    echo "✅ Setup complete!"
    echo ""
else
    source venv/bin/activate
fi

# Run Sentinel automatically (use python3 instead of python)
echo "🚀 Running Sentinel..."
echo ""
python3 sentinel_v1.py
