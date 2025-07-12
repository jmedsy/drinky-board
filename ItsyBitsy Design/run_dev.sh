#!/bin/bash

# Exit on error
set -e

# Start Flask backend in development mode
cd backend

# Read port from .flaskenv file, default to 5000 if not found
FLASK_PORT=$(grep "FLASK_RUN_PORT=" .flaskenv | cut -d'=' -f2 2>/dev/null || echo "5000")
echo "Starting Flask backend (dev mode) on http://localhost:${FLASK_PORT} ..."

export FLASK_APP=app.py
export FLASK_ENV=development

# Activate virtual environment if it exists
if [ -d "../venv" ]; then
    source ../venv/bin/activate
    echo "Activated virtual environment"
fi

pip3 install -r requirements.txt
flask run &
BACKEND_PID=$!
cd ..

# Start Next.js frontend in development mode
cd web_client
echo "Starting Next.js frontend (dev mode) on http://localhost:3000 ..."
npm install
npm run dev &
FRONTEND_PID=$!
cd ..

echo "\nBoth servers are running."
echo "- Flask backend:   http://localhost:${FLASK_PORT}"
echo "- Next.js frontend: http://localhost:3000"
echo "\nTo stop both, press Ctrl+C or run: kill $BACKEND_PID $FRONTEND_PID"

# Wait for both to finish
wait 