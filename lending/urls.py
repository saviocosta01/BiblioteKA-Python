from django.urls import path
from .views import LendingView, ViewLoanHistory, DevolutionView

urlpatterns = [
    path("lendings/books/", LendingView.as_view()),
    path("lendings/users/<int:pk>/", ViewLoanHistory.as_view()),
    path("lendings/books/<int:pk>/", DevolutionView.as_view()),
]
