import json

from bot.keyboards.reply import get_courses, get_all_courses

from aiogram.dispatcher import FSMContext
from asyncio import Lock
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from bot.handlers.utils import send_message_safe, get_full_name_to_course


lock = Lock()


async def start(message: Message):
    await send_message_safe(message, "Привет, {} выбери валюту, либо напиши мне ее)".
                            format(message.from_user.first_name), get_all_courses())


async def course(message: Message):
    with open("result.json", mode="r", encoding="utf-8") as file:
        list_corses = json.loads(file.read())
        result = []
        for item in list_corses:
            words = list(temp.lower() for temp in item['code'].split(' '))
            if message.text.lower() == item['code']:
                await send_message_safe(message, f'{item["code"]}: {item["union"]}')
                return

            if message.text.lower() in words or message.text == item['code']:
                result.append(item['code'])

    if len(result):
        await send_message_safe(message, f'Выберите валюту', get_courses(result))


async def choice(message: Message):
    with open("result.json", mode="r", encoding="utf-8") as file:
        list_corses = json.loads(file.read())
        for item in list_corses:
            if message.text == item['code']:
                await send_message_safe(message, f'{item["code"]}: {item["union"]}', get_all_courses())
                return


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(choice, lambda mes: mes.text in get_full_name_to_course())
    dp.register_message_handler(course)
