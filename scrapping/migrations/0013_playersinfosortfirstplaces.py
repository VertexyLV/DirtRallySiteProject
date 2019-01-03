# Generated by Django 2.1 on 2018-09-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0012_playersinfosortaverageplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersInfoSortFirstPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('country_from', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('player_id', models.IntegerField()),
                ('events_finished', models.IntegerField()),
                ('average_finish_place', models.FloatField()),
                ('first_places', models.IntegerField()),
                ('top_3', models.IntegerField()),
                ('top_10', models.IntegerField()),
                ('top_100', models.IntegerField()),
                ('total_driving_time', models.FloatField()),
            ],
        ),
    ]