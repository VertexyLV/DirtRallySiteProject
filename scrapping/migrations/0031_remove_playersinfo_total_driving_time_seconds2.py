# Generated by Django 2.1 on 2018-11-02 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0030_playersinfo_total_driving_time_seconds2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playersinfo',
            name='total_driving_time_seconds2',
        ),
    ]
