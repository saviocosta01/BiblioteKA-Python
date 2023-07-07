from rest_framework import generics
from users.models import UserModel
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner,UserAccountOwner


class UserView(generics.ListCreateAPIView):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAccountOwner | UserAccountOwner]
    queryset = UserModel.objects.all()
    serializer_class= UserSerializer
    lookup_url_kwarg = "pk"
    




        