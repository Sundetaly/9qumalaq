from rest_framework import serializers

from core.serializers import NameSerializer, LeaderShipSerializer, NewsSerializer

from city.models import City, CityNews, CityLeaderShip, CityWinners


class CitySerializer(NameSerializer):
    class Meta(NameSerializer.Meta):
        model = City


class CityLeaderShipSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        fields = LeaderShipSerializer.Meta.fields + ('city',)
        model = CityLeaderShip


class CityNewsSerializer(NewsSerializer):
    class Meta(NewsSerializer.Meta):
        fields = NewsSerializer.Meta.fields + ('city',)
        model = CityNews


class CityWinnerSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        fields = LeaderShipSerializer.Meta.fields + ('city',)
        model = CityWinners
