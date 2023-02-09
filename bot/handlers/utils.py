import json

from aiogram.types import Message


def get_full_name_to_course():
    with open("result.json", mode="r", encoding="utf-8") as file:
        list_corses = json.loads(file.read())
        result = []
        for item in list_corses:
            result.append(item['code'])

    return result


async def send_message_safe(message: Message, text=None, reply_markup=None):
    try:
        await message.answer(text=text, reply_markup=reply_markup)
    except:
        pass