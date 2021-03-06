from rest_framework import serializers

from city.models import City, CityNews, CityLeaderShip, CityWinners


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityLeaderShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityLeaderShip
        fields = '__all__'


class CityNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityNews
        fields = '__all__'


class CityWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWinners
        fields = '__all__'
