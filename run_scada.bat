@echo off
chcp 65001 >nul
title TNNN Smart SCADA Pro - CPF Korat (Gateway B0-19-21-7D-96-12)
echo =========================================================================
echo      TNNN Smart SCADA Pro - Executive Next-Gen Web SCADA
echo      Gateway: B0-19-21-7D-96-12 (CPF Korat Plant - 46 Compressors)
echo =========================================================================
echo.
echo [*] Launching SCADA Dashboard in default browser...
start "" "http://localhost:8080"
echo [*] Starting Python Live Data Bridge Server on port 8080...
echo [*] Press Ctrl+C to stop the server.
echo.
"C:\Users\Jog\AppData\Local\Programs\Python\Python313\python.exe" server.py
if errorlevel 1 (
    echo.
    echo [!] Python 3.13 not found at default path, trying system 'python'...
    python server.py
)
pause
