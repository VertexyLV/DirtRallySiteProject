# Generated by Django 2.1 on 2018-09-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalUniqueDrivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderboard', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='leaderboard',
            options={'ordering': ['-position']},
        ),
    ]