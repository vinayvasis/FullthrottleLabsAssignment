from .models import User, ActivityPeriod
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import UserSerializer, ActivityPeriodSerializer


class UserViewSet(generics.ListAPIView):
    """
    This method is returns response.
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        load = serializer.data
        response_list = {'ok': True, 'members': load}
        return Response(response_list)


class ActivityPeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
