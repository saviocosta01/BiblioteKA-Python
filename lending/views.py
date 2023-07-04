from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer

# Create your views here.


class LendingView(generics.ListCreateAPIView):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
