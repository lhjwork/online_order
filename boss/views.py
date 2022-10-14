from django.shortcuts import render
from order.models import Shop, Menu, Order, OrderFood
from order.serializers import ShopSerializer, MenuSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone


@csrf_exempt
def time_input(request):
     if request.method == 'GET':
          order_list = Order.objects.all()
     
          return render(request,'boss/order_list.html', {'order_list':order_list})
     
     elif request.method == 'POST':
          order_item = Order.objects.get(pk=int(request.POST['order_id']))
          order_item.estimated_time = int(request.POST['estimated_time'])
          order_item.save()
          return render(request, 'boss/success.html')