from django.db.models import CharField, BooleanField, TextChoices
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    telegram_id = CharField(max_length=150, unique=True, null=True, blank=True)
    is_verified = BooleanField(default=False)
    phone_number = CharField(max_length=30, null=True, blank=True)
    gender = CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)

