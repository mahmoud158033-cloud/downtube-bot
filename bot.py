import os
from pyrogram import Client, filters, idle

API_ID = 38404667
API_HASH = "8d1844ef188331d279093845c479e00b"
BOT_TOKEN = "9061828584:AAGzFmU6E-ms9vp21Dl9nEjJ8PG15do2ALQ"

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
    app.start()
    print("Bot is running and listening for messages!")
    idle()
