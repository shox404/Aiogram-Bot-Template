from aiogram.types import BotCommand
from loader import bot


async def set_admin_commands():
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start"),
        ]
    )