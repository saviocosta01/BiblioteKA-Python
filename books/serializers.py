from rest_framework import serializers
from .models import Book
from users.serializers import CreateLendingUser


class BookSerializer(serializers.ModelSerializer):
    users = CreateLendingUser(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "book_name",
            "author",
            "category",
            "publication",
            "description",
            "publishing_company",
            "number_of_followers",
            "users",
        ]
        read_only_fields = ["id", "number_of_followers", "publication", "users"]
        # extra_kwargs = {
        #     "book_name": {"required": True},
        #     "autho": {"required": True},
        #     "category": {"required": True},
        #     "description": {"required": True},
        #     "publishing_company": {"required": True},
        # }

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class BookCopiesSerializer(serializers.ModelSerializer):
    users = CreateLendingUser(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "book_name",
            "users",
        ]
        read_only_fields = ["id", "users"]
