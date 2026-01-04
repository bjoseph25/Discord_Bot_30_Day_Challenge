import os
import importlib
import time
from infrastructure.bot_cache import response_time_cache, data_cache
from infrastructure.logging import setup_logging
from infrastructure.error_logging import handle_error


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

    cache_key = f"{command_name}:{ctx.author.id}:{args}"
    start = time.perf_counter()
    cache_hit = None
    result = None
    
    
    try:
        if command_name not in commands:
            await commands[command_name].run(ctx, *args)
            return
            
        # Check if command result is cached
        if cache_key in data_cache:
            result = data_cache[cache_key]
            cache_hit = True
        else:  
            await commands[command_name].run(ctx, *args)
            cache_hit = False
            data_cache[cache_key] =  f"Executed {command_name}" # placeholder
            
    except Exception as e:
            await handle_error(ctx, e)
            return
            
        # Measure and cache response time
    duration = time.perf_counter() - start
    response_time_cache[cache_key] = duration

        # Log chace hit/miss and duration
    logger.info(
        f"Command '{command_name}' by {ctx.author}"
        f"{'cache hit' if cache_hit else 'executed'} in {duration:.3f}s"
    )

        # Send cached response time
    await ctx.channel.send(
        f"{result}\nLast response time (cached): {response_time_cache[cache_key]:.3f}s"
    )
    

