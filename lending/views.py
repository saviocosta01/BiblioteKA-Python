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

    # def get_queryset(self):
    #     obj = get_object_or_404(UserModel, pk=self.request.user.pk)
    #     self.check_object_permissions(self.request, obj)
    #     return Lending.objects.filter()


class ViewLoanHistory(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, LoanHistory]

    serializer_class = LendingSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        user_id = str(self.kwargs["user_id"])
        user = UserModel.objects.get(pk=user_id)

        queryset = Lending.objects.filter(user=user)
        print(queryset)
        return queryset
