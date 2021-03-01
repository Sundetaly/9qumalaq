from django.contrib import admin

from city.models import City, CityLeaderShip, CityNews
# Register your models here.

admin.site.register(City)
admin.site.register(CityLeaderShip)
admin.site.register(CityNews)
