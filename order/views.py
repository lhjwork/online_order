from django.shortcuts import render
from order.models import Shop, Menu, Order, OrderFood
from order.serializers import ShopSerializer, MenuSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone


@csrf_exempt
def shop(request):
     if request.method == 'GET':
          # shop = Shop.objects.all()
          # # serializer을 통해서 json 형태로 parsing을 해서 데이터 형식을 json 형태로 response한다.
          # serializer = ShopSerializer(shop, many=True)
          # return JsonResponse(serializer.data, safe=False)
          
          shop = Shop.objects.all()
          return render(request,'order/shop_list.html',{'shop_list':shop})

     elif request.method == 'POST':
          data = JSONParser().parse(request)
          serializer = ShopSerializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, status=201)
          return JsonResponse(serializer.errors, status=400)
     
     
@csrf_exempt
def menu(request, shop):
     if request.method == 'GET':
          # objects.get은 하나만 가져 올 수 있어서 filter를 사용 filter가 여러개를 가져오는 것이라하는데 전체 호출인지는 확인이 필요
          menu = Menu.objects.filter(shop=shop)
          # serializer을 통해서 json 형태로 parsing을 해서 데이터 형식을 json 형태로 response한다.
          # serializer = MenuSerializer(menu, many=True)
          # return JsonResponse(serializer.data, safe=False)
          return render(request,'order/menu_list.html',{'menu_list':menu, 'shop':shop})

     elif request.method == 'POST':
          data = JSONParser().parse(request)
          serializer = MenuSerializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, status=201)
          return JsonResponse(serializer.errors, status=400)
     
     
@csrf_exempt
def order(request):
     if request.method == 'POST':
          address = request.POST['address']
          shop = request.POST['shop']
          order_date  = timezone.now()
          # getlist로 가져오기
          food_list = request.POST.getlist('menu')
          # url/order/menus/1(shop번호)에서 해당하는 shop 번호만 가져오는 것
          shop_item = Shop.objects.get(pk=int(shop))
          # create : shop에서 외래키를 받기 위해서 사용
          # request 받은 데이터 저장 해당하는 모델명_set.create하여 작성(모델명은 소문자로 작성)
          shop_item.order_set.create(address = address, order_date = order_date, shop=int(shop))
          # shop_item.order_set.latest('id').id : order table 상의 마지막 id값의 id 값 가져오기
          order_item = Order.objects.get(pk = shop_item.order_set.latest('id').id)
          
          # 어떤 음식을 주문했는지 추가
          for food in food_list:
               order_item.orderfood_set.create(food_name = food)
          
          # return HttpResponse(status=200)
          return render(request, 'order/success.html',)
     elif request.method == 'GET':
          # 내가 주문한 리스트 보여주기
          order_list = Order.objects.all()
          return render(request,'order/order_list.html',{'order_list':order_list})