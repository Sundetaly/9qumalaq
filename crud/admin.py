from django.contrib import admin

from crud.models import Country, CountryLeaderShip, CountryNews, \
    City, CityLeaderShip, CityNews


admin.site.register(Country)
admin.site.register(CountryLeaderShip)
admin.site.register(City)
admin.site.register(CityLeaderShip)
admin.site.register(CountryNews)
admin.site.register(CityNews)
