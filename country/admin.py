from django.contrib import admin

from country.models import Country, CountryLeaderShip, CountryNews, CountryWinner
from core.mixins import AdminDisplayNameMixin, AdminDisplayTitleMixin


@admin.register(Country)
class CountryAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CountryLeaderShip)
class CountryLeaderShipAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CountryNews)
class CountryNewsAdmin(AdminDisplayTitleMixin, admin.ModelAdmin):
    pass


@admin.register(CountryWinner)
class CountryNewsAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass
