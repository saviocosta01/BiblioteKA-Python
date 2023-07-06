from django.urls import path
from .views import LendingView, ViewLoanHistory

urlpatterns = [
    path("lendings/books", LendingView.as_view()),
    path("lendings/<int:user_id>/", ViewLoanHistory.as_view()),
]
