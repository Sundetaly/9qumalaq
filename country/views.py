from rest_framework import generics

from country.models import Country, CountryLeaderShip, CountryNews, CountryWinner
from country.serizlizers import CountrySerializer, CountryNewsSerializer, \
    CountryLeaderShipSerializer, CountryWinnerSerializer


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


class CountryWinnerListView(generics.ListAPIView):
    queryset = CountryWinner.objects.all()
    serializer_class = CountryWinnerSerializer


class CountryWinnerRetrieveView(generics.RetrieveAPIView):
    queryset = CountryWinner.objects.all()
    serializer_class = CountryWinnerSerializer
