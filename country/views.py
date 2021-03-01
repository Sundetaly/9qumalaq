from rest_framework import generics

from country.models import Country, CountryLeaderShip, CountryNews
from country.serizlizers import CountrySerializer, CountryNewsSerializer, \
    CountryLeaderShipSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryRetrieveView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryLeaderShipListView(generics.ListAPIView):
    queryset = CountryLeaderShip.objects.all()
    serializer_class = CountryLeaderShipSerializer


class CountryLeaderShipRetrieveView(generics.RetrieveAPIView):
    queryset = CountryLeaderShip.objects.all()
    serializer_class = CountryLeaderShipSerializer


class CountryNewsListView(generics.ListAPIView):
    queryset = CountryNews.objects.all()
    serializer_class = CountryNewsSerializer


class CountryNewsRetrieveView(generics.RetrieveAPIView):
    queryset = CountryNews.objects.all()
    serializer_class = CountryNewsSerializer
