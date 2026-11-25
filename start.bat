@echo off
echo ============================================
echo   RADIASENSE - AI Medical Imaging Platform
echo ============================================
echo.
echo Starting Backend (FastAPI on port 8000)...
start "RADIASENSE Backend" cmd /k "cd /d C:\Users\User\OneDrive\Desktop\RADIASENSE && python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

echo Waiting for backend to start...
timeout /t 4 /nobreak >nul

echo Starting Frontend (React on port 5173)...
start "RADIASENSE Frontend" cmd /k "cd /d C:\Users\User\OneDrive\Desktop\RADIASENSE\frontend && npm run dev"

echo.
echo ============================================
echo   RADIASENSE is starting up!
echo ============================================
echo   Backend API:  http://localhost:8000
echo   API Docs:     http://localhost:8000/docs
echo   Frontend UI:  http://localhost:5173
echo ============================================
echo.
timeout /t 5 /nobreak >nul
start http://localhost:5173
