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


class LeaderShipListView(generics.ListAPIView):
    queryset = CountryLeaderShip.objects.all()
    serializer_class = CountryLeaderShipSerializer


class LeaderShipCountryView(generics.ListAPIView):
    queryset = CountryLeaderShip.objects.all()
    serializer_class = CountryLeaderShipSerializer

    def get_queryset(self):
        return CountryLeaderShip.objects.filter(country__id=self.kwargs.get('pk'))


class LeaderShipRetrieveView(generics.RetrieveAPIView):
    queryset = CountryLeaderShip.objects.all()
    serializer_class = CountryLeaderShipSerializer


class NewsListView(generics.ListAPIView):
    queryset = CountryNews.objects.all()
    serializer_class = CountryNewsSerializer


class NewsCountryView(generics.ListAPIView):
    queryset = CountryNews.objects.all()
    serializer_class = CountryNewsSerializer

    def get_queryset(self):
        return CountryNews.objects.filter(country__id=self.kwargs.get('pk'))


class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = CountryNews.objects.all()
    serializer_class = CountryNewsSerializer


class WinnerListView(generics.ListAPIView):
    queryset = CountryWinner.objects.all()
    serializer_class = CountryWinnerSerializer


class WinnerCountryView(generics.ListAPIView):
    queryset = CountryWinner.objects.all()
    serializer_class = CountryWinnerSerializer

    def get_queryset(self):
        return CountryWinner.objects.filter(country__id=self.kwargs.get('pk'))


class WinnerRetrieveView(generics.RetrieveAPIView):
    queryset = CountryWinner.objects.all()
    serializer_class = CountryWinnerSerializer
