from aiogram import Bot, Dispatcher
from os import getenv
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = '6404476966:AAFH55jXaaJqYw4Mq_dZVlz1RxPkQTlkTXY'
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
