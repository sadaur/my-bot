import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# रेंडर पर बॉट को 24/7 लाइव रखने के लिए छोटा वेब सर्वर
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# डिस्कार्ड की इंटेंट्स (Intents) चालू करना
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'बॉट सफलतापूर्वक लॉगिन हो गया है: {bot.user.name}')

# !start कमांड का जवाब
@bot.command(name='start')
async def start_command(ctx):
    await ctx.send("🤖 **ट्रेडिंग बॉट तैयार है!**\n\n"
                   "नीचे दिए गए कमांड्स का उपयोग करें:\n"
                   "➡️ `!start` - बॉट शुरू करने के लिए\n"
                   "➡️ `!stop` - बॉट बंद करने के लिए\n"
                   "➡️ `!status` - बॉट की स्थिति देखने के लिए")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

keep_alive()

# रेंडर की सेटिंग से डिस्कार्ड टोकन उठाना
TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN नहीं मिला!")
