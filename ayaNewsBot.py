from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
        if message.forward_from.first_name != message.from_user.first_name:
            await bot.forward_message(chat_id='Chat', from_chat_id='Chat', message_id=message.message_id)


@dp.message_handler()
async def echo_all(message : types.Message):
        if message.forward_from != None and message.chat.id==-880918799:
                await bot.forward_message(chat_id='Chat', from_chat_id='Chat', message_id=message.message_id)

    

executor.start_polling(dp, skip_updates=True)
