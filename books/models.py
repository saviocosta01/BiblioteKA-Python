from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    book_name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    publication = models.DateField(auto_now_add=True)
    description = models.TextField()
    publishing_company = models.CharField(max_length=60)
    number_of_followers = models.IntegerField(default=0)
    follows = models.ManyToManyField("users.UserModel", through="books.BookFollow",related_name="follows")
    user = models.ForeignKey("users.UserModel", on_delete=models.PROTECT, related_name="books")


class BookFollow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey("users.UserModel", on_delete=models.CASCADE)

