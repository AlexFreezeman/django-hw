from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(email='alexcld@yandex.ru',
                                   first_name='Alex',
                                   last_name='Admin',
                                   is_staff=True,
                                   is_superuser=True)

        user.set_password('1337')
        user.save()
