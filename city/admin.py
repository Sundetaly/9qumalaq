from django.contrib import admin

from city.models import City, CityLeaderShip, CityNews, CityWinners
# Register your models here.

admin.site.register(City)
admin.site.register(CityLeaderShip)
admin.site.register(CityNews)
admin.site.register(CityWinners)

