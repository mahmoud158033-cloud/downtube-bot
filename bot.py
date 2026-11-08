import os
from pyrogram import Client, filters
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

API_ID = 38404667
API_HASH = "8d1844ef188331d279093845c479e00b"
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21Dl9nEjJ8PG15do2ALQ"

# 1. تشغيل سيرفر الويب الحقيقي كخدمة أساسية لترضي Fly.io بنسبة 100%
class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>DownTube Bot is Running!</h1>")
    def log_message(self, format, *args):
        return

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), WebHandler)
    print(f"Web server started on port {port}")
    server.serve_forever()

# بدء سيرفر الويب في خيط منفصل
web_thread = threading.Thread(target=run_web_server, daemon=True)
web_thread.start()

# 2. تشغيل بوت تيليجرام
app = Client(
    "downtube_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "أهلاً بيكم في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
    )

if __name__ == "__main__":
    print("Starting Telegram Bot...")
    # استخدام run() لأنها تدير دورة الحياة بنجاح مع السيرفرات
    app.run()
