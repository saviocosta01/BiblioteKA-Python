from django.db import models


class Copies(models.Model):
    class Meta:
        ordering = ("id",)

    amount = models.PositiveIntegerField()
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_copies",
    )
