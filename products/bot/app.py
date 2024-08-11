import asyncio
import logging
import sys

from bot.loader import bot, dp
import bot.handlers.users.start_handler


async def main() -> None:
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
