import os
from pyrogram import Client, filters, idle
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

API_ID = 38404667
API_HASH = "8d1844ef188331d279093845c479e00b"
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21Dl9nEjJ8PG15do2ALQ"

# تشغيل سيرفر الويب الوهمي أولاً على المنفذ 8080 لإرضاء منصة Fly.io
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")
    def log_message(self, format, *args):
        return

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# إعداد وتشغيل بوت تيليجرام
app = Client(
    "downtube_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "أهلاً بيكم في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
    )

print("Bot and Web Server are starting...")
app.start()
idle()
