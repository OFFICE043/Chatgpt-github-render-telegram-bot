import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from config import BOT_TOKEN
from handlers.user_handlers import register_user_handlers
from handlers.admin_handlers import register_admin_handlers

# Log yozuvini sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratamiz
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# /start komandasi
@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    user_id = message.from_user.id
    text = (
        "👋 Salom! Bu <b>AnimeBot</b>!\n\n"
        "🧑‍💻 /menu — Foydalanuvchilar menyusi\n"
        "🛠 /admin — Agar siz admin bo‘lsangiz, admin menyusini ochadi.\n\n"
        "Qaysi bo‘limga o‘tmoqchisiz?"
    )
    await message.answer(text)

# Handlerlarni ro‘yxatdan o‘tkazamiz
register_user_handlers(dp)
register_admin_handlers(dp)

# Botni ishga tushiramiz
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
