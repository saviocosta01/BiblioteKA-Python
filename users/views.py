from rest_framework import generics
from users.models import UserModel
from users.serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
