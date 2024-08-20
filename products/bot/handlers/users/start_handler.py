import re

from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# custom files
from products.bot.loader import dp
from products.bot.states.contact import Contact
from products.bot.keyboards.default.request_contact import get_contact_kb
from products.bot.keyboards.default.main_menu import get_main_menu

# imports from Django
from users.models import User
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")
    await message.answer(text="Ro'yxatdan o'tish uchun telefon raqamingizni kiriting.\nRaqamni +998********* shaklida yuboring.",  # noqa
                         reply_markup=await get_contact_kb())

    await state.set_state(Contact.contact)


@dp.message(Contact.contact)
async def get_contact_handler(message: Message, state: FSMContext):
    phone_number = None
    print('keldi')
    if message.contact:
        phone_number = message.contact.phone_number
        print(f'kontakt kelgandagisi: {phone_number}')
    else:
        pattern = r'^\+998\d{9}$'
        text = message.text
        if re.match(pattern, text):
            phone_number = text
            print(f'regex tekshirgandasi: {phone_number}')
        else:
            print('regex dan raqam o\'tolmadi!')
            await message.answer(text='Raqam xato kiritlgan')  # noqa
            return

    print(f'raqam tekshiruvi tugagandan so\'ng {phone_number}')
    if phone_number:
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = username if username else first_name + ' ' + last_name
        telegram_id = message.from_user.id
        user_pass = make_password(username)
        print(f"{username=}\n{first_name=}\n{last_name=}\n{telegram_id=}\n{user_pass=}\n")
        try:
            user = await User.objects.aget_or_create(
                first_name=first_name, last_name=last_name,
                username=username, telegram_id=telegram_id,
                password=user_pass
            )
            print(f"user yaratildi: {user}")
        except IntegrityError:
            pass

        await message.answer('Savatcha buyurtma berishga tayyor', reply_markup=await get_main_menu())
    else:
        return

    await state.clear()

