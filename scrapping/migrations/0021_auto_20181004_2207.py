# Generated by Django 2.1 on 2018-10-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0020_auto_20181004_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastDatabaseUpdateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_database_update_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='countriesinfo',
            options={'ordering': ['country_name']},
        ),
    ]
