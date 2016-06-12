# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('price', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(null=True, verbose_name='modified by', related_name='+', to=settings.AUTH_USER_MODEL)),
                ('treatments', models.ForeignKey(to='treatments.Treatments')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PricesHistories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(null=True, verbose_name='modified by', related_name='+', to=settings.AUTH_USER_MODEL)),
                ('price', models.ForeignKey(to='prices.Prices')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
