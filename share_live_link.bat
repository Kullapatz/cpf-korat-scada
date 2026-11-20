@echo off
chcp 65001 >nul
title TNNN-Link - Share Live SCADA Link
echo =========================================================================
echo      TNNN-Link | CPF Korat - Create Public Shareable Link
echo =========================================================================
echo.
echo [*] กำลังสร้างลิ้งค์สาธารณะสำหรับแชร์ให้ผู้อื่น...
echo.
"C:\Users\Jog\AppData\Local\Programs\Python\Python313\python.exe" share_live_link.py
if errorlevel 1 (
    python share_live_link.py
)
pause
