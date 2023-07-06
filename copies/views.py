from django.shortcuts import render
from .serializers import CopiesSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Copies
from permissions.permissions import IsAdminOrReadOnly, IsAdminOrOwner


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Copies.objects.all()
    serializer_class = CopiesSerializer

    def get_queryset(self):
        return Copies.objects.filter(book_id=self.kwargs.get("book_id"))

    def perform_create(self, serializer):
        return serializer.save(book_id=self.kwargs.get("book_id"))


class CopiesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()
    lookup_url_kwarg = "Copies_id"
    second_lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Copies.objects.filter(**{
            "book_id": self.kwargs.get("book_id"),
            "id": self.kwargs.get("copy_id")})
