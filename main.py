import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from bot import MainMenu, ProfileScene

from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    menu = MainMenu()
    await menu.start(message)

@dp.callback_query(lambda x: x.data == "main_menu")
async def on_menu_callback(callback_query: CallbackQuery):
    menu = MainMenu()
    await menu.change_media(callback_query.message)
    await callback_query.answer()

@dp.callback_query(lambda x: x.data == "profile")
async def on_profile_callback(callback_query: CallbackQuery):
    scene = ProfileScene('img/pic2.jpg', 'Сценарий для профиля')
    await scene.change_media(callback_query.message)
    await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())