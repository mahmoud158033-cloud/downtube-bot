import os
from pyrogram import Client, filters
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

API_ID = 38404667
API_HASH = "8d1844ef188331d279093845c479e00b"
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21Dl9nEjJ8PG15do2ALQ"

# سيرفر ويب حقيقي يستجيب لأي طلب فحص من منصة Fly.io فوراً
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        return

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

# تشغيل السيرفر في الخلفية بشكل فوري
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# تشغيل بوت تيليجرام
app = Client(
    "downtube_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "أهلاً بيكم في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
    )

if __name__ == "__main__":
    print("Starting Bot with Instant Web Health-Check...")
    app.run()
