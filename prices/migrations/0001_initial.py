# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True)),
                ('treatments', models.OneToOneField(to='treatments.Treatments')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PricesHistories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('sell_price', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='+', verbose_name='modified by', to=settings.AUTH_USER_MODEL, null=True)),
                ('price', models.ForeignKey(to='prices.Prices')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
