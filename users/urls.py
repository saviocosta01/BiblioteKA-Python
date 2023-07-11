from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/lendings/", views.UsersLendingsHistory.as_view()),
    path("users/<int:pk>/lendings/", views.UsersLendingsHistoryDetails.as_view()),
    path("users/<int:pk>/", views.UserDetailsView.as_view()),
    path("users/login/", views.Login.as_view()),
    path("sendmail/", views.SendEmailView.as_view()),
]
