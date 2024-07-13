
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram  import Router, F, types
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main = ReplyKeyboardMarkup(keyboard= [[KeyboardButton(text='Искать текст песни')],
        [KeyboardButton(text='Помощь')]
    ])

