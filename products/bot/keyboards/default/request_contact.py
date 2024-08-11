from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_contact_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📱Raqamni yuborish', request_contact=True)]  # noqa
        ],
        resize_keyboard=True
    )
