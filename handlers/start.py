from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from utils.commands import set_admin_commands
from utils.detect_admin import is_admin
from data.config import ADMINS

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):

    if await is_admin(message):
        await set_admin_commands()
    await message.answer(f"Salom, {message.from_user.full_name}!")
