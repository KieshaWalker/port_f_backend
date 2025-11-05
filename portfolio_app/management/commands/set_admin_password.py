from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set password for admin user'

    def add_arguments(self, parser):
        parser.add_argument('password', type=str, help='Password to set for admin user')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username='admin')
            user.set_password(options['password'])
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully set password for user "{user.username}"')
            )
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('User "admin" does not exist')
            )