# Generated by Django 2.1 on 2018-11-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0028_remove_countriesinfo_total_driving_time_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='countriesinfo',
            name='total_driving_time_string',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
