# Discord Bot
import os

import discord
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from config/.env (if you keep your .env in the config folder)
env_path = Path(__file__).parent / 'config' / '.env'

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('DISCORD_TOKEN')   # My Discord Bot Token
GUILD = os.getenv('DISCORD_GUILD')   # My Discord Guild Name

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)

