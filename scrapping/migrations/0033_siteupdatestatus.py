# Generated by Django 2.1 on 2018-11-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0032_lastdatabaseupdatetime_days_database_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUpdateStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_status', models.CharField(max_length=50)),
            ],
        ),
    ]
