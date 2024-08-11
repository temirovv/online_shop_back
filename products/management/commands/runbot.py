from django.core.management.base import BaseCommand
from products.bot.app import run


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        run()
