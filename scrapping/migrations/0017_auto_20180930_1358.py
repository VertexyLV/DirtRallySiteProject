# Generated by Django 2.1 on 2018-09-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0016_totalqualifieddrivers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayersInfoSortAveragePlace',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortEventsFinished',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortFirstPlaces',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortTop10',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortTop100',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortTop3',
        ),
        migrations.DeleteModel(
            name='PlayersInfoSortTotalDrivingTime',
        ),
    ]