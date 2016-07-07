# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dental_system.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0002_auto_20160707_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('sku', dental_system.fields.CodeField(db_index=True, max_length=40)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('is_sellable', models.BooleanField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesPricing',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('sell_price', models.FloatField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesStock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesStockMutation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('mutation_qty', models.IntegerField()),
                ('price_pcs', models.FloatField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, verbose_name='modified by')),
                ('vendors', models.ForeignKey(to='vendors.Vendors')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
