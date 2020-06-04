from django.contrib import admin
from .models import User, ActivityPeriod


#adding models to admin ui for basic crud
admin.site.register(User)
admin.site.register(ActivityPeriod)

