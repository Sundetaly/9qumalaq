from rest_framework import generics

from city.models import City, CityNews, CityLeaderShip, CityWinners
from city.serizlizers import CitySerializer, CityNewsSerializer, \
    CityLeaderShipSerializer, CityWinnerSerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityRetrieveView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LeaderShipListView(generics.ListAPIView):
    queryset = CityLeaderShip.objects.all()
    serializer_class = CityLeaderShipSerializer


class LeaderShipCityView(generics.ListAPIView):
    queryset = CityLeaderShip.objects.all()
    serializer_class = CityLeaderShipSerializer

    def get_queryset(self):
        return CityLeaderShip.objects.filter(city__id=self.kwargs.get('pk'))


class LeaderShipRetrieveView(generics.RetrieveAPIView):
    queryset = CityLeaderShip.objects.all()
    serializer_class = CityLeaderShipSerializer


class NewsListView(generics.ListAPIView):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer


class NewsCityView(generics.ListAPIView):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer

    def get_queryset(self):
        return CityNews.objects.filter(city__id=self.kwargs.get('pk'))


class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer


class WinnerListView(generics.ListAPIView):
    queryset = CityWinners.objects.all()
    serializer_class = CityWinnerSerializer


class WinnerCityView(generics.ListAPIView):
    queryset = CityWinners.objects.all()
    serializer_class = CityWinnerSerializer

    def get_queryset(self):
        return CityWinners.objects.filter(city__id=self.kwargs.get('pk'))


class WinnerRetrieveView(generics.RetrieveAPIView):
    queryset = CityWinners.objects.all()
    serializer_class = CityWinnerSerializer
