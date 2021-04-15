from django.db import models
from core.models import Name, LeaderShip, News


class Country(Name):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class CountryWinner(LeaderShip):
    class Meta:
        verbose_name = 'Лучший игрок'
        verbose_name_plural = 'Лучшие игроки'
    image = models.ImageField(upload_to='country_winner/')
    country = models.ForeignKey('Country', related_name='winner',
                                on_delete=models.SET_NULL, null=True)


class CountryLeaderShip(LeaderShip):
    class Meta:
        verbose_name = 'Руководствы'
        verbose_name_plural = 'Руководства'
    image = models.ImageField(upload_to='country_leader/')
    country = models.ForeignKey('Country', related_name='leader_ships',
                                on_delete=models.SET_NULL, null=True)


class CountryNews(News):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости стран'
    image = models.ImageField(upload_to='country_news/')
    country = models.ForeignKey('Country', related_name='news',
                                on_delete=models.SET_NULL, null=True)



