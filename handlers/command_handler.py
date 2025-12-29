import os
import importlib
import time
from cache import response_time_cahce, data_cache
from logging import setup_logging


logger = setup_logging()

commands = {}

commands_folder = os.path.join(os.path.dirname(__file__),"..", "commands")

for filename in os.listdir(commands_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f"commands.{module_name}")
        commands[module_name] = module
         

async def handle_command(ctx, command_name, *args):
    print("Loaded commands:", list(commands.keys()))  # debug
    print("Command received:", command_name)         # debug
    if command_name in commands:
        cache_key = f"{command_name}:{ctx.author.id}:{args}"
        start = time.perf_coutner()

        # Check if command result is cached
        if cache_key in data_cache:
            result = data_cache[cache_key]
            cache_hit = True
        else:
            try:
                await commands[command_name].run(ctx, *args)
                result = f"Executed {command_name}" # placeholder
                data_cache[cache_key] = result
                cache_hit = False
            except Exception as e:
                await ctx.channel.send(f"Error: {e}")
                return
            
        # Measure and cache response time
        duration = time.perf_counter() - start
        response_time_cahce[cache_key] = duration

        # Log chace hit/miss and duration
        logger.info(
            f"Command '{command_name}' by {ctx.author}"
            f"{'cache hit' if cache_hit else 'executed'} in {duration:.3f}s"
        )

        # Send cached response time
        await ctx.channel.send(
            f"{result}\nLast response time (cached): {response_time_cahce[cache_key]:.3f}s"
        )
    else:
        await ctx.channel.send("Unknown command.") 

