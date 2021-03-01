from rest_framework import generics

from city.models import City, CityNews, CityLeaderShip
from city.serizlizers import CitySerializer, CityNewsSerializer, \
    CityLeaderShipSerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityRetrieveView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityLeaderShipListView(generics.ListAPIView):
    queryset = CityLeaderShip.objects.all()
    serializer_class = CityLeaderShipSerializer


class CityLeaderShipRetrieveView(generics.RetrieveAPIView):
    queryset = CityLeaderShip.objects.all()
    serializer_class = CityLeaderShipSerializer


class CityNewsListView(generics.ListAPIView):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer


class CityNewsRetrieveView(generics.RetrieveAPIView):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer