from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer, DevolutionSerializer, TesteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from copies.models import Copies


class LendingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def perform_create(self, serializer):
        id = self.kwargs["pk"]
        copies = Copies.objects.get(id=id)
        copies.amount -= 1
        copies.save()
        return serializer.save(user=self.request.user, copies=copies)


class DevolutionView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DevolutionSerializer
    queryset = Lending.objects.all()


class TesteLendings(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"
    queryset = Lending.objects.all()
    serializer_class = TesteSerializer
