import os
from pyrogram import Client, filters

# البيانات الصحيحة للبوت
API_ID = 38404667
API_HASH = "أكتب_هنا_الـ_api_hash_الحقيقي_الخاص_بحسابك"  # ليس التوكن
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21DL9nEjJ8PG15do2ALQ"

app = Client(
    "downtube_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start_command(client, message):
  await message.reply_text(
      "أهلاً بك في بوت التحميل DownTube! أرسل لي رابط الفيديو لتحميله."
  )


# تشغيل البوت
print("Bot is starting...")
app.run()
