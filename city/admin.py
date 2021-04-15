from django.contrib import admin

from city.models import City, CityLeaderShip, CityNews, CityWinners
from core.mixins import AdminDisplayNameMixin, AdminDisplayTitleMixin


@admin.register(City)
class CityAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CityLeaderShip)
class CityLeaderShipAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    list_display = AdminDisplayNameMixin.list_display+("city",)
    list_display_links = AdminDisplayNameMixin.list_display + ("city",)


@admin.register(CityNews)
class CityNewsAdmin(AdminDisplayTitleMixin, admin.ModelAdmin):
    list_display = AdminDisplayTitleMixin.list_display + ("city",)
    list_display_links = AdminDisplayTitleMixin.list_display + ("city", )


@admin.register(CityWinners)
class CityNewsAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    list_display = AdminDisplayNameMixin.list_display + ("city",)
    list_display_links = AdminDisplayNameMixin.list_display + ("city", )
