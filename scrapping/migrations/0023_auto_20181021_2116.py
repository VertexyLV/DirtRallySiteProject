# Generated by Django 2.1 on 2018-10-21 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0022_auto_20181004_2208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventinfo',
            options={'ordering': ['event_category', 'date']},
        ),
    ]