from asyncio import Lock
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from bot.handlers.utils import send_message_safe


lock = Lock()


def register_admin_handlers(dp: Dispatcher):
    # todo: register all user handlers
    pass