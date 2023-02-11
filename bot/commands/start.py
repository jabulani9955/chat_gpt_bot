from aiogram import types


async def start(message: types.Message) -> None:
    await message.answer(f"Привет, {message.from_user.first_name}. Введи текстовый запрос и модель сгенерирует тебе ответ...")