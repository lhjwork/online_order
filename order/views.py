from django.shortcuts import render
from order.models import Shop, Menu, Order, OrderFood
from order.serializers import ShopSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



@csrf_exempt
def shop(request):
     if request.method == 'GET':
          shop = Shop.objects.all()
          # serializer을 통해서 json 형태로 parsing을 해서 데이터 형식을 json 형태로 response한다.
          serializer = ShopSerializer(shop, many=True)
          return JsonResponse(serializer.data, safe=False)

     elif request.method == 'POST':
          data = JSONParser().parse(request)
          serializer = ShopSerializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, status=201)
          return JsonResponse(serializer.errors, status=400)