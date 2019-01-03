# Generated by Django 2.1 on 2018-10-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0019_auto_20181004_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('number_of_drivers', models.IntegerField()),
                ('events_finished', models.IntegerField()),
                ('average_finish_place', models.FloatField()),
                ('first_places', models.IntegerField()),
                ('top_3', models.IntegerField()),
                ('top_10', models.IntegerField()),
                ('top_100', models.IntegerField()),
                ('total_driving_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalQualifiedCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualified_countries', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='CounriesInfo',
        ),
    ]
