from threading import Thread
import os
import django
import asyncio


# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


# Function to run Django server
def run_django():
    os.system('python manage.py runserver')


def run_bot():
    from products.bot.app import main
    asyncio.run(main())


if __name__ == '__main__':
    django_thread = Thread(target=run_django)
    bot_thread = Thread(target=run_bot)

    django_thread.start()
    bot_thread.start()

    django_thread.join()
    bot_thread.join()
