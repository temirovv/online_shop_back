from django.utils.translation import gettext_lazy as _

from django.db.models import CharField, BooleanField, TextChoices, EmailField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    first_name = CharField(_("first name"), max_length=150, null=True, blank=True)
    last_name = CharField(_("last name"), max_length=150, null=True, blank=True)
    email = EmailField(_("email address"), null=True, blank=True)
    telegram_id = CharField(max_length=150, unique=True)

    is_verified = BooleanField(default=False)
    phone_number = CharField(max_length=30, null=True, blank=True)
    gender = CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)

