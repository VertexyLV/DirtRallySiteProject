# Generated by Django 2.1 on 2018-09-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0008_auto_20180921_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersinfo',
            name='total_driving_time',
            field=models.FloatField(),
        ),
    ]