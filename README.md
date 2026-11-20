# TNNN-Link | CPF Korat Industrial Web SCADA

ระบบ Web SCADA แสดงผลและติดตามสภาวะการทำงานของคอมเพรสเซอร์เครื่องทำความเย็น 46 เครื่อง โรงงานแปรรูปเนื้อไก่ นครราชสีมา (CPF Korat)

## สถาปัตยกรรมระบบ (Architecture)
- **โหมดการทำงาน:** Pure Frontend / Serverless 24/7 (ไม่ต้องใช้เซิร์ฟเวอร์แบ็กเอนด์)
- **แหล่งข้อมูล:** เชื่อมต่อ WebSocket 1:1 กับ TNNN Gateway Cloud (`wss://wsmqtt.tnnn-link.com/ws/`)
- **อุปกรณ์ที่ตรวจวัด:** 
  - มิเตอร์กำลังไฟฟ้า DMG800 (Power kW, Energy kWh)
  - เครื่องควบคุมคอมเพรสเซอร์ (GEA Omni, MYPRO TOUCH, MIII)
- **กระบวนการผลิต:** Booster Stage (19 เครื่อง), High Stage (27 เครื่อง)
- **UI Framework:** Tailwind CSS, JetBrains Mono, Prompt font (Industrial Slate ISA-101 Standard)

## การเปิดใช้งาน
เปิดดูผ่าน GitHub Pages: `https://kpatzdoe.github.io/cpf-scada/`
