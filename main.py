import os
import telebot
from telebot import types

# रेंडर की सेटिंग से टोकन उठाएं
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🚀 START BOT"), types.KeyboardButton("🔴 STOP BOT"), types.KeyboardButton("📊 STATUS"))
    bot.send_message(message.chat.id, "🤖 ट्रेडिंग बॉट तैयार है! नीचे दिए गए बटन का उपयोग करें।", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🚀 START BOT":
        bot.reply_to(message, "✅ बोट शुरू हो गया है!")
    elif message.text == "🔴 STOP BOT":
        bot.reply_to(message, "❌ बोट बंद हो गया है!")
    elif message.text == "📊 STATUS":
        bot.reply_to(message, "📈 बोट लाइव है और निगरानी कर रहा है!")

bot.polling(none_stop=True)
