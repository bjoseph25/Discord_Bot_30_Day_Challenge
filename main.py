# Discord Bot
import os

import discord
from dotenv import load_dotenv
from pathlib import Path
from handlers.command_handler import handle_command

# Load environment variables from config/.env (if you keep your .env in the config folder)
env_path = Path(__file__).parent / 'config' / '.env'

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('DISCORD_TOKEN')   # My Discord Bot Token
GUILD = os.getenv('DISCORD_GUILD')   # My Discord Guild Name

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    parts = message.content.split()
    if not parts:
        return 
    
    command = parts[0][1:]  # remove $ prefix
    args = parts[1:]

    # pass the whole message as ctx
    await handle_command(message, command, *args)

client.run(TOKEN)

