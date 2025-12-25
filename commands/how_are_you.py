import asyncio
import discord
from discord.ext import commands

name = "How are you"
description = "A simple How are you command"

intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='$', intents=intents)

#@bot.command()
async def run(ctx, *arg):
    await ctx.channel.send("How are you") # Test 
    await asyncio.sleep(1)
    await ctx.channel.send("I'm doing well how bout you")
    