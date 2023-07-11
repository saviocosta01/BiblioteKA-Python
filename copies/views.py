from .models import Copies
from .serializers import CopiesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.models import Book


class CopiesView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = (JWTAuthentication,)
    lookup_url_kwarg = "pk"
    queryset = Copies.objects.all()
    serializer_class = CopiesSerializer

    def perform_create(self, serializer):
        id = self.kwargs["pk"]
        book = Book.objects.get(id=id)
        return serializer.save(book=book)
