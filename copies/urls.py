from django.urls import path
from .views import CopiesView

urlpatterns = [path("copies/", CopiesView.as_view())]
