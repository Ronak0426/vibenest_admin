# Generated by Django 5.1.5 on 2025-01-24 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('member_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('f_datetime', models.DateTimeField(default=None)),
                ('status', models.CharField(default=None, max_length=30)),
                ('groups_id', models.ForeignKey(db_column='groups_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='Groups.usergroups')),
                ('user_id', models.ForeignKey(db_column='id', default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
