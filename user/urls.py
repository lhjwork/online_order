from django.urls import path, include
from user import views

urlpatterns = [
     path('user', views.user, name = "user"),
     
]