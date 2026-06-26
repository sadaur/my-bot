import os
from flask import Flask
from threading import Thread
from metaapi_cloud_sdk import MetaApi
from telegram.ext import ApplicationBuilder, CommandHandler

# MetaAPI सेटअप (यह Render के Environment Variables से टोकन उठाएगा)
TOKEN = os.environ.get("METAAPI_TOKEN")
ACCOUNT_ID = os.environ.get("METAAPI_ACCOUNT_ID")
meta_api = MetaApi(token=TOKEN)
account = meta_api.get_account(ACCOUNT_ID)

# Flask सर्वर (बोट को अलाइव रखने के लिए)
app = Flask(__name__)
@app.route('/')
def home():
    return "Trading Bot is running with MetaAPI!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# टेलीग्राम कमांड्स
async def start(update, context):
    await update.message.reply_text("बोट MetaAPI के जरिए कनेक्टेड है! अब मैं तैयार हूँ।")

if __name__ == '__main__':
    # Flask को बैकग्राउंड में चलाएं
    Thread(target=run_flask).start()
    
    # टेलीग्राम बोट शुरू करें
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
