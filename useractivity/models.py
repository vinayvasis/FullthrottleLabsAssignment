from django.db import models


class ActivityPeriod(models.Model):
    """
    This is django model class.
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class User(models.Model):
    """
    This is basic django model class.
    """
    id = models.CharField(primary_key=True, max_length=30)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)
    activity_periods = models.ManyToManyField(ActivityPeriod)
