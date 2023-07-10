from rest_framework import generics
from users.models import UserModel
from users.serializers import SendEmailSerializer, UserSerializer, RetrieveLendingUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response
from django.core.mail import send_mail
from django.conf import settings
from .permissions import IsAccountOwner, UserAccountOwner


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
    queryset = UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [IsAdminUser]


class UsersLendingsHistoryDetails(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [UserAccountOwner]
    lookup_url_kwarg = "pk"


class SendEmailView(APIView):
    def post(self, req: Request) -> Response:
        serializer = SendEmailSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        send_mail(
            **serializer.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )

        return Response({"message": "E-mails enviados"})
