import discord
from discord.ext import commands
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# रेंडर के पोर्ट एरर को ठीक करने के लिए एक छोटा वेब सर्वर सेटअप
class DummyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is running alive!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), DummyServer)
    print(f"वेब सर्वर पोर्ट {port} पर चालू हो गया है।")
    server.serve_forever()

# वेब सर्वर को बैकग्राउंड में शुरू करना
threading.Thread(target=run_web_server, daemon=True).start()

# --- डिस्कार्ड बॉट सेटअप ---
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"बॉट तैयार है! {bot.user} के रूप में लॉग इन हुआ।")

@bot.command(name="start")
async def send_welcome(ctx):
    await ctx.send("🤖 **ट्रेडिंग बॉट तैयार है!**\n\n"
                   "नीचे दिए गए कमांड्स का उपयोग करें:\n"
                   "➡️ `!start` - बॉट शुरू करने के लिए\n"
                   "➡️ `!stop` - बॉट बंद करने के लिए\n"
                   "➡️ `!status` - बॉट की स्थिति देखने के लिए")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "🚀 START BOT" or message.content == "!start":
        await message.reply("✅ बॉट शुरू हो रहा है!")
    elif message.content == "🔴 STOP BOT" or message.content == "!stop":
        await message.reply("❌ बॉट बंद हो गया है!")
    elif message.content == "📊 STATUS" or message.content == "!status":
        await message.reply("📈 बॉट लाइव है और निगरानी कर रहा है!")

    await bot.process_commands(message)

TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN नहीं मिला!")
