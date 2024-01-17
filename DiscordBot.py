# Discord Bot 
import discord
from discord.ext import commands 


bot_token = "#Add your bot token"
prefix = '!'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)
admin_id = "admin id"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    
    if message.channel.name == 'screen-time':
        
        admin_user = bot.get_user(int(admin_id))
        if admin_user:
            await admin_user.send(f"New message in 'screen-time' channel: {message.content}")

bot.run(bot_token)
