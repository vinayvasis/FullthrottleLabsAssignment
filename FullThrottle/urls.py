from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from useractivity.views import UserViewSet, ActivityPeriodViewSet

router = routers.DefaultRouter()
router.register(r'activityperiod', ActivityPeriodViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', UserViewSet.as_view(), name="activity-list"),
    path('app/', include('useractivity.urls')),
    path('activityperiod/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
