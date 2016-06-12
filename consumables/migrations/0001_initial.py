# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dental_system.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, db_index=True)),
                ('reference_code', dental_system.fields.CodeField(max_length=40)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('vendor', models.ForeignKey(to='vendors.Vendors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumablesPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('price', models.FloatField()),
                ('consumable', models.ForeignKey(to='consumables.Consumables')),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
