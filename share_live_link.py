import subprocess
import re
import sys
import os
import time

print("=" * 65)
print("  TNNN-Link | CPF Korat - Live Public Sharing Link")
print("=" * 65)
print("[*] Starting Cloudflare Tunnel to port 8080...")

proc = subprocess.Popen(
    [os.path.join(os.path.dirname(__file__), "cloudflared.exe"), "tunnel", "--url", "http://localhost:8080"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

tunnel_url = None
start_time = time.time()

for line in proc.stdout:
    # Look for trycloudflare.com
    m = re.search(r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com", line)
    if m:
        tunnel_url = m.group(0)
        break
    if time.time() - start_time > 30:
        break

if tunnel_url:
    print("\n" + "=" * 65)
    print("  ✅ สำเร็จ! ลิ้งค์สาธารณะสำหรับแชร์ให้ผู้อื่นดู:")
    print(f"  👉  {tunnel_url}")
    print("=" * 65)
    print("[*] คัดลอกลิ้งค์ลง Clipboard อัตโนมัติแล้ว (กด Ctrl+V เพื่อวางได้เลย)")
    print("[*] แชร์ลิ้งค์นี้ผ่าน LINE, Email หรือเปิดบนมือถือได้ทันที")
    print("[*] หน้าต่างนี้ต้องเปิดไว้เพื่อส่งข้อมูลสด (กด Ctrl+C เพื่อหยุดแชร์)\n")
    
    # Copy to clipboard
    try:
        subprocess.run(["clip"], input=tunnel_url.strip(), text=True, check=True)
    except Exception:
        pass

    # Keep alive and print status
    try:
        for line in proc.stdout:
            pass
    except KeyboardInterrupt:
        print("\nStopping share tunnel...")
        proc.terminate()
else:
    print("\n[!] ไม่สามารถสร้าง Tunnel ได้ โปรดตรวจสอบการเชื่อมต่ออินเทอร์เน็ต")
    proc.terminate()
