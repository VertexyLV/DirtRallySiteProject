# Generated by Django 2.1 on 2018-09-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0009_auto_20180921_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersinfo',
            name='average_finish_place',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
