from aiogram import Bot, Dispatcher, types, F, Router

from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

import asyncio
import logging


from handlers import user_handlers

TOKEN = "TOKEN"

dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(user_handlers.router)
    
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())