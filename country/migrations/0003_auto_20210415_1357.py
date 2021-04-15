# Generated by Django 2.2.5 on 2021-04-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_countrywinner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='name_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='address_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='address_kz',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='degree_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='degree_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='description_kz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='name_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='rank_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countryleadership',
            name='rank_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrynews',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countrynews',
            name='description_kz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countrynews',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrynews',
            name='title_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='address_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='address_kz',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='degree_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='degree_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='description_kz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='name_kz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='rank_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='countrywinner',
            name='rank_kz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
