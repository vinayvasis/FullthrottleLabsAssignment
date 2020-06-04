from .models import User, ActivityPeriod
from rest_framework import serializers


class ActivityPeriodSerializer(serializers.ModelSerializer):
    """
    This is ModelSerializer class for ActivityPeriod model.
    """
    class Meta:
        model = ActivityPeriod
        fields = ("start_time", "end_time")


class UserSerializer(serializers.ModelSerializer):
    """
    This is ModelSerializer class for User model.
    """
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "real_name", "tz", "activity_periods")
