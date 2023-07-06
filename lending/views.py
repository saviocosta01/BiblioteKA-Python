from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import LoanHistory
from django.shortcuts import get_object_or_404
from users.models import UserModel
from users.serializers import UserSerializer

# Create your views here.


class LendingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ViewLoanHistory(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, LoanHistory]

    serializer_class = LendingSerializer

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        # self.check_object_permissions(request=self.request.user, obj=user_id)
        user = UserModel.objects.get(pk=user_id)
        queryset = Lending.objects.filter(user=user)
        return queryset
