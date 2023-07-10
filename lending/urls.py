from django.urls import path
from .views import LendingView, DevolutionView, TesteLendings

urlpatterns = [
    path("lendings/copies/<int:pk>/", LendingView.as_view()),
    path("lendings/books/<int:pk>/", DevolutionView.as_view()),
    path("lendings/<int:pk>/", TesteLendings.as_view()),
]
