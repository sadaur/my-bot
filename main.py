import discord
from discord.ext import commands
import os

# डिस्कार्ड बॉट सेटअप
intents = discord.Intents.default()
intents.message_content = True  # मैसेजेस पढ़ने की परमिशन
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"बॉट तैयार है! {bot.user} के रूप में लॉग इन हुआ।")

# !start कमांड के लिए
@bot.command(name="start")
async def send_welcome(ctx):
    await ctx.send("🤖 **ट्रेडिंग बॉट तैयार है!**\n\n"
                   "नीचे दिए गए कमांड्स का उपयोग करें:\n"
                   "➡️ `!start` - बॉट शुरू करने के लिए\n"
                   "➡️ `!stop` - बॉट बंद करने के लिए\n"
                   "➡️ `!status` - बॉट की स्थिति देखने के लिए")

# मैसेज हैंडलर (बटन टेक्स्ट की तरह काम करने के लिए)
@bot.event
async def on_message(message):
    # अगर मैसेज बॉट खुद भेज रहा है, तो कुछ मत करो
    if message.author == bot.user:
        return

    # टेक्स्ट के हिसाब से जवाब
    if message.content == "🚀 START BOT" or message.content == "!start":
        await message.reply("✅ बॉट शुरू हो रहा है!")
    elif message.content == "🔴 STOP BOT" or message.content == "!stop":
        await message.reply("❌ बॉट बंद हो गया है!")
    elif message.content == "📊 STATUS" or message.content == "!status":
        await message.reply("📈 बॉट लाइव है और निगरानी कर रहा है!")

    # कमांड्स को प्रोसेस करने के लिए ज़रूरी लाइन
    await bot.process_commands(message)

# रेंडर की एन्वायरमेंट सेटिंग से DISCORD_TOKEN उठाना
TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN नहीं मिला!")
