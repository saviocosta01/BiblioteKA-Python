from django.shortcuts import render
from .models import Copies
from .serializers import CopiesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopiesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)

    queryset = Copies.objects.all()
    serializer_class = CopiesSerializer

    def get_queryset(self):
        book_id = self.kwargs.get("book_id")
        return Copies.objects.filter(book_id=book_id)