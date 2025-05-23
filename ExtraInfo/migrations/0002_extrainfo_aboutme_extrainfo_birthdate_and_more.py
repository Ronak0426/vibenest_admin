# Generated by Django 5.1.5 on 2025-02-12 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City', '0001_initial'),
        ('ExtraInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='aboutme',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='birthdate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='city_id',
            field=models.ForeignKey(db_column='city_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='City.city'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='coverphoto',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
