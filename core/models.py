from django.db import models


class Name(models.Model):
    class Meta:
        abstract = True
        ordering = ['name']

    name = models.CharField(max_length=150)
    name_kz = models.CharField(max_length=150, null=True)
    name_en = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    title = models.CharField(max_length=150)
    title_kz = models.CharField(max_length=150, null=True)
    title_en = models.CharField(max_length=150, null=True)
    description = models.TextField()
    description_kz = models.TextField(null=True)
    description_en = models.TextField(null=True)

    published = models.DateTimeField(auto_now_add=True)
    altered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LeaderShip(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150)
    name_kz = models.CharField(max_length=150, null=True)
    name_en = models.CharField(max_length=150, null=True)
    rank = models.CharField(max_length=150)
    rank_kz = models.CharField(max_length=150, null=True)
    rank_en = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=250)
    address_kz = models.CharField(max_length=250, null=True)
    address_en = models.CharField(max_length=250, null=True)
    degree = models.CharField(max_length=150)
    degree_kz = models.CharField(max_length=150, null=True)
    degree_en = models.CharField(max_length=150, null=True)
    description = models.TextField()
    description_kz = models.TextField(null=True)
    description_en = models.TextField(null=True)

    bitrhday = models.DateField()
    assigned_degree = models.DateField()

    def __str__(self):
        return self.name
