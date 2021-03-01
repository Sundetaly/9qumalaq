from django.db import models


class News(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    title = models.CharField(max_length=150)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    altered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LeaderShip(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150)
    rank = models.CharField(max_length=150)
    bitrhday = models.DateField()
    address = models.CharField(max_length=250)
    degree = models.CharField(max_length=150)
    assigned_degree = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
