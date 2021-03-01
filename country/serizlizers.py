from rest_framework import serializers

from country.models import Country, CountryLeaderShip, CountryNews


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryLeaderShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryLeaderShip
        fields = '__all__'


class CountryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryNews
        fields = '__all__'


