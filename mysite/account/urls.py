from django.urls import path

from . import views

urlpatterns = [
    path("", views.AccountView.as_view()),
]
