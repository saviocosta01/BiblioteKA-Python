from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer, DevolutionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from copies.models import Copies
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse


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


class DevolutionView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    serializer_class = DevolutionSerializer
    queryset = Lending.objects.all()

    def perform_update(self, serializer):
        lendings_data = Lending.objects.filter(user=self.request.user)

        lending_id = self.kwargs["pk"]
        # copy = get_object_or_404(Copies, id=copies_id)
        # lending_instance = Lending.objects.filter(copies=copy)

        lending_instance = Lending.objects.get(id=lending_id, user=self.request.user)

        for i in lendings_data:
            if not date.today() < i.expiration_date:
                i.lending_acess = True
                i.save()

        block_date = date.today() + timedelta(days=lending_instance.lock_time)
        if date.today() < block_date:
            raise PermissionDenied()

        lending_instance.avaliable = False
        lending_instance.save()

        # for j in lending_instance:
        #     block_date = date.today() + timedelta(days=j.lock_time)
        #     if date.today() < block_date:
        #         raise PermissionDenied()

        #     j.avaliable = False
        #     j.save()
