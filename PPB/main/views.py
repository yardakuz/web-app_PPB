from django.shortcuts import render
from .models import City, Street, Shop
from .serializers import ShopSerializer, CitySerializer, StreetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from rest_framework import status


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

class Cities_list(APIView):
    def get(self, request):
        serializer = CitySerializer(City.objects.all(), many=True)
        return Response(serializer.data)


class City_streets_list(APIView):
    def get(self, requset, city_id):
        city_name = City.objects.get(id=city_id).name
        streets_list = Street.objects.filter(city=city_id)
        serializer = StreetSerializer(streets_list, many=True)
        for element in serializer.data:
            element['city'] = city_name
        return Response(serializer.data)


class Shops_list(APIView):
    def get(self, request):
        shops_list = Shop.objects.all()
        street_value = request.GET.get('street')
        city_value = request.GET.get('city')
        open_value = request.GET.get('open')
        if street_value != None:
            try:
                street_value = int(street_value)
            except ValueError:
                return Response({'error': 'street value error'}, status=status.HTTP_400_BAD_REQUEST)
            shops_list = shops_list.filter(street=street_value)
        if city_value != None:
            try:
                city_value = int(city_value)
            except ValueError:
                return Response({'error': 'city value error'}, status=status.HTTP_400_BAD_REQUEST)
            shops_list = shops_list.filter(city=city_value)
        if open_value != None:
            if open_value == '0':
                many_close = shops_list.exclude(time_close__gte=datetime.datetime.now().time())
                many_open = shops_list.exclude(time_open__lte=datetime.datetime.now().time())
                shops_list = many_close.union(many_open)
            elif open_value == '1':
                shops_list = shops_list.filter(time_close__gt=datetime.datetime.now().time())
                shops_list = shops_list.filter(time_open__lt=datetime.datetime.now().time())
            else:
                return Response({'error': 'open value error'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = ShopSerializer(shops_list, many=True)
            for element in serializer.data:
                element['city'] = City.objects.get(id=element['city']).name
                element['street'] = Street.objects.get(id=element['street']).name
            return Response(serializer.data)
        serializer = ShopSerializer(shops_list, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            new_obj = serializer.save()
            return Response({"id": new_obj.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

