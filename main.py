from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN

from waifupics import waifu_nsfw, waifu_sfw
from aiogram import types
import asyncio

bot = Bot(token=BOT_TOKEN)
dp= Dispatcher(bot)

#-----------------------------------------
markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('/sfw')
).add(
    KeyboardButton('/nsfw')
)
#-----------------------------------------

@dp.message_handler(commands=['start'])
async def nsf(message: types.Message):
    await message.reply('Выберите категорию, чтобы начать:', reply_markup=markup_request)


#sfw mode per sec---------------------------
    
async def send_waifu_sfw(message):
    while True:
        response = await waifu_sfw()
        await message.reply(f'<a href="{response}">Вайфу</a>', reply_markup=markup_request, parse_mode='HTML')
        await asyncio.sleep(5)  # Задержка в секундах между итерациями
        
@dp.message_handler(commands=['sfw'])
async def nsf(message: types.Message):
    asyncio.create_task(send_waifu_sfw(message))

        
#nsfw mega mode ----------------------------

@dp.message_handler(commands=['nsfw'])
async def nsf(message: types.Message):
    while True:  # Здесь вы можете задать ваше условие для выхода из цикла
        response = await waifu_nsfw()
        await message.reply(f'<a href="{response}">Вайфу</a>', reply_markup=markup_request, parse_mode='HTML')
        

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    