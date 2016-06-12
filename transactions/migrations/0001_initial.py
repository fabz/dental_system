# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dentists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('detail_type', models.CharField(max_length=100, db_index=True)),
                ('detail_id', models.IntegerField(db_index=True)),
                ('qty', models.FloatField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by', related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=False, db_index=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('trx_number', models.CharField(max_length=80, db_index=True)),
                ('trx_date', models.DateTimeField(db_index=True)),
                ('total_amount', models.CharField(max_length=12)),
                ('counter', models.SmallIntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('customer', models.ForeignKey(to='customers.Customer')),
                ('dentist', models.ForeignKey(to='dentists.Dentists')),
                ('modified_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by', related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='transactiondetail',
            name='transaction',
            field=models.ForeignKey(to='transactions.Transactions'),
        ),
    ]
