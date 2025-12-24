import os
import importlib

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
        try:
            await commands[command_name].run(ctx, *args)
        except Exception as e:
            await ctx.channel.send(f"Error: {e}")
    else:
        await ctx.channel.send("Unknown command.")

