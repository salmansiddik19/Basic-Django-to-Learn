from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **options):
        time = timezone.now()
        self.stdout.write("%s" % time)
