from core.serializers import NameSerializer, NewsSerializer, LeaderShipSerializer

from country.models import Country, CountryLeaderShip, CountryNews, CountryWinner


class CountrySerializer(NameSerializer):
    class Meta(NameSerializer.Meta):
        model = Country


class CountryLeaderShipSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        model = CountryLeaderShip


class CountryNewsSerializer(NewsSerializer):
    class Meta(NewsSerializer.Meta):
        model = CountryNews


class CountryWinnerSerializer(LeaderShipSerializer):
    class Meta(LeaderShipSerializer.Meta):
        model = CountryWinner


