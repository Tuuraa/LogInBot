from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.handlers.utils import get_full_name_to_course


def get_courses(courses: list):
    reply = ReplyKeyboardMarkup(resize_keyboard=True)

    for course in courses:
        reply.add(course)

    return reply


def get_all_courses():
    courses = get_full_name_to_course()

    reply = ReplyKeyboardMarkup(resize_keyboard=True)

    for course in courses:
        reply.add(course)

    return reply