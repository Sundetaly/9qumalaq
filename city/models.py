from django.db import models

from core.models import Name, News, LeaderShip


class City(Name):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class CityWinners(LeaderShip):
    class Meta:
        verbose_name = 'Лучший игрок'
        verbose_name_plural = 'Лучшие игроки'

    image = models.ImageField(upload_to='city_winner/')
    city = models.ForeignKey('City', related_name='winners',
                             on_delete=models.SET_NULL, null=True)


class CityLeaderShip(LeaderShip):
    class Meta:
        verbose_name = 'Руководствы'
        verbose_name_plural = 'Руководства'

    image = models.ImageField(upload_to='city_leader/')
    city = models.ForeignKey('City', related_name='leader_ships',
                             on_delete=models.SET_NULL, null=True)


class CityNews(News):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости городов'
    image = models.ImageField(upload_to='city_news/')
    city = models.ForeignKey('City', related_name='news',
                             on_delete=models.SET_NULL, null=True)