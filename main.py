# Discord Bot
import os

import discord
from dotenv import load_dotenv
from pathlib import Path
from handlers.command_handler import handle_command
from infrastructure.rate_limiting import RateLimiter
from infrastructure.logging import setup_logging
import importlib
from events.on_ready import on_ready as handle_on_ready
from events.on_message import on_message as handle_on_message
from infrastructure.database import connect, init_db

DB_PATH = "data/bot.db"
conn = connect(DB_PATH)
init_db(conn)


# Load environment variables from config/.env (if you keep your .env in the config folder)
env_path = Path(__file__).parent / 'config' / '.env'

rate_limiter = RateLimiter(limit=5, window=10)



logger = setup_logging()

commands = {}

commands_folder = os.path.join(os.path.dirname(__file__), "commands")

for filename in os.listdir(commands_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f"commands.{module_name}")
        commands[module_name] = module

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('DISCORD_TOKEN')   # My Discord Bot Token
GUILD = os.getenv('DISCORD_GUILD')   # My Discord Guild Name

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await handle_on_ready(client)

@client.event
async def on_message(message):
    await handle_on_message(message, client)

client.run(TOKEN)

