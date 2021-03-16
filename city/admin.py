from django.contrib import admin

from city.models import City, CityLeaderShip, CityNews, CityWinners
from core.mixins import AdminDisplayNameMixin, AdminDisplayTitleMixin


@admin.register(City)
class CityAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CityLeaderShip)
class CityLeaderShipAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CityNews)
class CityNewsAdmin(AdminDisplayTitleMixin, admin.ModelAdmin):
    pass


@admin.register(CityWinners)
class CityNewsAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass
