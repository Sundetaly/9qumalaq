from django.contrib import admin

from country.models import Country, CountryLeaderShip, CountryNews, CountryWinner
from core.mixins import AdminDisplayNameMixin, AdminDisplayTitleMixin


@admin.register(Country)
class CountryAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    pass


@admin.register(CountryLeaderShip)
class CountryLeaderShipAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    list_display = AdminDisplayNameMixin.list_display + ("country",)
    list_display_links = AdminDisplayNameMixin.list_display_links + ("country",)


@admin.register(CountryNews)
class CountryNewsAdmin(AdminDisplayTitleMixin, admin.ModelAdmin):
    list_display = AdminDisplayTitleMixin.list_display + ("country",)
    list_display_links = AdminDisplayTitleMixin.list_display_links + ("country",)


@admin.register(CountryWinner)
class CountryNewsAdmin(AdminDisplayNameMixin, admin.ModelAdmin):
    list_display = AdminDisplayNameMixin.list_display + ("country",)
    list_display_links = AdminDisplayNameMixin.list_display_links + ("country",)
