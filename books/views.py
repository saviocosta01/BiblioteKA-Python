from .models import Book
from .serializers import  BookFollowSerializer, BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from django.shortcuts import get_object_or_404


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)



class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FollowBookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookFollowSerializer

    def perform_create(self, serializer):
        user = self.request.user
        book = get_object_or_404(Book, id=self.kwargs.get("book_id"))
        return serializer.save(user=user, book=book)

   