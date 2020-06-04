from django.core.management.base import BaseCommand
from useractivity.models import User, ActivityPeriod
import string
import random

id = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k=9))

real_name = ''.join(random.choices(string.ascii_uppercase, k=15))

tz = ''.join(random.choices(string.ascii_uppercase, k=15))

ap = ActivityPeriod.objects.all()

# inserting all random values.

class Command(BaseCommand):
    """
    This is a Base command class and can be viewed by help() method.
    """
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        """

        :param args: arguments.
        :param options: options if necessary
        :return: creates user objects
        """
        sample_object = User.objects.create(id=id, real_name=real_name, tz=tz)
        sample_object.activity_periods.set(ap)
