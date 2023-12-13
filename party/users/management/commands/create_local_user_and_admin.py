from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    """
    Create the basic superuser
    `docker-compose -f local.yml run --rm django python manage.py create_local_user_and_admin`
    """

    help = "Seed database with 'admin' and 'normal user'"

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError(
                "This command cannot be run when settings DEBUG == False,"
                + " to guard against accidental use on production."
            )
        # SuperUser
        if User.objects.filter(email="admin@email.com").exists():
            print("The admin user already exists.")
        else:
            self.stdout.write("Creating local SUPER user...")
            create_local_superuser()
            self.stdout.write('Local superuser "admin" was created')
        # Local Normal User
        if User.objects.filter(email="user@email.com").exists():
            print("The local default user already exists.")
        else:
            self.stdout.write("Creating local NORMAL user...")
            create_local_normal_user()
            self.stdout.write('Local local user "user" was created')

        # else:
        #     print("Sorry, this command can be only executed when running locally.")


def create_local_superuser():
    User.objects.create_superuser(
        email="admin@email.com",
        password="testpass123",
        name="Admin",
    )
    EmailAddress.objects.create(
        user=User.objects.get(email="admin@email.com"),
        email="admin@email.com",
        verified=True,
        primary=True,
    )


def create_local_normal_user():
    User.objects.create_user(
        email="user@email.com",
        password="testpass123",
        name="user_00",
    )
    EmailAddress.objects.create(
        user=User.objects.get(email="user@email.com"),
        email="user@email.com",
        verified=True,
        primary=True,
    )
