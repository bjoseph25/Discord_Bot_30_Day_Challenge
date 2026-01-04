from infrastructure.logging import setup_logging
import logging

logger = logging.getLogger(__name__)

async def handle_error(ctx, e):
    logger.error(
        "Command failed",
        extra={
            "user": str(ctx.author),
            "channel": str(ctx.channel),
            "error": str(e),
        },
        exc_info=True
    )

    await ctx.channel.send(
        "Something went wrong while running that command."
    )
