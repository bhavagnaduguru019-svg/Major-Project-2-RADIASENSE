#!/bin/bash
echo "============================================"
echo "  RADIASENSE - AI Medical Imaging Platform"
echo "============================================"

cd "$(dirname "$0")"

echo "Starting Backend (FastAPI on port 8000)..."
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

sleep 3

echo "Starting Frontend (React on port 5173)..."
cd frontend && npm run dev &
FRONTEND_PID=$!

echo ""
echo "============================================"
echo "  Backend API:  http://localhost:8000"
echo "  API Docs:     http://localhost:8000/docs"
echo "  Frontend UI:  http://localhost:5173"
echo "============================================"
echo "Press Ctrl+C to stop both servers."

wait $BACKEND_PID $FRONTEND_PID
