from rest_framework import serializers
from .models import Lending


class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["id", "lending_date", "expiration_date"]
        read_only_fields = ["id", "lending_date", "expiration_date"]
