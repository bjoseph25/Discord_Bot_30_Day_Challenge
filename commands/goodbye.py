import discord
from discord.ext import commands

name = "goodbye"
description = "A simple goodbye command"

intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='$', intents=intents)

#@bot.command()
async def run(ctx, *arg):
    await ctx.channel.send("Goodbye") # Test 