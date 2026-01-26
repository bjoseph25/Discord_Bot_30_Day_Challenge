from handlers.command_handler import handle_command
from handlers.points_handler import add_point, get_points

async def on_message(message, client):
    if message.author == client.user:
        return

    parts = message.content.split()
    if not parts:
        return

    command = parts[0][1:]
    args = parts[1:]

    # Points commands handled here
    if command == "addpoint":
        add_point(str(message.author.id), conn)
        await message.channel.send("Point added!")

    elif command == "points":
        points = get_points(str(message.author.id), conn)
        await message.channel.send(f"You have {points} points.")

    # Other commands handled by command handler
    else:
        await handle_command(message, command, *args)
