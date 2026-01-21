import os
import time
from infrastructure.bot_cache import response_time_cache, data_cache
from infrastructure.error_logging import handle_error

         

async def handle_command(ctx, command_name, *args, commands, rate_limiter=None, logger=None):
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
        rate_key = f"{ctx.author.id}:{command_name}"

            
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

        # Send cached response time
    await ctx.channel.send(
        f"{result}\nLast response time (cached): {response_time_cache[cache_key]:.3f}s"
    )
    

