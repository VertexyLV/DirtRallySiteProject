# Generated by Django 2.1 on 2018-11-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0029_countriesinfo_total_driving_time_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersinfo',
            name='total_driving_time_seconds2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
