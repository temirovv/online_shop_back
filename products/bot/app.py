import asyncio
import logging
import sys

from products.bot.loader import bot, dp
from products.bot.handlers.users import start_handler


async def main() -> None:
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
