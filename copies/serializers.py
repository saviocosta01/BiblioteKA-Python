from rest_framework import serializers
from .models import Copies
from books.serializers import BookCopiesSerializer


class CopiesSerializer(serializers.ModelSerializer):
    book = BookCopiesSerializer(read_only=True)

    class Meta:
        model = Copies
        fields = ["id", "amount", "book"]
        read_only_fields = ["id","book"]

    def create(self, validated_data):
        return Copies.objects.create(**validated_data)

