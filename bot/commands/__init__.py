__all__ = ['register_user_commands', 'bot_commands']

from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart, Command

from bot.commands.start import start
from bot.commands.send import send
from bot.commands.bot_commands import bot_commands


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(send)
