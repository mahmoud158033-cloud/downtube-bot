import os
from pyrogram import Client, filters

# بيانات الاتصال (تم جلبها من إعدادات تيليجرام الخاصة بك)
API_ID = 2040  # استبدل هذا بالرقم الخاص بك إن وجد
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client(
    "downtube_bot",
    api_id=API_ID,
    api_api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("أهلاً بك في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله.")

# تشغيل البوت
print("Bot is starting...")
app.run()
