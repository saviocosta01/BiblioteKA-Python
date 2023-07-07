from .models import Book
from .serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save(users=self.request.user)
    
