from django.urls import path
from .views import LendingView

urlpatterns = [
    path("lendings/", LendingView.as_view()),
]
