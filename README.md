Discord Bot Documentation
Introduction

This Python script implements a Discord Bot using the discord.py library. The bot is designed to monitor a specific channel named 'screen-time' and notify an admin user whenever a new message is posted in that channel. This documentation provides an overview of the code structure, setup, and usage.
Getting Started

To use this Discord Bot, follow these steps:

    Create a Discord Bot on the Discord Developer Portal and obtain a bot token.

    Clone or download this repository to your local machine.

    Install the discord.py library using the following command:


  pip install discord.py

Open the Python script in a code editor and replace "#Add your bot token" with your actual bot token.

Optionally, replace "admin id" with the Discord User ID of the admin user who will receive notifications.

Run the script using the command:


    python bot.py

Code Structure

The Discord Bot code consists of the following components:
1. Bot Initialization

bot_token = "#Add your bot token"
prefix = '!'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)
admin_id = "admin id"

This section initializes the bot with your bot token, sets the command prefix, and configures Discord intents to enable monitoring message content.
2. Bot Events

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    
    if message.channel.name == 'screen-time':
        
        admin_user = bot.get_user(int(admin_id))
        if admin_user:
            await admin_user.send(f"New message in 'screen-time' channel: {message.content}")

    on_ready: This event is triggered when the bot successfully logs in to Discord. It prints a message to the console indicating the bot's username.

    on_message: This event is triggered whenever a message is sent on any channel the bot can see. It checks if the message was sent in a channel named 'screen-time' and, if so, sends a notification to the admin user with the content of the message.

3. Bot Execution

  bot.run(bot_token)

This line of code starts the bot and connects it to Discord using the provided bot token. The bot will listen for events and respond accordingly.
Usage

    Run the Python script to start the bot:


    python bot.py

    Ensure the bot is invited to your Discord server and has the necessary permissions to read messages in the 'screen-time' channel.

    Whenever a new message is posted in the 'screen-time' channel, the bot will send a notification to the admin user (specified by their Discord User ID).

    You can customize the bot's behavior further by modifying the code to suit your specific requirements.

Conclusion

This documentation provides an overview of the Discord Bot code, which monitors a specific channel for new messages and notifies an admin user. You can customize and extend this bot to add more features and functionality as needed.
