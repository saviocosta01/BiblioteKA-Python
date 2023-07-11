from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer, DevolutionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from copies.models import Copies
from datetime import date, timedelta
from django.core.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema


class LendingView(generics.ListCreateAPIView):
   
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def perform_create(self, serializer):
        id = self.kwargs["pk"]
        copies = Copies.objects.get(id=id)
        if copies.amount <= 0:
            raise Exception("there are no copies")
        copies.amount -= 1
        copies.save()
        return serializer.save(user=self.request.user, copies=copies)
    @extend_schema(
        operation_id="lending_get",
        description="Rota para listar todos os empréstimos de livros",
        summary="Listar empréstimos"

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @extend_schema(
        operation_id="lending_post",
        description="Rota para criar empréstimos de livros",
        summary="Criar empréstimos"
    )
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DevolutionView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    serializer_class = DevolutionSerializer
    queryset = Lending.objects.all()

    def perform_update(self, serializer):
        Lending_data = Lending.objects.filter(user=self.request.user)

        lending_id = self.kwargs["pk"]
        lending_instance = Lending.objects.get(id=lending_id)

        block_date = date.today() + timedelta(days=lending_instance.lock_time)

        for i in Lending_data:
            if date.today() < i.expiration_date:
                self.request.user.lending_acess = True
                self.request.user.save()

        if date.today() < block_date:
            raise PermissionDenied()

        lending_instance.avaliable = False
        lending_instance.save()

    @extend_schema(
        operation_id="devolution_patch",
        description="Rota para devolver livros",
        summary="Devolução de livros"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    @extend_schema(
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)