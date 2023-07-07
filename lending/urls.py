from django.urls import path
from .views import LendingView, DevolutionView

urlpatterns = [
    path("lendings/books/", LendingView.as_view()),
    path("lendings/books/<int:pk>/", DevolutionView.as_view()),
]
