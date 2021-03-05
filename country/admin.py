from django.contrib import admin

from country.models import Country, CountryLeaderShip, CountryNews, CountryWinner


admin.site.register(Country)
admin.site.register(CountryLeaderShip)
admin.site.register(CountryNews)
admin.site.register(CountryWinner)
