from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://77.232.131.69/")


async def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🛍 Katalog', web_app=web_app)],
            [KeyboardButton(text='😍 Aksiya', web_app=web_app), KeyboardButton(text='🛒 Buyurtmalarim')],
            [KeyboardButton(text='☎️ Bog\'glanish', web_app=web_app)]
        ]
    )
