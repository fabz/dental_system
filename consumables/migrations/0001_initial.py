# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import dental_system.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('sku', dental_system.fields.CodeField(max_length=40, db_index=True)),
                ('name', models.CharField(max_length=255, unique=True, db_index=True)),
                ('description', models.TextField()),
                ('is_sellable', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('sell_price', models.FloatField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesStockMutation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('mutation_qty', models.IntegerField()),
                ('price_pcs', models.FloatField()),
                ('remarks', models.TextField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True, related_name='+')),
                ('vendors', models.ForeignKey(to='vendors.Vendors')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
