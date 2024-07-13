from aiogram.types import Message, CallbackQuery, message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram  import F, types
from config import  bot, dp
from ParseShazam import get_text_song
import asyncio
import keyboard
from datetime import datetime

class get_text_user(StatesGroup):
    name_song = State()

@dp.message(CommandStart())
async def cmd_start(message: Message ):
    print(f'[{message.from_user.id} |{message.from_user.first_name} | {message.from_user.last_name} |{message.text}| {datetime.now()} ]')
    await message.answer(f"Добро пожаловать в бот 'Название вашего бота' ",reply_markup=keyboard.main)

@dp.message(F.text == 'Искать текст песни')
async def print_text(message: Message, state: FSMContext):
    print(f'[{message.from_user.id} |{message.from_user.first_name} | {message.from_user.last_name} |{message.text} | {datetime.now()}]')
    await message.answer('Введите название песни.Например: Дора - Дора дура')
    await state.set_state(get_text_user.name_song)

@dp.message(get_text_user.name_song)
async def get_name_text(message: Message, state: FSMContext):
    print(f'[{message.from_user.id} |{message.from_user.first_name} | {message.from_user.last_name} |{message.text} | {datetime.now()}]')
    text_song = await state.update_data(name_song=message.text.lower())
    await state.clear()
    await message.answer(get_text_song(message.text.lower()))

@dp.message(F.text == 'Помощь')
async def print_text(message: Message):
    print(f'[{message.from_user.id} |{message.from_user.first_name} | {message.from_user.last_name} |{message.text} | {datetime.now()}]')
    await message.answer('Возникли вопросы ? Надеюсь,  нет')

@dp.message(F.text)
async def print_text_user(message: Message):
    print(f'[{message.from_user.id} |{message.from_user.first_name} | {message.from_user.last_name} |{message.text} | {datetime.now()} ]')

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    print("Бот работает")
    asyncio.run(main())