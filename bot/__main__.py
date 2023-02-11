import os
import logging

import openai
import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from bot.commands import bot_commands, register_user_commands


load_dotenv()

logging.basicConfig(
    filename='log.log', 
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
)


async def main() -> None:
    openai.api_key = os.getenv('chatgpt_token')
    commands_for_bot = []

    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))


    dp = Dispatcher()
    bot = Bot(token=os.getenv('tg_token'), parse_mode='HTML')
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
