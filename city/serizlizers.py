from rest_framework import serializers

from core.serializers import NameSerializer, LeaderShipSerializer, NewsSerializer

from city.models import City, CityNews, CityLeaderShip, CityWinners


class CitySerializer(NameSerializer):
    class Meta(NameSerializer.Meta):
        model = City


class CityLeaderShipSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        model = CityLeaderShip


class CityNewsSerializer(NewsSerializer):
    class Meta(NewsSerializer.Meta):
        model = CityNews


class CityWinnerSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        model = CityWinners
