import re

from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# custom files
from bot.loader import dp
from bot.states.contact import Contact
from bot.keyboards.default.request_contact import get_contact_kb

# imports from Django
from users.models import User


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")
    await message.answer(text="Ro'yxatdan o'tish uchun telefon raqamingizni kiriting.\nRaqamni +998********* shaklida yuboring.",  # noqa
                         reply_markup=await get_contact_kb())

    await state.set_state(Contact.contact)


@dp.message(Contact.contact)
async def get_contact_handler(message: Message, state: FSMContext):
    phone_number = None

    if message.contact:
        phone_number = message.contact.phone_number
    else:
        pattern = r'^\+998\d{9}$'
        text = message.text
        if re.match(pattern, text):
            phone_number = text
        else:
            await message.answer(text='Raqam xato kiritlgan')  # noqa
            return

    if phone_number:
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = username if username else first_name + ' ' + last_name
        telegram_id = message.from_user.id

        user = User.objects.create(
            first_name=first_name, last_name=last_name,
            username=username, telegram_id=telegram_id
        )
        user.set_password(username)
        user.save()
    else:
        return

    await state.clear()

