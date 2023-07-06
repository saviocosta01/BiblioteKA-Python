from .models import Copies
from rest_framework import serializers
from loans.serializers import LoanSerializer


class CopiesSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(read_only=True)

    class Meta:
        model = Copies
        fields = ['id', 'amount', 'book']
        read_only_fields = ['book']

    def create(self, validated_data):
        return Copies.objects.create(**validated_data)
