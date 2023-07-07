from rest_framework import serializers
from .models import Copies
from books.serializers import BooksSerializer


class CopiesSerializer(serializers.ModelSerializer):
    book = BooksSerializer(read_only=True)

    class Meta:
        model = Copies
        fields = ("id", "amount", "book_id")
        read_only_fields = ("id",)

    def create(self, validated_data):
        book = self.context["book"]
        validated_data["book"] = book
        return Copies.objects.create(**validated_data)

    def update(self, instance: Copies, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

