from django.urls import path, include
from delivery import views

urlpatterns = [
     # path('shops/', views.shop, name = "shop"),
     # path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
     # path('menus/<int:shop>', views.menu, name = "menu"),
     path('orders/', views.order_list, name = "order_list"),
     
]