from rest_framework import serializers
from .models import Copies
from books.serializers import BookSerializer





class CopiesSerializer(serializers.ModelSerializer):
    book_id = BookSerializer(read_only=True)

    class Meta:
        model = Copies
        fields = ["id", "amount", "book_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        book = self.context["pk"]
        print(book)
        validated_data["pk"] = book
        return Copies.objects.create(**validated_data)

    # def update(self, instance: Copies, validated_data):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)

    #     instance.save()
    #     return instance

