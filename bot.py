import os
from pyrogram import Client, filters

# جلب البيانات من متغيرات البيئة بأمان
API_ID = int(os.environ.get("API_ID", "2040"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21DL9nEjJ8PG15do2ALQ"

app = Client(
    "downtube_bot",
    api_id=API_ID,
    api_hash=API_HASH,  # تم تصحيح الخطأ الإملائي هنا
    bot_token=BOT_TOKEN,
)


@app.on_message(filters.command("start"))
async def start_command(client, message):
  await message.reply_text(
      "أهلاً بك في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
  )


# تشغيل البوت
print("Bot is starting...")
app.run()
