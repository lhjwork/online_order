from django.urls import path, include
from order import views

urlpatterns = [
     path('shops/', views.shop, name = "shop"),
     path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
     path('menus/<int:shop>', views.menu, name = "menu"),
     path('order/', views.order, name = "order"),
     
]