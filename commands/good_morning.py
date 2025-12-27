import discord
from discord.ext import commands

name = "good morning"
description = "A simple good morning command"

intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='$', intents=intents)

#@bot.command()
async def run(ctx, *arg):
    await ctx.channel.send("Good Morning") # Test 