from .models import Copies
from .serializers import CopiesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.models import Book
from drf_spectacular.utils import extend_schema



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

    @extend_schema(
        operation_id="copies_get",
        description="Rota para listar todos as cópias de livros",
        summary="Listar cópias"

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @extend_schema(
        operation_id="copies_post",
        description="Rota para criar cópias de livros",
        summary="Criar cópias"
    )
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)