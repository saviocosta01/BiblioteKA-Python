from django.shortcuts import render
from .models import Copies
from .serializers import CopiesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopiesView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    lookup_url_kwarg = "pk"
    queryset = Copies.objects.all()
    serializer_class = CopiesSerializer
    # def perform_create(self, serializer, pk):
    #     print(pk)

