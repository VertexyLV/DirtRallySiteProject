# Generated by Django 2.1.5 on 2019-03-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersinfo',
            name='daily2_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='daily_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='monthly_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='overall_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='weekly2_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='weekly_average_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
