import os
import MetaTrader5 as mt5
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# 1. MT5 लॉगिन फंक्शन
def connect_mt5():
    if not mt5.initialize(login=315028459, password="4Z!RRs7X!d", server="GoatFunded-Server"):
        print("MT5 कनेक्ट नहीं हो पाया")
        return False
    return True

# 2. Flask सर्वर (Render को अलाइव रखने के लिए)
app = Flask(__name__)
@app.route('/')
def home():
    return "Trading Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# 3. टेलीग्राम कमांड्स
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ट्रेडिंग बोट तैयार है! मैं मार्केट एनालाइज कर रहा हूँ।")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # यहाँ आप अपना प्राइस एक्शन या PnL चेक करने का कोड डाल सकते हैं
    await update.message.reply_text("बोट सक्रिय है। मार्केट डेटा फेच हो रहा है...")

# 4. मुख्य फंक्शन
if __name__ == '__main__':
    # Flask को बैकग्राउंड में चलाएं
    t = Thread(target=run_flask)
    t.start()

    # MT5 कनेक्ट करें
    connect_mt5()

    # टेलीग्राम बोट शुरू करें
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    application.run_polling()
