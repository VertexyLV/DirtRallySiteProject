# Generated by Django 2.1 on 2018-09-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0015_playersinfosorttop10_playersinfosorttop100_playersinfosorttotaldrivingtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalQualifiedDrivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualified_drivers', models.IntegerField()),
            ],
        ),
    ]