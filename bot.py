import os
from pyrogram import Client, filters
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

API_ID = 38404667
API_HASH = "8d1844ef188331d279093845c479e00b"
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21Dl9nEjJ8PG15do2ALQ"

# سيرفر ويب حقيقي على بورت 8080 لإرضاء منصة Fly.io ومنع التوقف
class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"DownTube Bot is Active!")
    def log_message(self, format, *args):
        return

def run_web_server():
    server = HTTPServer(('0.0.0.0', 8080), WebHandler)
    server.serve_forever()

# تشغيل سيرفر الويب في الخلفية
web_thread = threading.Thread(target=run_web_server, daemon=True)
web_thread.start()

# تشغيل بوت تيليجرام بالطريقة القياسية
app = Client(
    "downtube_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "أهلاً بيكم في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
    )

if __name__ == "__main__":
    print("Bot and Web Server are running...")
    app.run()
