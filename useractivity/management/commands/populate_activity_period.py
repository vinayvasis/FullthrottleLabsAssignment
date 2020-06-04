from django.core.management.base import BaseCommand
from useractivity.models import ActivityPeriod
from datetime import datetime




class Command(BaseCommand):
    """
    This is a Base command class and can be viewed by help() method.
    """
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        """
        This is handle method for command execution.
        :param args: arguments
        :param options: options if necessary.
        :return: creates Activity period object.
        """
        ActivityPeriod.objects.create(start_time = datetime.now(), end_time =datetime.now() )