# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-01-07 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=9.99, max_digits=10)),
                ('address', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
