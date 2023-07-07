from rest_framework import generics
from users.models import UserModel
from users.serializers import UserSerializer,RetrieveLendingUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import IsAccountOwner,UserAccountOwner


class UserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | UserAccountOwner]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"

class UsersLendingsHistory(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset= UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [IsAdminUser]


class UsersLendingsHistoryDetails(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    queryset= UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [UserAccountOwner]
    lookup_url_kwarg = "pk"