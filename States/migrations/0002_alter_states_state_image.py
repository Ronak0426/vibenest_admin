# Generated by Django 5.1.4 on 2025-01-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('States', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='state_image',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
