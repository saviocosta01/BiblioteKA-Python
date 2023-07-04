from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class LendingView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)
