import os
import asyncio
from flask import Flask
from threading import Thread
from metaapi_cloud_sdk import MetaApi
from telegram.ext import ApplicationBuilder, CommandHandler

# Flask सर्वर
app = Flask(__name__)
@app.route('/')
def home():
    return "Trading Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

async def start(update, context):
    # MetaAPI को यहाँ (अंदर) इनिशियलाइज़ करें
    token = os.environ.get("METAAPI_TOKEN")
    account_id = os.environ.get("METAAPI_ACCOUNT_ID")
    meta_api = MetaApi(token=token)
    account = meta_api.get_account(account_id)
    
    await update.message.reply_text("बोट MetaAPI के जरिए कनेक्टेड है!")

if __name__ == '__main__':
    Thread(target=run_flask).start()
    
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
